from django.db import router
from django.urls.conf import include, path
from gomo_apis.serializer import LoginSerializer
from rest_framework import routers
# from rest_framework.viewset import ModelViewset
from .views import LoginViewSet
from .views import RegistrationViewSet
from .views import DashBoardBillListViewSet
from .views import UploadBillPhotoViewSet
from .views import BillDetailsViewSet
from .views import PaymentConfirmationDetailsViewSet

router=routers.DefaultRouter()
router.register("login/",LoginViewSet)
router.register("register/",RegistrationViewSet)
router.register("dashboard/",DashBoardBillListViewSet)
router.register("upload/",UploadBillPhotoViewSet)
router.register("detail/",BillDetailsViewSet)
router.register("confirmation/",PaymentConfirmationDetailsViewSet)
urlpatterns = [
    path("",include(router.urls))
]

