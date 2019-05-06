from django.db import models

# Create your models here.
class Pizza(models.Model):
    text = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = 'pizza'

    def __str__(self):
        """Return a string when called"""
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza)
    text = models.TextField()

    def __str__(self):
        """Return sample string of toppings"""
        if len(self.text) < 40:
            return self.text
        else:
            return self.text[:40] + '...'