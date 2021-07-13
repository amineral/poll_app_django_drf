from django.urls import path, include
from . import views
from .views import QuestionViewSet, ChoiceViewSet, PollViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('question', QuestionViewSet, basename='question')
router.register('choice', ChoiceViewSet, basename='choice')
router.register('poll', PollViewSet, basename='poll')

urlpatterns = [
    path('', include(router.urls)), 
    path('polls_list/', views.polls_list, name='polls_list'),
    path('poll/<int:id>', views.poll, name='poll'),
    path('poll/question/<int:id>', views.question, name='question')
]