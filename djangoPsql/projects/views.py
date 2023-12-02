from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from projects.models import Projects
from projects.serializers import ProjectsSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def project_list(request):
    if request.method == 'GET':
        projects = Projects.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            projects = projects.filter(title__icontains=title)
        
        projects_serializer = ProjectsSerializer(projects, many=True)
        return JsonResponse(projects_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        project_data = JSONParser().parse(request)
        project_serializer = ProjectsSerializer(data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse(project_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = project.objects.all().delete()
        return JsonResponse({'message': '{} projects were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    try: 
        project = project.objects.get(pk=pk) 
    except project.DoesNotExist: 
        return JsonResponse({'message': 'The project does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        project_serializer = ProjectsSerializer(project) 
        return JsonResponse(project_serializer.data) 
 
    elif request.method == 'PUT': 
        project_data = JSONParser().parse(request) 
        project_serializer = ProjectsSerializer(project, data=project_data) 
        if project_serializer.is_valid(): 
            project_serializer.save() 
            return JsonResponse(project_serializer.data) 
        return JsonResponse(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        project.delete() 
        return JsonResponse({'message': 'project was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def project_list_published(request):
    projects = project.objects.filter(published=True)
        
    if request.method == 'GET': 
        projects_serializer = ProjectsSerializer(projects, many=True)
        return JsonResponse(projects_serializer.data, safe=False)
    