from django.urls import path
from . import views

urlpatterns = [
    path('anatomy_answers', views.anatomy_llm),
]