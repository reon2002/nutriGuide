from .views import *
from django.urls import path

urlpatterns = [
    path('', login, name='login'),
    path('homepage/', homepage, name='homepage'),
    path('addFruit/', addFruit, name='addFruit'),
    path('editFruit/', editFruit, name='editFruit'),
    path('searchResults/', searchResults, name='searchResults'),
    path('notFound/', notFound, name='notFound'),
    path('deleteFruit/', deleteFruit, name='deleteFruit'),

]