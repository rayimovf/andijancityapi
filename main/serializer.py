from rest_framework import serializers
from .models import Information, Banner, PaymentType, Advertising, Contact, Company, ComplexType, Category, \
    Stata, ComplexImage, FeatureImage, EnvironmentImg, Complex, Services, AboutMe, RealtorAbout, Realtor


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'


class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ComplexTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplexType
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class StataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stata
        fields = '__all__'


class ComplexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplexImage
        fields = '__all__'


class FeatureImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureImage
        fields = '__all__'


class EnvironmentImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentImg
        fields = '__all__'


class ComplexSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Complex
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'


class RealtorAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealtorAbout
        fields = '__all__'


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'

