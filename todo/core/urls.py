from django.urls import path
from . import views

app_name = "Todo"

urlpatterns = [
    path('', views.index, name="index"),
    path("detalhes/<int:id>", views.detail, name="detail"),
    path("editar/<int:id>", views.edit, name="edit"),
    path("delete/<int:id>", views.delete, name="delete"),
]