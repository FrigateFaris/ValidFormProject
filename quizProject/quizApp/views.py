from django.shortcuts import render
from quizApp.models import Quiz


# Create your views here.
def show_forms(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_surname = request.POST.get('surname')
        user_nick = request.POST.get('nick')
        user_email = request.POST.get('email')
        user_date = request.POST.get('date')
        user_visit = request.POST.get('place')
        why_we = request.POST.get('we')
        why_filial = request.POST.get('filial')
        computer_work = request.POST.get('computer')
        administration_work = request.POST.get('admins')

        Quiz.objects.create(user_name=user_name,
                            user_surname=user_surname,
                            user_nick=user_nick,
                            user_date=user_date,
                            user_visit=user_visit,
                            user_email=user_email,
                            why_we=why_we,
                            why_filial=why_filial,
                            computer_work=computer_work,
                            administration_work=administration_work)

    return render(request, 'index.html')


def show_plug(request):
    return render(request, 'index2.html')
