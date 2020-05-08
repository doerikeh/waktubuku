from django.db import models
from profilebuku.models import UserModel

class SubCategories(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    deskripsi = models.TextField()
    image_sub_categories = models.ImageField(upload_to="categories/")
    active = models.BooleanField()

    def __str__(self):
        return self.title

class Categories(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    deskripsi = models.TextField()
    image_categories = models.ImageField(upload_to="categories/")
    active = models.BooleanField()

    def __str__(self):
        return self.title



class Cerita(models.Model):

    STATUS_CHOICE = (
        ('Draft', 'draft'),
        ("Ready", "ready")
    )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    judul = models.CharField(max_length=200)
    categories = models.ManyToManyField(Categories)
    sub_categories = models.ManyToManyField(SubCategories)
    chapter = models.CharField(max_length=200)
    status = models.CharField(max_length=80, choices=STATUS_CHOICE)
    slug = models.SlugField()
    isi_cerita = models.TextField()
    image_cover = models.ImageField(upload_to="cerita/%Y/%m/%d")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul
