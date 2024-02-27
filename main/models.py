from django.db import models


class Information(models.Model):
    name = models.CharField(max_length=255)
    tg = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()
    facebook = models.URLField()
    phone = models.URLField()
    logo = models.ImageField(upload_to='InfoLogo')

    def __str__(self):
        return self.name


class Banner(models.Model):
    img = models.ImageField(upload_to='BannerIMG')
    title = models.CharField(max_length=255)


class PaymentType(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=500)
    img = models.ImageField(upload_to='PaymentIMG')

    def __str__(self):
        return self.name


class Advertising(models.Model):
    bg_img = models.ImageField(upload_to='AdvertisingBGIMG')
    title = models.CharField(max_length=255)
    text = models.TextField()
    bonus = models.IntegerField(default=0)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.name


class CompanyComplexIMG(models.Model):
    img = models.ImageField(upload_to='CompanyComplexIMG')


class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='CompanyLogo')
    announcement = models.IntegerField(default=0)
    complex_img = models.ManyToManyField(CompanyComplexIMG)

    def __str__(self):
        return self.name


class ComplexType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Stata(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ComplexImage(models.Model):
    img = models.ImageField(upload_to='ComplexIMG')


class FeatureImage(models.Model):
    img = models.ImageField(upload_to='FeaturesIMG')


class EnvironmentImg(models.Model):
    img = models.ImageField(upload_to='EnvironmentIMG')


class Complex(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    lifetime = models.DateField()
    homes = models.IntegerField()
    floor = models.IntegerField()
    ceilings = models.IntegerField()
    type = models.ForeignKey(ComplexType, on_delete=models.CASCADE)
    payment_date = models.CharField(max_length=255)
    parking = models.CharField(max_length=255)
    finishing = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    balcony = models.CharField(max_length=255)
    heating_type = models.CharField(max_length=255)
    territory = models.CharField(max_length=255)
    about = models.TextField()
    viewed = models.IntegerField(default=0)
    state = models.ForeignKey(Stata, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=3)
    square = models.FloatField()
    img = models.ManyToManyField(ComplexImage)
    feature_img = models.ManyToManyField(FeatureImage)
    environment_img = models.ManyToManyField(EnvironmentImg)
    # payment_type = models.CharField(max_length=255)
    number_room = models.IntegerField(choices=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4+')
    ))

    def __str__(self):
        return self.name


class Services(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    icon = models.ImageField(upload_to='ServicesIcon')


class AboutMe(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


class RealtorAbout(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    icon = models.ImageField(upload_to='RieltorIcon')


class Realtor(models.Model):
    full_name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='RieltorIMG')
    rating = models.FloatField()
    comments = models.IntegerField()

    def __str__(self):
        return self.full_name
