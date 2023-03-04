from django.db import models

from account.models import User
from course.models import Course

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='ratings', on_delete=models.CASCADE)
    CHOICES = (
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    )
    rating = models.IntegerField(choices=CHOICES, default=5)

    def __str__(self):
        return f'{self.user} rated {self.course} with {self.rating} stars'


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.body) > 50:
            return f'{self.body[:50]}...'
        else:
            return self.body


class Like(models.ForeignKey):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.is_liked}'
