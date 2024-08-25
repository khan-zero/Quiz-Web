from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Quiz, QuestionSet, Question, Option, Answer, AnswerDetail
from .forms import QuestionForm

from colorama import Fore, init

#pip install colorama

#to make difference in terminal
# Initialize colorama | Coloramani ishga tushirish
init(autoreset=True)

def index(request):

    quizzes = Quiz.objects.all()

    # for i in quizzes:
    #     print(Fore.RED + str(f'quiz: {i.name}'))

    context = {
        'quizzes': quizzes,
    }

    return render(request, 'index.html', context)

def quiz(request, id):

    quiz = Quiz.objects.get(id=id)
    question_sets = QuestionSet.objects.filter(quiz=quiz)
    questions = Question.objects.filter(set__in=question_sets)

    opinions = Option.objects.filter(question__in=questions)

    # for i in questions:
    #     print(Fore.RED + str(f"question: {i.name}"))

    # for i in opinions:
    #     print(Fore.RED + str(f"opinion: {i.name}"))

    # for i in quizzes:
    #     print(Fore.RED + str(f'i: {i}'))

    context = {
        'questions': questions,
        'opinions': opinions
    }

    return render(request, 'quiz.html', context)

def create(request):
    return render(request, 'create_question.html')


def create_quiz(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author_id = request.POST.get('author')
        amount = request.POST.get('amount')

        if name and author_id and amount:
            author = User.objects.get(id=author_id)
            Quiz.objects.create(name=name, author=author, amount=amount)
            return redirect('index')

    users = User.objects.all()
    return render(request, 'create_quiz.html', {'users': users})

# Create a QuestionSet
def create_questionset(request):
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz')

        if quiz_id:
            quiz = Quiz.objects.get(id=quiz_id)
            QuestionSet.objects.create(quiz=quiz)
            return redirect('index')

    quizzes = Quiz.objects.all()
    return render(request, 'create_questionset.html', {'quizzes': quizzes})

# Create a Question
def create_question(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        question_set_id = request.POST.get('question_set')

        if name and question_set_id:
            question_set = QuestionSet.objects.get(id=question_set_id)
            Question.objects.create(name=name, set=question_set)
            return redirect('index')

    question_sets = QuestionSet.objects.all()
    return render(request, 'create_question.html', {'question_sets': question_sets})

# Create an Option
def create_option(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        question_id = request.POST.get('question')
        correct = request.POST.get('correct') == 'on'

        if name and question_id:
            question = Question.objects.get(id=question_id)
            Option.objects.create(name=name, question=question, correct=correct)
            return redirect('index')

    questions = Question.objects.all()
    return render(request, 'create_option.html', {'questions': questions})

# Submit an Answer
def submit_answer(request):
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz')
        author_id = request.POST.get('author')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        if quiz_id and author_id and start_time and end_time:
            quiz = Quiz.objects.get(id=quiz_id)
            author = User.objects.get(id=author_id)
            Answer.objects.create(quiz=quiz, author=author, start_time=start_time, end_time=end_time)
            return redirect('index')

    quizzes = Quiz.objects.all()
    users = User.objects.all()
    return render(request, 'submit_answer.html', {'quizzes': quizzes, 'users': users})

# Submit Answer Details
def submit_answerdetail(request):
    if request.method == 'POST':
        answer_id = request.POST.get('answer')
        question_id = request.POST.get('question')
        user_choice_id = request.POST.get('user_choice')

        if answer_id and question_id and user_choice_id:
            answer = Answer.objects.get(id=answer_id)
            question = Question.objects.get(id=question_id)
            user_choice = Option.objects.get(id=user_choice_id)
            AnswerDetail.objects.create(answer=answer, question=question, user_choice=user_choice)
            return redirect('index')

    answers = Answer.objects.all()
    questions = Question.objects.all()
    options = Option.objects.all()
    return render(request, 'submit_answerdetail.html', {
        'answers': answers,
        'questions': questions,
        'options': options,
    })


