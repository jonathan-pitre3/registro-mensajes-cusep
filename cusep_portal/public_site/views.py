from django.shortcuts import redirect, render
from .forms import SolicitudServicioForm


def home(request):
    return render(request, 'public_site/home.html')


def services(request):
    return render(request, 'public_site/servicios.html')


def about(request):
    return render(request, 'public_site/sobre_nosotros.html')


def intake_form(request):
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solicitud_enviada')
    else:
        form = SolicitudServicioForm()
    return render(request, 'public_site/formulario.html', {'form': form})


def submitted(request):
    return render(request, 'public_site/solicitud_enviada.html')
