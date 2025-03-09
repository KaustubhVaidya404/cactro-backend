from django.urls import path

from github import views

app_name = 'github'

urlpatterns = [
    path('getgithubdata/', views.get_github_data, name='getgithubdata')
]
