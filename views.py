from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        
        # Create new user
        user = User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({'message': 'User registered successfully'}, status=201)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Logs the user in and creates a session
            return JsonResponse({'message': 'User logged in successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
from django.contrib.auth import logout

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)  # Ends the user session
        return JsonResponse({'message': 'User logged out successfully'}, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
from .models import ChatHistory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
def chat_history(request):
    if request.method == 'GET':
        user = request.user
        history = ChatHistory.objects.filter(user=user)
        response_data = [{'question': h.question, 'response': h.response, 'date': h.date} for h in history]
        return JsonResponse({'chat_history': response_data}, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
from .models import Analysis

@method_decorator(login_required, name='dispatch')
def analysis_report(request):
    if request.method == 'GET':
        user = request.user
        reports = Analysis.objects.filter(user=user)
        response_data = [{'date': report.date, 'score': report.score, 'report': report.report} for report in reports]
        return JsonResponse({'analysis_report': response_data}, status=200)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        score = data.get('score')
        report = data.get('report')
        
        # Save analysis report
        Analysis.objects.create(user=request.user, score=score, report=report)
        return JsonResponse({'message': 'Analysis report saved'}, status=201)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
