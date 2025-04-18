from django.contrib import admin
from django.urls import path

from app import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('/hot', views.hot, name = "hot"),
    path('/reg', views.reg, name = "reg"),
    path('/log', views.log, name = "log"),
    path('/ask', views.ask, name = "ask"),

    path('/question/<int:question_id>',views.question, name = "question")
]
