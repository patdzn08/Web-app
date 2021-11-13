from django.shortcuts import render
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "yPfDRcQKBMOkOjMAG3WtXIzcCmmI0t5j"
main_api2 ="http://www.mapquestapi.com/directions/v2/alternateroutes?"




def home(request):
    #Input Directions
    InputOrig=request.POST.get('inputlocation')
    InputDest=request.POST.get('inputDestination')
    
    #MapQuest
    url = main_api + urllib.parse.urlencode({"key": key, "from":InputOrig, "to":InputDest})
    url2 = main_api2 +urllib.parse.urlencode({"key": key, "from":InputOrig, "to" :InputDest})
    print(url)
    print(url2)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    json_data2 = requests.get(url2).json()


    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        directions=[]
        directions2=[]
        #Detination Time
        Trip_Duration=json_data["route"]["formattedTime"] 
        Trip_Duration2=json_data2["route"]["formattedTime"]
        #Distance in KM
        KM=str("{:.2f}".format((json_data["route"]["distance"])*1.61))
        KM2=str("{:.2f}".format((json_data2["route"]["distance"])*1.61))
        #Fuel in Liters
        Fuel=str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))
        Fuel2=str("{:.2f}".format((json_data2["route"]["fuelUsed"])*3.78))
        #Directions
        Manuever=json_data["route"]["legs"][0]["maneuvers"]
        if (InputDest and InputOrig is not None):
            for each in Manuever:
                directions.append(each["narrative"]+ " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))


        Manuever2=json_data2["route"]["legs"][0]["maneuvers"]
        if (InputDest and InputOrig is not None):
            for each2 in Manuever2:
                directions2.append(each2["narrative"]+ " (" + str("{:.2f}".format((each2["distance"])*1.61) + " km)"))


        data={
            "InputOrig":InputOrig,
            "InputDest":InputDest,
            "KM":KM,
            "Trip_Duration":Trip_Duration,
            "Fuel": Fuel,
            "directions":directions,
            "directions2":directions2,
            "Fuel2": Fuel2,
            "Trip_Duration2":Trip_Duration2,
            "KM2":KM2,


        }
    
        return render(request, 'Maps/home.html',data)


def about(request):
    return render(request, 'Maps/about.html', {'title': 'About'})

