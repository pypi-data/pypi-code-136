import random
import numpy as np
from std.file import Text

def initialize_vocab(file, start=2):
    index = start
    vocab = {}
    for word in Text(file):
        assert word and word == word.strip()
        assert word not in vocab
        vocab[word] = index
        index += 1
    return vocab


class SymbolicModel:
    def __init__(self, model=None):
        self.model = model
        
    def sanctity_check(self):
        if self.vocab:
            assert min(self.vocab.values()) == 2
            assert max(self.vocab.values()) == self.dimension - 1
        return True
        
    def initialize_vocab(self, start=2):
        self.vocab = initialize_vocab(self.vocabFile, start=start)
        self.sanctity_check()
        self.UNK_INDEX = 1
        
    def preprocess(self, modelPath=''):
        self.model.outputs
        self.model.make_substitutions()
        if modelPath:
            print(modelPath)
            import h5py
            with h5py.File(modelPath, mode='r') as f:
                self.model.load_weights(f)
                
    def forward(self, *inputs):
        for symbol, data in zip(self.model.inputs, inputs):
            symbol.numpy = data
            for symbolic_size, size in zip(symbol.shape, data.shape):
                symbolic_size.numpy = np.array(size)
        
        outputs = self.model.outputs
        
        if isinstance(outputs, (tuple, list)):
            data = type(outputs)((type(output)(output.torch for output in output) if isinstance(output, (tuple, list)) else output.torch for output in outputs))
        else:
            data = outputs.torch
            
        for symbol, data in zip(self.model.inputs, inputs):
            del symbol.numpy
            self.model._assumptions_clear_cache('torch', symbol)
            for symbolic_size, size in zip(symbol.shape, data.shape):
                try:
                    del symbolic_size.numpy
                    self.model._assumptions_clear_cache('torch', symbolic_size)
                except AttributeError:
                    ...

        return data


class Sequence:

    def __init__(self,
                 original_list,
                 x_name=None,
                 y_name=None,
                 batch_size=32,
                 dynamic_batch_size=None,
                 shuffle=False,
                 numpify_x=None,
                 numpify_y=None,
                 sort=True,
                 reverse=False,
                 device=-1):
        
        if dynamic_batch_size:
            self.batch_size = dynamic_batch_size
            self.dynamic_batch_size = True
        else:
            self.batch_size = batch_size
            self.dynamic_batch_size = False
            
        if x_name is None:
            *x_name, y_name = eval(original_list[0].__doc__.strip())
            if len(x_name) == 1:
                x_name = x_name[0]
        
        self.x_name = x_name
        if sort:
            self.original_list = original_list
            self.counting_sort(reverse=reverse)
        else:
            self.training_list = original_list        

        self.y_name = y_name
        self.numpify_x = numpify_x
        self.numpify_y = numpify_y if y_name else None
        self.shuffle = shuffle if y_name else False
        self.device = device
#         self.indexDict = {}

    def predict(self, model, numpy=True): 
        return self.reorder(model.predict_generator(self), numpy=numpy)
    
    def reorder(self, y_pred, numpy=True):
        if not hasattr(self, 'original_list'):
            return y_pred
        
        for inst, result in zip(self.training_list, y_pred):
            inst.result = result
        y_pred = [inst.result for inst in self.original_list]
        
        if numpy:
            y_pred = np.array(y_pred)           
        return y_pred
        
    def counting_sort_utility(self, x_name, original_list, reverse=False):
        training_list = []
        dicOfInstance = []    
                
        for inst in original_list:
            seq_length = len(getattr(inst, x_name))            
            assert seq_length > 0
            
            if len(dicOfInstance) < seq_length:
                dicOfInstance += [None] * (seq_length - len(dicOfInstance))
                
            index = seq_length - 1            
            
            if dicOfInstance[index] is None:
                dicOfInstance[index] = []            
            
            dicOfInstance[index].append(inst)
            
        # concatenate all the instances order by seq_length
        print('maximum seq_length =', len(dicOfInstance))
        
        for index in range(len(dicOfInstance)):
            if dicOfInstance[index] is not None:
                training_list += dicOfInstance[index]
                
        if reverse:
            training_list.reverse()
            
        return training_list          
        
    def counting_sort(self, reverse=False):
        if isinstance(self.x_name, str):
            self.training_list = self.counting_sort_utility(self.x_name, self.original_list, reverse=reverse)
        else:
            training_list = self.original_list
            for x_name in self.x_name:
                training_list = self.counting_sort_utility(x_name, training_list, reverse=reverse)
            self.training_list = training_list            
        
    def __getitem__(self, index):
        return self.arr[index]
    
    def batches(self): 
        if self.dynamic_batch_size:
            if isinstance(self.x_name, str):
                x_name = self.x_name
            else:
                x_name = self.x_name[0]
                
            seq_length = sum(len(getattr(inst, x_name)) for inst in self.training_list) // len(self.training_list)        
            total_memory = self.batch_size * seq_length
            i = 0
            batch_size = self.batch_size            
            while i < len(self.training_list):
                batch = self.training_list[i:i + batch_size]
                _seq_length = len(getattr(batch[-1], x_name))
                if _seq_length > seq_length:
                    seq_length = _seq_length
                    batch_size = max(1, total_memory // seq_length)
#                 array.append(self.training_list[i:i + batch_size])      
                yield self.training_list[i:i + batch_size]
                i += batch_size
#             return array            
        else: 
            for i in range(0, len(self.training_list), self.batch_size):
                yield self.training_list[i:i + self.batch_size]

    def shuffling(self):
        if len(self):
            print("def shuffling(self):")
            random.shuffle(self.arr)
        
    def __len__(self):
        if hasattr(self, 'arr'):
#             print('len(self.arr) =', len(self.arr))
            return len(self.arr)

        self.arr = [self.torchify(batch) for batch in self.batches()]

        if self.shuffle:
            random.shuffle(self.arr)

        return len(self.arr)

    def on_epoch_end(self):
        print('\none epoch has ended!')

    @staticmethod
    def format_sample(batch, attribute, format_func):
        sample = [getattr(s, attribute) for s in batch]
        batch = format_func(sample) if format_func else np.array(sample)
        if batch.dtype == np.object:
            return utility.numpify(sample)
        return batch 

    @staticmethod
    def format_data(batch, attributes, format_func):
        if isinstance(attributes, (list, tuple)):
            samples = []
            if isinstance(format_func, (list, tuple)):
                for attribute, format_func in zip(attributes, format_func):
                    samples.append(Sequence.format_sample(batch, attribute, format_func))
            else:
                for attribute in attributes:
                    samples.append(Sequence.format_sample(batch, attribute, format_func))                
            return samples
        elif attributes:
            return Sequence.format_sample(batch, attributes, format_func)

    def torchify(self, batch):
        args = self.numpify(batch)
        if isinstance(args, tuple):
            return tuple([self.from_numpy(arg, self.device) for arg in arg] if isinstance(arg, list) else self.from_numpy(arg, self.device) for arg in args)
        
        if isinstance(args, list):
            return tuple(self.from_numpy(arg, self.device) for arg in args)
        
        return self.from_numpy(args, self.device)
                
    def numpify(self, batch):
        assert batch is not None

        x_sample = self.format_data(batch, self.x_name, self.numpify_x)

        if self.y_name:
            y_sample = self.format_data(batch, self.y_name, self.numpify_y)
            return x_sample, y_sample
        return x_sample

    @staticmethod
    def from_numpy(ndarray, device=-1):
        import torch
        data = torch.from_numpy(ndarray)
        return data.cuda(device) if device >= 0 else data



def extend(arr, mask, maxlength, padding_type):
    if isinstance(arr, (tuple, np.ndarray)):
        arr = [*arr]

    padding = [mask] * (maxlength - len(arr))
    if padding_type == 'tailing':
        arr.extend(padding)
    elif padding_type == 'leading':
        arr = padding + arr
    else:
        assert padding_type == 'general'
        for mask in padding:
            arr.insert(random.randrange(0, len(arr)), mask)

    return arr


def extend_tailing(arr, mask, maxlength):
    if isinstance(arr, tuple):
        arr = [*arr]

    padding = [mask] * (maxlength - len(arr))

    arr.extend(padding)

    return arr


def numpify_tailing(arr, mask_value=0):
    maxWidth = max(len(x) for x in arr)
    # arr is a 2-dimension array
    for i in range(len(arr)):
        arr[i] = extend_tailing(arr[i], mask_value, maxWidth)
    return np.array(arr)


def numpify_leading(arr, mask_value=0):
    return numpify(arr, mask_value, padding='leading')

# arr is a 3-dimension array
# def numpify(arr, mask_value=0, padding='general'):
# def numpify(arr, mask_value=0, padding='leading'):

def numpify(arr, mask_value=0, padding='tailing'):
    '''
    
    :param arr:
    :param mask_value:
    :param shuffle: randomly insert the padding mask into the sequence, this is used for testing masking algorithms!
    '''

    try:
        maxWidth = max(len(x) for x in arr)
    except (TypeError, AttributeError) as _:
        return np.array(arr)

    try:
        maxHeight = max(max(len(word) for word in x) for x in arr)
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j] = extend(arr[i][j], mask_value, maxHeight, padding)
            arr[i] = extend(arr[i], [mask_value] * maxHeight, maxWidth, padding)
    except (TypeError, AttributeError, ValueError) as _:

        # arr is a 2-dimension array
        for i in range(len(arr)):
            arr[i] = extend(arr[i], mask_value, maxWidth, padding)

    return np.array(arr)


