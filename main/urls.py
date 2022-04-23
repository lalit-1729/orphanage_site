from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
    path("homepage", views.homepage, name="homepage"),
    path("orphanage/<int:id>", views.orphanage_details, name="orphanage_details"),
    path("orphanage_registration", views.register_orphanage, name="orphanage_registration"),
    path("admit_orphan", views.admit_orphan, name="admit_orphan"),
    path("orphanages", views.orphanages, name="orphanages"),
    path("events", views.events, name="events"),
    path("adoption", views.adoption, name="adoption"),
    path("about_us", views.about_us, name="about_us"),
]

# orphanage_registration.html
