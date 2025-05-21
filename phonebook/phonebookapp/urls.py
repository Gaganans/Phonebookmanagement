from django.urls import path
from.import views

urlpatterns=[
    path('',views.phn),
    path('phn',views.addnumber),
    path('dis',views.display),
    path('updt',views.update),
    path('del',views.delete),
    
]