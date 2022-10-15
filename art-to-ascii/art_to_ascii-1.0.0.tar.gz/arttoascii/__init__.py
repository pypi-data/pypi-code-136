from PIL import Image
import functions


class ita:
    def __init__(self, path):
        self.img = Image.open(path)
        self.size = self.img.size

    def resize(self, width):
        wpercent = (width/float(self.img.size[0]))
        hsize = int((float(self.img.size[1])*float(wpercent)))
        self.img = self.img.resize((width, hsize), Image.ANTIALIAS)
        self.size = self.img.size


class ascii:
    def __init__(self, obj):
        image = obj.img
        ascii_art = []
        (width, height) = image.size
        for y in range(0, height - 1):
            line = ''
            for x in range(0, width - 1):
                px = image.getpixel((x, y))
                line += functions.convert_pixel_to_character(px)
            ascii_art.append(line)
        self.ascii_art = "\n".join(ascii_art)
        self.img_size = obj.size

    def saveToText(self, dir, name="output"):
        if (name.find('.') == -1):
            name = name + '.txt'
        with open(f'{dir}/{name}', "w") as file:
            file.write(self.ascii_art)
            file.close()
