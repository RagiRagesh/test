
from django.urls import path

from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('operations/',views.operations,name='operations'),
#     path('contact/',views.contact,name='contact'),
]
