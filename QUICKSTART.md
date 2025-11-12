# 🚀 מדריך התחלה מהיר - 5 דקות

## צעד 1: קבל את המפתחות (2 דקות)

### Telegram Bot Token
1. פתח טלגרם
2. חפש: `@BotFather`
3. שלח: `/newbot`
4. תן שם ו-username לבוט
5. **העתק את הטוקן!**

### Groq API Key
1. לך ל: https://console.groq.com
2. הירשם (חינמי!)
3. API Keys → Create API Key
4. **העתק את המפתח!**

---

## צעד 2: העלה ל-GitHub (1 דקה)

1. New repository: `hebrew-subtitle-bot`
2. Add README: ✅
3. License: MIT
4. Create repository
5. Upload files → העלה את כל הקבצים
6. Commit

---

## צעד 3: פרוס ב-Render (2 דקות)

1. לך ל: https://render.com
2. New + → Web Service
3. Connect GitHub → בחר את הRepo
4. הגדרות:
   - Runtime: **Docker**
   - Instance Type: **Free**
5. Environment Variables:
   ```
   TELEGRAM_TOKEN = הטוקן_שלך
   GROQ_API_KEY = המפתח_שלך
   ```
6. Create Web Service
7. חכה 5-10 דקות ☕

---

## צעד 4: בדיקה! ✅

1. פתח את הבוט בטלגרם
2. `/start`
3. שלח סרטון קצר
4. קבל SRT תוך שניות! 🎉

---

## 🎬 איך להוסיף את ה-SRT לסרטון?

### CapCut (הכי קל!)
1. הורד: https://play.google.com/store/apps/details?id=com.lemon.lvoverseas
2. פתח את הסרטון ב-CapCut
3. טקסט → ייבוא כתוביות
4. בחר את קובץ ה-SRT
5. בום! זהו! 🎉

---

## ❓ בעיות?

### הבוט לא עונה
- שלח `/start` (הוא אולי ישן)
- בדוק Logs ב-Render

### שגיאת API
- בדוק את המפתחות ב-Render Environment
- ודא שאין רווחים נוספים

### עוד עזרה?
ראה את README.md המלא!

---

**זהו! הבוט שלך רץ! 🚀**
