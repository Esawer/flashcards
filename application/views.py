from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .utils import captcha_script
from django.views.decorators.cache import never_cache
import io

from .models import *
from .forms import *


def home(request):
    if not request.user.is_authenticated:
        decks = Deck.objects.filter(owner__user=None)
    else:
        decks = Deck.objects.filter(owner__user=request.user)

    return render(request, "application/index.html", {"decks": decks})


def add_deck(request):
    if not request.user.is_authenticated:
        return redirect("home")

    form = AddDeck()

    if request.method == "POST":
        form = AddDeck(request.POST)
        deck_name = form.save(commit=False)
        deck_name.owner = UserClass.objects.get(user=request.user)
        deck_name.save()

        cards = request.FILES.get("cards")

        if cards:
            for i in cards:
                i = i.decode("utf-8").strip()
                if ";" not in i:
                    continue

                i_question, i_answer = i.split(";")

                if i_question == "" or i_answer == "":
                    continue
                else:
                    Card.objects.create(
                        question=i_question, answer=i_answer, deck=deck_name
                    )
        return redirect("edit_deck")

    context = {"form": form}
    return render(request, "application/add_deck.html", context)


def edit_deck(request):
    if not request.user.is_authenticated:
        return redirect("home")

    deck = Deck.objects.filter(owner__user=request.user)

    if request.method == "POST":
        Deck.objects.get(id=request.POST["submit"]).delete()

    context = {"deck": deck}
    return render(request, "application/edit_deck.html", context)


def update_deck(request, id_deck):
    if not request.user.is_authenticated:
        return redirect("home")

    deck = Deck.objects.get(id=id_deck)
    deck_len = deck.card_set.all().count()  # type: ignore

    if request.method == "POST":
        Card.objects.get(id=request.POST["submit"]).delete()

    context = {"deck": deck, "deck_len": deck_len}
    return render(request, "application/update_deck.html", context)


def update_card(request, id_deck, id_card):
    if not request.user.is_authenticated:
        return redirect("home")

    deck = Deck.objects.get(id=id_deck)
    card = deck.card_set.get(id=id_card)  # type: ignore
    form = EditCard(initial={"question": card.question, "answer": card.answer})

    if request.method == "POST":
        form = EditCard(request.POST, instance=card)
        form.save()
        return redirect("update_deck", id_deck)

    context = {"deck": deck, "card": card, "form": form}
    return render(request, "application/update_card.html", context)


def add_card(request, id_deck):
    if not request.user.is_authenticated:
        return redirect("home")

    deck = Deck.objects.get(id=id_deck)
    form = EditCard()

    if request.method == "POST":
        form = EditCard(request.POST)
        deck_value = form.save(commit=False)
        deck_value.deck = Deck.objects.get(id=id_deck)
        deck_value.save()
        return redirect("update_deck", id_deck)

    context = {"deck": deck, "form": form}
    return render(request, "application/add_card.html", context)


def learn(request, id_deck, id_card):
    deck = Deck.objects.get(id=id_deck)
    deck_len = deck.card_set.all().count()  # type: ignore

    if deck_len == id_card:
        next_item = deck_len - 1
        id_card = deck_len - 1
        # return redirect('home')
    else:
        next_item = id_card + 1

    if 0 == id_card:
        previous_item = id_card
    else:
        previous_item = id_card - 1

    card = deck.card_set.all()[id_card]  # type: ignore
    question = deck.card_set.all()[id_card].question  # type: ignore
    answer = deck.card_set.all()[id_card].answer  # type: ignore

    context = {
        "deck": deck,
        "card": card,
        "next_item": next_item,
        "previous_item": previous_item,
        "deck_len": deck_len,
        "question": question,
        "answer": answer,
        "card_num": id_card + 1,
    }

    return render(request, "application/learn.html", context)


def update_deck_info(request, id_deck):
    if not request.user.is_authenticated:
        return redirect("home")

    deck = Deck.objects.get(id=id_deck)
    form = AddDeck(initial={"name": deck.name})

    if request.method == "POST":
        form = AddDeck(request.POST, instance=deck)
        form.save()
        return redirect("update_deck", id_deck)

    context = {"deck": deck, "form": form}

    return render(request, "application/update_deck_settings.html", context)


@never_cache
def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "application/login.html")


def user_logout(request):
    logout(request)
    return redirect("home")


@never_cache
def user_register(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = CreateUser()

    if request.method == "POST":
        form = CreateUser(request.POST)

        if form.is_valid() and request.session[
            "captcha_answer"
        ] == captcha_script.encrypt_string(
            request.POST.get("captcha_input", "").strip()
        ):

            user_obj = form.save()
            UserClass.objects.create(user=user_obj)
            return redirect("login_page")

    context = {"form": form, "captcha_img": captcha_img}
    return render(request, "application/register.html", context)


def captcha_img(request):
    raw_text = captcha_script.generate_strings()
    request.session["captcha_answer"] = captcha_script.encrypt_string(raw_text)

    return captcha_script.create_images(raw_text)
