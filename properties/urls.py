from django.urls import path

from .views import PropertiesListView

urlpatterns = [
    path("properties/", PropertiesListView.as_view()),
]
