from django.urls import path
from . import views

urlpatterns=[
    path('',views.LoginPage,name='login'),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),
    path('home/',views.Home,name="home"),
    path('create/',views.ListCreate,name="create-list"),
    path('display/<int:pk>/',views.DisplayList,name="display-list"),
    path('update/<int:pk>/',views.ListUpdate,name="update-list"),
    path('delete/<int:pk>/',views.ListDelete,name="delete-list"),
    path('mark-completed/<int:pk>/',views.MarkAsCompleted,name='mark-completed')
]