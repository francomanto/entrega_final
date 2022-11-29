from django.urls import path

from profesional import views

app_name = "profesional"
urlpatterns = [
    path("profesionales/", views.ProfesionalListView.as_view(), name="profesional-list"),
    path("profesional/add/", views.ProfesionalCreateView.as_view(), name="profesional-add"),
    path("profesional/<int:pk>/detail/", views.ProfesionalDetailView.as_view(), name="profesional-detail"),
    path("profesional/<int:pk>/update/", views.ProfesionalUpdateView.as_view(), name="profesional-update"),
    path("profesional/<int:pk>/delete/", views.ProfesionalDeleteView.as_view(), name="profesional-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]
