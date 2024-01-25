from pylsl import StreamInlet,resolve_stream #import pylsl to use LSL and recover the data from the sensors
import numpy as np #import numpy to calculate the average of the EDA values
import mido #import mido to send notes to loopMidi
from mido import Message
import time #import time to make the pulsing effect

ports = mido.get_output_names() #getting the names of all the detected mido ports 
print(ports)
outport = mido.open_output('loopMIDI Port FL 1') #selecting the port to receive the "heartbeat" notes
outport2 = mido.open_output('loopMIDI Port FL2 2') #selecting the port to receive the "breathing" notes
outport3 = mido.open_output('loopMIDI Port MM 3')

streams = resolve_stream('name','OpenSignals') #receive the LSL stream from OpenSignals
stream = StreamInlet(streams[0]) #create an stream from the first stream of the list

in_resp = False #boolean checking if the user is inhaling or exhaling
eda_value = 0 #mean value of all the EDA values received in 10 seconds
pulse_count = 0 #counting the number of pulses
n=0 #counting the number of values received
inPulse = False #boolean checking if a pulse is happening
keynote = 0 #defining the note to be sent as the "breathing" note
r=0 #RGB values for the visuals' color
g=0
b=0

def pulse_effect(min, max, sleep): #function that creates the "pulse" effect on MadMapper
    n = 20
    count=0
    while n < 100:
        outport3.send(Message('note_on', note=127, velocity=n))
        time.sleep(sleep)
        n+=1
        count+=1
    #outport3.send(Message('note_on', note=126, velocity=n))
    while n>20:
        outport3.send(Message('note_on', note=127, velocity=n))
        time.sleep(sleep)
        n-=1
        count+=1
    #outport3.send(Message('note_on', note=126, velocity=n))
    print(count)




while True:
        n+=1
        data_eda = [] #create an empty list to recover the eda data
        timestamp = [] #create an empty list to recover the timestamp
        resp_count = 0
    
    
        values, timestamp = stream.pull_sample() #recover the data and their timestamp
        if values[1] < -0.4 and inPulse==False: #if the pulse value is under -0.4, we consider that a pulse is happening
                print("heartbeat")
                inPulse = True
                try:
                        pulse_count +=1
                        
                        if(pulse_count%4 == 0): #output a note every 4 pulse
                                
                                outport.send(Message('note_on', note=60, velocity=127))
                                pulse_effect(10,127,0.005)
                                print("pulse sent")
                except ValueError:
                        print("Invalid input. Please enter a valid integer between 21 and 108.")

        elif values[1] > 0 and inPulse==True:
            inPulse = False
            print("pulse false")

        data_eda.append(values[2]) #add the latest eda value to an array

        if(n >= 10000): #calculate the average eda value every 10 seconds and resets the counter
              eda_value = np.mean(data_eda)
              print(eda_value)
              outport3.send(Message('note_on', note=126, velocity=r))
              outport3.send(Message('note_on', note=125, velocity=g))
              outport3.send(Message('note_on', note=124, velocity=b))
              
              n=0

        if(eda_value > 0): #choosing the note to be sent depending on the average eda value of the last 10s
                
                if(eda_value < 2):
                    keynote = 30
                    r=127
                    g=127
                    b=127
                elif(eda_value > 2 and eda_value < 6):
                      keynote = 35
                      r=127
                      g=127
                      b=0
                elif(eda_value > 6 and eda_value < 10):
                      keynote = 40
                      r=0
                      g=127
                      b=0
                elif(eda_value > 10 and eda_value < 14):
                      keynote = 45
                      r=0
                      g=127
                      b=127
                elif(eda_value > 14 and eda_value < 18):
                      keynote = 50
                      r=0
                      g=0
                      b=127
                elif(eda_value > 18 and eda_value < 22):
                      keynote = 55
                      r=127
                      g=0
                      b=127
                elif(eda_value > 22 and eda_value < 26):
                      r=127
                      g=0
                      b=0
                elif(eda_value > 26):
                      keynote = 70
                      r=63
                      g=63
                      b=63
        
        if in_resp == True:
            if values[3] < -0.1: #detecting if the user is exhaling
                print("fin resp")
                in_resp = False
                #print(resp_count)
                #time.sleep(0.1)
                outport2.send(Message('note_off', note=keynote)) #stopping the "breathing" note
                outport3.send(Message('note_on', note=123, velocity=10)) #sending the "breathing" note
        elif in_resp == False:
            if values[3] > 0.1: #detecting if the user is inhaling
                 print("début resp")
                 resp_count+=1
                 in_resp = True
                 #print(resp_count)
                 #time.sleep(0.1)
                 outport2.send(Message('note_on', note=keynote, velocity=127)) #sending the "breathing" note
                 outport3.send(Message('note_on', note=123, velocity=50)) #sending the "breathing" note

        