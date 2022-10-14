

def In_s2Out_s(shape, padding, dilation, kernel_size, stride):
    out_size = shape + 2 * padding - dilation * (kernel_size - 1) - 1
    out_size = out_size / float(stride)
    out_size = out_size + 1
    return out_size


def Shape2Padding(in_shape, out_shape, kernel_size, dilation = 1, stride = 1):
    a = (out_shape - 1) * stride
    b = a + 1 - in_shape + dilation * (kernel_size - 1)
    padding = b / 2.0
    return padding