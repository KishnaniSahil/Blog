from django.urls import path
from . import views

urlpatterns=[
    path('about/',views.about),
    path('create/',views.create,name="create"),
    path('insert/',views.insert,name="add"),
    path('edit/<pk>',views.edit,name="edit"),
    path('update/',views.update,name="update"),
    ]