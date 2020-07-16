from django.db import models

# Create your models here.


class Expand(models.Model):
    expression = models.CharField(max_length=100)
    expression1 = models.CharField(max_length=1000)

    def __str__(self):
        return self.expression

