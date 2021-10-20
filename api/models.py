from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True