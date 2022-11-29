from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField


class Profesional(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    especialidad = models.CharField(max_length=40)
    tel= models.IntegerField()
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='profesional', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = (
            "name",
            "last_name",
            "especialidad",
            "tel",
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"Profesional: {self.name} {self.last_name} | especialidad: {self.especialidad}"
    

class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

