from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import Vacuna

def registrar_persona(request):
    if request.method == 'POST':
        persona_form = PersonaForm(request.POST)
        if persona_form.is_valid():
            # Guardar los datos de la persona
            persona = persona_form.save()

            # Obtener los datos de la única vacuna
            tipo_vacuna = request.POST.get('tipo_vacuna')
            fecha_aplicacion = request.POST.get('fecha_aplicacion')

            if tipo_vacuna and fecha_aplicacion:  # Si ambos campos tienen datos
                Vacuna.objects.create(
                    persona=persona,
                    tipo_vacuna=tipo_vacuna,
                    fecha_aplicacion=fecha_aplicacion
                )
            return redirect('success')  # Redirige a una página de éxito
    else:
        persona_form = PersonaForm()
    return render(request, 'persona_form.html', {'persona_form': persona_form})

from django.shortcuts import render, get_object_or_404
from .models import Persona, Vacuna

def buscar_informe(request):
    persona = None
    vacunas = None

    if request.method == 'POST':
        numero_documento = request.POST.get('numero_documento')  # Mantén el nombre del input en el formulario
        try:
            persona = Persona.objects.get(numero_documento=numero_documento)
            vacunas = Vacuna.objects.filter(persona=persona)
        except Persona.DoesNotExist:
            persona = None
            vacunas = None
            mensaje = "No se encontró una persona con ese número de documento."
            return render(request, 'informe.html', {'mensaje': mensaje})
    
    return render(request, 'informe.html', {'persona': persona, 'vacunas': vacunas})

