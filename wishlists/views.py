from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist
from .serializers import WishListSerializer

# create your views here


class Wishlists(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlists = Wishlist.objects.filter(user=request.user)
        serializer = WishListSerializer(
            all_wishlists,
            many=True,
            contect={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = WishListSerializer(data=request.data)
        if serializer.is_valid():
            wishlist = serializer.save(user=request.user)
            serializer = WishListSerializer(wishlist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
