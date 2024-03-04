from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
import firebase_admin
from firebase_admin import db
from django.conf import settings


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('homepage')
        else:
            #display the error message on failed login
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def homepage(request):
    if request.method == "GET":
        return render(request, 'homepage.html')
    elif request.method == "POST":
        global searchbar_text
        searchbar_text=request.POST.get('searchbar').lower()
        ref = db.reference("/fruits")
        global search_exists
        search_exists=ref.child(searchbar_text).get()
        if search_exists:
            return redirect("searchResults")
        else:
            return redirect('notFound')
    else:
        return HttpResponse("Method not allowed")


def searchResults(request):
    return render(request, 'searchResults.html', {
                'fruit': searchbar_text[0].upper() + searchbar_text[1:],
                'calories': search_exists['calories'],
                'protein': search_exists['protein'],
                'carbs': search_exists['carbohydrates'],
                'sugar': search_exists['sugar'],
                'fat': search_exists['fat']
            })
    

def notFound(request):
    if request.method=="GET":
        return render(request, 'notFound.html')


def addFruit(request):
    if request.method == "GET":
        return render(request, 'addFruit.html')
    elif request.method == "POST":
        name=request.POST.get('name').lower()
        calories=float(request.POST.get('calories',0))
        protein=float(request.POST.get('protein',0))
        fat=float(request.POST.get('fat',0))
        sugar=float(request.POST.get('sugar',0))
        carbs=float(request.POST.get('carbs',0))

        ref = db.reference("/fruits")
        existing=ref.child(name).get()

        #if fruit is already in the database, then it will get updated.
        if not existing:
            ref.child(name).set({
                'calories': calories,
                'protein': protein,
                'fat': fat,
                'sugar': sugar,
                'carbohydrates': carbs
            })
            print("New fruit added to the database")
        else:
            ref.child(name).update({
                'calories': calories,
                'protein': protein,
                'fat': fat,
                'sugar': sugar,
                'carbohydrates': carbs
            })
            print("Updated existing fruit")

        return redirect('addFruit')
    else:
        return HttpResponse("Method not allowed")
    
def editFruit(request):
    if request.method == "GET":
        global fruit
        fruit = request.GET.get('fruit')
        calories = request.GET.get('calories')
        protein = request.GET.get('protein')
        fat = request.GET.get('fat')
        sugar = request.GET.get('sugar')
        carbs = request.GET.get('carbs')
        return render(request, 'editFruit.html', {'fruit': fruit, 'calories': calories, 'protein': protein, 'fat': fat, 'sugar': sugar, 'carbs': carbs})
    elif request.method == "POST":
        calories=float(request.POST.get('calories',0))
        protein=float(request.POST.get('protein',0))
        fat=float(request.POST.get('fat',0))
        sugar=float(request.POST.get('sugar',0))
        carbs=float(request.POST.get('carbs',0))

        ref = db.reference("/fruits")
        ref.child(fruit.lower()).update({
            'calories': calories,
            'protein': protein,
            'fat': fat,
            'sugar': sugar,
            'carbohydrates': carbs
        })
        return redirect('homepage')
    else:
        return HttpResponse("Method not allowed")

    

def deleteFruit(request):
    if request.method == "POST":
        ref = db.reference("/fruits")
        ref.child(searchbar_text).delete() #searchbar_text was retrieved earlier from the searchbar input (global declaration)
        return redirect("homepage")
    else:
        return HttpResponse("Method not allowed")