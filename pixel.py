class Pixel:
    def __init__(self, red: int, green: int, blue: int, brightness: float = 1) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.brightness = brightness

    @staticmethod
    def from_bytes(data: bytes) -> "Pixel":
        if len(data) != 3:
            raise ValueError("One pixel contains exactly 3 bytes of data.")
        else:
            return Pixel(data[0], data[1], data[2])

    def to_bytes(self) -> bytes:
        red = int(self.red * self.brightness)
        green = int(self.green * self.brightness)
        blue = int(self.blue * self.brightness)
        int_value = (red << 16) + (green << 8) + blue
        return int_value.to_bytes(3, "big")
