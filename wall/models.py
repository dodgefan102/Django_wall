from django.db import models
from login.models import Users

class WallManager(models.Manager):
    def postVal(self,data):
        pass
    def comVal(self,data):
        pass
    
class Posts(models.Model):
    text=models.CharField(max_length=2048)
    user=models.ForeignKey(Users, related_name='posts', on_delete= models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=WallManager()

class Comments(models.Model):
    text=models.CharField(max_length=2048)
    post=models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    user=models.ForeignKey(Users, related_name='comments', on_delete= models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=WallManager()