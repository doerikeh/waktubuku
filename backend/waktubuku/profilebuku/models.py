from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


class Saldo(models.Model):
    penghasilan = models.DecimalField(decimal_places=2, max_digits=30)
    dana_masuk = models.DecimalField(decimal_places=2, max_digits=30)
    dana_keluar = models.DecimalField(decimal_places=2, max_digits=30)
    keterangan = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.penghasilan)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username_user, password, **extra_field):
        if not email:
            raise ValueError("harus memasukan email")
        # if username_user is None:
        #     raise ValueError("username Harus Di isi")
        email = self.normalize_email(email)
        user = self.model(email=email, username_user=username_user, **extra_field)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username_user, password=None, **extra_field):
        extra_field.setdefault("is_staff", False)
        extra_field.setdefault("is_superuser", False)
        return self._create_user(email, username_user, password, **extra_field)

    def _create_superuser(self, email, password, **extra_field):
        if not email:
            raise ValueError("harus memasukan email")
        # if username_user is None:
        #     raise ValueError("username Harus Di isi")
        email = self.normalize_email(email)
        user = self.model(email=email,  **extra_field)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password, **extra_field):
        extra_field.setdefault("is_staff", True)
        extra_field.setdefault("is_superuser", True)

        if extra_field.get("is_staff") is not True:
            raise ValueError(
            "Superuser must have is_staff=True."
            )

        if extra_field.get("is_superuser") is not True:
            raise ValueError(
            "Superuser must have is_supaseruser=True."
            )
        return self._create_superuser(email, password, **extra_field)


class UserModel(AbstractUser):

    GENDER_CHOICES = (
        ('Wanita', 'wanita'),
        ('Laki-Laki', 'laki-laki')
    )

    username = None
    username_user = models.CharField('username_user', max_length=200, blank=True, null=True)
    slug = models.SlugField()
    email = models.EmailField('email address', unique=True)
    no_telepon = models.CharField( max_length=20)
    image_profile = models.ImageField(upload_to="image_profile/%Y/%m/%d", blank=True)
    image_walpaper = models.ImageField(upload_to="image_penwlpr_field/%Y/%m/%d", blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    biografi = models.TextField()
    alamat = models.CharField(max_length=300)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    saldo = models.ForeignKey(Saldo, on_delete=models.CASCADE, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username_user']
    objects = UserManager()

    def __str__(self):
        return f'{self.username_user} User'

    class Meta:
        permissions = (
                ('user','Can read user'),
            )




    

class AuditEntry(models.Model):
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    username = models.CharField(max_length=256, null=True)

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):  
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_in', ip=ip, username=user.username_user)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):  
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_out', ip=ip, username=user.username_user)


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    AuditEntry.objects.create(action='user_login_failed', username=credentials.get('username_user', None))