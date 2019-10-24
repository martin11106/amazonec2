from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from UploadImage.models import UploadImage

from UploadImage.serializer import UploadImageSerializers

class AlumnoList(APIView):
    # METODO GET PARA SOLICITAR INFO
    def get(self, request, format=None):
        queryset = UploadImage.objects.filter()
        serializer = UploadImageSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UploadImageSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    