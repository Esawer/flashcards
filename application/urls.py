from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # main page
    path("add/", views.add_deck, name="add_deck"),  # add new deck
    path("learn/<int:id_deck>/<int:id_card>/", views.learn, name="learn"),  # flash cards page
    path("edit/", views.edit_deck, name="edit_deck"), # all decks edit page
    path("edit/<int:id_deck>/", views.update_deck, name="update_deck"), # deck edit page
    path("edit/<int:id_deck>/add/", views.add_card, name="add_card"), # add card page
    path("edit/<int:id_deck>/update/", views.update_deck_info, name="update_deck_info"), # deck update info page - deck name
    path("edit/<int:id_deck>/<int:id_card>/", views.update_card, name="update_card"), # update card page

    path("login/", views.user_login, name="login_page"),
    path("register/", views.user_register, name="register_page"),
    path("logout/", views.user_logout, name="logout_page"),
    path("captcha/", views.captcha_img, name="captcha_img"),
]

