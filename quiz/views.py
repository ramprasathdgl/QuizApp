from django.shortcuts import render, get_object_or_404
from quiz.models import Question
from quiz.forms import UserDetailForm
from django.http import HttpResponse, HttpResponseRedirect

questions = []


def get_user_detail(request):
    if request.method == "POST":
        form = UserDetailForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = UserDetailForm()

    return render(request, 'quiz/register.html', {'form': form})


def index(request):
    global questions
    print request.POST.items()
    user_name = request.POST["name"]
    if user_name != "":
        print "User_name", user_name
        request.session['name'] = user_name
    questions = Question.objects.all()
    context = {'question_list': questions}
    print "session >>>>>>>>>>>>>>>>>>>>>>>>>>>>##\n"
    print request.session['name']
    return render(request, 'quiz/index.html', context)


def next(request):
    choice = {}
    for i in questions:
        key = str(i.id)
        choice[i] = request.POST.get(key, False)
        context = {'question_list': questions, 'choice_': choice}
    print choice
    print "session >>>>>>>>>>>>>>>>>>>>>>>>>>>>##\n"
    print request.session['name']
    return render(request, 'quiz/results.html', context)
