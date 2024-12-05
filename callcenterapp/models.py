from django.db import models

class Book(models.Model):
    chindi = models.TextField()
    cenglish = models.TextField()

    def __str__(self):
        return self.sentence
