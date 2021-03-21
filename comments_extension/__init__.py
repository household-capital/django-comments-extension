from __future__ import absolute_import
from django.urls import reverse

# Try to import django_comments otherwise fallback to the django contrib comments
try:
    import django_comments as django_comments
except ImportError:
    try:
        from django.contrib import comments as django_comments
    except ImportError:
        raise ImportError('django-comments-extension requires django-contrib-comments to be installed or the deprecated'
                          ' (as of django 1.6) django.contrib.comments.')


def get_edit_form():
    """
    Returns a (new) comment edit form object
    """
    from comments_extension.forms import CommentEditForm
    if django_comments.get_comment_app_name() != django_comments.DEFAULT_COMMENTS_APP and \
            hasattr(django_comments.get_comment_app(), "get_edit_form"):
        return django_comments.get_comment_app().get_edit_form()
    else:
        return CommentEditForm
    
    
def get_edit_modelform(comment):
    """
    Returns the comment ModelForm instance
    """
    from comments_extension.forms import CommentEditForm
    if django_comments.get_comment_app_name() != django_comments.DEFAULT_COMMENTS_APP and \
            hasattr(django_comments.get_comment_app(), "get_edit_modelform"):
        return django_comments.get_comment_app().get_edit_modelform()
    else:
        return CommentEditForm(instance=comment)


def get_edit_form_target(comment):
    """
    Returns the target URL for the comment edit form submission view.
    """
    from comments_extension.forms import CommentEditForm
    if django_comments.get_comment_app_name() != django_comments.DEFAULT_COMMENTS_APP and \
            hasattr(django_comments.get_comment_app(), "get_edit_form_target"):
        return django_comments.get_comment_app().get_edit_form_target()
    else:
        return reverse("comments_extension.views.moderation.edit", args=(comment.id,))
