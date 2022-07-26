from django.db import models

class Empresa(models.Model):
  name    = models.CharField('Empresa', max_length = 255, blank = True, null = True)
  address = models.CharField('Direccion',max_length = 255, blank = True, null = True)
  nit     = models.CharField('NIT',max_length = 255, unique = True, blank = True, null = True)
  phone   = models.IntegerField('Telefono', blank = True, null = True)
      
  def __str__(self):
    return self.name
