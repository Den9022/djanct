from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    def _str_(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Rating(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.rating
