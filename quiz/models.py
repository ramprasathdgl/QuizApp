from django.db import models

TITLE_CHOICES = (
    ('MR', 'Male'),
    ('MRS', 'Female'),
    ('MS', 'Other'),
)


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    answer_text = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class UserDetail(models.Model):
    sex = models.CharField(max_length=10, choices=TITLE_CHOICES)
    name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=70, unique=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
