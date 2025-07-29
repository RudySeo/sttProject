from openai import OpenAI
import os
from dotenv import load_dotenv

# .env 파일의 변수들을 환경변수로 로드
load_dotenv()

# 환경변수에서 API 키를 가져와 OpenAI 클라이언트 초기화
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def validate_api_key() -> bool:
    """
    OpenAI API 키가 유효한지 테스트 요청으로 확인
    """
    try:
        response = client.models.list()
        print("✅ 인증 성공: 사용 가능한 모델 리스트를 가져왔습니다.")
        return True
    except Exception as e:
        print(f"[ERROR] OpenAI 인증 실패: {e}")
        return False


def transcribe_audio_with_api(file_path: str) -> dict:
    """
    OpenAI Whisper API로 음성 파일을 텍스트로 변환합니다
    """
    try:
        with open(file_path, "rb") as audio_file:
            result = client.audio.transcriptions.create(
                model="whisper-1", file=audio_file
            )
            return result.text
    except Exception as e:
        print(f"[ERROR] STT 처리 실패: {e}")
