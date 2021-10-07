from django.shortcuts import render
from .models import ToDo


def index(request):
    all_todos = ToDo.objects.all()
    return render(request, 'core/index.html', context={"all_todos": all_todos})
