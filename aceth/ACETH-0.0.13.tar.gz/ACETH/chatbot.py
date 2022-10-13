import emoji,os
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import torch
from transformers import logging
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import warnings

warnings.filterwarnings("ignore")

class chatbot:
    def __init__(self,emoji=True):
        self.emoji = emoji
        print('Loading model and other dependecies..',sep='')
        logging.disable_progress_bar()
        loc = os.path.dirname(__file__)
        model = 'facebook/blenderbot-400M-distill'
        self.token_chat = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
        self.model_chat = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")

        with open(loc+'/data/token_emoji.pkl','rb') as f:
            self.token_em = pickle.load(f)
        with open(loc+'/data/encoder_emoji.pkl','rb') as f:
            self.encod_em = pickle.load(f)

        self.model_emoji = load_model(loc+'/data/emoji_model.h5')
        print('Model and tokenizer is loaded')
        self.main()

    def addEmoji(self,text):
        x = pad_sequences(self.token_em.texts_to_sequences([text]),maxlen=30)
        y_hot = self.model_emoji.predict([x],verbose=0)[0]
        w_sum = sum(y_hot)
        sort = list(sorted(y_hot))
        dummy = []
        count = 0
        for i in sort:
            count+=i
            dummy.append(count)
        sort = dummy
        r = np.random.uniform(0,1)
        y = np.argmax(y_hot)
        for i,w in enumerate(sort[:-1]):
            if r <= w:
                y = i
                break
        y = self.encod_em.inverse_transform([y])[0]

      
        text = emoji.emojize(f'{text} :{y}:')
        return text
    def main(self): 
        torch.manual_seed(42)
        last = '-1'
        while 1:
            user_text = input('>> User : ')
            if user_text == ':q':
                break
            inputs = self.token_chat([user_text], return_tensors='pt')
            reply_ids = self.model_chat.generate(**inputs,max_length=30)

            
            text = self.token_chat.batch_decode(reply_ids, skip_special_tokens=True)[0]            
            if last in text or text in last or 'bye' in text or 'ok' in text or 'alright' in text:
                last = '-1'
            else:
                last = text
            if self.emoji and ':D' not in text and ':)' not in text:
                text = self.addEmoji(text)
            
            print('ACE chatbot : {}'.format(text))
        s = input("You wanna talk to me again? (Y/n)")
        if s == 'Y':
            self.main()
            return
        
        
