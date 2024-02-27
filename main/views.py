from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Information, Banner, PaymentType, Advertising, Contact, Company, Complex, Services, AboutMe, RealtorAbout, Realtor

from .serializer import InformationSerializer, BannerSerializer, PaymentTypeSerializer, AdvertisingSerializer, ContactSerializer, CompanySerializer, \
    ComplexSerializer, ServicesSerializer, AboutMeSerializer, RealtorAboutSerializer, RealtorSerializer\

from .filters import ComplexFilterOne, ComplexFilterTwo


class GetInformation(ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

    def list(self, request):
        queryset = self.get_queryset().last()
        serializer = self.get_serializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)


class GetBanner(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def list(self, request):
        queryset = self.get_queryset().last()
        serializer = self.get_serializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)


class HomeComplexFilter(ListAPIView):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComplexFilterOne


class GetPopularComplex(ListAPIView):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer

    def list(self, request):
        queryset = self.get_queryset().order_by('-viewed')[:6]
        serializer = self.get_serializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


class GetPaymentType(ListAPIView):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

    def list(self, request):
        queryset = self.get_queryset().order_by('-id')[:3]
        serializer = self.get_serializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


class GetComplex(ListAPIView):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer

    def list(self, request):
        queryset = self.get_queryset().order_by('-id')[:6]
        serializer = self.get_serializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


class GetAdvertising(ListAPIView):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer

    def list(self, request):
        queryset = self.get_queryset().last()
        serializer = self.get_serializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)


class GetPopularCompany(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request):
        queryset = self.get_queryset().order_by('-announcement')[:4]
        serializer = self.get_serializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


class CreateContact(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class GetComplexSingle(RetrieveAPIView):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer

    def retrieve(self, request, *args, **kwargs):
        complex = self.get_object()
        complex.viewed += 1
        complex.save()
        complex.company.announcement += 1
        complex.company.save()
        ser_data = ComplexSerializer(complex).data
        return Response(ser_data)


class ComplexFilter(ListAPIView):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComplexFilterTwo


class GetServices(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class GetRealtorAbout(ListAPIView):
    queryset = RealtorAbout.objects.all()
    serializer_class = RealtorAboutSerializer

    def list(self, request):
        queryset = self.get_queryset().order_by('-id')[:3]
        serializer = self.get_serializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


class GetRealtor(ListAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer

    def list(self, request):
        queryset = self.get_queryset().order_by('-id')[:8]
        serializer = self.get_serializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


class GetAboutMe(ListAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

    def list(self, request):
        queryset = self.get_queryset().order_by('-id')[:3]
        serializer = self.get_serializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)