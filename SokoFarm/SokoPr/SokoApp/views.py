
from django.http import HttpResponse
from django.template import loader

def SokoApp(request):
    template = loader.get_template('SokoFarmApp.html')
    return HttpResponse(template.render())

# Create your views here.
