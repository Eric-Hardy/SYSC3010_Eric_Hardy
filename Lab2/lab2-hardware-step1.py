from sense_hat import SenseHat
import time

#Note: The online emulator does not support importing the required module

s = SenseHat()
s.low_light = True

white = (255,255,255)
nothing = (0,0,0)

def e():
    W = white
    O = nothing
    logo = [
    O, W, W, W, W, W, O, O, 
    O, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, W, W, W, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, W, W, W, W, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def h():
    W = white
    O = nothing
    logo = [
    O, W, O, O, O, W, O, O,
    O, W, O, O, O, W, O, O,
    O, W, O, O, O, W, O, O,
    O, W, W, W, W, W, O, O,
    O, W, O, O, O, W, O, O,
    O, W, O, O, O, W, O, O,
    O, W, O, O, O, W, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

images = [ e, h]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1