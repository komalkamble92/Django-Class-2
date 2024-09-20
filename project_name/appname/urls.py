from django.urls import path
from .views import * # . = root path
from appname.api import * # all classes imported

from . import api
from appname import views 



# {{base url}}/app(prefix)/about/

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home2/', views.home2, name='home2'), 
    path('students/', views.student_list, name='student_list'),  # URL for student list

    # path('Login/', Login, name='home yguuy jhiiu '),
    # path(endpoint , filename.classname, discription)
    
    
    
    # path('about/', api.about, name='about'),
    # path('about/', about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('services/', views.services, name='services'),
    # path('products/', views.products, name='products'),
]
