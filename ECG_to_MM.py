import mido
from mido import Message
from pylsl import StreamInlet,resolve_stream #import pylsl to use LSL and recover the data from the sensors
import time

ports = mido.get_output_names()
print(ports)

outport = mido.open_output('loopMIDI Port 3')
outport2 = mido.open_output('loopMIDI Port FL 1')
outport3 = mido.open_output('loopMIDI Port FL2 2')

streams = resolve_stream('name','OpenSignals') #recover the list of LSL stream of type 'ecg'
stream = StreamInlet(streams[0]) #create an stream from the first stream of the list
def calcul_temps_bpm(bpm):
    return (bpm/60)/160

def pulse_effect(sleep):
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
print("bito")
position = 0
while True:
    n = 0
    while n < 10000 : 
        values, timestamp = stream.pull_sample() #recover the data and their timestamp_ecg
        if values[1] < -0.4:
            last_index = position
            position = n
            #np.where(ecg_transform = i)
            if position-last_index > 200:
                #peak_count+=1
                print(n)
                print("heartbeat")
                #outport2.send(Message('note_on', note=50, velocity=127))
                #outport2.send(Message('note_off', note=50))
                #pulse_effect(calcul_temps_bpm(20))
                
                
        n+=1