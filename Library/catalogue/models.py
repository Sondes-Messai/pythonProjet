from django.db import models

# Create your models here.
class Genre(models.Model):
    
  name = models.CharField(
      max_length=200,
      help_text="genre(s) du livre"
      unique=True,  
  )  
  
  def __str__(self):
      return self.name
  
  class Language(models.Model):
    
   name = models.CharField(
      max_length=200,
      help_text="langue original du livre"
      unique=True,  
  )  
   
   class Author(models.Model):
    
     name = models.CharField(max_length=100)  
     date_birth = models.DateField(null=True,blank=True)
     date_death = models.DateField(null=True,blank=True)
    
  def __str__(self):
      return self.name
  
class Book(models.Model):

 title = models.CharField('Titre',max_length=200)
 summary =models.TimeField(
    'Deprecation',
     max_length=1000,
     help_text="Résumé du livre",
 )
 years = models.DateField('Date de sortie',null=False,blank=False)
 isbn = models.CharField(
     'ISBN',
     max_length=13,
     unique=True,
     help_text="ISBN de 13 caractéres",
 )
 author =models.ForeignKey(
     'Auteur',
     null=True,
     on_delete=models.RESTRICT()
      
 )
 language = models.ForeignKey(
     'lange',
     on_delete=models.SET_NULL,
     null=True,
 )
 genre = models.ManyToManyField(
    Genre, help_text="selectionnez le genre de livre" 
 )

class State(models.Model):
    id = models.UUIDField
    primary_key = True,
    default= uuid.uuid4,
    help_text="Numero unique de livre dans la librirerie"
    )
    book = models.ForeignKey
    
    
    book = models.ForeignKey(
        'Livre'
        on_delete=models.RESTRICT,
        null=True
    )
    date_emrrunt = models.DateField(null=False)
    date_retour = models.DateField(null=True, blank= True)
    Var_status=
         ('m',maintenace
         'd',Disponible
         'r',reservé),
     )
    stattus = models.CharField(
        max_length=1,
        blank=True,
        help_text="status du livre ?"
        choices=Var_status
        
        
    )    
        
        
    