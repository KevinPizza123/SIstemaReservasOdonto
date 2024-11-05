from django.shortcuts import render, redirect
from .models import Paciente, Cita
from .forms import CitaForm

def reservar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citas')
    else:
        form = CitaForm()
    return render(request, 'reservas/reservar_cita.html', {'form': form})

def listar_citas(request):
    citas = Cita.objects.all()
    return render(request, 'reservas/listar_citas.html', {'citas': citas})
