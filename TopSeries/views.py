from django.shortcuts import render
from TopSeries.models import serie

# Create your views here.
def mostrar_texto(request):
    series = serie.objects.all()

    return render(request, 'TopSeries/index_TopSeries.html', {'series': series})


