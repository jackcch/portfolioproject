from django.db import models

class Blogmodel(models.Model):
    blogtitle=models.CharField(max_length=100)
    blogdate=models.DateField()
    blogcontent=models.TextField()

    def __str__(self):
        return self.blogtitle
