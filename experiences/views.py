from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,  # Added the missing import
)
from rest_framework.exceptions import NotFound
from .models import Perk
from .serializers import PerksSerializer


class Perks(APIView):

    def get(self, request):
        all_perks = Perk.objects.all()
        serializer = PerksSerializer(all_perks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerksSerializer(data=request.data)
        if serializer.is_valid():
            perk = serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class PerksDetail(APIView):

    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            return None

    def get(self, request, pk):
        perk = self.get_object(pk)
        if perk is None:
            return Response({"detail": "Not found."}, status=HTTP_404_NOT_FOUND)
        serializer = PerksSerializer(perk)
        return Response(serializer.data)

    def put(self, request, pk):
        perk = self.get_object(pk)
        if perk is None:
            # Create new record if it doesn't exist
            data = request.data
            data["id"] = pk  # Ensure the ID is set to the pk
            serializer = PerksSerializer(data=data)
            if serializer.is_valid():
                perk = serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        # Update the existing record
        serializer = PerksSerializer(perk, data=request.data)
        if serializer.is_valid():
            updated_perk = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        perk = self.get_object(pk)
        if perk is None:
            return Response({"detail": "Not found."}, status=HTTP_404_NOT_FOUND)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)
