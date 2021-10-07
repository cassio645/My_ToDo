from django.shortcuts import render, get_object_or_404
from .models import ToDo
from .forms import ToDoForms


def index(request):
    all_todos = ToDo.objects.all()
    form = ToDoForms()
    return render(request, 'core/index.html', context={"all_todos": all_todos, "form":form})


def detail(request, id):
    todo = get_object_or_404(ToDo, pk=id)
    return render(request, "core/detail.html", context={"todo":todo})
