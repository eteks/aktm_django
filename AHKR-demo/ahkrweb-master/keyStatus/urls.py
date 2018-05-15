from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$save_key_status', keyStatus.views.saveKeyStatus, name='Save Key Status'),
]
