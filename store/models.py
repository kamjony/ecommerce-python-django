from django.db import models

from django.urls import reverse

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True) #db index: is used for query acceleration. 
    #Improved memory usage and faster lookup for the table. 

    slug = models.SlugField(max_length=250, unique=True)


    #Used to change object name
    class Meta:
        verbose_name_plural = 'categories' 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])
    

class Product(models.Model):

    # FK
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField(blank=True)  #Textfield for lots of characters
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'products' 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])












