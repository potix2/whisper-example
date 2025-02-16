# Whisper音声文字起こしツール

OpenAI Whisper APIを使用して音声ファイルをテキストに変換するシンプルなツールです。

## セットアップ

このプロジェクトは`uv`パッケージマネージャーを使用しています。

### 必要条件

- Python 3.8以上
- uv

### インストール手順

1. 必要な依存関係をインストール:

```bash
uv venv
source .venv/bin/activate
uv sync
```

2. OpenAI APIキーを設定:

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

## 使用方法

以下のコマンドで音声ファイルをテキストに変換:

```bash
python transcribe.py <音声ファイルのパス>
```

