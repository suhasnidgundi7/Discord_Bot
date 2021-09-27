from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question
from .serializers import RandomQuestionSerializer

# Create your views here.
class RandomQuestion(APIView):
    def get(self, request, formate=None, **kwargs):
        question = Question.objects.filter().order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)