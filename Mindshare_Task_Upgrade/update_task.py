import requests
import json
from datetime import datetime
import os
from bs4 import BeautifulSoup

CACHE_FILE = 'tasks_cache_test.json'
UPDATING_CACHE_FILE = 'tasks_updating_cache_test.json'
PROJECT_CACHE_FILE = 'projects_cache_test.json'
PERMANENT_CACHE_FILE = 'permanent_cache.json'

# URLs for Phabricator and Mindshare APIs
PHABRICATOR_URL = 'https://phabricator.fifthgentech.com/api/maniphest.query'
USER_QUERY_URL = 'https://phabricator.fifthgentech.com/api/user.query'
PROJECT_QUERY_URL = 'https://phabricator.fifthgentech.com/api/project.query'
MINDSHARE_BASE_URL = 'http://192.168.17.174:9004'
LOGIN_URL = f"{MINDSHARE_BASE_URL}/login/"
TASKS_SAVE_URL = f"{MINDSHARE_BASE_URL}/tasks/save/"
API_TOKEN = "api-fy2ucwk5nsdaoagf3qizbqe3m4yb"
USERNAME = "badri"
PASSWORD = "1234"
USER_ID_URL = f"{MINDSHARE_BASE_URL}/users/fetch_users_data/"

def fetch_csrf_token(session):
    try:
        response = session.get(LOGIN_URL)
        response.raise_for_status()
        csrf_token = response.cookies.get("csrftoken", None)
        print(f"Fetched CSRF token: {csrf_token}")
        return csrf_token
    except requests.RequestException as e:
        print(f"Error fetching CSRF token: {str(e)}")
        return None

def login_to_mindshare(session):
    try:
        response = session.get(LOGIN_URL)
        response.raise_for_status()
        csrf_token = session.cookies.get("csrftoken", None)
        if not csrf_token:
            csrf_token = response.cookies.get("csrftoken", None)

        if not csrf_token:
            print("CSRF token not found.")
            return False

        login_data = {
            "username": USERNAME,
            "password": PASSWORD,
            "csrfmiddlewaretoken": csrf_token
        }
        headers = {
            "Referer": LOGIN_URL
        }
        response = session.post(LOGIN_URL, data=login_data, headers=headers)
        response.raise_for_status()
        
        sessionid = session.cookies.get("sessionid", None)
        if sessionid:
            print("Successfully logged in to Mindshare. Session ID:", sessionid)
            return True
        else:
            print("Failed to log in to Mindshare. No sessionid found in cookies.")
            return False
    except requests.RequestException as e:
        print(f"Error logging in to Mindshare: {str(e)}")
        return False

def fetch_user_data():
    """Fetch user data from Phabricator and build a PHID to name mapping."""
    print("Fetching user data from Phabricator...")
    params = {
        'api.token': API_TOKEN
    }
    try:
        response = requests.get(USER_QUERY_URL, params=params)
        response.raise_for_status()
        user_data = response.json().get("result", [])
        
        if isinstance(user_data, list):
            phid_to_name = {user["phid"]: user.get("userName", "Unknown") for user in user_data}
            return phid_to_name
        else:
            print("Unexpected user data format:", type(user_data))
            return {}
    except requests.RequestException as e:
        print(f"Error fetching user data: {str(e)}")
        return {}

def fetch_user_ids():
    # import pdb; pdb.set_trace();
    """Fetch user IDs from Mindshare."""
    print("Fetching user IDs from Mindshare...")
    try:
        response = requests.get(USER_ID_URL)
        response.raise_for_status()
        user_data = response.json().get("users", [])
        
        if isinstance(user_data, list):
            username_to_id = {user["user__username"]: user["user__id"] for user in user_data}
            return username_to_id
        else:
            print("Unexpected user data format:", type(user_data))
            return {}
    except requests.RequestException as e:
        print(f"Error fetching user IDs: {str(e)}")
        return {}

def fetch_tasks_from_phabricator():
    # import pdb; pdb.set_trace();
    print("Fetching tasks from Phabricator...")
    params = {
        "api.token": API_TOKEN,
    }
    try:
        response = requests.get(PHABRICATOR_URL, params=params)
        response.raise_for_status()
        tasks = response.json().get("result", {})

        with open(CACHE_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)

        return tasks

    except requests.RequestException as e:
        print(f"Error fetching tasks from Phabricator: {str(e)}")
        return {}


def fetch_projects_from_phabricator():
    # import pdb; pdb.set_trace();
    """Fetch projects from Phabricator and save to cache."""
    print("Fetching projects from Phabricator...")
    params = {
        "api.token": API_TOKEN,
    }
    try:
        response = requests.get(PROJECT_QUERY_URL, params=params)
        response.raise_for_status()
        projects = response.json().get("result", {})

        with open(PROJECT_CACHE_FILE, 'w') as f:
            json.dump(projects, f, indent=2)

        return projects

    except requests.RequestException as e:
        print(f"Error fetching projects from Phabricator: {str(e)}")
        return {}


def fetch_project_mapping():
    """Fetch project mappings from Mindshare."""
    print("Fetching project mappings from Mindshare...")
    try:
        response = requests.get(f'{MINDSHARE_BASE_URL}/projects/projects_mapping')
        response.raise_for_status()
        project_data = response.json()
        
        # Ensure 'projects' is a list
        projects = project_data.get("projects", [])
        if not isinstance(projects, list):
            print("Unexpected format: 'projects' is not a list.")
            return {}

        # Build the mapping dictionary
        project_mapping_dict = {
            proj["project_phids"]: proj["mindshare_project_id"]
            for proj in projects
            if proj.get("project_phids") and proj.get("mindshare_project_id") is not None
        }

        return project_mapping_dict

    except requests.RequestException as e:
        print(f"Error fetching project mappings: {str(e)}")
        return {}


def load_cache(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}

def save_cache(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def update_projects_in_mindshare(owner_id, mindshare_project_ids, csrf_token=None):
    """Update projects in Mindshare to add the owner_id to assigned resources."""
    # import pdb; pdb.set_trace();
    print("Updating projects in Mindshare...")
    try:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Add CSRF token to headers if available
        if csrf_token:
            headers["X-CSRFToken"] = csrf_token

        for project_id in mindshare_project_ids:
            if project_id:
                project_update_url = f"http://192.168.17.174:9004/projects/update/?ids={project_id}"
                data = {
                    "Project_Leads": owner_id,
                    "Save": "Save"
                }

                response = requests.post(project_update_url, data=data, headers=headers)
                
                if response.status_code == 200:
                    print(f"Successfully updated project {project_id} with owner {owner_id}.")
                else:
                    print(f"Error: Received status code {response.status_code} from project update URL for project {project_id}.")
    except requests.RequestException as e:
        print(f"Error updating projects in Mindshare: {str(e)}")


def extract_existing_options(html_content):
    """Extract existing options for assigned_resources from HTML content."""
    # import pdb; pdb.set_trace();
    soup = BeautifulSoup(html_content, 'html.parser')
    select_element = soup.find('select', {'name': 'assigned_resources'})
    
    if not select_element:
        return []

    options = select_element.find_all('option')
    return {option['value']: option.get_text(strip=True) for option in options}


def update_tasks_in_mindshare(session, tasks, csrf_token, username_to_id, project_mapping):
    # import pdb; pdb.set_trace();
    try:
        print("Updating tasks in Mindshare...")
        # updating_tasks = []
        existing_tasks = load_cache(UPDATING_CACHE_FILE)
        if not existing_tasks:
            existing_tasks = []
        
        updating_tasks = existing_tasks.copy()

        for task in tasks:
            task_name = task.get("name", "")
            owner_id = task.get("owner", "")  
            task_type_name = task.get("type_name", "").strip() or "105"
            mindshare_project_ids = task.get("pid", None)
            owner_name = task.get("owner_name", "")

            # Check if `mindshare_project_ids` is None or empty
            if not mindshare_project_ids:
                print(f"Task '{task_name}' has no projectPHIDs. Skipping...")
                continue  # Skip tasks without projectPHIDs

            # Check if the task already exists in existing_tasks
            if task_name in existing_tasks:
                print(f"Task '{task_name}' already exists. Skipping...")
                continue  # Skip tasks that already exist in existing_tasks

            # Check if assigned_resources is valid
            # assigned_resources = 74
            # if not assigned_resources or not all(id in username_to_id.values() for id in assigned_resources):
            #     print(f"Task '{task_name}' has invalid assigned resources. Skipping...")
            #     continue  # Skip tasks with invalid assigned resources
            
            priority = "major"
            status = "open"


            payload = {
                "csrfmiddlewaretoken": csrf_token,
                "name": task_name,
                "owner": owner_id,
                "start_date": task.get("start_date", ""),
                "end_date": task.get("end_date", ""),
                "priority": priority,  
                "status": status,
                "type": task_type_name, 
                "sub_type": task.get("sub_type", ""),
                "milestone": task.get("milestone", ""),
                "parent": task.get("parent", ""),
                "assigned_resources": [owner_id], 
                "notes": task.get("notes", "")
            }

            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": csrf_token,
                "Referer": TASKS_SAVE_URL
            }
            

            for mindshare_project_id in mindshare_project_ids:
                if mindshare_project_id:
                    task_save_url = f"{TASKS_SAVE_URL}?pid={mindshare_project_id}"
                    response = session.post(task_save_url, data=payload, headers=headers)

                    if response.status_code == 200:
                        # if task_name not in existing_tasks:
                        #     print(f"Adding new task: {task_name}")
                        #     updating_tasks.append(task)

                        html_content = response.text
                        existing_options = extract_existing_options(html_content)
                        print("owner ID:",owner_id)
                        print(f"Existing Options: {existing_options}")
                        
                        if f'{owner_id}' not in existing_options:
                            print(f"Owner ID {owner_id} not found in existing options. Retrying with updated assigned_resources.")
                            
                            # Update the project's assigned_resources
                            update_projects_in_mindshare(owner_id, mindshare_project_ids, csrf_token)
                            
                            # Retry with updated `assigned_resources`
                            updated_payload = {
                                "csrfmiddlewaretoken": csrf_token,
                                "name": task_name,
                                "owner": owner_id,
                                "start_date": task.get("start_date", ""),
                                "end_date": task.get("end_date", ""),
                                "priority": priority,  
                                "status": status,
                                "type": task_type_name, 
                                "sub_type": task.get("sub_type", ""),
                                "milestone": task.get("milestone", ""),
                                "parent": task.get("parent", ""),
                                "assigned_resources": [f'{owner_id}'],
                                "notes": task.get("notes", "")
                            }
                            
                            retry_response = session.post(task_save_url, data=updated_payload, headers=headers)
                            if retry_response.status_code == 200:
                                print(f"Successfully updated task '{task_name}' with new assigned_resources in {mindshare_project_ids}")
                                updating_tasks.append(task['name'])
                                
                            else:
                                print(f"Retry failed with status code {retry_response.status_code} for task '{task_name}'")
                        else:
                            if task_name not in existing_tasks:
                                print(f"Adding new task: {task_name}")
                                updating_tasks.append(task['name'])

                    else:
                        print(f"Error: Received status code {response.status_code} from Mindshare for task '{task_name}'")

            # if updating_tasks:
            #     save_cache(updating_tasks, UPDATING_CACHE_FILE)
            save_cache(updating_tasks, UPDATING_CACHE_FILE)
    except requests.RequestException as e:
        print(f"Error updating tasks in Mindshare: {str(e)}")

def main(): 
    # import pdb; pdb.set_trace();
    print("Starting script...")
    session = requests.Session()
    
    if not login_to_mindshare(session):
        print("Exiting script due to failed login.")
        return
    
    csrf_token = fetch_csrf_token(session)
    if not csrf_token:
        print("Exiting script due to failed CSRF token fetch.")
        return

    phid_to_name = fetch_user_data()
    username_to_id = fetch_user_ids()
    tasks_from_phabricator = fetch_tasks_from_phabricator()
    # projects_from_phabricator = fetch_projects_from_phabricator()
    project_mapping = fetch_project_mapping()

    if tasks_from_phabricator:
        print("Preparing tasks for Mindshare update...")
        tasks_for_mindshare = []
        cache = load_cache(CACHE_FILE)
        
        for task_id, task_data in tasks_from_phabricator.items():
            task_name = task_data.get("title", "")
            owner_phid = task_data.get("ownerPHID", "")
            # owner_id = username_to_id.get(owner_name, None)
            owner_name = phid_to_name.get(owner_phid, "Unknown")
            priority = task_data.get("priority", "")
            status = task_data.get("status", "")
            task_type_name = task_data.get("type_name", "").strip() or "105"

            project_phids = task_data.get("projectPHIDs", [])
            mindshare_project_ids = {project_mapping.get(phid, None) for phid in project_phids}
           
            
            task_data_mindshare = {
                "name": task_name,
                "owner": username_to_id.get(owner_name, None),
                "owner_name": owner_name,  
                "priority": priority,
                "status": status,
                "type": task_type_name,
                "assigned_resources": [username_to_id.get(owner_name, None)],
                "start_date": "",  
                "end_date": "",   
                "sub_type": "",
                "milestone": "",
                "parent": "",
                "notes": "",
                "pid": mindshare_project_ids
            }

            if task_name in cache:
                print(f"Updating existing task: {task_name}")
                cache[task_name].update(task_data_mindshare)
            else:
                print(f"Adding new task: {task_name}")
                cache[task_name] = task_data_mindshare
                tasks_for_mindshare.append(task_data_mindshare)

        update_tasks_in_mindshare(session, tasks_for_mindshare, csrf_token, username_to_id, project_mapping)
        save_cache(cache, CACHE_FILE)

    else:
        print("No tasks found in Phabricator.")

if __name__ == "__main__":
    main()
