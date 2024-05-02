from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyCalendar.as_view(), name='calendar'),
    path('<int:year>/<int:month>/<int:day>/',
        views.MyCalendar.as_view(), name='calendar'),
]