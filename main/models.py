from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Language(models.Model):
    code = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Tasks(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    question = RichTextField(blank=True)
    desk = RichTextField(blank=True)
    solution = RichTextField(blank=True)
    index_id = models.IntegerField(default=0)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class Clue(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, blank=True, null=True)
    desk = RichTextField(blank=True)
    position = models.IntegerField(default=0)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.desk


class Comment(models.Model):
    advice = RichTextField(blank=True)
    index_id = models.IntegerField(default=0)
    comment_id = models.IntegerField(default=0)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.advice
    

class Trans(models.Model):
    key = models.CharField(max_length=100)  # masalan: 'choose_language', 'send' va h.k.
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    value = models.TextField()  # Tarjima matni
    position = models.IntegerField(default=0)  # Keyinchalik sort qilish uchun

    def __str__(self):
        return f"{self.key} ({self.language.code})"



