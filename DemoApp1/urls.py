from django.urls import path
from DemoApp1 import views
from django.urls import re_path

urlpatterns = [
    path('one/',views.f1),
    path('two/',views.f2),
    re_path('^.*$',views.home),

]



