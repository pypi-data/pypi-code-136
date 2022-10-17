import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import  Bidirectional, Flatten, Dense, Dropout, LSTM, Input ,TimeDistributed,GRU,Conv1D,MaxPooling1D
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, mean_squared_log_error, mean_absolute_percentage_error
import keras.layers
import keras.backend as K
from keras.models import Model
from keras.layers import Lambda, SpatialDropout1D, Activation , Convolution1D ,GlobalMaxPooling1D



def root_mean_squared_error(y_true, y_pred):    
    return np.sqrt(mean_squared_error(y_true, y_pred))


class BiLSTM(tf.keras.Model):
    def __init__(self,n_steps,n_features,n_outputs=1):
        
        super(BiLSTM, self).__init__()
        self.n_steps=n_steps
        self.n_features=n_features
        self.n_outputs=n_outputs
        self.blstm1=Bidirectional(LSTM(128 , activation='relu',  return_sequences=True))
        self.blstm2=Bidirectional(LSTM(64, activation='relu'))
        self.flatten =Flatten()
        self.fc1=Dense(32, activation='relu')
        self.drp=Dropout(0.2)
        self.fc2=Dense(self.n_outputs)
        
        
    def call(self, inputs):
        x=self.blstm1(inputs)
        x=self.blstm2(x)
        x=self.flatten(x)
        x=self.fc1(x)
        x=self.drp(x)
        x=self.fc2(x)
        return x
    def getModel(self):
        inp = Input(shape=(self.n_steps,self.n_features))
        x = BiLSTM(self.n_steps, self.n_features,self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model 
    
class BiGRU(tf.keras.Model):
    def __init__(self,n_steps,n_features,n_outputs=1):
        super(BiGRU, self).__init__()
        self.n_steps=n_steps
        self.n_features=n_features
        self.n_outputs=n_outputs
        self.bigru_1= Bidirectional(GRU(256, activation='tanh',return_sequences=True))
        self.dropout_1 = Dropout(0.3)   
        self.bigru_2= Bidirectional(GRU(128, activation='tanh',return_sequences=True))
        self.bigru_3= Bidirectional(GRU(64, activation='tanh',return_sequences=True))
        self.dropout_2 = Dropout(0.2)   
        self.bigru_4= Bidirectional(GRU(32, activation='tanh'))
        self.flatten_1= Flatten()
        self.dropout_3 = Dropout(0.2)   
        self.dense_1 = Dense(10, activation='softmax')
        self.flatten_2= Flatten()
        self.dropout_4 = Dropout(0.1)
        self.dense_2 = Dense(self.n_outputs)

    def call(self, x):

        x = self.bigru_1(x)
        x = self.dropout_1(x)
        x = self.bigru_2(x)
        x = self.bigru_3(x)
        x = self.dropout_2(x)
        x = self.bigru_4(x)
        x=self.flatten_1(x)
        x = self.dropout_3(x)
        x = self.dense_1(x)
        x=self.flatten_2(x)
        x = self.dropout_4(x)
        x = self.dense_2(x)
        return x
    
    def getModel(self):
        inp = Input(shape=(self.n_steps,self.n_features))
        x = BiGRU(self.n_steps, self.n_features,self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model 
    
    

class TD (tf.keras.Model):
    def __init__(self,n_steps,n_features,n_outputs=1):
        super(TD, self).__init__()
        self.n_steps=n_steps
        self.n_features=n_features
        self.n_outputs=n_outputs
        self.td_1 = TimeDistributed(Conv1D(filters=64, kernel_size=3, activation='relu', padding='same'))
        self.td_2 = TimeDistributed(Conv1D(filters=32, kernel_size=2, activation='relu', padding='same'))
        self.dropout_1 =TimeDistributed(Dropout(0.2))
        self.max_pooling1D=TimeDistributed(MaxPooling1D(pool_size=2, padding='same')) 
        self.flatten=TimeDistributed(Flatten())
        self.lstm_1 = LSTM(75)
        self.dropout_2 = Dropout(0.2)
        self.dense_1 = Dense(50, activation='relu')
        self.dense_2 = Dense(self.n_outputs)
         
        
    def call(self, x):

        x = self.td_1(x)
        x = self.td_2(x)
        x = self.dropout_1(x)
        x = self.max_pooling1D(x)
        x = self.flatten(x)
        x = self.lstm_1(x)
        x = self.dropout_2(x)
        x = self.dense_1(x)
        x = self.dense_2(x)

        return x
    
    def getModel(self):
        inp = tf.keras.Input(shape=(None,self.n_steps,self.n_features))
        x = TD(self.n_steps, self.n_features,self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model

class CNN(tf.keras.Model):
    def __init__(self,n_steps,n_features,n_outputs=1):
        super(CNN, self).__init__()
        self.n_steps=n_steps
        self.n_features=n_features
        self.n_outputs=n_outputs
        self.CNN_L1=(Conv1D(filters=64, kernel_size=4, activation='relu', padding='same'))
        self.CNN_L2=(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
        self.CNN_L3=(Conv1D(filters=16, kernel_size=2, padding='same', activation='relu'))           
        self.CNN_maxpooling=(MaxPooling1D(pool_size=1))
        self.CNN_flatten=(Flatten())
        self.CNN_dense1=(Dense(100, activation='relu'))
        self.CNN_droupout=(Dropout(0.3))
        self.CNN_dense2=(Dense(20, activation='relu'))
        self.CNN_dense3=(Dense(self.n_outputs))

    def call(self, x):

        x = self.CNN_L1(x)
        x = self.CNN_L2(x)
        x = self.CNN_L3(x)
        x = self.CNN_maxpooling(x)
        x = self.CNN_flatten(x)
        x = self.CNN_dense1(x)
        x = self.CNN_droupout(x)
        x = self.CNN_dense2(x)
        x = self.CNN_dense3(x)
        return x
    
    def getModel(self):
        inp = Input(shape=(self.n_steps,self.n_features))
        x = CNN(self.n_steps, self.n_features,self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model 
    
class GRU_model(tf.keras.Model):
    def __init__(self,n_steps,n_features,n_outputs=1):
        super(GRU_model, self).__init__()
        self.n_steps=n_steps
        self.n_features=n_features
        self.n_outputs=n_outputs
        self.gru_1= GRU(300, activation='tanh',return_sequences=True)
        self.gru_2= GRU(200, activation='tanh',return_sequences=True)
        self.dropout_1 = Dropout(0.2)
        self.gru_3= GRU(100, activation='tanh',return_sequences=True)
        self.gru_4= GRU(50, activation='tanh')
        self.dropout_2 = Dropout(0.2)
        self.dense_1 = Dense(20, activation='softmax')
        self.dense_2 = Dense(self.n_outputs)

    def call(self, x):

        x = self.gru_1(x)
        x = self.gru_2(x)
        x = self.dropout_1(x)
        x = self.gru_3(x)
        x = self.gru_4(x)
        x = self.dropout_2(x)
        x = self.dense_1(x)
        x = self.dense_2(x)
        return x
    
    def getModel(self):
        inp = Input(shape=(self.n_steps,self.n_features))
        x = GRU_model(self.n_steps, self.n_features,self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model 
    
class lstm(tf.keras.Model):
    def __init__(self,n_steps,n_features,n_outputs=1):
        super(lstm, self).__init__()
        self.n_steps=n_steps
        self.n_features=n_features
        self.n_outputs=n_outputs
        self.lstm_1 = LSTM(128, activation='relu', return_sequences=True)
        self.lstm_2 = LSTM(64, activation='relu',  return_sequences=True)
        self.lstm_3 = LSTM(64, activation='relu')
        self.dropout_1 = Dropout(0.1)
        self.dropout_2 = Dropout(0.1)
        self.dense_1 = Dense(32, activation='relu')
        self.dense_2 = Dense(self.n_outputs)
    
    def call(self, x):

        x = self.lstm_1(x)
        x = self.dropout_1(x)
        x = self.lstm_2(x)
        x = self.lstm_3(x)
        x = self.dropout_2(x)
        x = self.dense_1(x)
        x = self.dense_2(x)

        return x
    def getModel(self):
        inp = Input(shape=(self.n_steps,self.n_features))
        x = lstm(self.n_steps, self.n_features,self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model
    

class TCN_Model:
    class TCN_layer:
        def channel_normalization(self, x):
            max_values = K.max(K.abs(x), 2, keepdims=True) + 1e-5
            out = x / max_values
            return out

        def residual_block(self, x, s, i, activation, nb_filters, kernel_size, padding, dropout_rate=0, name=''):
            original_x = x
            conv = Conv1D(filters=nb_filters, kernel_size=kernel_size,
                          dilation_rate=i, padding=padding,
                          name=name + '_dilated_conv_%d_tanh_s%d' % (i, s))(x)
            if activation == 'norm_relu':
                x = Activation('relu')(conv)
                x = Lambda(self.channel_normalization)(x)
            else:
                x = Activation(activation)(conv)

            x = SpatialDropout1D(dropout_rate, name=name + '_spatial_dropout1d_%d_s%d_%f' % (i, s, dropout_rate))(x)

            # 1x1 conv.
            x = Convolution1D(nb_filters, 1, padding='same')(x)
            res_x = keras.layers.add([original_x, x])
            return res_x, x

        def __init__(self,
                     nb_filters=64,
                     kernel_size=2,
                     nb_stacks=1,
                     dilations=None,
                     activation='norm_relu',
                     padding='causal',
                     use_skip_connections=True,
                     dropout_rate=0.0,
                     return_sequences=True,
                     name='tcn'):
            self.name = name
            self.return_sequences = return_sequences
            self.dropout_rate = dropout_rate
            self.use_skip_connections = use_skip_connections
            self.activation = activation
            self.dilations = dilations
            self.nb_stacks = nb_stacks
            self.kernel_size = kernel_size
            self.nb_filters = nb_filters
            self.padding = padding

            if padding != 'causal' and padding != 'same':
                raise ValueError("Only 'causal' or 'same' paddings are compatible for this layer.")

            if not isinstance(nb_filters, int):
                print('An interface change occurred after the version 2.1.2.')
                print('Before: tcn.TCN(i, return_sequences=False, ...)')
                print('Now should be: tcn.TCN(return_sequences=False, ...)(i)')
                print('Second solution is to pip install keras-tcn==2.1.2 to downgrade.')
                raise Exception()

        def __call__(self, inputs):
            if self.dilations is None:
                self.dilations = [1, 2, 4, 8, 16, 32]
            x = inputs
            x = Convolution1D(self.nb_filters, 1, padding=self.padding, name=self.name + '_initial_conv')(x)
            skip_connections = []
            for s in range(self.nb_stacks):
                for i in self.dilations:
                    x, skip_out = self.residual_block(x, s, i, self.activation, self.nb_filters,
                                                      self.kernel_size, self.padding, self.dropout_rate, name=self.name)
                    skip_connections.append(skip_out)
            if self.use_skip_connections:
                x = keras.layers.add(skip_connections)
            x = Activation('relu')(x)

            if not self.return_sequences:
                output_slice_index = -1
                x = Lambda(lambda tt: tt[:, output_slice_index, :])(x)
            return x

    def build(self,
              X, y,
              batch_size=100,
              epochs=200,
              verbose=1,

              tcn1_units=128,
              tcn2_units=64,
              tcn1_kernel_size=5,
              tcn2_kernel_size=1,
              activation="relu",
              return_sequences=True,
              dropout=0.2):

        input = Input(shape=X.shape[1:])

        try:
            output = y.shape[1]
        except:
            output = 1

        x = SpatialDropout1D(dropout)(input)

        x = TCN_Model.TCN_layer(tcn1_units,
                                dilations=[1, 2, 4, 8, 16],
                                kernel_size=tcn1_kernel_size,
                                return_sequences=return_sequences,
                                name='tnc1')(x)

        x = TCN_Model.TCN_layer(tcn2_units,
                                dilations=[1, 2, 4],
                                kernel_size=tcn2_kernel_size,
                                return_sequences=return_sequences,
                                name='tnc2')(x)

        max_pool = GlobalMaxPooling1D()(x)
        x = Dense(tcn2_units, activation=activation)(max_pool)
        x = Dropout(dropout)(x)
        output = Dense(output)(x)
        model = Model(inputs=input, outputs=output)

        model.compile(optimizer='adam', loss='mean_squared_error')
        callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=5)

        model.fit(X, y, batch_size=100, epochs=200, verbose=1, shuffle=False, callbacks=[callback])
        return model

    
def evaluate(model,X,Y):
        print('evaluation : %.3f ' % model.evaluate(X,Y))
        
def print_metrics(model,Y_train,Y_pred_train,Y_test,Y_pred_test):
    print('Train RMSE value   : %.3f ' % root_mean_squared_error(Y_train, Y_pred_train))
    print('Train MSE value    : %.3f ' % mean_squared_error(Y_train, Y_pred_train))
    print('Train R2 value     : %.3f ' % r2_score(Y_train, Y_pred_train))
    print('Train MAPE value   : %.3f ' % mean_absolute_percentage_error(Y_train, Y_pred_train))
    print('Train RMLSE value  : %.3f ' % mean_squared_log_error(Y_train, Y_pred_train))
    print('Train MAE value    : %.3f ' % mean_absolute_error(Y_train, Y_pred_train))
    print('---------------------------------------------')
    print('Test RMSE value   : %.3f ' % root_mean_squared_error(Y_test, Y_pred_test))
    print('Test MSE value   : %.3f ' % mean_squared_error(Y_test, Y_pred_test))
    print('Test R2 value   : %.3f ' % r2_score(Y_test, Y_pred_test))
    print('Test MAPE value  : %.3f ' % mean_absolute_percentage_error(Y_test, Y_pred_test))
    print('Test RMLSE value  : %.3f ' % mean_squared_log_error(Y_test, Y_pred_test))
    print('Test MAE value : %.3f ' % mean_absolute_error(Y_test, Y_pred_test))

