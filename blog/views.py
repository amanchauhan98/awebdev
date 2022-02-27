from django.shortcuts import render, HttpResponse
from blog.models import theory_topic, course_blog

def index(request):
    blog_theory = theory_topic.objects.all()
    course_detail = course_blog.objects.all()
    params = {
        "blog_theory":blog_theory,
        "course_detail":course_detail
    }
    return render(request, 'blogindex.html', params)


