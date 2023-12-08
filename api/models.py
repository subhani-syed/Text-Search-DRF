from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager,PermissionsMixin
from django.utils import timezone

class Paragraph(models.Model):

    description  = models.TextField()

    def __str__(self):
        return f"{self.description[:10]}..."
    

class CustomUserManager(UserManager):

    def _create_user(self,email,password,**extra_fields):
    
        if not email:
            raise ValueError("Email is required to create the User")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_user(self,email=None,password=None,**extra_fields):

        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)
    
    def create_superuser(self,email=None,password=None,**extra_fields):
        
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,**extra_fields)


class CustomUser(AbstractUser,PermissionsMixin):

    email = models.EmailField(unique=True,blank=True,default='')
    name = models.CharField(max_length=255,blank=True,default='')    

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    dob = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name or self.email.split('@')[0]
    
