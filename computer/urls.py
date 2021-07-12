from django.urls import path

from computer.views import ComputerListCreate, ComputerViewUpdateDelete

urlpatterns = [

    path('', ComputerListCreate.as_view(), name='computer_list_create'),
    path('<int:pk>', ComputerViewUpdateDelete.as_view(), name='computer_view_update_delete')
]
