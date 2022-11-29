from django import forms


class SedeForm(forms.Form):
    name = forms.CharField(
        label="Nombre de la Sede",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "sede-name",
                "placeholder": "Nombre de la sede",
                "required": "True",
            }
        ),
    )
    cod = forms.IntegerField(
        label="Código de la Sede",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "sede-cod",
                "placeholder": "Código",
                "required": "True",
            }
        ),
    )
    dir = forms.CharField(
        label="Direccion:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "sede-dir",
                "placeholder": "Direccion",
                "required": "True",
            }
        ),
    )
    
    tel = forms.IntegerField(
        label="Telefono:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "sede-tel",
                "placeholder": "Telefono",
                "required": "True",
            }
        ),
    )