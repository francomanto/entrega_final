from django.shortcuts import render
from django.contrib import messages

from sede.models import Sede
from sede.forms import SedeForm


def get_sedes(request):
    sedes = Sede.objects.all()
    return sedes


def create_sede(request):
    if request.method == "POST":
        sede_form = SedeForm(request.POST)
        if sede_form.is_valid():
            data = sede_form.cleaned_data
            actual_objects = Sede.objects.filter(
                name=data["name"],
                cod=data["cod"],
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"La sede {data['name']} codigo: {data['cod']} ya está creada",
                )
            else:
                sede = Sede(
                    name=data["name"],
                    cod=data["cod"],
                    tel=data["tel"],
                    dir=data["dir"],
                )
                sede.save()
                messages.success(
                    request,
                    f"Sede {data['name']} codigo: {data['cod']} creada exitosamente!",
                )

            return render(
                request=request,
                context={"sedes": get_sedes(request)},
                template_name="sede/sede_list.html",
            )

    sede_form = SedeForm(request.POST)
    context_dict = {"form": sede_form}
    return render(
        request=request,
        context=context_dict,
        template_name="sede/sede_form.html",
    )


def sedes(request):
    sedes = Sede.objects.all()

    context_dict = {"sedes": sedes}

    return render(
        request=request,
        context=context_dict,
        template_name="sede/sede_list.html",
    )


