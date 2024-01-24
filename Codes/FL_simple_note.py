import mido
from mido import Message
import time

ports = mido.get_output_names()
print(ports)

outport = mido.open_output('loopMIDI Port FL 1')
outport2 = mido.open_output('loopMIDI Port FL2 2')

while True:
    outport.send(Message('note_on', note=60, velocity=127))
        
    time.sleep(3)
    outport2.send(Message('note_on', note=50, velocity=127))
    

    outport.send(Message('note_off', note=60))
    
    time.sleep(10)
    