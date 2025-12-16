from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """ Pagina principal do Learning_log """
    return render(request, 'app_learning_logs/index.html')

def topics(request):
    """ Mostra todos os assuntos """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'app_learning_logs/topics.html', context)