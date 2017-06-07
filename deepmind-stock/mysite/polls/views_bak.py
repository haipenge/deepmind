# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from .models import Question,Choice
from tools import reset_password
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ','.join([p.question_text for p in latest_question_list])
#    template = loader.get_template('polls/index.html')
#    context = RequestContext(request,{'latest_question_list':latest_question_list,})
    context = {'latest_question_list':latest_question_list}
#    return HttpResponse(output)
#    return HttpResponse(template.render(context))
    return render(request,'polls/index.html',context)

def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
    #return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})    

def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(keyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question': question,'error_message': "you do not select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
#    return HttpResponseRedirect(reverse('pools:results',args=(question.id,)))
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
#    return HttpResponse("You're voting on question %s." % question_id)
