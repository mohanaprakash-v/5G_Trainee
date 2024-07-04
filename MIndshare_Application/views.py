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

#-------------------------------------------------------------------------------------#

# The Type and SubType objects have a created_at field

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Task, Type, SubType
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Max

@csrf_exempt
def update_tasks_from_phabricator(request):
    if request.method == 'POST':
        try:
            phabricator_data = json.loads(request.body).get('tasks', [])
            for task_data in phabricator_data:
                username = task_data.get('username')
                
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    return JsonResponse({'status': 'error', 'message': f'User with username {username} not found'}, status=400)
                
                try:
                    task_type_name = task_data.get('type', '').strip()
                    task_type = Type.objects.filter(name=task_type_name).order_by('-created_at').first()
                    if not task_type:
                        return JsonResponse({'status': 'error', 'message': f'Invalid type specified: {task_type_name}'}, status=400)
                except Type.DoesNotExist:
                    return JsonResponse({'status': 'error', 'message': f'Invalid type specified: {task_type_name}'}, status=400)
                
                try:
                    sub_type_name = task_data.get('sub_type', '').strip()
                    sub_type = SubType.objects.filter(name=sub_type_name).order_by('-created_at').first()
                    if not sub_type:
                        return JsonResponse({'status': 'error', 'message': f'Invalid subtype specified: {sub_type_name}'}, status=400)
                except SubType.DoesNotExist:
                    return JsonResponse({'status': 'error', 'message': f'Invalid subtype specified: {sub_type_name}'}, status=400)

                # Update or create the task
                task_name = task_data['name']
                task, created = Task.objects.update_or_create(
                    name=task_name,
                    defaults={
                        'owner': user,
                        'start_date': task_data.get('start_date'),
                        'end_date': task_data.get('end_date'),
                        'priority': task_data.get('priority'),
                        'status': task_data.get('status'),
                        'type': task_type,
                        'sub_type': sub_type,
                        'notes': task_data.get('notes'),
                    }
                )
                
                if created:
                    task.author = user
                    task.editor = user
                    task.save()
            
            return JsonResponse({'status': 'success'})
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        
        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Missing key: {str(e)}'}, status=400)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
