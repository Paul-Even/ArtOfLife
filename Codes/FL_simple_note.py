import mido
from mido import Message
import time

ports = mido.get_output_names()
print(ports)

outport = mido.open_output('loopMIDI Port 1')

while True:
    outport.send(Message('note_on', note=90, velocity=100))
    outport.send(Message('note_off', note=90))
    time.sleep(1)