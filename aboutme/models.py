from django.db import models
from django.utils import timezone

# Define Django model object 'Post'
class Post(models.Model):
    author = models.ForeignKey('auth.User') # Link to another model
    title = models.CharField(max_length=200) # Define text with limited number of characters
    text = models.TextField() # Limitless length text field. Ideal for blog post content.
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # Define publish function using timezone.now() and save.()
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Return text string with Post title
    def __str__(self):
        return self.title

