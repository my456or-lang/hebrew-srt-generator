# ⚡ Hebrew Subtitle Bot - SRT Fast Version

> Lightning-fast Telegram bot that transcribes English videos and generates Hebrew subtitle files (SRT) using Groq Whisper AI

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-Latest-blue.svg)](https://core.telegram.org/bots/api)
[![Groq](https://img.shields.io/badge/Groq-Whisper%20v3-green.svg)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<div dir="rtl">

## 🇮🇱 בעברית

בוט טלגרם מהיר שמתמלל סרטונים באנגלית ויוצר קובץ כתוביות (SRT) בעברית!

**מה הבוט עושה?**
- 📤 שולחים סרטון/אודיו באנגלית
- 🎤 הבוט מתמלל את האודיו (Whisper AI)
- 🌐 מתרגם לעברית
- 📄 מחזיר קובץ SRT מוכן!
- ⚡ הכל תוך שניות!

**למה זה מעולה?**
- 🆓 חינמי לגמרי (14,400 דקות/חודש)
- ⚡ מהיר מאוד
- 🎨 אפשר להוסיף את ה-SRT ב-CapCut תוך דקה
- 📦 עובד עם סרטונים בכל אורך

</div>

---

## ✨ Features

- 🎤 **Accurate Transcription** - Uses Groq's Whisper-large-v3 for high-quality transcription
- 🌐 **Free Translation** - Automatically translates English to Hebrew using Google Translate
- ⚡ **Lightning Fast** - Get SRT file in seconds (5-minute video = ~30 seconds)
- 📄 **Standard SRT Format** - Compatible with all video editors and players
- 🎨 **Flexible Styling** - Customize subtitles in CapCut, Premiere Pro, or any video editor
- 🆓 **Completely Free** - No API costs (14,400 minutes/month free on Groq)
- 📱 **Easy Integration** - Import SRT into CapCut with one click
- 🎬 **No Size Limit** - Works with videos of any length

---

## 🎯 Perfect For

- ✅ **All video lengths** - No processing timeout issues
- ✅ **Fast turnaround** - Get subtitles in seconds
- ✅ **Custom styling** - Full control over subtitle appearance
- ✅ **Batch processing** - Process multiple videos quickly
- ✅ **Professional workflow** - Standard SRT format

---

## 📋 Prerequisites

Before you begin, you'll need:

### 1. Telegram Bot Token

1. Open Telegram and search for: [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Choose a name for your bot (e.g., "My Subtitle Bot")
4. Choose a username (must end with `bot`, e.g., `my_subtitle_bot`)
5. **Save the token** (looks like: `1234567890:ABCdef...`)

### 2. Groq API Key (Free!)

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up (free - 14,400 minutes/month!)
3. Click "API Keys" in the left menu
4. Click "Create API Key"
5. Name it (e.g., "Telegram Bot")
6. **Copy and save the key** (you'll only see it once!)

---

## 🚀 Quick Deploy to Render (Free!)

### Step 1: Fork or Clone This Repository

Click the "Fork" button on GitHub, or:

```bash
git clone https://github.com/YOUR_USERNAME/hebrew-subtitle-bot-srt.git
cd hebrew-subtitle-bot-srt
```

### Step 2: Deploy to Render

1. Go to [render.com](https://render.com) and sign up (free)
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `hebrew-srt-bot` (or any name you like)
   - **Region**: Singapore / Frankfurt (choose closest)
   - **Branch**: `main`
   - **Runtime**: **Docker**
   - **Instance Type**: **Free** 💰

5. **Environment Variables** - Click "Add Environment Variable" twice:
   ```
   Key: TELEGRAM_TOKEN
   Value: [paste your Telegram bot token]
   
   Key: GROQ_API_KEY
   Value: [paste your Groq API key]
   ```

6. Click **Create Web Service**
7. Wait 5-10 minutes for deployment ☕
8. ✅ Your bot is live!

---

## 💻 Local Development

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/hebrew-subtitle-bot-srt.git
cd hebrew-subtitle-bot-srt

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your credentials:
   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. Run the bot:
   ```bash
   python bot_srt_only.py
   ```

4. You should see:
   ```
   Starting bot with SRT-only mode...
   Bot started successfully!
   ```

---

## 📖 How to Use

### Basic Usage

1. Start a chat with your bot on Telegram
2. Send `/start` to see the welcome message
3. Send any video, audio, or voice message in English
4. Wait a few seconds ⏳
5. Receive an SRT file + full transcript!

### Example Flow

```
👤 User: [Sends 5-minute English video]

🤖 Bot: ⏳ מעבד את הקובץ...
🤖 Bot: 🎤 מתמלל... (זה יכול לקחת כמה שניות)
🤖 Bot: 🌐 מתרגם לעברית ויוצר קובץ SRT...
🤖 Bot: [Sends subtitles_hebrew.srt file] ✅
🤖 Bot: 📝 התמליל המלא בעברית:
        [Full Hebrew transcription text]
```

---

## 🎬 How to Add SRT to Your Video

### Option 1: CapCut Mobile (Easiest! 🔥)

**Download:** [CapCut on Google Play](https://play.google.com/store/apps/details?id=com.lemon.lvoverseas)

**Steps:**
1. Open CapCut app
2. **New Project** → Select your video
3. Tap **Text** (bottom menu)
4. Select **Import Captions** (or **ייבוא כתוביות** in Hebrew)
5. Choose the SRT file the bot sent you
6. ✨ **Magic!** Subtitles appear automatically with perfect timing
7. Customize style (color, font, size, position, animation)
8. Export your video

**Time needed:** 1-2 minutes! ⚡

**Video Tutorial:** Search YouTube for "CapCut import SRT subtitles"

### Option 2: DaVinci Resolve (Desktop - Free & Pro)

1. Import your video to timeline
2. **File** → **Import** → **Subtitle**
3. Select the SRT file
4. Subtitles appear on timeline with correct timing
5. Customize in the subtitle panel
6. Export

### Option 3: Adobe Premiere Pro

1. Open your project
2. **Window** → **Text** → **Captions**
3. Import SRT file
4. Customize styling
5. Export

### Option 4: Final Cut Pro

1. Import video
2. Import SRT as captions
3. Edit in captions inspector
4. Export

---

## ⚙️ How It Works

```
┌─────────────┐
│ Send Video  │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ Download File   │
└──────┬──────────┘
       │
       ▼
┌──────────────────────────┐
│ Transcribe (Groq Whisper)│  ⚡ Super fast!
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────┐
│ Translate to Hebrew  │
└──────┬───────────────┘
       │
       ▼
┌─────────────────┐
│ Generate SRT    │
└──────┬──────────┘
       │
       ▼
┌──────────────────────┐
│ Send SRT + Transcript│
└──────────────────────┘
```

**Technology Stack:**
- **Transcription**: Groq Whisper-large-v3 (fastest available)
- **Translation**: Google Translate via deep-translator
- **Bot Framework**: python-telegram-bot
- **Format**: Standard SRT with timestamps

---

## 📊 Performance

| Video Length | Processing Time | Output |
|--------------|----------------|--------|
| 30 seconds | ~5-8 seconds | SRT file |
| 1 minute | ~10 seconds | SRT file |
| 5 minutes | ~30 seconds | SRT file |
| 10 minutes | ~1 minute | SRT file |
| 30 minutes | ~3 minutes | SRT file |
| 1 hour | ~5-6 minutes | SRT file |

*Times may vary based on server load and audio clarity*

---

## 📁 Project Structure

```
hebrew-subtitle-bot-srt/
├── bot_srt_only.py       # 🤖 Main bot code
├── requirements.txt       # 📦 Python dependencies
├── Dockerfile            # 🐳 Docker configuration
├── .dockerignore         # 🚫 Docker exclusions
├── .gitignore            # 🚫 Git exclusions
├── .env.example          # 📝 Environment variables template
├── README.md             # 📖 This file
└── LICENSE               # ⚖️ MIT License
```

---

## 🔧 Troubleshooting

### Bot doesn't respond

**Check:**
- ✅ Service is running on Render (status should be green "Live")
- ✅ Environment variables are set correctly
- ✅ No typos in TELEGRAM_TOKEN or GROQ_API_KEY
- ✅ Check logs in Render Dashboard

**Fix:**
- Try sending `/start` to wake the bot (free tier sleeps after 15 min)
- Click "Manual Deploy" → "Clear build cache & deploy"

### "Groq API error"

**Possible causes:**
- ❌ Invalid API key
- ❌ Exceeded monthly quota (14,400 minutes)
- ❌ Audio is not clear or not in English

**Fix:**
- Verify API key at [console.groq.com](https://console.groq.com)
- Check usage quota on Groq dashboard
- Try creating a new API key
- Ensure video has clear English audio

### Translation quality issues

**Note:** The bot uses Google Translate for free translation.

**Improve quality:**
- Edit the SRT file manually in any text editor
- For better translation, consider upgrading to:
  - DeepL API (paid but high quality)
  - Claude API (excellent but paid after free tier)

### SRT file won't import

**Check:**
- ✅ File encoding is UTF-8
- ✅ Using compatible video editor
- ✅ SRT format is valid

**Fix:**
- Open SRT in text editor to verify format
- Ensure timestamps are correct (00:00:00,000)
- Try different video editor

### Bot "sleeps" after inactivity

**This is normal on Render's free tier!**
- Free tier sleeps after 15 minutes of no activity
- Simply send `/start` to wake it up (~30 seconds)
- Or upgrade to Render's paid plan for 24/7 uptime

---

## 📊 Supported Formats

### Input Formats ✅
- 🎥 **Video**: MP4, AVI, MOV, MKV, WEBM, FLV
- 🎵 **Audio**: MP3, WAV, FLAC, OGG, M4A, AAC
- 🎤 **Voice**: Telegram voice messages (OGG)
- 📄 **Documents**: Any video/audio file sent as document

### Output Format ✅
- 📄 **SRT**: Universal subtitle format (works everywhere)

---

## 🎨 SRT File Format Example

The bot generates standard SRT format:

```srt
1
00:00:00,000 --> 00:00:05,000
זוהי הכתובית הראשונה בעברית

2
00:00:05,500 --> 00:00:10,000
וזוהי הכתובית השנייה עם תזמון מדויק

3
00:00:10,200 --> 00:00:15,800
כל כתובית מסונכרנת עם האודיו המקורי
```

**You can edit this file:**
- Fix any translation errors
- Adjust timing
- Merge or split subtitles
- Add custom formatting

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open** a Pull Request

### Ideas for Contributions 💡

- [ ] Support for more target languages (Arabic, Spanish, etc.)
- [ ] Better translation service (DeepL, Claude API)
- [ ] VTT format support
- [ ] Batch processing multiple files
- [ ] Custom subtitle timing adjustments
- [ ] Web interface for non-Telegram users
- [ ] Progress indicators for long videos
- [ ] Subtitle editor bot commands

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**TL;DR:** Free to use, modify, and distribute! 🎉

---

## 🙏 Acknowledgments

- [Groq](https://groq.com/) - Amazing free Whisper API with incredible speed
- [python-telegram-bot](https://python-telegram-bot.org/) - Excellent Telegram Bot framework
- [deep-translator](https://github.com/nidhaloff/deep-translator) - Reliable translation library
- [srt](https://github.com/cdown/srt) - SRT file handling made easy

---

## 📞 Support & Contact

- 🐛 **Bug Reports**: [Open an issue](https://github.com/YOUR_USERNAME/hebrew-subtitle-bot-srt/issues)
- 💡 **Feature Requests**: [Open an issue](https://github.com/YOUR_USERNAME/hebrew-subtitle-bot-srt/issues)
- ⭐ **Star** this repo if you find it useful!
- 🔀 **Fork** to create your own version

---

## 💡 Pro Tips

- 📱 **Mobile Workflow**: Send video to bot → Download SRT → Import to CapCut → Export (all on phone!)
- 🎨 **Custom Styling**: Import SRT first, then customize appearance in your editor
- ⚡ **Batch Process**: Send multiple videos back-to-back, collect SRTs later
- 📝 **Fix Translations**: Open SRT in any text editor to manually improve translations
- 🔄 **Reusable**: Keep SRT files to use with different video versions or edits
- 🎓 **Learn**: The SRT format is simple - great for learning about subtitles!

---

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_USERNAME/hebrew-subtitle-bot-srt&type=Date)](https://star-history.com/#YOUR_USERNAME/hebrew-subtitle-bot-srt&Date)

---

## 📈 Roadmap

- [ ] Support for more languages (Spanish, French, Arabic)
- [ ] WebVTT format support
- [ ] Better translation options (DeepL, Claude)
- [ ] Web interface (no Telegram needed)
- [ ] Subtitle editing commands in Telegram
- [ ] Multiple subtitle tracks
- [ ] Progress bars for long videos
- [ ] Video preview with subtitles

---

<div dir="rtl">

## 🇮🇱 תמיכה בעברית

יש שאלות? בעיות? רעיונות?

**דרכי יצירת קשר:**
- 🐛 פתח Issue ב-GitHub
- 💬 שלח הודעה בטלגרם (אם יש לך את פרטי הקשר)
- ⭐ תן כוכב לפרויקט אם עזר לך!

**זקוק לעזרה?**
ראה את [מדריך פתרון הבעיות](#-troubleshooting) למעלה

</div>

---

**Made with ❤️ for the Hebrew-speaking community**

**Enjoy fast, free, and accurate Hebrew subtitles!** 🎬✨
