from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, p_key):
    project = Project.objects.get(pk=p_key)
    context = {'project'=project}
    return render(request,"project_detail.html", context)