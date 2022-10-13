from dataclasses import dataclass


class DataLoader:

    def __init__(self, path):
        self.path = path
        self.file = open(self.path, "rb")
    
    def close(self):
        self.file.close()
    
    def load(self, start, size=None):
        self.file.seek(start, 0)
        if size is None:
            return self.file.read()
        return self.file.read(size)


class BufferedDataLoader:
    """
    Wrapper for other DataLoaders that buffers. Used internally by the BigWigReader.
    self class does not implement DataLoader. It is not meant to be passed in in
    BigWigReader as the DataLoader you must provide. When you initially request data,
    potentially much more (buffer_size) than you ask for is loaded into a buffer.
    self buffer is checked first for subsequent requests. Can also be used for streaming.
    When self option is used, data is stored in the buffer until it's read, at which
    point the read data and all data preceding is deleted.
    """

    def __init__(self, data_loader, buffer_size=None):
        self.data_loader = data_loader
        self.buffer_size = buffer_size
        self.buffer = None

    def load(self, start, size):
        # if the data isn't in the buffer, load it
        if not self.buffer_contains_data(start, size):
            self.load_data_into_buffer(start, size)
        return self.get_data_from_buffer(start, size)
    
    def load_data_into_buffer(self, start, size):
        end = None if self.buffer_size is None else max(self.buffer_size, size)
        data = self.data_loader.load(start, end)
        self.buffer = LoaderBuffer(
            data=data,
            start=start)

    def buffer_contains_data(self, start, size):
        if self.buffer is None:
            return False
        if self.buffer_size is None:
            return True
        end = start + size
        buffer_end = self.buffer.start + len(self.buffer.data)
        return start >= self.buffer.start and end <= buffer_end
    
    def get_data_from_buffer(self, start, size):
        """
        returns the given ranges data if it's currently in the buffer, otherwise throws error,
        works under the assumption that we've already loaded the data
        """
        if self.buffer is None:
            raise RuntimeError("invalid state: buffer should not be empty")
        slice_start = start - self.buffer.start
        slice_end = slice_start + size
        if size > len(self.buffer.data):
            raise RuntimeError(f"requested {size} bytes but only got back {len(self.buffer.data)}")
        return self.buffer.data[slice_start:slice_end]


@dataclass
class LoaderBuffer:
    data: bytes
    start: int
