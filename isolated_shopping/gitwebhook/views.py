import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git

# automated githook for updating server
@csrf_exempt
def UpdateServer(request):
    if request.method == "POST":
        repo = git.Repo("/home/nextgenshop/Backend_Django/") 
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Successfully updated server", status=200)
    else:
        return HttpResponse("Failed to update", status=500)