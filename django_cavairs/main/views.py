from django.shortcuts import render
# from django.http import HttpResponse
import datetime
import os

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def times(request):
    current_time = datetime.datetime.now()
    context = {'current_time': current_time}
    return render(request, 'main/time.html', context)


def direct(request):
    # project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # context = {'project_dir': project_dir}

    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = os.listdir(project_dir)
    context = {'project_dir': project_dir, 'files': files}

    return render(request, 'main/osdirectory.html', context)
