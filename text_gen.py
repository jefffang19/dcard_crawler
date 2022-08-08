from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline
from opencc import OpenCC
import torch
import os

tokenizer = BertTokenizer.from_pretrained("uer/gpt2-chinese-lyric")
model = GPT2LMHeadModel.from_pretrained("uer/gpt2-chinese-lyric")
text_generator = TextGenerationPipeline(model, tokenizer)

# init transformer chinese text generator model

# tranditional and simpified chinese convert
cc_t2s = OpenCC('t2s')
cc_s2t = OpenCC('s2t')

def generate_text(input, out_len=150):
    print(input)

    # generate text
    model_gen = text_generator(cc_t2s.convert(
        input), max_length=out_len, do_sample=True)
    t_chi_gen_text = cc_s2t.convert(
        str(model_gen[0]['generated_text']))

    # responed
    responed_text = t_chi_gen_text
    print(responed_text)

    return responed_text