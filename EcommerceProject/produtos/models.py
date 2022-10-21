from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produto', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add =True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name