from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from computer.models import ComputerModel
from computer.serializer import ComputerSerializer


class ComputerListCreate(APIView):

    def get(self, *args, **kwargs):
        qs = ComputerModel.objects.all()
        serializer = ComputerSerializer(qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):

        data = self.request.data

        serializer = ComputerSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class ComputerViewUpdateDelete(APIView):

    def get(self, *args, **kwargs):

        pk = kwargs.get('pk')
        computer = get_object_or_404(ComputerModel, pk=pk)
        serializer = ComputerSerializer(computer)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):

        pk = kwargs.get('pk')
        computer = get_object_or_404(ComputerModel, pk=pk)
        computer.delete()

        return Response('No Content', status.HTTP_204_NO_CONTENT)

    def patch(self, *args, **kwargs):

        pk = kwargs.get('pk')
        data = self.request.data
        computer = get_object_or_404(ComputerModel, pk=pk)

        serializer = ComputerSerializer(computer, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_202_ACCEPTED)


    def put(self, *args, **kwargs):

        pk = kwargs.get('pk')
        data = self.request.data
        computer = get_object_or_404(ComputerModel, pk=pk)

        serializer = ComputerSerializer(computer, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_202_ACCEPTED)


