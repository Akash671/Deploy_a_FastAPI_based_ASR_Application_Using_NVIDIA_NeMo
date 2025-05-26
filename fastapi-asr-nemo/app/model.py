# model.py

import nemo.collections.asr as nemo_asr
import torch
import torchaudio
import os

# Path to the .nemo model file
MODEL_PATH = "models/stt_hi_conformer_ctc_medium.nemo"

# Load the model once and reuse it
print("Loading NeMo ASR model...")
asr_model = nemo_asr.models.EncDecCTCModel.restore_from(MODEL_PATH)
asr_model.eval()
print("Model loaded successfully.")

def transcribe_audio(file_path: str) -> str:
    """
    Transcribe a given audio file using the loaded ASR model.

    Args:
        file_path (str): Path to the WAV/FLAC/MP3 file.

    Returns:
        str: Transcribed text.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    # Load audio file using torchaudio
    signal, sample_rate = torchaudio.load(file_path)

    # Resample if needed
    if sample_rate != asr_model.cfg.sample_rate:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=asr_model.cfg.sample_rate)
        signal = resampler(signal)

    # Run transcription
    transcription = asr_model.transcribe([signal])[0]
    return transcription
