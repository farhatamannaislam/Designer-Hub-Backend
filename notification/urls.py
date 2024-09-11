from django.urls import path
from notification import views

urlpatterns = [
    path('notification/', views.NotificationList.as_view()),
    path('notification/<int:pk>/', views.NotificationUpdate.as_view())
]