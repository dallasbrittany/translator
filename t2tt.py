import sys
import torch
from seamless_communication.inference import Translator

model_name = "seamlessM4T_v2_large"
vocoder_name = "vocoder_v2" if model_name == "seamlessM4T_v2_large" else "vocoder_36langs"

if len(sys.argv) > 3:
    input_lang = sys.argv[1]
    output_lang = sys.argv[2]
    text = sys.argv[3]
print(f"\nTranslating the following sentence from {input_lang} to {output_lang}:\n{text}\n")

translator = Translator(
    model_name,
    vocoder_name,
    device=torch.device("cpu"),
    dtype=torch.float16,
)

text_output, _ = translator.predict(
    input=text,
    task_str="T2TT",
    tgt_lang=output_lang,
    src_lang=input_lang,
    # text_generation_opts=text_generation_opts,
    unit_generation_opts=None
)
print(f"\nTranslated text:\n{text_output[0]}\n")
