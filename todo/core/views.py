from django.core import paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import ToDo
from .forms import ToDoForms


def index(request):
    # Pegando todos as tarefas criadas
    lista_todos = ToDo.objects.all()

    # Paginação
    paginator = Paginator(lista_todos, 5)
    page = request.GET.get("page")
    todos = paginator.get_page(page)

    # Formulário para criar novas tarefas
    form = ToDoForms()
    if request.method == "POST":
        form = ToDoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Todo:index")
        return render(request, 'core/index.html', context={"todos": todos, "form":form})

    return render(request, 'core/index.html', context={"todos": todos, "form":form})


def detail(request, id):
    todo = get_object_or_404(ToDo, pk=id)
    return render(request, "core/detail.html", context={"todo":todo})


def edit(request, id):
    todo = get_object_or_404(ToDo, pk=id)
    form = ToDoForms(instance=todo)

    if request.method == "POST":
        form = ToDoForms(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("Todo:index")
        
        return render(request, 'core/edit.html', context={"form":form, "todo":todo})
        
    return render(request, 'core/edit.html', context={"form":form, "todo":todo})


def delete(request, id):
    todo = get_object_or_404(ToDo, pk=id)
    todo.delete()
    return redirect('Todo:index')
