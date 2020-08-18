from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        'title': 'E-Sports-Soccer-Blog',
        'teste': 'titulo qualquer'
    }

    return render(request, template_name='index.html', context=context)
