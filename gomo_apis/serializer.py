from gomo_app.models import Login
from gomo_app.models import Registration
from gomo_app.models import UploadBillPhoto
from gomo_app.models import DashBoardBillList
from gomo_app.models import PaymentConfirmationDetails
from gomo_app.models import BillDetails
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView



class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=("email","password")
class RegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields=("first_name","last_name","phone_number","email","password")
class UploadBillPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=UploadBillPhoto
        fields=("bill_photo",)
class DashBoardBillListSerializer(serializers.ModelSerializer):
    class Meta:
        model=DashBoardBillList
        fields=("id_number","bill_name","bill_icon_image")

class BillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillDetails
        fields=("image","name","account","amount","available_payment_method_details")
        
class PaymentConfirmationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentConfirmationDetails
        fields=("name",)


class RegisterationSerializer(serializers.ModelSerializer):
    lastChanged = serializers.DateTimeField(read_only=True)
    identifier = serializers.CharField(read_only=True)
    revision = serializers.IntegerField(read_only=True)
    class Meta:
        model =Registration
        fields = ("first_name","last_name","phone_number","email","password","lastChanged","identifier","revision")



