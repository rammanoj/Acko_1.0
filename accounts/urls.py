from django.conf.urls import url
from . import views

urlpatterns = [
    url('^login/$', views.UserLoginView.as_view(), name='login'),
    url('^logout/$', views.UserLogoutView.as_view(), name='logout'),
    url('^product/$', views.ProductComplaintView, name='product-view'),
    url('^subproduct/$', views.SubProductComplaint),
]



