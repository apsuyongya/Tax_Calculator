from django.shortcuts import render
from .models import News


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Atom'})


def calc(request):
    # val1 = int(request.POST['num1'])
    # val2 = int(request.POST['num2'])
    # res = val1 + val2
    # return render(request, 'home.html', {'result':res})
    job1 = request.POST['job']
    salary1 = int(request.POST['salary'])
    if job1 == "Teacher" or job1 == "teacher" or job1 == "TEACHER":
        if salary1 > 50000:
            res = (10 / 100) * salary1
            return render(request, 'home.html', {'result': res})

        elif 20000 <= salary1 < 50000:
            res = (5 / 100) * salary1
            return render(request, 'home.html', {'result': res})

        else:
            return render(request, 'home.html', {'result': "You don't have to pay tax"})

    else:
        return render(request, 'home.html', {'result': "Sorry. No information"})


def news(request):
    data = News.objects.all()
    return render(request, 'News.html', {'data': data})
