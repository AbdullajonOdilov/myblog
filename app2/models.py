from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=300)
    sana = models.DateField()
    matn = models.TextField()
    rasm = models.FileField(blank=True, null=True)
    def __str__(self):
        return self.sarlavha

class Intervyu(models.Model):
    sarlavha = models.CharField(max_length=200)
    sana = models.DateField()
    link = models.CharField(max_length=200)
    rasm = models.FileField(blank=True, null=True)
    def __str__(self):
        return self.sarlavha
