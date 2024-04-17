from django.shortcuts import render

from .models import Greeting

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt




# Create your views here.


@csrf_exempt
@require_http_methods(["POST"])
def receive_signal(request):
    # Here, you can process the request data
    data = request.POST.get('data', '')
    print("Data received:", data)
    # Perform actions based on the data received
    
    return JsonResponse({"status": "success", "message": "Signal received successfully"})

def index(request):
    return render(request, "index.html")


def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
