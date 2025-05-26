from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.model import load_model, transcribe_audio
from app.utils import validate_audio_file
import tempfile

app = FastAPI(title="ASR API using NVIDIA NeMo")

model = load_model()

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="Only .wav files are supported.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    if not validate_audio_file(tmp_path):
        raise HTTPException(status_code=400, detail="Invalid audio: Ensure it is 16kHz mono and 5–10s long.")

    try:
        transcript = transcribe_audio(tmp_path, model)
        return JSONResponse(content={"transcription": transcript})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
