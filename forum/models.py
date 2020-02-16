from django.db import models

# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
