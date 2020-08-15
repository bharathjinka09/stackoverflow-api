from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer
from bs4 import BeautifulSoup

import json,requests
# Create your views here.


def home(request):
    return HttpResponse('Questions')

class QuestionApi(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-id')
    serializer_class = QuestionSerializer


def latest(request):
    try:
        res = requests.get("https://stackoverflow.com/questions")

        soup = BeautifulSoup(res.text, "html.parser")
        
        questions = soup.select(".question-summary")

        for que in questions:
            q = que.select_one('.question-hyperlink').getText()
            vote_count = que.select_one('.vote-count-post').getText()
            views = que.select_one('.views').attrs['title']
            tags = [tag.getText() for tag in (que.select('.post-tag'))]
            time = que.select_one(".relativetime").getText()
            asked_by = que.select_one(".user-details").a.getText()

            question = Question()
            question.question = q
            question.vote_count = vote_count
            question.views = views
            question.tags = tags
            question.time = time
            question.asked_by = asked_by

            question.save()
        return HttpResponse('Latest data fetched from stackoverflow')
    
    except Exception as e:
        print(e)


