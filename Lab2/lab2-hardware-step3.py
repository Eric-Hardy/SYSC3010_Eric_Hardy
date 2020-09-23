#using the sense hat
from sense_hat import SenseHat

sense = SenseHat()
blue = (0, 0, 100)
red = (100, 0, 0)
pressure = str(round(sense.get_pressure(), 1))
temperature = str(round(sense.get_temperature(), 1))
humidity = str(round(sense.get_humidity(), 1))
while True:
    sense.show_message("Temp: " + temperature, text_colour=red, back_colour=blue)