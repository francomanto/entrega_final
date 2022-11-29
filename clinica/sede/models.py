from django.db import models

class Sede(models.Model):
    name = models.CharField(max_length=40)
    cod = models.IntegerField()
    tel= models.IntegerField()
    dir= models.CharField(max_length=40)

    def __str__(self):
        return f"Sede: {self.name} | codigo: {self.cod} | direccion: {self.dir}"
    