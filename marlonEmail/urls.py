from django.urls import path, include

urlpatterns = [
    path('', include('email_sender.urls')),
   
]
