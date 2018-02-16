from sense_hat import SenseHat
import time

sense = SenseHat()
sense.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)
pink = (255, 105, 180)
zeissblue = (0, 0, 255)  # 20,30,140


sense.set_pixel(5,0, zeissblue)
sense.set_pixel(5,1, zeissblue)
sense.set_pixel(5,2, zeissblue)
sense.set_pixel(5,3, zeissblue)
sense.set_pixel(5,4, zeissblue)
sense.set_pixel(5,5, zeissblue)
sense.set_pixel(5,6, zeissblue)
sense.set_pixel(5,7, zeissblue)

sense.set_pixel(6,0, zeissblue)
sense.set_pixel(6,1, zeissblue)
sense.set_pixel(6,2, zeissblue)
sense.set_pixel(6,3, zeissblue)
sense.set_pixel(6,4, zeissblue)
sense.set_pixel(6,5, zeissblue)
sense.set_pixel(6,6, zeissblue)
sense.set_pixel(6,7, zeissblue)

sense.set_pixel(7,0, zeissblue)
sense.set_pixel(7,1, zeissblue)
sense.set_pixel(7,2, zeissblue)
sense.set_pixel(7,3, zeissblue)
sense.set_pixel(7,4, zeissblue)
sense.set_pixel(7,5, zeissblue)
sense.set_pixel(7,6, zeissblue)
sense.set_pixel(7,7, zeissblue)

images = [raspi_logo, raspi_logo, plus, z, e, i, es, full, es, equals, heart]
count = 0

while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1