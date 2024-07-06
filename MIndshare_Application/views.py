#users/views.py

#----------------------------GET METHOD CSRF TOKEN FUNCTION---------------------------#

# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.http import JsonResponse
# from django.middleware.csrf import get_token

# @ensure_csrf_cookie
# def get_csrf_token(request):
#     csrf_token = get_token(request)
#     return JsonResponse({'csrf_token': csrf_token})



# UPDATED CSRF TOKEN GENERATION ------------------------------------------------#


from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def csrf_token(request):
    # import pdb;pdb.set_trace()    
    if request.method == 'GET':
        # For GET requests, set the CSRF token in the response cookies
        csrf_token = get_token(request)
        response = JsonResponse({'detail': 'CSRF cookie set'})
        response.set_cookie('csrftoken', csrf_token)
        return response
    elif request.method == 'POST':
        # import pdb;pdb.set_trace()
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # For Login success --- CSRF TOKEN GENERATE
            
            csrf_token = get_token(request)
            return JsonResponse({'csrf_token': csrf_token})
        else:
            # For Invalid credentials
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        # Other than POST and GET Request
        return JsonResponse({'error': 'Method not allowed'}, status=405)

#---------------------------------------------------------------------------------------#

#----------------------------Update Tasks from Phabricator------------------------------#

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Task, Type
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def update_tasks_from_phabricator(request):
    # import pdb;pdb.set_trace();
    if request.method == 'POST':
        try:
            phabricator_data = json.loads(request.body).get('tasks', [])
            
            for task_data in phabricator_data:
                username = task_data.get('username')
                
                # Ensure user exists
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    return JsonResponse({'status': 'error', 'message': f'User with username {username} not found'}, status=400)
                
                # Task data from Phabricator
                task_name = task_data['name']
                start_date = task_data.get('start_date')
                end_date = task_data.get('end_date')
                priority = task_data.get('priority')
                status = task_data.get('status')
                notes = task_data.get('notes')
                task_type_name = task_data.get('type', '').strip()
                
                # Retrieve or filter task types
                task_types = Type.objects.filter(name=task_type_name)

                # Retrieve or create the task type
                # task_type, created = Type.objects.get_or_create(name=task_type_name)
                
                if not task_types.exists():
                    return JsonResponse({'status': 'error', 'message': f'Invalid type specified: {task_type_name}'}, status=400)
                
                # Assuming you handle multiple types or select the first one
                task_type = task_types.first()
                
                # Update or create the task
                task, created = Task.objects.update_or_create(
                    name=task_name,
                    defaults={
                        'owner': user,
                        'start_date': start_date,
                        'end_date': end_date,
                        'priority': priority,
                        'status': status,
                        'type': task_type,
                        'notes': notes,
                        'author': user
                    }
                )
                
                # Set author and editor
                # if created:
                #     task.author = user
                task.editor = user
                task.save()
            
            return JsonResponse({'status': 'success', 'message': 'Tasks updated successfully'})
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        
        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Missing key: {str(e)}'}, status=400)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
