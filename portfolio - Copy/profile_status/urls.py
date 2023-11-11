from profile_status import views
from django.urls import path

urlpatterns = [
    path('', views.propro,name="Home"),
    path('Statistics/',views.Statistics,name="Statistics"),
]
