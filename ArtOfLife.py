# This is an example of a script to measure the heart rate of an user

# Once you have put the info of your sensor in the resolve_stream function, it will find the stream and create an stream to access the 
# data

from pylsl import StreamInlet,resolve_stream #import pylsl to use LSL and recover the data from the sensors
import numpy as np #import numpy to create the ecg_peak filter
import matplotlib.pyplot as plt #import matplotlib to plot the graph
import time
import random
import mido
from mido import Message

ports = mido.get_output_names()
portname = [name for name in ports if 'Disklavier' in name]



streams = resolve_stream('name','OpenSignals') #recover the list of LSL stream of type 'ecg'

stream = StreamInlet(streams[0]) #create an stream from the first stream of the list

v = np.linspace(0.5 * np.pi, 1.5 * np.pi, 15) #create a linear vector between pi/2 and 3pi/2
peak_filter = np.sin(v) #create a sin wave on the linear space

n=0



in_resp = False
resp_count_final = 30
position = 0
eda_value = 0
heart_rate = 0


while True:

    print("start")
    data_eda = [] #create an empty list to recover the data
    data_ecg = [] #create an empty list to recover the data
    timestamp_ecg = [] #create an empty list to recover the timestamp_ecg
    resp_count = 0
    data_resp = [] #create an empty list to recover the data
    
    while n < 10000: #collect 1000 datapoint
        values, timestamp = stream.pull_sample() #recover the data and their timestamp_ecg
        data_ecg.append(values[1]) #add the values to the data
        timestamp_ecg.append(timestamp) #add the timestamp_ecg to the time data
        if values[1] < -0.3:
            last_index = position
            position = n
            #np.where(ecg_transform = i)
            if position-last_index > 200:
                #peak_count+=1
                print(n)
                print("heartbeat")
                if(eda_value != 0):
                    print("note de piano")
                    with mido.open_output(portname[0]) as port:
                        try:
                            midi_note = max(0, min(resp_count_final*2, 128))
                            print("midi = ", midi_note)
                            port.send(Message('note_on', note=int(midi_note), velocity=eda_value*5))
                            
                            # Send a note-off message (optional)
                            port.send(Message('note_off', note=int(midi_note), velocity=0))
                        except ValueError:
                            print("Invalid input. Please enter a valid integer between 21 and 108.")


        sample_eda, timestamp_eda = stream.pull_sample() #recover the sample_eda and the corresponding timestamp_eda from the stream
        data_eda.append(values[2]) #add the sample_eda to the data

        data_resp.append(values[3]) #add the sample to the data
        if in_resp == True:
            if values[3] < -0.1:
                #print("fin resp")
                in_resp = False
                #print(resp_count)
                #time.sleep(0.1)
        elif in_resp == False:
            if values[3] > 0.1:
                 #print("début resp")
                 resp_count+=1
                 in_resp = True
                 #print(resp_count)
                 #time.sleep(0.1)

        n+=1

        


    print("end")

    ecg_transform = np.correlate(data_ecg,peak_filter,mode='same') #correlate the ecg_peak filter with the signal to highlight the ecg_peak
    print("length: ",len(ecg_transform))

    ecg_peak = float(abs(max(ecg_transform))) * 0.50 #create the threshold for the max ecg_peak
    print("max: ",ecg_peak)
    time = timestamp_ecg[-1] - timestamp_ecg[0] #compute the total time of the data
    peak_count = 0 #create a counter for the ecg_peak in the data
    last_index = 0

    for i in ecg_transform: #look at the number of ecg_peak in the data
        if i > ecg_peak:
            position = int(np.where(ecg_transform == i)[0][0])
            #np.where(ecg_transform = i)
            if position != last_index +1 and position != last_index +2:
                peak_count+=1
                #print(i)
                
                #print("index: ", np.where(ecg_transform == i)[0][0])
            last_index = int(np.where(ecg_transform == i)[0][0])
            #print("index: ", last_index)

    peak_count+=0
    heart_rate = (peak_count/time)*60 #to compute the heart rate divide the number of ecg_peak by the time and multiply it by 60 to have the bpm
    resp_count = (resp_count/time)*60
    #print("number of ecg_peak: ",peak_count)
    #print("time: ",time)
    eda_value = sum(data_eda)/len(data_eda)
    print("heart rate: ",int(heart_rate))
    print("EDA : ", eda_value)
    print("Resp count: ",int(resp_count))
    
    print("oui")
    list_value = []
    n=0
    resp_count_final = resp_count

    #plt.plot(ecg_transform)
    #plt.show()

    

    
    
    