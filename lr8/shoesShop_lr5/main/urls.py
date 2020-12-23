from django.urls import path
from . import views
from django.views import i18n

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.IndexView.as_view(), name='home'),
    path('add-shoes', views.add_shoes, name='add-shoes'),
    # path('add-shoes', views.ShoesCreateView.as_view(), name='add-shoes'),
    path('update-shoes/<int:id>/', views.update_shoes, name='update-shoes'),
    path('delete-shoes/<int:id>/', views.delete_shoes, name='delete-shoes'),

    path('manufacturers', views.show_manufacturers, name='manufacturers'),
    path('add-manufacturer', views.add_manufacturer, name='add-manufacturer'),
    path('update-manufacturer/<int:id>/', views.update_manufacturer, name='update-manufacturer'),
    path('delete-manufacturer/<int:id>/', views.delete_manufacturer, name='delete-manufacturer'),

    path('categories', views.show_categories, name='categories'),
    path('add-category', views.add_category, name='add-category'),
    path('update-category/<int:id>/', views.update_category, name='update-category'),
    path('delete-category/<int:id>/', views.delete_category, name='delete-category'),

    path('colors', views.show_colors, name='colors'),
    path('add-color', views.add_color, name='add-color'),
    path('update-color/<int:id>/', views.update_color, name='update-color'),
    path('delete-color/<int:id>/', views.delete_color, name='delete-color'),

    path('login', views.userLogin, name='login'),
    path('logout', views.userLogout, name='logout'),
    path('register', views.userRegister, name='register'),
    path('set-language/', i18n.set_language, name='set_language')
]
