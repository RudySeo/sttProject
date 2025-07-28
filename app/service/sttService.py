
import whisper

# Whisper 모델 로드 (한 번만 로드해서 재사용)
model = whisper.load_model("base")

def transcribe_audio(file_path: str) -> str:
    """
    주어진 오디오 파일 경로를 텍스트로 변환한다.
    """
    result = model.transcribe(file_path)
    return result["text"]
