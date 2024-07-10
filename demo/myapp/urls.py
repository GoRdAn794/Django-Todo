from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"), #f we are calling home function inside the views file which will execute
    path("todos/",views.todos,name="Todos"),
    path("shows/",views.show,name="Show")

]