import struct
import zlib


class BinaryParser:

    struct_objects = dict()
    type_codes = dict(
        int8="b", uint8="B", int16="h", uint16="H",
        int32="i", uint32="I", int64="q", uint64="Q",
        float16="e", float32="f", float64="d")

    def __init__(self, data, little_endian=True):
        self.data = data
        self.position = 0
        self.little_endian = little_endian
        
    @property
    def length(self):
        return len(self.data)

    @property
    def remaining_length(self):
        return self.length - self.position

    def get_struct(self, type_code):
        endian_code = "<" if self.little_endian else ">"
        struct_code = endian_code + type_code
        try:
            struct_object = self.struct_objects[struct_code]
        except KeyError:
            struct_object = struct.Struct(struct_code)
            self.struct_objects[struct_code] = struct_object
        return struct_object

    def read(self, type_code):
        struct_object = self.get_struct(type_code)
        chunk = self.data[self.position:self.position + struct_object.size]
        output = struct_object.unpack(chunk)
        self.position += struct_object.size
        return output

    def read_number(self, type):
        return self.read(self.type_codes[type])[0]

    def read_int8(self):
        return self.read("b")[0]

    def read_uint8(self):
        return self.read("B")[0]

    def read_int16(self):
        return self.read("h")[0]

    def read_uint16(self):
        return self.read("H")[0]

    def read_int32(self):
        return self.read("i")[0]

    def read_uint32(self):
        return self.read("I")[0]

    def read_int64(self):
        return self.read("q")[0]

    def read_uint64(self):
        return self.read("Q")[0]

    def read_float16(self):
        return self.read("e")[0]

    def read_float32(self):
        return self.read("f")[0]

    def read_float64(self):
        return self.read("d")[0]

    def read_string(self, length=None):
        length = min(length or self.remaining_length, self.remaining_length)
        chunk = self.data[self.position:self.position + length]
        null_index = chunk.find(b"\0")
        if null_index >= 0:
            length = null_index + 1
            chunk = chunk[:null_index]
        self.position += length
        return chunk.decode()

    def read_fixed_length_string(self, length):
        output = []
        for _ in range(length):
            character = self.data[self.position]
            self.position += 1
            if character > 0:
                output.append(chr(character))
        return "".join(output)

    def read_fixed_length_trimmed_string(self, length):
        output = []
        for _ in range(length):
            character = self.data[self.position]
            self.position += 1
            if character > 32:
                output.append(chr(character))
        return "".join(output)


def add_in_resize_array(array, index, value, fill=None):
    if index >= len(array):
        array.extend([fill] * (index - len(array) + 1))
    array[index] = value


def decompress_bgzf(data):
    chunks = []
    decompressor = zlib.decompressobj(31)
    chunks.append(decompressor.decompress(data))
    while decompressor.unused_data:
        remaining_bytes = decompressor.unused_data
        decompressor = zlib.decompressobj(31)
        chunks.append(decompressor.decompress(remaining_bytes))
    return b"".join(chunks)
