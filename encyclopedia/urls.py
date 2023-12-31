from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('form/', views.form, name="form"),
    path('create/', views.create, name="create"),
    path('edit/', views.edit, name="edit"),
    path('random/', views.random_title, name="random"),
    path('<str:title>/', views.get_title, name='get_title'),
]
