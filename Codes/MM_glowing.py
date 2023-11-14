import mido
from mido import Message
import time
import random

ports = mido.get_output_names()
print(ports)

outport = mido.open_output('loopMIDI Port 1')

def pulse_effect(min, max, sleep):
    n = 20
    count=0
    while n < 100:
        outport.send(Message('note_on', note=90, velocity=n))
        time.sleep(sleep)
        n+=1
        count+=1
    while n>20:
        outport.send(Message('note_on', note=90, velocity=n))
        time.sleep(sleep)
        n-=1
        count+=1
    print(count)

def calcul_temps_bpm(bpm):
    return (bpm/60)/160

    
while True:
    
    pulse_effect(20,100,calcul_temps_bpm(60))

    

# Fermer le port MIDI
outport.close()


