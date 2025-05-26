import torchaudio

def validate_audio_file(path):
    waveform, sr = torchaudio.load(path)
    duration = waveform.shape[1] / sr
    return sr == 16000 and 5 <= duration <= 10
