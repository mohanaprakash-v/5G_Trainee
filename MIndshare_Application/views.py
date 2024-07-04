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