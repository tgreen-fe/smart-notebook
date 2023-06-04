import urequests
import network
import time
import ujson

ssid = 'Green'
wifiPassword = 'thamsams'


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,wifiPassword)
 
# connect the network       
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    #print('connected')
    ip=wlan.ifconfig()[0]
    #print('IP: ', ip)
    

url = "http://86.3.69.37:81/testUpload.json"

res = urequests.post(url)

parsed = ujson.loads(res.text)

for i in range(len(parsed)):
    
    title = parsed[i]["title"]
    summary = parsed[i]["summary"]
    pageNumber = parsed[i]["pageNum"]
    date = parsed[i]["date"]

    print(title, pageNumber, date, "\n")




