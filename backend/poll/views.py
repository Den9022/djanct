from django.shortcuts import render
from rest_framework import viewsets
from .serializers import QuestionSerializer
from .serializers import EmployeeSerializer
from .serializers import RatingSerializer
from .models import Employee
from .models import Question
from .models import Rating

# Create your views here.

class QuestionView(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class RatingView(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()