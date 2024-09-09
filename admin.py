from django.contrib import admin
from .models import BlogPost, Question, Answer

admin.site.register(BlogPost)
admin.site.register(Question)
admin.site.register(Answer)