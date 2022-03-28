from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('cars/', views.CarList.as_view(), name="car_list"),
    path('cars/new/', views.Car_Create.as_view(), name="car_create"),
    path('cars/<int:pk>/', views.CarDetail.as_view(), name="car_detail"),
    path('cars/<int:pk>/update', views.CarUpdate.as_view(), name="car_update"),
    path('cars/<int:pk>/delete', views.CarDelete.as_view(), name="car_delete"),
    path('user/<username>/', views.profile, name='profile'),
    #cartype routes
    path('cartypes/', views.cartypes_index, name='cartypes_index'),
    path('cartypes/<int:cartype_id>', views.cartypes_show, name = 'cartypes_show'),
    path('cartypes/create/', views.CarTypeCreate.as_view(), name='cartypes_create'),
    path('cartypes/<int:pk>/update/', views.CarTypeUpdate.as_view(), name='cartypes_update'),
    path('cartypes/<int:pk>/delete/', views.CarTypeDelete.as_view(), name='cartypes_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    

]

