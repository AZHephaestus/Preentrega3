from django.db import models

class game(models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.nombre
    
class gamegenre(models.Model):
    genero = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self) -> str:
        return self.genero
    
class gamebygenre(models.Model):
    game = models.ForeignKey(game, on_delete = models.CASCADE)
    genre = models.ForeignKey(gamegenre, on_delete = models.CASCADE)
    def __str__(self) -> str:
        return f"{self.game}:{self.genre}"