from django.urls import path

from . import views


app_name = "api"

urlpatterns = [
    path("funds/", views.FundListView.as_view(), name="funds_list"),
    path("funds/<int:pk>/", views.FundDetailView.as_view(), name="funds_detail"),
]
