from django.db import models
from slugify import slugify

from account.models import User


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Course(models.Model):
    user = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    sub_title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    language_list = (
        ('en', 'English'),
        ('ru', 'Russian'),
        ('kg', 'Kyrgyz'),
    )
    language = models.CharField(max_length=2, choices=language_list, default="ru")
    level = models.IntegerField(default=1, blank=True)
    sub_category = models.IntegerField(blank=True)
    image = models.ImageField(blank=True, upload_to="media/images/")
    video = models.FileField(blank=True, upload_to="media/videos/")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class CourseItem(models.Model):
    course = models.ForeignKey(Course, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class CourseItemFile(models.Model):
    course_item = models.ForeignKey(CourseItem, related_name="files", on_delete=models.CASCADE)
    file = models.FileField(blank=True, upload_to="media/files/")

    def __str__(self):
        return f'files of: {self.course_item.title}'


class Archive(models.Model):
    user = models.ForeignKey(User, related_name='archives', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='archives', on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='orders', on_delete=models.CASCADE)
