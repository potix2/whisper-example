import sys
import json
from openai import OpenAI

def transcribe_audio(file_path):
    client = OpenAI()
    
    try:
        with open(file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="ja",
                prompt="この音声は、日本語で話されています。"
            )
            print(transcript.text)
    except Exception as e:
        print(f"エラーが発生しました: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python transcribe.py <音声ファイルのパス>", file=sys.stderr)
        sys.exit(1)
    
    audio_file_path = sys.argv[1]
    transcribe_audio(audio_file_path) 