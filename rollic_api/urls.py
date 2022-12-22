from django.contrib import admin
from django.urls import path, include
from .views import (
    RollicListApiView,
    RollicDetailApiView,
)

urlpatterns = [
    path('api', RollicListApiView.as_view()),
    path('api/<int:user_id>/', RollicDetailApiView.as_view()),
]
