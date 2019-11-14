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

    def __str__(self):
        return f"({self.category_code})-{self.category_title}"


class SubCategory(Timestamp):
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    sub_category_code = models.CharField(unique=True, max_length=100, db_index=True)
    sub_category_title = models.CharField(unique=True, max_length=100, db_index=True)
    sub_category_slug = models.CharField(unique=True, max_length=100)
    sub_category_status = models.BooleanField(default=1)
