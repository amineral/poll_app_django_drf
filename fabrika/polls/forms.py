from django import forms
from django.forms import ModelForm
from .models import Question, Poll, Choice

class ChoiceForm(forms.Form):
    answer = forms.ModelChoiceField(queryset=None, widget=forms.RadioSelect)
    def __init__(self, choices, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        self.fields['answer'].queryset = choices
        self.fields['answer'].label = "Choose your answer"
        self.fields['answer'].required = True

class MultipleChoiceForm(forms.Form):
    answer = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)
    def __init__(self, choices, *args, **kwargs):
        super(MultipleChoiceForm, self).__init__(*args, **kwargs)
        self.fields['answer'].queryset = choices
        self.fields['answer'].label = "Choose your answer or answers"
        self.fields['answer'].required = True
        

class UserTextForm(forms.Form):
    answer = forms.CharField(max_length=200, label="Write your answer", required=True)