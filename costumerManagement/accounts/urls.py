from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name='account'),
    path('products/', views.products, name="products"),
    path('costumers/<str:cust_id>/', views.costumers, name="costumers"),
    path('create_order/<str:cust_id>', views.createOrder, name="create_order"),
    path('update_order/<str:cust_id>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:cust_id>/', views.deleteOrder, name="delete_order"),
]

urlpatterns+=staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)