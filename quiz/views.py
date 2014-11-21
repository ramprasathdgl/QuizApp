from __future__ import division
from django.shortcuts import render, redirect
from quiz.models import Question
from quiz.forms import UserDetailForm, QuestionForm
# from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

questions = []
DEBUG = True


def get_user_detail(request):
    if request.method == "POST":
        form = UserDetailForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect("/quiz/quiz/")
        else:
            print form.errors
    else:
        form = UserDetailForm()

    return render(request, 'quiz/register.html', {'form': form})


def quiz(request):
    global questions
    questions = Question.objects.all()
    FORM = []
    if request.method == "POST":
        choice = request.POST.get("title")
        if choice:
            k, v = eval(choice)
            request.session[k] = v
        if DEBUG:
            print "request.POST==================>", request.POST
            print "request.session==================>",\
                request.session.get("page")
        page = request.session.get("page")
        if page <= request.session.get("num_pages"):
            url_ = "/quiz/quiz/?page={0}".format(page)
        else:
            # return HttpResponse("Reached the Final Page")
            url_ = "/quiz/result/"
        return redirect(url_)
    else:
        for q in questions:
            form = QuestionForm(q)
            FORM.append(form)
        paginator = Paginator(FORM, 1)
        print "request.GET==================>", request.GET
        page = request.GET.get("page")
        print "request.pageno==================>", paginator.num_pages
        request.session["num_pages"] = int(paginator.num_pages)
        try:
            if page:
                pages = int(page) + 1
                request.session["page"] = pages
            FORM = paginator.page(page)
        except PageNotAnInteger:
            FORM = paginator.page(1)
            request.session["page"] = 2
        except EmptyPage:
            FORM = paginator.page(
                paginator.num_pages)

        return render(request, 'quiz/questions.html', {'FORM': FORM})


def result(request):
    choice = {}
    print request.session.items()
    for i in questions:
        key = str(i.id)
        choice[i] = request.session.get(key, False)
    quest_answered = len([v for v in choice.values() if v])
    correct_answer_count = 0
    for k, v in choice.items():
        if v:
            if k.answer_text.strip() == str(v).strip():
                correct_answer_count += 1
    percentage = (correct_answer_count / 14)*100
    context = {'question_list': questions, 'choice_': choice,
               "quest_answered": quest_answered,
               'correct_answer_count': correct_answer_count,
               'percentage': percentage}
    request.session.flush()
    return render(request, 'quiz/results.html', context)
