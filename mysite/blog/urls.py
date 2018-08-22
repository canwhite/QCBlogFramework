#这个是我们需要的url

from django.conf.urls import url

from blog import views_if


urlpatterns = [
    
    #ex:/api/get_commen_data/
    url(r'get_common_data/',views_if.get_common_data,name = 'get_common_data')
    
    
    
    
]