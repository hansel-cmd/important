from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField('created_at', auto_now_add=True)

    def __str__(self):
        return f"{type(self).__name__}(author = {self.author}, title = {self.title}, title = {self.category}, content = {self.content})"



class Favorite(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{type(self).__name__}(blog_id = {self.blog_id})"

