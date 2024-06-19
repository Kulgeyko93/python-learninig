class Image:
    def __init__(self, resolution, title, extension) -> None:
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def set_resize(self, resolution):
        self.resolution = resolution

    def get_resize(self):
        return self.resolution


class PNGImage(Image):
    def get_name(self):
        return f"{self.resolution}.{self.extension}"


png = PNGImage('5x5', 't', 'png')

print(png.get_name())
print(png.resolution)

png.set_resize('34x3')
print(png.resolution)
