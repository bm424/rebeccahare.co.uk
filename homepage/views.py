from django.shortcuts import render
from homepage.models import *
from photologue.models import Gallery


def index(request):
    return render(request, 'index.html')


def about(request):
    about = Actor.objects.first()
    return render(request, 'about.html', {'about': about})


def cv(request):
    theatre_credits = TheatreCredit.objects.order_by('-final')
    education = Education.objects.order_by('end_date')
    skills = Skill.objects.all()
    about = Actor.objects.first()
    context = {
        'theatre_credits': theatre_credits,
        'education': education,
        'skills': skills,
        'about': about,
    }
    return render(request, 'cv.html', context)


# def gallery_list(request):
#     gallery = Gallery.objects.all()
#     return render(request, 'gallery.html', {'gallery': gallery})


def gallery_detail(request, slug):
    gallery = Gallery.objects.get(slug=slug)
    return render(request, 'gallery_detail.html', {'gallery': gallery})

