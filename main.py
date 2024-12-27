# import io
# import json
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import mmap
# import numpy
# import soundfile
import torchaudio
import torch

# from collections import defaultdict
# from IPython.display import Audio, display
# from pathlib import Path
# from pydub import AudioSegment

from seamless_communication.inference import Translator
# from seamless_communication.streaming.dataloaders.s2tt import SileroVADSilenceRemover

print("Starting translations.")

model_name = "seamlessM4T_v2_large"
vocoder_name = "vocoder_v2" if model_name == "seamlessM4T_v2_large" else "vocoder_36langs"

# NOTE: Use the torch device that makes sense for your machine (tutorial has `cuda:0`)
translator = Translator(
    model_name,
    vocoder_name,
    device=torch.device("cpu"),
    dtype=torch.float16,
)

# README:  https://github.com/facebookresearch/seamless_communication/tree/main/src/seamless_communication/cli/m4t/predict
# Please use audios with duration under 20 seconds for optimal performance.

# Resample the audio in 16khz if sample rate is not 16khz already.
# torchaudio.functional.resample(audio, orig_freq=orig_freq, new_freq=16_000)

AUDIO_DIRECTORY = "audio_samples"
INFILE_DIRECTORY = f"{AUDIO_DIRECTORY}/input"
OUTFILE_DIRECTORY = f"{AUDIO_DIRECTORY}/output"
tgt_langs = ("eng", "spa", "fra", "deu", "ita", "hin", "cmn")

in_file = f"{INFILE_DIRECTORY}/LJ037-0171_sr16k.wav"

# TODO: This is Jupyter notebook specific - could find a replacement other than just adding "eng" to tgt_lang and showing text
# print("English audio:")
# display(Audio(in_file, rate=16000, autoplay=False, normalize=True))

for tgt_lang in tgt_langs:
    text_output, speech_output = translator.predict(
        input=in_file,
        task_str="s2st",
        tgt_lang=tgt_lang,
    )

    print(f"Translated text in {tgt_lang}:\n{text_output[0]}")
    print()

    out_file = f"{OUTFILE_DIRECTORY}/translated_LJ_{tgt_lang}.wav"

    torchaudio.save(out_file, speech_output.audio_wavs[0][0].to(torch.float32).cpu(), speech_output.sample_rate)

    # TODO: Replace this Jupyter-notebook specific code:
    # print(f"Translated audio in {tgt_lang}:")
    # audio_play = Audio(out_file, rate=speech_output.sample_rate, autoplay=False, normalize=True)
    # display(audio_play)
    # print()

    print(f"Saved translated audio file for {tgt_lang}.")
print()

SAMPLE_TEXT = "Hey everyone! I hope you're all doing well. Thank you for attending our workshop."
for tgt_lang in tgt_langs:
    text_output, speech_output = translator.predict(
        input=SAMPLE_TEXT,
        task_str="t2st",
        tgt_lang=tgt_lang,
        src_lang="eng",
    )

    print(f"Translated text in {tgt_lang}: {text_output[0]}")
    print()

    out_file = f"{OUTFILE_DIRECTORY}/{tgt_lang}.wav"

    torchaudio.save(out_file, speech_output.audio_wavs[0][0].to(torch.float32).cpu(), speech_output.sample_rate)

    # TODO: Replace Jupyter-specific code
    # print(f"Translated audio in {tgt_lang}:")
    # audio_play = Audio(out_file, rate=speech_output.sample_rate, autoplay=False, normalize=True)
    # display(audio_play)
    # print()

# T2TT
text_output, _ = translator.predict(
    input=SAMPLE_TEXT,
    task_str="T2TT",
    tgt_lang="spa",
    src_lang="eng",
    # text_generation_opts=text_generation_opts,
    unit_generation_opts=None
)
print(f"{text_output[0]}")

print("Finished.")
