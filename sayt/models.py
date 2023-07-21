from django.db import models
from .auth_model import User


class Category(models.Model):
    name = models.CharField(max_length=123)
    is_menu = models.BooleanField()

    def __str__(self):
        return self.name


class New(models.Model):
    title = models.CharField(max_length=123)
    short_des = models.TextField()
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    img = models.ImageField()
    view = models.IntegerField(default=0)
    cate = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.view = View.objects.filter(new_id=self.id).count()
        return super(New,self).save(*args, **kwargs)


class Contact(models.Model):
    ism = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    is_trash = models.BooleanField(default=False)
    is_view = models.BooleanField(default=False)
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ism} | trash : {self.is_trash} | Viewed | {self.is_view} |Contacted | {self.contacted}"



class View(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name='new_view')




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    trash = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.trash} | {self.comment}'

# Create your models here.
