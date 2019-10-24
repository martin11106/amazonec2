from rest_framework import routers, serializers, viewsets

from UploadImage.models import UploadImage

class UploadImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=UploadImage
        fields=('__all__')#visulisar 

