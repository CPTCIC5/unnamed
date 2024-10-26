from rest_framework import  viewsets,status,permissions
from rest_framework.response import Response
from . import models
from .serializers import FirmSerializer,CreateFirmSerialzer,EntitySerializer, CreateEntitySerializer
from .models import Firm
# Create your views here.

class FirmsViewSet(viewsets.ModelViewSet):
    # permission_classes = (WorkSpaceViewSetPermissions,)
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = FirmSerializer

    def get_queryset(self):
        firm= (self.request.user.firms)

        # All the firms the request user is a member of
        return Firm.objects.filter(pk=firm.pk)
    #https://xyz.com
    
    

    def create(self, request, *args, **kwargs):
        serializer = CreateFirmSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(root_user=self.request.user)

        return Response(self.get_serializer(instance).data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = CreateFirmSerialzer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)

        new_instance = serializer.save()

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(self.get_serializer(new_instance).data)
    


class EntityViewSet(viewsets.ModelViewSet):
    permission_classes= [permissions.IsAuthenticated]
    serializer_class = EntitySerializer
    
    def get_queryset(self):
        return models.Entity.objects.filter(firm=self.request.user.firms)

    
    def create(self, request, *args, **kwargs):
        serializer = CreateEntitySerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = CreateEntitySerializer(
            instance=instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance= self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)