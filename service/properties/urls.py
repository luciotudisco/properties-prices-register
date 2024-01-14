from django.urls import path
from properties.views import PropertiesListView
from properties.views import PropertiesStatsView

urlpatterns = [
    path("properties/", PropertiesListView.as_view()),
    path("properties/stats", PropertiesStatsView.as_view({"get": "aggregation"})),
]
