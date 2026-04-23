from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nama")
    description = models.TextField(verbose_name="Deskripsi")
    image = models.ImageField(upload_to='products/', verbose_name="Gambar")

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Judul")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    content = models.TextField(verbose_name="Konten (HTML)")
    main_image = models.ImageField(upload_to='articles/', verbose_name="Gambar Utama")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name="Judul")
    image = models.ImageField(upload_to='gallery/', verbose_name="File Gambar")

    def __str__(self):
        return self.title

class CompanyProfile(models.Model):
    history = models.TextField(verbose_name="Sejarah")
    vision = models.TextField(verbose_name="Visi")
    mission = models.TextField(verbose_name="Misi")
    address = models.TextField(verbose_name="Alamat")
    phone = models.CharField(max_length=50, verbose_name="No HP")
    email = models.EmailField(verbose_name="Email")

    def save(self, *args, **kwargs):
        self.pk = 1
        super(CompanyProfile, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Company Profile"

    class Meta:
        verbose_name = "Company Profile"
        verbose_name_plural = "Company Profile"
