from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Question

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts})

def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'question_list.html', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'question_detail.html', {'question': question})

def contact_page(request):
    return render(request, 'contact.html')