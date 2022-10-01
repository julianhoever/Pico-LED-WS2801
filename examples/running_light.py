from time import sleep

from led_strip import LEDStrip
from pixel import Pixel


def main() -> None:
    strip = LEDStrip(leds=3, auto_update=False, baudrate=10000)
    strip.update_leds()

    while True:
        for i in range(len(strip)):
            strip[i] = Pixel(0, 255, 0)
            strip[i - 1] = Pixel(0, 0, 0)
            strip.update_leds()
            sleep(0.5)


if __name__ == "__main__":
    main()
