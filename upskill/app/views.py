from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .forms import UserForm
from .models import Email
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import requests
import random

from dotenv import load_dotenv

load_dotenv()


# Create your views here.
def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(username, email)
        if User.objects.filter(username=username).exists():
            raise ValidationError("The username is taken please try another.")
        user = User.objects.create_user(username, email, password)
        user.save()
    return render(request, "signup.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("blog/")

        else:
            # No backend authenticated the credentials
            return render(request, "login.html")

    return render(request, "login.html")


def decider(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "form.html")


def profile(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "profile.html")


def logout_user(request):
    logout(request)
    return render(request, "index.html")


def newsletter(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        email = request.POST.get("email")
        u = request.user
        u.email = email
        u.save()
        print(email)
        email_obj = Email(email=email)
        email_obj.save()
        subject = "Welcome to Upskill"
        message = f"Thanks for joining our newsletter . "
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            email,
        ]
        send_email = EmailMessage(subject, message, email_from, recipient_list)
        # send_email.attach_file('D:\Ansh\Dev\Projects\Django_Project\chrome\home\GFG.pdf')
        send_email.send()
        return render(request, "newsletter.html")

    return render(request, "newsletter.html")


# api urls


def locate(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "locate.html")


def locate_api(request, state):
    print(state)
    url = "http://universities.hipolabs.com/search?name=technolo&country=india"
    r = requests.get(url)
    target_dict = random.choice(r.json())
    data = {
        "state": state,
        "link": target_dict["web_pages"][0],
        "name": target_dict["name"],
        "country": target_dict["country"],
    }
    print(data)
    return JsonResponse(data)


def chatbot(request ):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'chatbot.html') 


# def chatbot_api(request, question):
#     print(question)
#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=question,
#         temperature=0.9,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=0.0,
#         presence_penalty=0.6,
#         stop=[" Human:", " AI:"],
#     )
#     return JsonResponse(response)
