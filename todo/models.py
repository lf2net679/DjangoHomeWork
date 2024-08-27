from django.db import models

# Create your models here.


class Todo(models.Model): #在Django中創建資料表默認為todo_todo
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)  # 預設為 False 

    def __str__(self):
        return self.text
    


class Member(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=128)
    user_email = models.CharField(unique=True, max_length=100)
    user_age = models.IntegerField(default=30)
    user_avatar = models.CharField(max_length=100, default='empty.jpg')
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'member'



