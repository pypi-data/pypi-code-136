def bounds_to_center_and_size(bounds):
    width = bounds[1] - bounds[0]
    heigth = bounds[3] - bounds[2]

    center_x = (bounds[1] + bounds[0]) / 2.0
    center_y = (bounds[3] + bounds[2]) / 2.0

    return center_x, center_y, width, heigth
