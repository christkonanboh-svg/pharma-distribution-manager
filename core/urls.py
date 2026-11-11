from django.urls import path

from . import views

urlpatterns = [
    path("", views.root_view, name="home"),
    path("connexion/", views.login_view, name="login"),
    path("deconnexion/", views.logout_view, name="logout"),
    path("tableau-de-bord/", views.dashboard_view, name="dashboard"),
    path("alertes/", views.alertes_view, name="alertes"),
    path("commandes/", views.commandes_view, name="commandes"),
    path("commandes/nouvelle/", views.commande_nouvelle_view, name="commande_nouvelle"),
    path("commandes/<int:pk>/", views.commande_page_view, name="commande_page"),
    path("commandes/<int:pk>/detail/", views.commande_detail_view, name="commande_detail"),
    path("preparation/", views.preparation_view, name="preparation"),
    path("livraisons/", views.livraisons_view, name="livraisons"),
    path("stock/", views.stock_lots_view, name="stock_lots"),
    path("stock/reception/", views.reception_lot_view, name="reception_lot"),
    path("tracabilite/", views.tracabilite_view, name="tracabilite"),
    path("tracabilite/rappel/", views.rappel_lot_view, name="rappel_lot"),
    path("referentiels/", views.referentiels_view, name="referentiels"),
    path("administration/", views.administration_view, name="administration"),
]
