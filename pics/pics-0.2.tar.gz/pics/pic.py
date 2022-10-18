import os


class Pics:
    def __init__(self, Image):
        self.Image = Image

    def cut_picture(self, pic_path: str,
                    output_jpg_path=None,
                    size_list: list = '',
                    limit_size: float = 3):
        """
        输入一张任意比例的图片，裁切成指定大小的图片。嵌套列表以应对多尺寸情况。
        """
        pic_folder = os.path.dirname(pic_path)
        output_jpg_path = pic_folder if not output_jpg_path else output_jpg_path
        size_list = [[1440, 2560]] if not size_list else size_list

        for once in size_list:
            width, high = int(once[0]), int(once[1])
            output_file = os.path.join(output_jpg_path, "{}x{}.jpg".format(width, high))
            if os.path.exists(output_file):
                continue

            try:
                pic_opened = self.Image.open(pic_path)
                pic_opened.convert('RGB')
            except FileNotFoundError as e:
                print("异常：文件没找到 %s" % e)
                continue
            except Exception as e:
                raise TypeError("异常：此文件打不开或有问题 %s" % pic_path)

            jpg_ = self.__crop__(pic_opened, width, high)
            if not jpg_:
                print("该图片资源有有误%s" % output_file)
                continue
            else:
                jpg_.convert('RGB').save(output_file, quality=100)
            pic_after_cut = os.path.join(output_jpg_path, '{}x{}.jpg'.format(width, high))
            if limit_size:
                quality = 100
                while True:
                    pic_size = os.path.getsize(pic_after_cut)
                    if pic_size > limit_size * 1024 * 1024:
                        quality -= 2
                        jpg_.convert('RGB').save(output_file, quality=quality)
                    else:
                        print(quality)
                        break
            return output_file

    def __crop__(self, pic_image, nx, ny):
        """
        剪裁图片，小图切大，大图切小。
        """
        try:
            x, y = pic_image.size
        except AttributeError:
            return None

        k = x / y
        nk = nx / ny
        if k > nk:  # 切两边
            x_left = (x / 2) - (y * nk / 2)
            x_right = (x / 2) + (y * nk / 2)
            region = (x_left, 0, x_right, y)  # 对角线两点坐标的合集
            pic_image = pic_image.crop(region)
        else:  # 切上下
            y_top = (y / 2) - (x / nk / 2)
            y_bottom = (y / 2) + (x / nk / 2)
            region = (0, y_top, x, y_bottom)
            pic_image = pic_image.crop(region)

        return pic_image.resize((nx, ny), 1)
