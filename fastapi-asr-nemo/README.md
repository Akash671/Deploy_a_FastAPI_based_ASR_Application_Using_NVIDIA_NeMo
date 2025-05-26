# FastAPI ASR with NVIDIA NeMo

##  Model
Uses the Hindi Conformer CTC Medium model from [NVIDIA NeMo](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_hi_conformer_ctc_medium).

##  Run Locally

# download "stt_hi_conformer_ctc_medium.nemo" model using the below URL:
URL : https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_hi_conformer_ctc_medium
then copy this model from the download folder to "fastapi-asr-nemo\models\" location

# Build Docker image
$ docker build -t asr-nemo .

# Run the container:
$ docker run -p 8000:8000 asr-nemo


# Test the API with a .wav file:
Please copy as sample.wav file into "fastapi-asr-nemo\test_audio\" location 
and then run below command...

$ curl -X POST http://localhost:8000/transcribe -F "file=@sample.wav"
