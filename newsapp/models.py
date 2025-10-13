from django.db import models

# Create your models here.
class Articles (models.Model):
    article_title = models.CharField (max_length=100)
    article_story = models.CharField (max_length=300)
    created_at =  models.DateTimeField (auto_now_add=True)

    def __str__ (self):
        return self.article_title