# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('News Title',{'fields':['question_text']}),('Date Information',{'fields':['pub_date'],'classes':['collapse']}),]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 30

#admin.site.register(Question)
admin.site.register(Question,QuestionAdmin)
