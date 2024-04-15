from django.contrib.auth.models import User
from django.db import models


class TranslationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_text = models.TextField()
    source_lang = models.CharField(max_length=10)
    target_text = models.TextField()
    target_lang = models.CharField(max_length=10)
    translated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.translated_at}"
