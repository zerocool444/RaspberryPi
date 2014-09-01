from django.shortcuts import render
from django.http.response import Http404, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess

class Led:
    number = "0"
    state = False

    def __init__(self, number, state):
        self.number = number
        self.state = state


def index(request):
    subprocess.call(['gpio', '-g', 'write', '11', '0'])
    subprocess.call(['gpio', '-g', 'write', '13', '0'])
    subprocess.call(['gpio', '-g', 'write', '15', '0'])
    subprocess.call(['gpio', '-g', 'write', '16', '0'])
    subprocess.call(['gpio', '-g', 'write', '18', '0'])

    leds = []
    if request.method == "GET":
        leds = [Led(count,False) for count in range(5)]

    return render(request,"home/index.html",{"leds":leds})

@csrf_exempt
def indexAjax(request):
    if not request.is_ajax():
        raise Http404
    if request.is_ajax():
        if request.method == 'POST':
            json_data = json.loads(request.body)
            if json_data["number"] == 0:
                subprocess.call(['gpio', '-g', 'write', '11', '1'])
            if json_data["state"]:
                state = 1
            else:
                state = 0
            number = json_data["number"]
            #print "Number: " + str(number) + ", State: " + str(state)
            #statement = "gpio write " + str(number) + " " + str(state)
            #call(statement)


    return JsonResponse({"status": True})
