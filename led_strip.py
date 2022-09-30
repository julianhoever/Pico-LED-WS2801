from machine import Pin, SPI


class Pixel:
    def __init__(self, red: int, green: int, blue: int, brightness: float = 1) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.brightness = brightness

    @property
    def bytes(self) -> bytes:
        red = int(self.red * self.brightness)
        green = int(self.green * self.brightness)
        blue = int(self.blue * self.brightness)
        int_value = (red << 16) + (green << 8) + blue
        return int_value.to_bytes(3, "big")


class LEDStrip:
    def __init__(self, leds: list[Pixel], spi_id: int, sck: Pin, mosi: Pin, baudrate: int = 4000) -> None:
        self.leds = leds
        self.spi_device = SPI(
            spi_id,
            sck=sck,
            mosi=mosi,
            baudrate=baudrate,
            firstbit=SPI.MSB,
            bits=24,
        )
        self._update_leds()

    @property
    def bytes(self) -> bytes:
        result = bytearray()
        for led in self.leds:
            result += led.bytes
        return bytes(result)

    def _update_leds(self) -> None:
        for led in self.leds:
            self.spi_device.write(led.bytes)

    def set_led(self, pos: int, pixel: Pixel) -> None:
        self.leds[pos] = pixel
        self._update_leds()

    def get_led(self, pos: int) -> Pixel:
        return self.leds[pos]
