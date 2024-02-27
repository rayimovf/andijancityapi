from django_filters import FilterSet, NumberFilter
from .models import Complex


class ComplexFilterOne(FilterSet):
    price__gte = NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = NumberFilter(field_name='price', lookup_expr='lte')
    square__gte = NumberFilter(field_name='square', lookup_expr='gte')
    square__lte = NumberFilter(field_name='square', lookup_expr='lte')

    class Meta:
        model = Complex
        fields = ['state', 'number_room', 'price__gte', 'price__lte', 'square__gte', 'square__lte']


class ComplexFilterTwo(FilterSet):
    price__gte = NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = NumberFilter(field_name='price', lookup_expr='lte')
    square__gte = NumberFilter(field_name='square', lookup_expr='gte')
    square__lte = NumberFilter(field_name='square', lookup_expr='lte')

    class Meta:
        model = Complex
        fields = ['company', 'type', 'square__gte', 'square__lte', 'price__gte', 'price__lte']
