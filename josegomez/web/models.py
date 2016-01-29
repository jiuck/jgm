# Create your models here.
from django.db    import models 
from django.utils import timezone
 
class Post(models.Model): 
    headline = models.CharField(max_length=255)
    text     = models.TextField()
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField(default=timezone.now)
    #author   = models.ManyToManyField(Author)
    kudos    = models.IntegerField()
    draft    = models.BooleanField(default=True)
    image    = models.ImageField(upload_to = 'image/')
    tags     = models.TextField()

    def __str__(self):
        return self.headline

    def publish(self):
        self.pub_date = timezone.now()
        self.draft = False
        self.save()