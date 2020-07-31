from django.shortcuts import render
from .models import Item, Course

# Create your views here.

def index(request):
    courses=Course.objects.all()
    return render(request, 'index.html', {'courses':courses})

def video(request, course_code, pos):
    videos = Item.objects.filter(code = course_code)

    course_qs = Course.objects.filter(code= course_code)
    if course_qs.exists():
        course = course_qs.first()

    video = videos.filter(position = pos)

    obj = [videos, course]

    return render(request, 'course.html', {'obj':obj, 'pos':pos})
