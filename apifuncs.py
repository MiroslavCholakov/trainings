import requests
import random 

#randcodes=[]
#apilinksfromid=[]

def locationcodes():
    br=0
    rnd=random.randint(20,100)
    randcodes=random.sample(range(833, 102908597), 10000) 
    #for i in range(len(randcodes)):print(randcodes[i])
        #randcodes.append(random.randint(833,102908597))
    for i in range(rnd):
        complete_api_link="https://api.openweathermap.org/data/2.5/weather?id="+str(randcodes[i])+"&appid=eb26abb859972dffb7a0c0001421729b"
        api_link=requests.get(complete_api_link)
        api_data=api_link.json()
        if api_data['cod']!='404':
            apilinksfromid.append(api_link)

def average():
         tempsum=0
         avg=0
         numberoftowns=len(apilinksfromid)
  
         for i in range(numberoftowns): 
             api_data=apilinksfromid[i].json()
             town_temps=((api_data['main']['temp'])-273.15)
             tempsum+=town_temps
             avg=tempsum/numberoftowns     
         return numberoftowns, avg 
     
def  coldest():
     mintemp=9000
     coldesttown=" "
     for i in range(len(apilinksfromid)):
         api_data=apilinksfromid[i].json()
         town_temps=((api_data['main']['temp'])-273.15)
         if town_temps<mintemp:
             mintemp=town_temps
         if mintemp==town_temps:
             coldesttown=api_data['name']
     return coldesttown
 
def singletowncheck(input):
    location=input
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=eb26abb859972dffb7a0c0001421729b"
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()
    if api_data['cod']=='404':
        print("Wrong city{}",format(location))
    else:
        town_temps=((api_data['main']['temp'])-273.15) 
        weather=(api_data['weather'][0]['description'])
        hmdt=api_data['main']['humidity']
        return town_temps,weather,hmdt