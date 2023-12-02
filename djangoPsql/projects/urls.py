from django.urls import path
from projects import views

urlpatterns = [
    path('api/projects', views.project_list, name='project-list'),
    path('api/projects/<int:pk>', views.project_detail, name='project-detail'),
    path('api/projects/published', views.project_list_published, name='project-list-published'),
]