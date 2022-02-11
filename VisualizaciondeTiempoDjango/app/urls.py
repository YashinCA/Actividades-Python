from django.urls import path
from . import views
# esto parte desde http://127.0.0.1:8000/
urlpatterns = [
    path('', views.index),
    path('time_display', views.time_display),

]
