from django.urls import path

from . import views

urlpatterns = [
    path("", views.root_view, name="home"),
    path("connexion/", views.login_view, name="login"),
    path("deconnexion/", views.logout_view, name="logout"),
    path("tableau-de-bord/", views.dashboard_view, name="dashboard"),
    path("commandes/", views.commandes_view, name="commandes"),
    path("commandes/<int:pk>/detail/", views.commande_detail_view, name="commande_detail"),
]
