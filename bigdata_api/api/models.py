from django.db import models

class LargeDataset(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
