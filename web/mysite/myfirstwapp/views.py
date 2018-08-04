from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .models import Question, Choice

def index(request):
    q_list = Question.objects.order_by('-pub_date')[:3]
    temp = loader.get_template('./myfirstwapp/index.html')
    #out = ' '.join([q.question_text for q in q_list])
    context = {

        'latest_question_list': q_list,
    }
    return HttpResponse(temp.render(context, request))


def detail(request, question_id):
    try:
        q = Question.objects.get(id=question_id)
    
    except Question.DoesNotExist:
        raise Http404("Invalid Question") 
    return HttpResponse("You're Looking at this Question {}".format(question_id))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myfirstwapp/results.html', {'question': question})

def vote(request, question_id):
    
    question = get_object_or_404(Question, id=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myfirstwapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('myfirstwapp:results', args=(question.id,)))
    #return HttpResponse("Voting on Question {}".format(question_id))





# Create your views here.
