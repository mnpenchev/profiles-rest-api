from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """ for the custom user model"""

    def create_user(self, email, name, password=None):
        """ new user profile object"""
        if not email:
            raise ValueError('User must have email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """ creates superuser """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ represent user profile inside the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Used to get a users full name. """
        return self.name

    def get_short_name(self):
        """ Used to get a users short  name. """
        return self.name

    def __str__(self):
        """ turn object to string"""
        return self.email


class ProfileFeedItem(models.Model):
    """ profile status update """
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ return model as string """
        return self.status_text
