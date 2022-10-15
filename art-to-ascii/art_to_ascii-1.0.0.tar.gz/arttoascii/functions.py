chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def convert_pixel_to_character(pixel):
    if (len(pixel) != 3):
        (r, g, b) = pixel[:-1]
    else:
        (r, g, b) = pixel
    pixel_brightness = r + g + b
    max_brightness = 255 * 3
    brightness_weight = len(chars) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    return chars[index]

