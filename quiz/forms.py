from django.forms import ModelForm
from django import forms
from quiz.models import UserDetail


# Create the form
class UserDetailForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = UserDetail
        fields = ["name", "sex", "email_id", "birth_date"]

    def __init__(self, *args, **kwargs):
        super(UserDetailForm, self).__init__(*args,  **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Name'})
        self.fields['sex'].widget.attrs.update({'class': 'form-control',
                                                'placeholder': ''})
        self.fields['email_id'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder':
                                                     'someone@gmail.com'})
        self.fields['birth_date'].widget.attrs.update({'class': 'form-control',
                                                       'placeholder':
                                                       'YYYY-MM-DD'})


class QuestionForm(forms.Form):
    title = forms.ChoiceField(widget=forms.RadioSelect())

    def __init__(self, question="", *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = question.question_text
        self.fields['title'].choices = \
            [([question.id, chi.choice_text], chi)
             for chi in question.choice_set.all()]
