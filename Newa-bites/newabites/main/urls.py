from django.urls import path
from .views import *
urlpatterns=[
    path('contribution/',contribution,name="contribution"),
    path('recommendations/<int:id>',recommendations, name='recommendations'),
    path('recipe/<int:id>',recipe, name='recipe'),
    path('',home,name='home'),
    path('listoffood/',listoffood,name='listoffood'),
    path('donate/',donate,name='donate'),

]