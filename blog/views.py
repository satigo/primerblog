from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion
from django.shortcuts import render, get_object_or_404
from .forms import PublicacionForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    publicaciones = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/post_list.html', {'publicaciones' : publicaciones})


def post_detail(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/post_detail.html', {'publicacion': publicacion})

def publicacion_nueva(request):
    if request.method == "POST":    
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.fecha_publicacion = timezone.now()
            publicacion.save()
            return redirect('post_detail', pk=publicacion.pk)

    else:
        form = PublicacionForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def publicacion_editar(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.fecha_publicacion = timezone.now()
            publicacion.save()
            return redirect('post_detail', pk=publicacion.pk)
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'blog/post_edit.html', {'form': form})