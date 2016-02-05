# Create your models here.
import random
from django.db                import models 
from django.db.models.signals import pre_save
from django.utils             import timezone
from django.utils.text        import slugify

class Tags(models.Model):
    tag = models.CharField(max_length=35)

    def __str__(self):
        return self.tag        

class Category(models.Model):
    category = models.CharField(max_length=35)

    def __str__(self):
        return self.category        

class Post(models.Model): 
    headline  = models.CharField(max_length=255)
    slug      = models.SlugField(unique=True)
    text      = models.TextField()
    pub_date  = models.DateTimeField(blank=True, null=True)
    mod_date  = models.DateTimeField(default=timezone.now)
    #author    = 
    #category  = models.ManyToOne(Category)
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

    def get_absolute_url(self): 
        return True

    class Meta: 
        ordering = ["-pub_date", "mod_date"] 
        verbose_name_plural = "Posts" 

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.headline)
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
    instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Post)
