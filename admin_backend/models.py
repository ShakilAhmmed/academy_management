from django.db import models


# Create your models here.
class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Timestamp):
    category_code = models.CharField(unique=True, db_index=True, max_length=100)
    category_title = models.CharField(unique=True, max_length=100)
    category_slug = models.CharField(unique=True, max_length=100)
    category_status = models.BooleanField(default=1)
