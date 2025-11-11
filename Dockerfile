FROM python:3.11-slim

# יצירת תיקיית עבודה
WORKDIR /app

# העתקת קבצי requirements והתקנת חבילות
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת הקוד
COPY bot_srt_only.py .

# הרצת הבוט
CMD ["python", "bot_srt_only.py"]
