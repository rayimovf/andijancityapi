from django.urls import path

from .views import GetInformation, GetBanner, HomeComplexFilter, GetPopularComplex, GetPaymentType, GetComplex, GetAdvertising, \
    GetPopularCompany, CreateContact, GetComplexSingle, ComplexFilter, GetServices, GetRealtorAbout, GetRealtor, GetAboutMe

urlpatterns = [
    path('get-information/', GetInformation.as_view()),
    path('get-banner/', GetBanner.as_view()),
    path('home-complex-filter/', HomeComplexFilter.as_view()),
    path('get-popular-complex/', GetPopularComplex.as_view()),
    path('get-payment-type/', GetPaymentType.as_view()),
    path('get-complex/', GetComplex.as_view()),
    path('get-advertising/', GetAdvertising.as_view()),
    path('get-popular-company/', GetPopularCompany.as_view()),
    path('create-contact/', CreateContact.as_view()),
    path('get-complex-single/<int:pk>/', GetComplexSingle.as_view()),
    path('complex-filter/', ComplexFilter.as_view()),
    path('get-services/', GetServices.as_view()),
    path('get-realtor-about/', GetRealtorAbout.as_view()),
    path('get-realtors/', GetRealtor.as_view()),
    path('get-about-me/', GetAboutMe.as_view())
]
