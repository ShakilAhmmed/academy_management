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


class Courses(Timestamp):
    course_title = models.CharField(max_length=100, unique=True)
    course_short_description = models.TextField()
    course_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    level = models.BooleanField(default=1)
    course_language = models.CharField(max_length=50)
    is_top = models.BooleanField(default=0)


class CourseRequirements(Timestamp):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    requirements = models.CharField(max_length=100)


class CourseOutcomes(Timestamp):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    outcomes = models.CharField(max_length=100)


class CoursePricing(Timestamp):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=0)
    price = models.PositiveIntegerField()
    have_discount = models.BooleanField(default=0)
    discount = models.PositiveIntegerField(default=0)


class CourseMediaDetails(Timestamp):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    course_overview_provider = models.CharField(max_length=40)
    course_overview_url = models.URLField(max_length=255)
