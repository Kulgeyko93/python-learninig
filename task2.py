class Image:
    def __init__(self, resolution, title, extension) -> None:
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def set_resize(self, resolution):
        self.resolution = resolution

    def get_resize(self):
        return self.resolution


image = Image('64x64', 'title1', 'extension1')

print(image.get_resize())

image.set_resize('128x128')

print(image.get_resize())

image2 = Image('6x6', 'title2', 'extension2')

print(image2.get_resize())

image2.set_resize('12x12')

print(image2.get_resize())
