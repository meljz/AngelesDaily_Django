from django.db import models


""" THIS PART IS FOR INPUTTING ARTICLES (CAN BE DONE IN ADMIN)"""
class Articles (models.Model):
    article_title = models.CharField (max_length=100) 
    article_image = models.ImageField (upload_to="my_images", blank=True, null=True)
    article_story = models.CharField (max_length=300)
    created_at =  models.DateTimeField (auto_now_add=True)

    def __str__ (self):                 # this will set the proper names in the list of admin panel
        return self.article_title
    
class Blogs (models.Model):
    blog_title = models.CharField (max_length=100) 
    blog_image = models.ImageField (upload_to="my_images", blank=True, null=True)
    blog_story = models.TextField()
    created_at =  models.DateTimeField (auto_now_add=True)

    def __str__ (self):                 # this will set the proper names in the list of admin panel
        return self.blog_title
    