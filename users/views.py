from django_filters.rest_framework.backends import DjangoFilterBackend
from users.models import Payment
from rest_framework import generics
from users.serializers import PaymentSerializer
from rest_framework.filters import OrderingFilter


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('user', 'date', 'course', 'lesson', 'cost', 'way_of_payment')
    ordering_fields = ('date',)
