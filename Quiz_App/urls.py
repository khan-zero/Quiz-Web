from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/<int:id>/', views.quiz, name='quiz'),
    path('create', views.create, name='create'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('create_questionset/', views.create_questionset, name='create_questionset'),
    path('create_question/', views.create_question, name='create_question'),
    path('create_option/', views.create_option, name='create_option'),
    path('submit_answer/', views.submit_answer, name='submit_answer'),
    path('submit_answerdetail/', views.submit_answerdetail, name='submit_answerdetail'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
