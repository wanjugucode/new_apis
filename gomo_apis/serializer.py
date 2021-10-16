from gomo_app.models import Login
from gomo_app.models import Registration
from gomo_app.models import UploadBillPhoto
from gomo_app.models import DashBoardBillList
from gomo_app.models import PaymentConfirmationDetails
from gomo_app.models import BillDetails
from rest_framework import serializers


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
        fields=(" bill_id","bill_name","bill_icon_image")

class BillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillDetails
        fields=("image","name","account","amount","available_payment_method_details")
        
class PaymentConfirmationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentConfirmationDetails
        fields=("payment_confirmation_details",)





