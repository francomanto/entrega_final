from django.urls import path

from sede import views

app_name = "sede"
urlpatterns = [
    path("sedes", views.sedes, name="sede-list"),
    path("sede/add", views.create_sede, name="sede-add"),
]
