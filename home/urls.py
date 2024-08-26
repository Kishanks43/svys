from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('' , views.index,name='home'),
    # path('/home',views.index,name='')
    path('about/' , views.about,name='about'),
    path('services/',views.services,name='services'),
    path('add-entry',views.add_entry,name='add_entry'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout')
  

]
