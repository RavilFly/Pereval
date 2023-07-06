from django.urls import path
from django.views.generic import TemplateView
from .views import SubmitData, UpdateSubmitData, UserPerevalList

urlpatterns = [
    path('submitdata/', SubmitData.as_view(), name="submit_data"),
    path('submitdata/<int:pk>/', UpdateSubmitData.as_view()),
    path('submitdata/user__email=<str:email>/', UserPerevalList.as_view()),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]