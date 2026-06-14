# -*- coding: utf-8 -*-
"""
B VARIANT: Yangi qo'shiladigan funksiyalar (F9-F14) qo'shimcha hujjati.
Asosiy Texnik_Hujjat.pdf ga ilova sifatida.
Chiqish: Texnik_Hujjat_v2_B.pdf
"""

import datetime
from pdf_engine import Doc, render

d = Doc()

# --- Title ---
d.blank(110)
d.title("QO'SHIMCHA FUNKSIYALAR")
d.title("(F9 - F14)")
d.blank(14)
d.center("Asosiy texnik hujjatga ilova", size=13, color=(0.3, 0.3, 0.3),
         font="F2")
d.blank(40)
d.center("Asosiy hujjat: Texnik_Hujjat.pdf")
d.center("Bu ilova: boshliq talabi bo'yicha qo'shilgan yangi funksiyalar")
d.center("Backend: .NET 10  |  Frontend: Vue 3  |  DB: PostgreSQL")
d.blank(30)
d.center("Sana: " + datetime.date.today().strftime("%d.%m.%Y"),
         size=10, color=(0.3, 0.3, 0.3))
d.newpage()

# --- Kirish ---
d.h1("Ushbu ilova haqida")
d.para("Asosiy Texnik_Hujjat.pdf hujjatida F1-F8 funksiyalar tavsiflangan. "
       "Boshliq ko'rib chiqqach, tizimga qo'shimcha funksiyalar kiritish "
       "so'raldi. Ushbu ilovada F9-F14 yangi funksiyalar, ularning DB, API "
       "va frontend ta'siri qisqacha berilgan.")

d.h2("Yangi funksiyalar ro'yxati")
d.pre(
"+-----+------------------------------------+------------------+\n"
"| #   | Funksiya                           | Asosiy aktor     |\n"
"+-----+------------------------------------+------------------+\n"
"| F9  | Retry / qayta yuborish             | operator         |\n"
"| F10 | Bosh sahifa dashboard widgetlari   | operator         |\n"
"| F11 | Izoh va status tarixi              | operator         |\n"
"| F12 | Audit jurnali (lite)               | admin / auditor  |\n"
"| F13 | Bildirishnoma (threshold alert)    | admin            |\n"
"| F14 | Parol o'zgartirish va 2FA          | hammasi          |\n"
"+-----+------------------------------------+------------------+")

# --- F9 ---
d.h1("F9. Retry / qayta yuborish")
d.para("Status 'failed' bo'lgan va texnik sabab (TIMEOUT) bilan to'xtagan "
       "o'tkazmani operator bitta tugma bilan partnyorga qayta yuboradi. "
       "KYC_FAIL, AML kabi mantiqiy xatolar retry qilinmaydi - faqat texnik "
       "xatolar.")
d.bullet("Tugma faqat error_category = TIMEOUT yoki OTHER (texnik) bo'lganda "
         "faol.")
d.bullet("Retry urinishi soni cheklangan (masalan, 3 marta).")
d.bullet("Har bir urinish izohlanadi va audit jurnaliga yoziladi (F12).")
d.h3("DB o'zgarishi")
d.code(
"ALTER TABLE payments ADD COLUMN retry_count SMALLINT DEFAULT 0;\n"
"ALTER TABLE payments ADD COLUMN last_retry_at TIMESTAMP;")
d.h3("API")
d.code("POST /api/payments/{id}/retry        -- rol: operator")

# --- F10 ---
d.h1("F10. Bosh sahifa dashboard widgetlari")
d.para("Operator tizimga kirganda bosh sahifada umumiy ko'rsatkichlar 4 ta "
       "widgetda chiqadi. Maqsad - kun holatini bir qarashda ko'rish.")
d.pre(
"+---------------------------+---------------------------+\n"
"| Bugungi o'tkazmalar       | Bugungi xatolar           |\n"
"|        1 248              |     37  (2.96 %)          |\n"
"+---------------------------+---------------------------+\n"
"| Top xato sababi           | Eng ko'p xato partnyor    |\n"
"|   TIMEOUT (14 ta)         |   Partnyor 2 (15 ta)      |\n"
"+---------------------------+---------------------------+\n"
"  Pastda: oxirgi 7 kun xato foizi - chiziqli grafik")
d.h3("API")
d.code(
"GET /api/dashboard/summary?date=2026-06-14   -- rol: operator\n"
"GET /api/dashboard/trend?days=7              -- rol: operator")

# --- F11 ---
d.h1("F11. Izoh va status tarixi")
d.para("Operator har bir o'tkazmaga ichki izoh yozishi mumkin (masalan, "
       "'mijozga qo'ng'iroq qilindi'). Bundan tashqari, o'tkazma statusi "
       "qanday o'zgarganini tarix sifatida ko'rsatadi.")
d.bullet("Izohlar tafsilot modalida ko'rinadi; kim va qachon yozgani bilan.")
d.bullet("Status tarixi: created -> sent -> failed -> retry -> paid kabi "
         "zanjir, har bir bosqich vaqti bilan.")
d.h3("DB o'zgarishi")
d.code(
"CREATE TABLE payment_notes (\n"
"    id BIGSERIAL PRIMARY KEY,\n"
"    payment_id BIGINT NOT NULL REFERENCES payments(id),\n"
"    user_id INT NOT NULL REFERENCES users(id),\n"
"    note TEXT NOT NULL,\n"
"    created_at TIMESTAMP DEFAULT now()\n"
");\n\n"
"CREATE TABLE payment_status_history (\n"
"    id BIGSERIAL PRIMARY KEY,\n"
"    payment_id BIGINT NOT NULL REFERENCES payments(id),\n"
"    old_status VARCHAR(20),\n"
"    new_status VARCHAR(20) NOT NULL,\n"
"    changed_at TIMESTAMP DEFAULT now(),\n"
"    source VARCHAR(20)   -- import / retry / manual\n"
");")
d.h3("API")
d.code(
"GET  /api/payments/{id}/notes          -- rol: operator\n"
"POST /api/payments/{id}/notes          -- rol: operator\n"
"GET  /api/payments/{id}/history        -- rol: operator")

# --- F12 ---
d.h1("F12. Audit jurnali (lite)")
d.para("Tizimdagi muhim harakatlar yoziladi: kim kirdi, kim eksport qildi, "
       "kim retry qildi, kim izoh qoldirdi. Bu to'liq audit (7 yil arxiv) "
       "emas, balki sodda jurnal - operatorlar harakatini kuzatish uchun.")
d.h3("DB o'zgarishi")
d.code(
"CREATE TABLE audit_log (\n"
"    id BIGSERIAL PRIMARY KEY,\n"
"    ts TIMESTAMP DEFAULT now(),\n"
"    user_id INT REFERENCES users(id),\n"
"    user_login VARCHAR(100),\n"
"    action VARCHAR(40) NOT NULL,\n"
"        -- LOGIN, EXPORT, RETRY, ADD_NOTE, CHANGE_USER\n"
"    entity_type VARCHAR(40),\n"
"    entity_id VARCHAR(64),\n"
"    ip_address VARCHAR(45)\n"
");")
d.h3("API")
d.code("GET /api/audit?user=&action=&from=&to=   -- rol: admin, auditor")

# --- F13 ---
d.h1("F13. Bildirishnoma (threshold alert)")
d.para("Agar biror partnyorda yoki toifada xatolar soni belgilangan "
       "chegaradan oshsa, tizim avtomatik xabar yuboradi (email yoki "
       "Telegram bot). Maqsad - operator kutib o'tirmasdan muammodan "
       "xabardor bo'lsin.")
d.bullet("Chegaralar admin tomonidan sozlanadi (masalan: 1 soatda 20 dan "
         "ortiq TIMEOUT).")
d.bullet("Background service har 10-15 daqiqada tekshiradi.")
d.bullet("Bir xil ogohlantirish takror yuborilmaydi (cooldown).")
d.h3("DB o'zgarishi")
d.code(
"CREATE TABLE alert_rules (\n"
"    id SERIAL PRIMARY KEY,\n"
"    partner_id INT REFERENCES partners(id),  -- NULL = barchasi\n"
"    error_category VARCHAR(40),               -- NULL = barchasi\n"
"    threshold INT NOT NULL,\n"
"    window_minutes INT NOT NULL DEFAULT 60,\n"
"    channel VARCHAR(20) NOT NULL,             -- email / telegram\n"
"    target VARCHAR(200) NOT NULL,\n"
"    is_active BOOLEAN DEFAULT true\n"
");")
d.h3("API")
d.code(
"GET  /api/admin/alert-rules            -- rol: admin\n"
"POST /api/admin/alert-rules            -- rol: admin\n"
"PUT  /api/admin/alert-rules/{id}       -- rol: admin")

# --- F14 ---
d.h1("F14. Parol o'zgartirish va 2FA")
d.para("Foydalanuvchi o'z parolini o'zgartira oladi. Qo'shimcha "
       "xavfsizlik uchun ixtiyoriy 2FA (TOTP - Google Authenticator kabi) "
       "qo'llab-quvvatlanadi. Admin 2FA ni majburiy qilib qo'yishi mumkin.")
d.bullet("Parol o'zgartirishda eski parol so'raladi.")
d.bullet("2FA yoqilganda login 2 bosqichli: parol + 6 raqamli kod.")
d.bullet("2FA maxfiy kaliti shifrlangan holda saqlanadi.")
d.h3("DB o'zgarishi")
d.code(
"ALTER TABLE users ADD COLUMN totp_secret VARCHAR(255);\n"
"ALTER TABLE users ADD COLUMN totp_enabled BOOLEAN DEFAULT false;")
d.h3("API")
d.code(
"POST /api/auth/change-password         -- rol: hammasi\n"
"POST /api/auth/2fa/setup               -- rol: hammasi\n"
"POST /api/auth/2fa/verify              -- rol: hammasi (login paytida)")

# --- Reja ta'siri ---
d.h1("Rejaga ta'siri")
d.para("Bu funksiyalar asosiy 4 haftalik rejaga qo'shimcha vaqt talab "
       "qiladi. Taxminiy baho:")
d.pre(
"+-----+------------------------------------+------------------+\n"
"| #   | Funksiya                           | Taxminiy mehnat  |\n"
"+-----+------------------------------------+------------------+\n"
"| F9  | Retry / qayta yuborish             | 2-3 kun          |\n"
"| F10 | Dashboard widgetlari               | 2-3 kun          |\n"
"| F11 | Izoh va status tarixi              | 2-3 kun          |\n"
"| F12 | Audit jurnali (lite)               | 2 kun            |\n"
"| F13 | Bildirishnoma                      | 3-4 kun          |\n"
"| F14 | Parol o'zgartirish va 2FA          | 3-4 kun          |\n"
"+-----+------------------------------------+------------------+\n"
"  Jami qo'shimcha: ~2.5-3 hafta (asosiy 4 hafta ustiga).\n"
"  Yakuniy taxminiy muddat: 6.5-7 hafta.")

d.blank(10)
d.para("--- Ilova yakuni ---")

pages, size = render(d.lines, "Texnik_Hujjat_v2_B.pdf")
print(f"B variant yaratildi: Texnik_Hujjat_v2_B.pdf | "
      f"sahifalar: {pages} | hajmi: {size} bayt")
