from django.db   import models

from core.models import TimeStampModel
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("must have email")
        if not password:
            raise ValueError("must have user password")
        user = self.model(
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, profile_url, **extra_fields):
        if not nickname:
            raise ValueError("must have nickname")
        if not profile_url:
            raise ValueError("must have profile")
        host = self.create_user(
            nickname = nickname,
            profile_url = profile_url,
            **extra_fields
        )
        return host

class User(AbstractBaseUser): 
    kakao_id    = models.BigIntegerField(null=True)
    name        = models.CharField(max_length=200, null=True)
    profile_url = models.CharField(max_length=2000, null=True)
    email       = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = "users"

class Host(AbstractBaseUser): 
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname    = models.CharField(max_length=200)
    profile_url = models.CharField(max_length=2000)
    is_deleted  = models.BooleanField(default=False)

    USERNAME_FIELD = 'profile_url'    
    REQUIRED_FIELDS = ['nickname']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    class Meta: 
        db_table = 'hosts'