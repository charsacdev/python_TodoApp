from django.db import models

# Create your models here.
class TodoList(models.Model):
    text= models.CharField(max_length=45)
    completed = models.BooleanField(default=False)

    #remeber this a class and we need the attribute displayed  with the function below
    def __str__(self):
        return self.text
