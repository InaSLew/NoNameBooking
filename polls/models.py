import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def display_choices_and_votes(self):
        choices_dict = dict()
        for choice in self.choice_set.all():
            choices_dict[choice] = choice.votes
        return choices_dict
    display_choices_and_votes.short_description = 'Choices and their number of votes'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #each Choice is associated with a Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text