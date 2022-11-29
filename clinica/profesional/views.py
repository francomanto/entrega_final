from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from profesional.forms import CommentForm
from profesional.forms import ProfesionalForm
from profesional.models import Comment
from profesional.models import Profesional


class ProfesionalListView(ListView):
    model = Profesional
    paginate_by = 3

class ProfesionalDetailView(DetailView):
    model = Profesional
    template_name = "profesional/profesional_detail.html"
    fields = ["name", "last_name","email", "especialidad","tel", "description", "image"]

    def get(self, request, pk):
        profesional = Profesional.objects.get(id=pk)
        comments = Comment.objects.filter(profesional=profesional).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "profesional": profesional,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)

class ProfesionalCreateView(LoginRequiredMixin, CreateView):
    model = Profesional
    success_url = reverse_lazy("profesional:profesional-list")

    form_class = ProfesionalForm

    def form_valid(self, form):
        """Filter to avoid duplicate profesionales"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Profesional.objects.filter(
            name=data["name"], last_name=data["last_name"], email=data["email"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El profesional {data['name']} - {data['last_name']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Profesional {data['name']} {data['last_name']} creado exitosamente!",
            )
            return super().form_valid(form)
        
class ProfesionalUpdateView(LoginRequiredMixin, UpdateView):
    model = Profesional
    fields = ["name", "last_name","email", "especialidad","tel", "description", "image" ]

    def get_success_url(self):
        profesional_id = self.kwargs["pk"]
        return reverse_lazy("profesional:profesional-detail", kwargs={"pk": profesional_id})
    

class ProfesionalDeleteView(LoginRequiredMixin, DeleteView):
    model = Profesional
    success_url = reverse_lazy("profesional:profesional-list")

class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        profesional = get_object_or_404(Profesional, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, profesional=profesional
        )
        comment.save()
        return redirect(reverse("profesional:profesional-detail", kwargs={"pk": pk}))
    
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        profesional = self.object.profesional
        return reverse("profesional:profesional-detail", kwargs={"pk": profesional.id})

