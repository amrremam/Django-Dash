from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.


TYPE_OF_PERSON=(
    ('M' , "MALE"),
    ('F' , "FEMALE"),
)

class Profile(models.Model):

    DOCTOR_IN={
        ('TOOTHS', "TOOTHS"),
        ('ANIMALS', "ANIMALS"),
        ('MOUSE', "MOUSE"),
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    who_I = models.TextField(max_length=50)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='profile', null=True)
    # join = models.DateTimeField(auto_now_add=False)
    type_of_person = models.CharField(choices=TYPE_OF_PERSON, max_length=233)
    doctor_section = models.CharField(choices=DOCTOR_IN, max_length=60)
    slug = models.SlugField(blank=True, null=True)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' %(self.user.username)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)