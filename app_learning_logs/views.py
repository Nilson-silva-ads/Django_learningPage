from django.shortcuts import render

# Create your views here.
def index(request):
    """ Pagina principal do Learning_log """
    return render(request, 'app_learning_logs/index.html')