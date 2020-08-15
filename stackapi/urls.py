from django.urls import path,include
from .import views
from .views import QuestionApi
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', QuestionApi)

urlpatterns = [
    path('',views.home,name='home'),
    path('',include(router.urls)),
    path('latest',views.latest,name='latest'),
]
