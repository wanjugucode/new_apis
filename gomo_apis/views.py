from gomo_app.models import Login
from gomo_app.models import Registration
from gomo_app.models import UploadBillPhoto
from gomo_app.models import DashBoardBillList
from gomo_app.models import PaymentConfirmationDetails
from gomo_app.models import BillDetails
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from .serializer import BillDetailSerializer, DashBoardBillListSerializer, LoginSerializer, PaymentConfirmationDetailsSerializer, RegisterationSerializer, UploadBillPhotoSerializer

class LoginViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)
    queryset=Login.objects.all()
    serializer_class=LoginSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset=Registration.objects.all()
    serializer_class=RegisterationSerializer

class UploadBillPhotoViewSet(viewsets.ModelViewSet):
    queryset=UploadBillPhoto.objects.all()
    serializer_class=UploadBillPhotoSerializer

class DashBoardBillListViewSet(viewsets.ModelViewSet):
    queryset=DashBoardBillList.objects.all()
    serializer_class=DashBoardBillListSerializer

class BillDetailsViewSet(viewsets.ModelViewSet):
    queryset=BillDetails.objects.all()
    serializer_class=BillDetailSerializer

class PaymentConfirmationDetailsViewSet(viewsets.ModelViewSet):
    queryset=PaymentConfirmationDetails.objects.all()
    serializer_class=PaymentConfirmationDetailsSerializer





