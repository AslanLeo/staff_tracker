from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from .models import User
from .permissions import IsAdmin
from .serializers import UserCrudSerializer


class UserCrudViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = User.objects.all()
    serializer_class = UserCrudSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    filter_fields = ['first_name']
    search_fields = ['phone_number']
    ordering_fields = ['first_name']

