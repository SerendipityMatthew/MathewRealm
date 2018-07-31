from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_time = models.DateTimeField('created time', default=now)
    last_mod_time = models.DateTimeField('last modified time', default=now)





class Article(BaseModel):
    title = models.CharField('title', max_length=200, unique=True)
    content = models.TextField('content')
    publish_time = models.DateTimeField('publish_time', blank=True,
        null=True)
    views = models.PositiveIntegerField('page_view', default=0)
    author = models.CharField('author', max_length=50, verbose_name='Author')
    category = models.CharField('category', max_length=50)
    tags = models.CharField('tags', verbose_name='TAG', blank=True)
    
    def __str__(self):
        return self.title
    
    def viewed(self):
        self.views += 1
        
