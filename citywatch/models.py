from django.db import models

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    image = models.ImageField(blank=True, null=True, upload_to='images/issue/')
    category = models.ForeignKey('IssueCategory', on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='OPEN')

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class IssueCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
    
class IssueComment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment