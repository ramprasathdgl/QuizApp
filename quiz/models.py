from django.db import models

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