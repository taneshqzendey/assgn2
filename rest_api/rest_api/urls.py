from django.urls import path
from manager import views

urlpatterns = [
    path("api/users/", views.CustomUserList.as_view(), name="users"),
    path("users/<str:pk>/", views.CustomUserDetailView.as_view(), name="user-detail"),
    path("api/transacts/", views.transactList.as_view(), name="transacts"),
    path("aa", views.aa.as_view(), name="aa")
 ]
