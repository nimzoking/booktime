from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from rest_framework import routers


from django.contrib.auth import views as auth_views

from main import views
from main import models
from main import forms
from main import endpoints
from main import admin

router = routers.DefaultRouter()
router.register(r"orderlines", endpoints.PaidOrderLineViewSet)
router.register(r"orders", endpoints.PaidOrderViewSet)


urlpatterns = [ 
    path(
        "contact-us/",
        views.ContactUsView.as_view(),
        name="contact_us",
    ),
    path(
        "about-us/",
        TemplateView.as_view(template_name="about_us.html"),
        name="about_us",
    ),
    path(
        "",
        TemplateView.as_view(template_name="home.html"),
        name="home",
    ), 
    path(
        "products/<slug:tag>/",
        views.ProductListView.as_view(),
        name="product",
    ), 
    path(
        "product/<slug:slug>/",
        DetailView.as_view(model=models.Product),
        name="product",
    ),
    path(
        "signup/", 
        views.SignupView.as_view(), 
        name="signup"
    ), 
    path(
        "login/", 
        auth_views.LoginView.as_view(
            template_name="login.html",
            form_class=forms.AuthenticationForm
        ), 
        name="login"
    ),
    path(
        "address/",
        views.AddressListView.as_view(),
        name="address_list",
    ),
    path(
        "address/create/",
        views.AddressCreateView.as_view(),
        name="address_create",
    ),
    path(
        "address/<int:pk>/",
        views.AddressUpdateView.as_view(),
        name="address_update",
    ),
    path(
        "address/<int:pk>/delete/",
        views.AddressDeleteView.as_view(),
        name="address_delete",
    ),
    path(
        "add_to_basket/",
        views.add_to_basket,
        name="add_to_basket",
    ),
    path(
        "basket/",
        views.manage_basket,
        name="basket",
    ),
    path(
        "order/done/",
        TemplateView.as_view(template_name="order_done.html"),
        name="checkout_done",
    ),
    path(
        "order/address_select/",
        views.AddressSelectionView.as_view(),
        name="address_select",
    ),
    path(
        "order-dashboard/",
        views.OrderView.as_view(),
        name="order_dashboard",
    ),
    path("api/", include(router.urls)),
    path("admin/", admin.main_admin.urls),
    path("office-admin/", admin.central_office_admin.urls),
    path("dispatch-admin/", admin.dispatchers_admin.urls),
]