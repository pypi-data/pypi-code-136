import time
import torch
from typing import List
import logging
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from optimum.onnxruntime import ORTOptimizer, ORTModelForSeq2SeqLM

logger = logging.getLogger(__name__)


class OpusMT:
    def __init__(self, easynmt_path: str = None, max_loaded_models: int = 10):
        self.models = {}
        self.pipeline = {}
        self.max_loaded_models = max_loaded_models
        self.max_length = None

    def load_model(self, model_name):
        if model_name in self.models:
            self.models[model_name]['last_loaded'] = time.time()
            return self.models[model_name]['tokenizer'], self.models[model_name]['model']
        else:
            logger.info("Load model: "+model_name)
            if torch.cuda.is_available():
                tokenizer = AutoTokenizer.from_pretrained(model_name, device=0, load_in_8bit=True)
                model = ORTModelForSeq2SeqLM.from_pretrained(model_name, device=0, device_map="auto", load_in_8bit=True, from_transformers=True)
            else:
                tokenizer = AutoTokenizer.from_pretrained(model_name, load_in_8bit=True)
                model = ORTModelForSeq2SeqLM.from_pretrained(model_name, device_map="auto", load_in_8bit=True, from_transformers=True)

            if len(self.models) >= self.max_loaded_models:
                oldest_time = time.time()
                oldest_model = None
                for loaded_model_name in self.models:
                    if self.models[loaded_model_name]['last_loaded'] <= oldest_time:
                        oldest_model = loaded_model_name
                        oldest_time = self.models[loaded_model_name]['last_loaded']
                del self.models[oldest_model]

            self.models[model_name] = {'tokenizer': tokenizer, 'model': model, 'last_loaded': time.time()}
            return tokenizer, model
    
    def load_pipeline(self, model_name: str, source_lang: str, target_lang: str):
        pipeline_name = "translation_{}_to_{}".format(source_lang, target_lang)
        tokenizer, model = self.load_model(model_name)
        if pipeline_name in self.pipeline:
            return self.pipeline[pipeline_name]
        else:
            self.pipeline[pipeline_name] = pipeline(pipeline_name, model=model, tokenizer=tokenizer)
            return self.pipeline[pipeline_name]


    def translate_sentences(self, sentences: List[str], source_lang: str, target_lang: str, device: str, beam_size: int = 5, **kwargs):
        model_name = 'Helsinki-NLP/opus-mt-{}-{}'.format(source_lang, target_lang)
        pipeline = self.load_pipeline(model_name, source_lang, target_lang)
        return list(map(lambda x: x['translation_text'], pipeline(sentences)))
        # model.to(device)
        
        # inputs = tokenizer(sentences, truncation=True, padding=True, max_length=self.max_length, return_tensors="pt")

        # for key in inputs:
        #     inputs[key] = inputs[key].to(device)

        # with torch.no_grad():
        #     translated = model.generate(**inputs, num_beams=beam_size, **kwargs)
        #     output = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
        # print(output)
        # return output

    def save(self, output_path):
        return {"max_loaded_models": self.max_loaded_models}

