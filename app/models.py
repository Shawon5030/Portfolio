from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Coding_profile_detail(models.Model):
    
    codeforces_rating = models.CharField(max_length=100)
    codeforces = models.CharField(max_length=100,blank=True, null=True)
    
    codechef_star = models.CharField(max_length=50,blank=True, null=True)
    codechef_rating = models.CharField(max_length=100,blank=True, null=True)
    
    leetcode  = models.CharField(max_length=20, blank=True, null=True)
    total_problem_solved = models.IntegerField()
    profile_pic = models.ImageField(blank=True,null=True)
    total_contest = models.IntegerField(blank=True,null=True)
    
    
class Technical_Expertise (models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    
    
from django.db import models
from django.utils import timezone

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    
    
