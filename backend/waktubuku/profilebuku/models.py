from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username_user, password, **extra_field):
        if not email:
            raise ValueError("harus memasukan email")
        # if username_user is None:
        #     raise ValueError("username Harus Di isi")
        email = self.normalize_email(email)
        user = self.model(email=email, username_user=username_user ,**extra_field)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username_user, password=None, **extra_field):
        extra_field.setdefault("is_staff", False)
        extra_field.setdefault("is_superuser", False)
        return self._create_user(email, password, username_user, **extra_field)

    def create_superuser(self, email, password, **extra_field):
        extra_field.setdefault("is_staff", True)
        extra_field.setdefault("is_superuser", True)

        if extra_field.get("is_staff") is not True:
            raise ValueError(
            "Superuser must have is_staff=True."
            )

        if extra_field.get("is_superuser") is not True:
            raise ValueError(
            "Superuser must have is_superuser=True."
            )
        return self._create_user(email, password, **extra_field)


class UserModel(AbstractUser):
    username = None
    username_user = models.CharField('username_user', max_length=200, blank=True, null=True)
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username_user']
    objects = UserManager()


class Saldo(models.Model):
    penghasilan = models.DecimalField(decimal_places=2, max_digits=30)
    dana_masuk = models.DecimalField(decimal_places=2, max_digits=30)
    dana_keluar = models.DecimalField(decimal_places=2, max_digits=30)
    keterangan = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.penghasilan)


class ProfileWBModel(models.Model):

    GENDER_CHOICES = (
        ('Wanita', 'wanita'),
        ('Laki-Laki', 'laki-laki')
    )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    slug = models.SlugField()
    saldo = models.ForeignKey(Saldo, on_delete=models.SET_DEFAULT, default=1)
    image_profile = models.ImageField(upload_to="image_profile/%Y/%m/%d", blank=True)
    image_walpaper = models.ImageField(upload_to="image_penwlpr_field/%Y/%m/%d", blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    biografi = models.TextField()
    alamat = models.CharField(max_length=300)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)

