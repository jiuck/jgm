# Create your models here.
from django.db    import models 
from django.utils import timezone
 

class Tags(models.Model):
    tag = models.CharField(max_length=35)

    def __str__(self):
        return self.tag        

class Post(models.Model): 
    headline  = models.CharField(max_length=255)
    text      = models.TextField()
    pub_date  = models.DateTimeField()
    mod_date  = models.DateTimeField(default=timezone.now)
    #author    = models.ManyToManyField(Author)
    kudos     = models.IntegerField(default=0)
    draft     = models.BooleanField(default=True)
    image     = models.ImageField(upload_to = 'image/', blank=True)
    #post_tags = models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.headline

    def publish(self):
        self.pub_date = timezone.now()
        self.draft = False
        self.save()

    def addKudos(self):
    	self.kudos = self.kudos + 1
    	self.save()

    class Meta: 
        ordering = ["-pub_date", "mod_date"] 
        verbose_name_plural = "Posts" 
