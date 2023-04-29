from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if password is None:
            raise TypeError('Superusers must have a password.')

        return self.create_user(email, password, **extra_fields)
    
    def has_module_perms(self, user_obj, app_label):
        # Return True if the user has any permissions in the given app_label.
        return  user_obj.is_staff

class CustomUser(AbstractBaseUser,  PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(max_length=254,null=True,unique=True)
    Phone_Number = models.IntegerField(null=True)
    first_name = models.CharField(max_length=150,null=True)
    last_name = models.CharField(max_length=150,null=True)
    password = models.CharField(max_length=128,null=True)
    gender = models.CharField(max_length=7,null=True)
    aadhaarno = models.IntegerField(null=True, blank=True)
    # country = models.CharField(max_length=20,null=True)
    state = models.CharField(max_length=20,null=True)
    district = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=500,null=True)
    pincode = models.IntegerField(null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)



    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True,)


    # country =removal
    # isactive removal
    # city = disrt
    # created at
    # updated at
    # isuser
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','Phone_Number','first_name','last_name','password','gender','aadhaarno','state','district','address','pincode']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
