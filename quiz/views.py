from __future__ import division
from django.shortcuts import render, redirect
from quiz.models import Question, ResultPercentage
from quiz.forms import UserDetailForm, QuestionForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

questions = []
DEBUG = True


def get_user_detail(request):
    if request.method == "POST":
        form = UserDetailForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # Save the name in session in the name so it can be used in
            # results.html
            request.session["name"] = request.POST["name"]
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
            request.session[str(k)] = v
        if DEBUG:
            print "request.session==================>", request.session.items()
            print "request.session[name]==================>",\
                request.session.get("name")
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
    percentage_ = (correct_answer_count / 14)*100
    # Convert the floating point with two decimal points
    percentage = float("{0:.2f}".format(percentage_))
    tmp = ResultPercentage.objects.all()[0]
    # Custom model method which checks for the range of percentages
    # and saves the values accordingly
    tmp.updatepercentage(percentage)
    # Save the database
    tmp.save()
    result_dict = {'No of questions answered': quest_answered,
                   'No of answers you got right': correct_answer_count,
                   'Percentage': percentage}
    context = {'question_list': questions,
               'choice_': choice,
               'result_dict': result_dict,
               'name': request.session.get("name"),
               }
    # Clear the current sessions
    request.session.flush()
    return render(request, 'quiz/results.html', context)


def draw_graph(request):
    tmp = ResultPercentage.objects.all()[0]
    # Fetch data from the database and pass it to pie
    data = [tmp.firstquarter, tmp.secondquarter, tmp.thirdquarter,
            tmp.fourthquarter]
    explode = (0.05, 0.05, 0.05, 0.05)

    fig = Figure(facecolor='white', figsize=(6, 6), frameon=False, dpi=300)
    ax = fig.add_subplot(111, aspect='equal')
    ax.pie(data,
           explode=explode,
           shadow=False,
           labels=['0% -25%', '25%-50%', '50%-75%', '75%-100%'],
           colors=['b', 'r', 'g'],
           )
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type="image/png")
    canvas.print_figure(response, dpi=300)
    return response
