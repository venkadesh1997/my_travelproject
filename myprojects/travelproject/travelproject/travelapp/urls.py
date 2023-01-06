from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo')
    # path('add/',views.addition,name='addition'),
    # path('',views.demo,name='demo'),
    # path('add/',views.multiplication,name='multiplication')
    # path('Home/',views.Home,name='Home'),
#     path('about/',views.about,name='about'),
#     path('contact/',views.contact,name='contact'),
#     path('details/',views.details,name='details'),
#     path('Thanks/',views.Thanks,name='Thanks')
]