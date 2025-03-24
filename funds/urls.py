from django.urls import path

from . import views


app_name = "funds"

urlpatterns = [
    path("", views.home, name="home"),
    path("funds/", views.funds, name="funds_all"),
    path("funds/upload/", views.FundDataUpload.as_view(), name="funds_upload"),
]
