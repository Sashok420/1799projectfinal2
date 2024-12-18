from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AvatarUploadForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def russia(request):
    return render(request, 'main/russia.html')


def japan(request):
    return render(request, 'main/japan.html')


def india(request):
    return render(request, 'main/india.html')


def china(request):
    return render(request, 'main/china.html')


def italy(request):
    return render(request, 'main/italy.html')


def ireland(request):
    return render(request, 'main/ireland.html')


def iceland(request):
    return render(request, 'main/iceland.html')


def germany(request):
    return render(request, 'main/germany.html')


def france(request):
    return render(request, 'main/france.html')


def austria(request):
    return render(request, 'main/austria.html')


def profile_view(request):
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AvatarUploadForm(instance=request.user)

    return render(request, 'main/profile.html', {'form': form})


def test_view(request):
    test_completed = request.session.get('test_completed', request.user.test_score)

    if request.method == "POST" and not test_completed:
        correct_answers = ["Россия", "Германия", "Индия", "Ирландия", "Австрия"]
        user_answers = [
            request.POST.get('question_1'),
            request.POST.get('question_2'),
            request.POST.get('question_3'),
            request.POST.get('question_4'),
            request.POST.get('question_5'),
        ]

        score = sum(1 for correct, user in zip(correct_answers, user_answers) if correct == user)

        request.user.test_score = score
        request.user.save()

        return render(request, 'main/test.html', {
            'result': score,
            'test_completed': True
        })

    return render(request, 'main/test.html', {
        'test_completed': test_completed,
    })
