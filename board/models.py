from django.db import models
from accounts.models import CustomUser



class Board(models.Model):

    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    body=models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    post=models.ForeignKey(Board,null=True,on_delete=models.CASCADE,related_name="comments")
    created_at=models.DateTimeField(auto_now_add=True)
    comment=models.TextField(default="")
    
    