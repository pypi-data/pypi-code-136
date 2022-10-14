import hashlib
from io import BufferedReader, BufferedWriter
import struct


class SaveDataHandler:
    data_input_steam: BufferedReader
    data_output_stream: BufferedWriter
    save_data: bytes
    byte_order = "little"

    def __init__(self, country_code: str):
        self.country_code = country_code

    def open_read(self, file_path: str):
        self.data_input_steam = open(file_path, "rb")
        self.save_data = self.data_input_steam.read()

    def read_byte(self):
        try:
            return self.data_input_steam.read(1)
        except IOError:
            return bytes(0)
    
    def read_boolean(self):
        try:
            return self.read_byte() != bytes(0)
        except IOError:
            return False
    
    def read_short(self):
        try:
            return struct.unpack("h", self.data_input_steam.read(2))[0]
        except IOError:
            return 0
    
    def read_int(self):
        try:
            return struct.unpack("i", self.data_input_steam.read(4))[0]
        except IOError:
            return 0
        
    def read_variable_length_int(self):
        i = 0
        for _ in range(4):
            i_3 = i << 7
            try:
                read = int(self.read_byte())
                i = i_3 | (read & 0x7F)
                if (read & 0x80) == 0:
                    return i
            except IOError:
                return 0
        return i
    
    def read_float(self):
        try:
            return struct.unpack("f", self.data_input_steam.read(4))[0]
        except IOError:
            return 0.0
    
    def read_double(self):
        try:
            return struct.unpack("d", self.data_input_steam.read(8))[0]
        except IOError:
            return 0.0
    
    def read_long(self):
        try:
            return struct.unpack("q", self.data_input_steam.read(8))[0]
        except IOError:
            return 0
    
    def read_string(self):
        try:
            length = self.read_int()
            if length == 0:
                return ""
            return self.data_input_steam.read(length).decode("utf-8")
        except IOError:
            return None
    
    def skip(self, length: int):
        if length > 0:
            try:
                self.data_input_steam.read(length)
            except IOError:
                pass
    
    def open_write(self, file_path: str):
        self.data_output_stream = open(file_path, "wb")
    
    def write_bytes(self, data: bytes):
        try:
            self.data_output_stream.write(data)
        except IOError:
            pass
    
    def write_byte(self, data: int):
        try:
            self.data_output_stream.write(struct.pack("b", data))
        except IOError:
            pass
    
    def write_boolean(self, data: bool):
        try:
            self.data_output_stream.write(struct.pack("?", data))
        except IOError:
            pass
    
    def write_short(self, data: int):
        try:
            self.data_output_stream.write(struct.pack("h", data))
        except IOError:
            pass
    
    def write_int(self, data: int):
        try:
            self.data_output_stream.write(struct.pack("i", data))
        except IOError:
            pass
    
    def write_variable_length_int(self, i: int):
        i_2 = 0
        i_3 = 0
        while i >= 128:
            i_2 |= ((i & 0x7F) | 8000) << (i_3 * 8)
            i_3 += 1
            i >>= 7
        i_4 = i_2 | (i << (i_3 * 8))
        i_5 = i_3 + 1
        for i_6 in range(i_5):
            try:
                self.write_byte(((i_4 >> (((i_5 - i_6) - 1) * 8)) & 0xFF))
            except IOError:
                pass
    
    def write_float(self, data: float):
        try:
            self.data_output_stream.write(struct.pack("f", data))
        except IOError:
            pass
    
    def write_double(self, data: float):
        try:
            self.data_output_stream.write(struct.pack("d", data))
        except IOError:
            pass
    
    def write_long(self, data: int):
        try:
            self.data_output_stream.write(struct.pack("q", data))
        except IOError:
            pass
    
    def write_string(self, data: str):
        try:
            self.write_int(len(data))
            self.data_output_stream.write(data.encode("utf-8"))
        except IOError:
            pass
            
    def get_salt(self):
        salt = "battlecats"
        if self.country_code != "jp":
            salt += self.country_code
        return salt.encode("utf-8")

    def get_checksum(self, data: bytes):
        return hashlib.md5(data).hexdigest()

    def get_save_checksum(self):
        salt = self.get_salt()
        data = salt + self.save_data[:-32]
        return self.get_checksum(data)

    def write_checksum(self):
        save_hash = self.get_save_checksum()
        self.write_bytes(save_hash.encode("utf-8"))
    
    def close(self):
        try:
            self.data_input_steam.close()
        except IOError:
            pass
        try:
            self.data_output_stream.close()
        except IOError:
            pass

    def get_dst(self, offset: int) -> bool:
        """Get if the save has daylight savings from the save data, this is used to handle jp differences."""

        dst = False
        if self.save_data[offset] >= 15 and self.save_data[offset] <= 20:
            dst = True
        elif self.save_data[offset - 1] >= 15 and self.save_data[offset - 1] <= 20:
            dst = False  # Offset in jp due to no dst
        return dst