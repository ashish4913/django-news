from django.db import models


# Create your models here.
class category(models.Model):
    cat=models.CharField(max_length=20)
    catid=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.cat
