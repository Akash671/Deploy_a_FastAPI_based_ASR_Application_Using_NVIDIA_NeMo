
## Features Implemented

- ONNX-based inference using Hindi Conformer model
- FastAPI server with file validation
- Dockerized with lightweight Python base
- Input validation and preprocessing

## Challenges Faced

- dependancy insallation mostly faced 
- Model conversion required GPU for best results
- Hindi decoder implementation was non-trivial

## Future Improvements

- Implement full decoder logic for Hindi output
- Add batch transcription support
- Integrate streaming input support

## Assumptions

- Input is mono-channel `.wav` at 16kHz
