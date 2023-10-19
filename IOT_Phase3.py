import requests
import time
import random

 
channel_id = "2310756 "   
write_api_key = "XQP9UCOC8P7L0YS8 "  
thing_speak_url = f"https://api.thingspeak.com/update?api_key={write_api_key}"

 
def sound_data():
     
    return random.uniform(0, 10)  
while True:
    try:
        
      sound = sound_data()   
     
         
        data = {
            "field1":sound
        }

        response = requests.post(thing_speak_url, data=data)
        print("Data sent to ThingSpeak. Status code:", response.status_code)

    except Exception as e:
        print("Error:", str(e))

    time.sleep(15)