from django.db import models

class Author(models.Model):
    author_id = models.IntegerField(unique=True, primary_key=True)
    author_lnme = models.CharField(max_length=100)
    author_fname = models.CharField(max_length=100)
    author_bdate=models.DateTimeField('Birth Date')
    author_hdate=models.DateTimeField('Hire Date')
    author_salary = models.IntegerField(default=0)
    
class News(models.Model):
    article_id = models.IntegerField(unique=True, primary_key=True)
    article_text = models.CharField(max_length=200)
    post_date=models.DateTimeField('Published Date')
    author_id = models.ForeignKey(Author, to_field='author_id')
# Create your models here.
