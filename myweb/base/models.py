from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Pict(models.Model):
    picture=models.CharField(max_length=400)
    # name=models.CharField(max_length=200)
    # author=models.CharField(max_length=200)
    # description=models.TextField(max_length=500)
    # content=models.CharField(max_length=200)

  # def __str__(self):
    #     return f"{self.name} _ {self.author}"

class JobCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
class JobListing(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    # published_at = models.DateTimeField(auto_now_add=True)
    # filled = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    # applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job_listing.title}"

# class User(AbstractUser):
#     job_listing=models.ManyToManyField(JobListing, related_name='job_listing', blank=True)
#
#
