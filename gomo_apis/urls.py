from django.db import router
from django.urls.conf import include, path
from rest_framework import routers
from .views import LoginViewSet
from .views import RegistrationViewSet
from .views import DashBoardBillViewSet
from .views import UploadBillPhotoViewSet
from .views import BillDetailsViewSet
from .views import PaymentConfirmationDetailsViewSet

router=routers.DefaultRouter()
router.register("login/",LoginViewSet)
router.register("register/",RegistrationViewSet)
router.register("dashboard/",DashBoardBillViewSet)
router.register("upload/",UploadBillPhotoViewSet)
router.register("detail/",BillDetailsViewSet)
router.register("confirmation/",PaymentConfirmationDetailsViewSet)
urlpatterns = [
    path("",include(router.urls))
]

