from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',IndexPage.as_view(),name='index'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('create/',CreateTicket.as_view(),name='create-ticket'),
    path('update/<int:pk>/',UpdateTicket.as_view(),name='update-ticket')

]
