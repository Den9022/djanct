from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from poll import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionView, 'question')
router.register(r'employees', views.EmployeeView, 'employee')
router.register(r'ratings', views.RatingView, 'rating')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]