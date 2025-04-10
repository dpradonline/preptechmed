from django.shortcuts import render, HttpResponse
from .forms import FileUploadForm
from .models import Point, About, Scripture, Introduction, Overview


def home(request):
    intro = Introduction.objects.all()
    overview = Overview.objects.all()
    point = Point.objects.all()
    scripture = Scripture.objects.all()
    return render(request, 'home.html', {'point': point, 'scripture': scripture, 'overview': overview, 'intro': intro})


def more(request):
    point = Point.objects.all()
    return render(request, 'more.html', {'point': point})


def account(request):
    return render(request, 'account.html')


def about(request):
    about = About.objects.all()
    return render(request, 'about.html', {'about': about})


def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Success!")
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})
