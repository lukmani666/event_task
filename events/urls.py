from . import views
from django.urls import path

urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('csrf_cookie_set/', views.GetCSRFToken.as_view()),
]