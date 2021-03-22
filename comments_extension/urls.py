from django.urls import path

from .views.moderation import edit, edit_done


app_name = "comments_extension"

urlpatterns = [
    path("edit/<int:comment_id>/", edit, name="comments-edit"),
    path("edited/", edit_done, name="comments-edit-done"),
]
