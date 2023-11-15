import mido
from mido import Message
import time

ports = mido.get_output_names()
print(ports)

outport = mido.open_output('loopMIDI Port FL 2')
outport2 = mido.open_output('loopMIDI Port FL2 3')

while True:
    outport.send(Message('note_on', note=50, velocity=127))
    outport.send(Message('note_off', note=50))
    time.sleep(0.2)
    outport2.send(Message('note_on', note=50, velocity=127))
    outport2.send(Message('note_off', note=50))
    time.sleep(0.7)