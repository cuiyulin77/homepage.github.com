from django.urls import path
from . import views
app_name = 'firstapp'
urlpatterns = [
    path('index/',views.index),
    path('fanapp/', views.fanapp, name="fanapp"),
]