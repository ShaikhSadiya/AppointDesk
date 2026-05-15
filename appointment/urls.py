from django.urls import path
from .views import add_appointment, appointments,delete_view,update_view, info_view


urlpatterns = [
    path('add_appointment/',add_appointment),
    path('appointments/',appointments ),
    path('appointments/delete/<id>/',delete_view),
    path('appointments/update/<id>/',update_view),
    path('appointments/info/<id>/', info_view)

]