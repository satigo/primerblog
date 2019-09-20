from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion
from django.shortcuts import render, get_object_or_404


# Create your views here.
def post_list(request):
    publicaciones = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/post_list.html', {'publicaciones' : publicaciones})


def post_detail(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/post_detail.html', {'publicacion': publicacion})
