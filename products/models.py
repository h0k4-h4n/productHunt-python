from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=0)
    image = models.ImageField()
    icon = models.ImageField()
    body = models.TextField()

    def pub_date_pretty(self):
