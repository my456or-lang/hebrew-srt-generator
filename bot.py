import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import aiohttp
from pathlib import Path
from googletrans import Translator
import srt
from datetime import timedelta

# הגדרות
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GROQ_API_URL = "https://api.groq.com/openai/v1/audio/transcriptions"

translator = Translator()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """פקודת התחלה"""
    await update.message.reply_text(
        "⚡ שלום! אני בוט מהיר לתמלול ותרגום!\n\n"
        "📤 שלח לי סרטון או קובץ אודיו באנגלית\n"
        "🎯 אתמלל ואתרגם לעברית\n"
        "📄 ואחזיר לך קובץ SRT מוכן!\n\n"
        "💡 טיפ: הוסף את קובץ ה-SRT ב-CapCut תוך דקה:\n"
        "1. פתח CapCut → פרויקט חדש\n"
        "2. טקסט → ייבוא כתוביות\n"
        "3. בחר את קובץ ה-SRT\n"
        "4. בום! הכתוביות מוכנות!"
    )

async def transcribe_with_groq(audio_path: str) -> dict:
    """תמלול עם Groq Whisper"""
    try:
        async with aiohttp.ClientSession() as session:
            with open(audio_path, 'rb') as f:
                form = aiohttp.FormData()
                form.add_field('file', f, filename=os.path.basename(audio_path))
                form.add_field('model', 'whisper-large-v3')
                form.add_field('language', 'en')
                form.add_field('response_format', 'verbose_json')
                form.add_field('timestamp_granularities[]', 'segment')
                
                headers = {'Authorization': f'Bearer {GROQ_API_KEY}'}
                
                async with session.post(GROQ_API_URL, data=form, headers=headers) as resp:
                    if resp.status == 200:
                        return await resp.json()
                    else:
                        error_text = await resp.text()
                        logger.error(f"Groq API error: {error_text}")
                        return None
    except Exception as e:
        logger.error(f"Transcription error: {e}")
        return None

def translate_to_hebrew(text: str) -> str:
    """תרגום לעברית עם Google Translate"""
    try:
        result = translator.translate(text, src='en', dest='he')
        return result.text
    except Exception as e:
        logger.error(f"Translation error: {e}")
        return text

def create_srt_file(segments: list, output_path: str):
    """יצירת קובץ SRT"""
    srt_subtitles = []
    
    for i, segment in enumerate(segments, 1):
        start = timedelta(seconds=segment['start'])
        end = timedelta(seconds=segment['end'])
        text_en = segment['text'].strip()
        
        # תרגום לעברית
        text_he = translate_to_hebrew(text_en)
        
        subtitle = srt.Subtitle(
            index=i,
            start=start,
            end=end,
            content=text_he
        )
        srt_subtitles.append(subtitle)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(srt.compose(srt_subtitles))

async def handle_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """טיפול בסרטונים ואודיו"""
    await update.message.reply_text("⏳ מעבד את הקובץ...")
    
    # יצירת תיקייה זמנית
    temp_dir = Path(f"temp_{update.message.message_id}")
    temp_dir.mkdir(exist_ok=True)
    
    try:
        # הורדת הקובץ
        if update.message.video:
            file = await update.message.video.get_file()
            file_ext = 'mp4'
        elif update.message.audio:
            file = await update.message.audio.get_file()
            file_ext = 'mp3'
        elif update.message.voice:
            file = await update.message.voice.get_file()
            file_ext = 'ogg'
        elif update.message.document:
            file = await update.message.document.get_file()
            file_ext = update.message.document.file_name.split('.')[-1]
        else:
            await update.message.reply_text("❌ פורמט לא נתמך")
            return
        
        media_path = temp_dir / f"input.{file_ext}"
        await file.download_to_drive(media_path)
        
        # תמלול
        await update.message.reply_text("🎤 מתמלל... (זה יכול לקחת כמה שניות)")
        transcription = await transcribe_with_groq(str(media_path))
        
        if not transcription or 'segments' not in transcription:
            await update.message.reply_text("❌ שגיאה בתמלול. נסה שוב.")
            return
        
        # תרגום ויצירת SRT
        await update.message.reply_text("🌐 מתרגם לעברית ויוצר קובץ SRT...")
        srt_path = temp_dir / "subtitles_he.srt"
        create_srt_file(transcription['segments'], str(srt_path))
        
        # שליחת קובץ ה-SRT
        with open(srt_path, 'rb') as f:
            await update.message.reply_document(
                document=f,
                filename="subtitles_hebrew.srt",
                caption=(
                    "✅ הנה קובץ הכתוביות שלך בעברית!\n\n"
                    "💡 להוסיף ב-CapCut:\n"
                    "1. פתח את הסרטון ב-CapCut\n"
                    "2. טקסט → ייבוא כתוביות\n"
                    "3. בחר את הקובץ הזה\n"
                    "4. ערוך עיצוב אם תרצה\n"
                    "5. ייצא!"
                )
            )
        
        # גם שליחת התמליל כטקסט
        full_text = "\n\n".join([
            translate_to_hebrew(seg['text'].strip()) 
            for seg in transcription['segments']
        ])
        
        if len(full_text) < 4000:
            await update.message.reply_text(
                f"📝 *התמליל המלא בעברית:*\n\n{full_text}",
                parse_mode='Markdown'
            )
        
    except Exception as e:
        logger.error(f"Error handling media: {e}")
        await update.message.reply_text(f"❌ שגיאה: {str(e)}")
    
    finally:
        # ניקוי קבצים זמניים
        try:
            for file in temp_dir.glob('*'):
                file.unlink()
            temp_dir.rmdir()
        except:
            pass

def main():
    """הפעלת הבוט"""
    if not TELEGRAM_TOKEN or not GROQ_API_KEY:
        logger.error("Missing TELEGRAM_TOKEN or GROQ_API_KEY")
        return
    
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.VIDEO | filters.AUDIO | filters.VOICE | filters.Document.VIDEO | filters.Document.AUDIO,
        handle_media
    ))
    
    logger.info("Bot started!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
