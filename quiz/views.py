from django.shortcuts import render, get_object_or_404
from quiz.models import Question
from django.http import HttpResponse, HttpResponseRedirect

questions = []


def get_user_name(request):
    return render(request, 'quiz/login.html')


def set_user_name_4_session(request):
    print request.method
    if request.method == "GET":
        return render(request, 'quiz/login.html')
    else:
        print "Hi"


def index(request):
    global questions
    user_name = request.POST["user_name"]
    if user_name != "":
        print "User_name", user_name
        request.session['user_name'] = user_name
    else:
        context = {'error_message': "Please Enter Your Name"}
        return render(request, 'quiz/login.html', context)
    questions = Question.objects.all()
    context = {'question_list': questions}
    print "session >>>>>>>>>>>>>>>>>>>>>>>>>>>>##\n"
    print request.session['user_name']
    return render(request, 'quiz/index.html', context)


def next(request):
    choice = {}
    for i in questions:
        key = str(i.id)
        choice[i] = request.POST.get(key, False)
        context = {'question_list': questions, 'choice_': choice}
    print choice
    print "session >>>>>>>>>>>>>>>>>>>>>>>>>>>>##\n"
    print request.session['user_name']
    return render(request, 'quiz/results.html', context)
