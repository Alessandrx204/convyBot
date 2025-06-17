# 🤖 ConvyBot

**ConvyBot** is a Telegram bot built using [Aiogram 3.x](https://docs.aiogram.dev/en/dev-3.x/) that automatically converts `.webm` videos to `.mp4` format and responds to user pings with a friendly message.

## 🚀 Features

- 🎥 Converts `.webm` files (≤20MB) into Telegram-friendly `.mp4` videos using `ffmpeg`
- 💬 Responds when mentioned by its username
- 😎 Reacts with Telegram-native emoji based on success/failure

## 🧰 Tech Stack

- [Python 3.10+](https://www.python.org/)
- [Aiogram 3.x](https://docs.aiogram.dev/en/dev-3.x/)
- `ffmpeg` (required in PATH)

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Alessandrx204/convyBot.git
cd convyBot/convy_bot
```


### 2. Create a Virtual Environment (optional)
```python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


### 3. Install Dependencies
```
pip install -r requirements.txt
```
