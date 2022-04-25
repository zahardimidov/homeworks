from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    image=models.ImageField()
    release_date=models.DateField()
    lte_exists=models.BooleanField()

    slug=models.SlugField()
