from django.db import models

# 1. 日記のモデル
class Diary(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='diary_images/', blank=True, null=True)

    def __str__(self):
        return self.title

# 2. お問い合わせ内容を保存するモデル
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    # ↓ ここを models.EmailField() に直しました
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}様からのメッセージ ({self.created_at})"