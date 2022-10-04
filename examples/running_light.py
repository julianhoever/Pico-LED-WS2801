from time import sleep

from led_strip import LEDStrip
from pixel import Pixel


def main() -> None:
    strip = LEDStrip(leds=3)

    while True:
        for i in range(len(strip)):
            strip[i] = Pixel(255, 0, 32)
            strip[i - 1] = Pixel(0, 0, 0)
            sleep(0.5)


if __name__ == "__main__":
    main()
