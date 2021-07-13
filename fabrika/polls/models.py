from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_ending = models.DateTimeField(blank=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    types = [
        ('Choice', 'Choice'),
        ('MultipleChoice', 'MultipleChoice'), 
        ('UserText', 'UserText'),
    ]
    question_type = models.CharField(max_length=14, choices=types, default='Choice')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)

    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.CharField(max_length=200, default=None)
    answer = models.CharField(max_length=50, default=None)
    answer_count = models.IntegerField(default=0)

