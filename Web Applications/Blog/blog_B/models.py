from django.db import models

# Create your models here.
class BlogPost(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string rep of blog topic."""
        return self.text

class Entry(models.Model):
    title = models.ForeignKey(BlogPost)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        """Return string rep of the topic content."""
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text