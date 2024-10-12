from django.urls import path
from .views import home,create,list,delete,update

urlpatterns = [
    path("", home, name='home'),
    path("create", create, name='create'),
    path("list", list, name='list'),
    path("delete/<int:id>/", delete, name='delete'),
    path("edit/<int:id>/", update, name='edit')
]
