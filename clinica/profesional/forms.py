from ckeditor.widgets import CKEditorWidget
from django import forms

from profesional.models import Profesional

class ProfesionalForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del Profesional",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesional-name",
                "placeholder": "Nombre de profesional",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido del profesional",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesional-last-name",
                "placeholder": "Apellido del profesional",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesional-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )
    especialidad = forms.CharField(
        label="Especialidad:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesional-especialidad",
                "placeholder": "Especialidad",
                "required": "True",
            }
        ),
    )
    tel = forms.IntegerField(
        label="Telefono:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesional-tel",
                "placeholder": "Telefono",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )

    image = forms.ImageField()

    class Meta:
        model = Profesional
        fields = ["name", "last_name","email","especialidad","tel","description", "image"]


class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )