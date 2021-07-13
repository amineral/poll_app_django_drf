from rest_framework import serializers
from .models import Question, Choice, Poll

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer
    class Meta:
        model = Choice
        fields = '__all__'

        