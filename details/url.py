from django.conf.urls import url
from details import views

urlpatterns=[
    url('add/',views.add),
    url('sea/',views.search)
    
]