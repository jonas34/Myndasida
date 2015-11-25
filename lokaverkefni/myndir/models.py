from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, dateofbirth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Notendur þurfa að hafa email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=dateofbirth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # Notandinn auðkenndur með netfangi hanns
        return self.email

    def get_short_name(self):
        # Notandinn auðkenndur með netfangi hanns
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"

        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"

        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"

        return self.is_admin

class Photos(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    author = models.ForeignKey(MyUser)

class Comments(models.Model):
    photo = models.ForeignKey(Photos)
    text = models.CharField(max_length=500)
    author = models.ForeignKey(MyUser)
