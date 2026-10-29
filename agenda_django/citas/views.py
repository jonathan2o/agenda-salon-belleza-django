import random
from django.shortcuts import render
from .models import Cita
from .forms import CitaForm

def inicio(request):
    form = CitaForm()
    return render(request, 'citas/inicio.html', {'form': form})


def agendar_cita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)

            while True:
                nuevo_codigo = str(random.randint(1000, 9999))
                if not Cita.objects.filter(codigo=nuevo_codigo).exists():
                    cita.codigo = nuevo_codigo
                    break

            cita.save()
            return render(request, "citas/confirmacion.html", {"cita": cita})

    return render(request, "citas/inicio.html", {"form": CitaForm()})


def consultar_cita(request):
    cita = None
    if request.method == "POST":
        codigo = request.POST.get("codigo")
        try:
            cita = Cita.objects.get(codigo=codigo, activa=True)
        except Cita.DoesNotExist:
            pass

    return render(request, "citas/consultar.html", {"cita": cita})

def cancelar_cita(request, codigo):
    try:
        cita = Cita.objects.get(codigo=codigo, activa=True)
        cita.activa = False
        cita.save()
        return render(request, "citas/cancelada.html", {"cita": cita})
    except Cita.DoesNotExist:
        return render(request, "citas/cancelada.html", {"error": True})
