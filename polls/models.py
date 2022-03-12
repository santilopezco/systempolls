import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone
# Create your models here.

#SE ESCRIBE CON PIRMERA EN MAYUS Y EN PLURAL 
#Se importa la clase model de Django
#Django crea un ID automáticamente
class Question(models.Model):
    question_text = models.CharField(max_length=200)  #CharField equivale a un VARCHAR en BD
    pu_date = models.DateTimeField("date published")
    
    #creo un metodo. siempre lleva self como primer atributo  
    def __str__(self):  
        return self.question_text 
    
    # creo un método personalizado para quyeretorne si la pregunta fue creada recientemente
    def was_published_recently(self):
        return self.pu_date >= timezone.now() - datetime.timedelta(days=1)
        
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #Llave foanea
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
   
    def __str__(self) -> str:  
        return self.choice_text
    
    