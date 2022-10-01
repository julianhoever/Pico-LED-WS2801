from machine import Pin, SPI
from pixel import Pixel, to_bytes


class LEDStrip:
    def __init__(
        self,
        leds: int | list[Pixel],
        auto_update: bool = True,
        spi_id: int = 0,
        sck: Pin = Pin(2, mode=Pin.OUT),
        mosi: Pin = Pin(3, mode=Pin.OUT),
        baudrate: int = 10000,
    ) -> None:
        if isinstance(leds, int):
            if leds < 0:
                raise ValueError(f"'leds' must be >= 0 (actual {leds})")
            self._leds = [Pixel(0, 0, 0) for _ in range(leds)]
        else:
            self._leds = leds

        self._auto_update = auto_update

        self._spi_device = SPI(
            spi_id, sck=sck, mosi=mosi, baudrate=baudrate, firstbit=SPI.MSB, bits=24
        )

        if self._auto_update:
            self.update_leds()

    @property
    def length(self) -> int:
        return len(self._leds)

    def update_leds(self) -> None:
        for led in self._leds:
            self._spi_device.write(to_bytes(led))

    def set_led(self, pos: int, pixel: Pixel) -> None:
        self._leds[pos] = pixel
        if self._auto_update:
            self.update_leds()

    def get_led(self, pos: int) -> Pixel:
        return self._leds[pos]

    def turn_off(self) -> None:
        self._leds = [Pixel(0, 0, 0) for _ in range(len(self))]
        if self._auto_update:
            self.update_leds()

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, key: int) -> Pixel:
        return self.get_led(key)

    def __setitem__(self, key: int, value: Pixel) -> None:
        self.set_led(key, value)
