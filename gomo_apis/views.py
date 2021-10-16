from gomo_app.models import Login
from gomo_app.models import Registration
from gomo_app.models import UploadBillPhoto
from gomo_app.models import DashBoardBill
from gomo_app.models import PaymentConfirmationDetails
from gomo_app.models import BillDetails

from rest_framework import viewsets
from .serializer import BillDetailSerializer, DashBoardBillSerializer, LoginSerializer, PaymentConfirmationDetailsSerializer, RegisterationSerializer, UploadBillPhotoSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset=Login.objects.all()
    serializer_class=LoginSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset=Registration.objects.all()
    serializer_class=RegisterationSerializer

class UploadBillPhotoViewSet(viewsets.ModelViewSet):
    queryset=UploadBillPhoto.objects.all()
    serializer_class=UploadBillPhotoSerializer

class DashBoardBillViewSet(viewsets.ModelViewSet):
    queryset=DashBoardBill.objects.all()
    serializer_class=DashBoardBillSerializer

class BillDetailsViewSet(viewsets.ModelViewSet):
    queryset=BillDetails.objects.all()
    serializer_class=BillDetailSerializer

class PaymentConfirmationDetailsViewSet(viewsets.ModelViewSet):
    queryset=PaymentConfirmationDetails.objects.all()
    serializer_class=PaymentConfirmationDetailsSerializer





