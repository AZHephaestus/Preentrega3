from django.db import models

class game(models.Model):
    nombre = models.CharField(max_length = 100, verbose_name="Nombre")
    precio = models.FloatField(null=True, blank=True, verbose_name="Precio")
    descripcion = models.TextField(max_length = 9999, null=True, blank=True, verbose_name="Descripción")
    def __str__(self) -> str:
        return f"{self.nombre}"
    
class gamegenre(models.Model):
    genero = models.CharField(max_length = 100, null = True, blank = True, verbose_name="Género")

    def __str__(self) -> str:
        return self.genero
    
class gamebygenre(models.Model):
    game = models.ForeignKey(game, on_delete = models.CASCADE, verbose_name="Juego")
    genre = models.ForeignKey(gamegenre, on_delete = models.CASCADE, verbose_name="Género")
    def __str__(self) -> str:
        return f"{self.game}:{self.genre}"
    
