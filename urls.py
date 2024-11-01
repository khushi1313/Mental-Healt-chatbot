from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('chat_history/', views.chat_history, name='chat_history'),
    path('analysis_report/', views.analysis_report, name='analysis_report'),
]
