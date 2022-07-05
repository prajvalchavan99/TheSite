from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home,name="index"),
    path('text-compare/', views.textcompare,name="textcompare"),
]
