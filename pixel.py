class Pixel:
    def __init__(self, red: int, green: int, blue: int, brightness: float = 1) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.brightness = brightness


def to_bytes(pixel: Pixel) -> bytes:
    red = int(pixel.red * pixel.brightness)
    green = int(pixel.green * pixel.brightness)
    blue = int(pixel.blue * pixel.brightness)
    int_value = (red << 16) + (green << 8) + blue
    return int_value.to_bytes(3, "big")
