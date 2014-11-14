from django.forms import ModelForm
from quiz.models import UserDetail


# Create the form
class UserDetailForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = UserDetail
        fields = ["title", "name",  "email_id", "birth_date"]
