from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.page, name = "page"),
    path("search", views.search, name = "search"),
    path("new_page", views.new_page, name = "new_page"),
    path("random_page", views.random_page, name = "random_page"),
    path("edit_title", views.edit_title, name = "edit_title"),
    path('edit_page', views.edit_page, name = "edit_page")
]
