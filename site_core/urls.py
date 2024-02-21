from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    
    path('',views.assets_all,name = 'assets_all'),
    # Athentication management
    path('login/', views.CustomLoginView.as_view(), name = "login"),
    path('sign_up/', views.sign_up, name='sign_up'),
    # Assets management
    path('asset_add/',views.asset_add,name = 'asset_add'),
    path('asset_update/<int:id>',views.asset_update,name = 'asset_update'),
    path('asset_delete/<int:id>',views.asset_delete,name = 'asset_delete'),
    # User library
    path('assets_library/',views.assets_library,name = 'assets_library'),
]