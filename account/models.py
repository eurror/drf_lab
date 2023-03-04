from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from slugify import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            return ValueError('email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    experience = models.IntegerField(default=0)
    audience = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)
    activation_code = models.CharField(max_length=10, default=get_random_string(10))

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    competence = models.CharField(max_length=255, blank=True)
    language_list = (
        ('en', 'English'),
        ('ru', 'Russian'),
        ('kg', 'Kyrgyz'),
    )
    language = models.CharField(max_length=2, choices=language_list, default="ru")
    site = models.URLField(max_length=255, blank=True)
    twitter = models.URLField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)
    linkedin = models.URLField(max_length=255, blank=True)
    youtube  = models.URLField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to="media/")
    is_hidden = models.BooleanField(default=False)
    is_hidden_courses = models.BooleanField(default=False)
    promotions = models.BooleanField(default=False)
    mentor_ads = models.BooleanField(default=False)
    email_ads = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
