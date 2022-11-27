from django.urls import path
from trainify_bridge import views

urlpatterns = [
    path('t/', views.test)
]
