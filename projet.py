
print('RUN : projet python')
import ConnectWifi
import umail 
import Pin, ADC 
import sleep

ConnectWifi.connect() #connecter au réseau Internet par wifi
flamme = ADC(Pin(34))
flamme.atten(ADC.ATTN_11DB) #Full range: 3.3v
buzzer=Pin(4,Pin.OUT)
while True:
  flamme_value = flamme.read() 
  sleep(0.1)
  if (flamme_value<4095): #détection d'une flamme
     buzzer.value(1) # le buzzer se met à sonner
     smtp = umail.SMTP('smtp.gmail.com', 587,username='emetteur@gmail.com', password='******')
     smtp.to('recepteur@gmail.com')
     smtp.send("Alerte incendie") # Envoie d'un email alerte
     smtp.quit()
  else:
     buzzer.value(0) #le buzzer s'arrête de sonner
