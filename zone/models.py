from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class tags(models.Model):
    name = models.CharField(max_length=30, unique=True)
    # user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-name']

    def save_tag(self):
        self.save()

class Profile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile",primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    bio = models.CharField(max_length=60, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    # profile_avatar = ProcessedImageField(upload_to = 'avatars/', processors=[ResizeToFill(100,100)], format = 'JPEG', options ={'quality':60})
    def __str__(self):
        return self.user_name.username

        # class Meta:
        #     ordering = ['user_name']

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_name=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def all_profiles(cls):
        all_profiles = cls.objects.all()
        return all_profiles

    @classmethod
    def search_profile(cls, profiles_name):
        return cls.objects.filter(user_name__user_name=profiles_name)

       

class Images(models.Model):
    image = models.ImageField(upload_to = 'posts/',default="")
    name = models.CharField(max_length=30, null=True)
    location = models.CharField(max_length=60)
    caption = models.TextField()
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tags, null=True)
    # comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    # likes = models.PositiveIntegerField(default=0)
    # user_liked= models.ManyToManyField(User,related_name='post_likes')

    def __str__(self):
        return self.image

    class Meta:
        ordering = ['-time']

    def save_image(self):
        self.save()
    
    @classmethod
    def get_all_images(cls):
        images = cls.objects.order_by(time)
        return images


    @classmethod
    def get_all_profiles(cls):
        profiless = Profile.objects.all()
        return profiles

    @classmethod
    def search_profile(cls,query):
        result = cls.objects.filter(user_name__username__icontains=query).first()
        return result

    @classmethod 
    def update_caption(cls):
        caption = cls.object.get(caption)    

class Comments(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Images, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ['-time']

    def save_comment(self):
        self.save()

    @classmethod
    def get_comment(cls,image_id):
        post_comment = Comments.objects.filter(post=image_id)
        return post_comment





class Follow(models.Model):
    following = models.ForeignKey(User, related_name="who_follows")
    follower = models.ForeignKey(User, related_name="who_is_followed")
    followed_time = models.DateTimeField(auto_now_add=True)
    #       
    def following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0 
    def __unicode__(self):
          return str(self.follow_time)

# class Like(models.Model):
#     liker = models.ForeignKey(User, related_name='liker')
#     image = models.ForeignKey(Images, related_name='image')
#     liked = models.BooleanField()
