#import the file (needs to be in the same directory)
import wol

#code to only create magic packet
magic_packet = wol.create_magic_packet('AB:CD:EF:GH:IJ:KL')

#code to wake up and machine
wol.wake_up('AB:CD:EF:GH:IJ:KL')