import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils.get_food_truck_recommendations import get_food_truck_recommendations

from .serializers import UserPreferenceSerializer


@api_view(["POST"])
def recommend_food_trucks(request):

    serializer = UserPreferenceSerializer(data=request.data)

    if serializer.is_valid():
        user_latitude = serializer.validated_data.get("latitude")
        user_longitude = serializer.validated_data.get("longitude")
        user_preference = serializer.validated_data.get("preference")

        try:
            recommendations = get_food_truck_recommendations(
                user_preference,
                user_latitude,
                user_longitude,
            )

            recommendations_data = json.loads(recommendations)
            return Response(recommendations_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
