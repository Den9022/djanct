from django.contrib import admin
from .models import Employee
from .models import Question
from .models import Rating

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text']
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
class RatingAdmin(admin.ModelAdmin):
    list_display = ('employee', 'question', 'rating')

# Register your models here.

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Rating, RatingAdmin)