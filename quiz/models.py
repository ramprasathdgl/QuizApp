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


class ResultPercentage(models.Model):
    # 0% - 25%
    firstquarter = models.IntegerField(default=0)
    # 25% - 50%
    secondquarter = models.IntegerField(default=0)
    # 50% - 75%
    thirdquarter = models.IntegerField(default=0)
    # 75% - 100%
    fourthquarter = models.IntegerField(default=0)

    def updatepercentage(self, percent):
        if percent > 0 and percent <= 25.0:
            self.firstquarter += 1
        elif percent <= 50 and percent > 25:
            self.secondquarter += 1
        elif percent > 50 and percent <= 75:
            self.thirdquarter += 1
        elif percent > 75 and percent <= 100:
            self.fourthquarter += 1
