from django.db import models

class Person(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large"
    }
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    qte = models.IntegerField(blank=True, default=0, null=True, verbose_name='quantité')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
        
    
    def __str__(self):
        return self.name
    
    def publish(self):
        prix_total = self.qte * self.prix
        return prix_total
        self.save()
    
    def general(self):
        som = 0
        for i in Person.objects.all():
            som = som + i.prix * i.qte
        return som
    
    def nb_client(self):
        a = Person.objects.all()
        return len(a)
    
    def nb_article(self):
        soma = 0
        for nb in Person.objects.all():
            soma = soma + nb.qte
        return soma
    
    
    
