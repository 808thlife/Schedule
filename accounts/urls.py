from django.urls import path
from . import views

#FOR AUTH APP
app_name = "accounts"

urlpatterns = [
    path("", views.index, name = "index"),
    path("signup", views.signup, name = "signup"),
    path("logout", views.signout, name = "signout"),
]
