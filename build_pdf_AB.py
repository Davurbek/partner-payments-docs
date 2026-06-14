# -*- coding: utf-8 -*-
"""
A+B VARIANT: Barcha funksiyalar (F1-F14) batafsil tavsiflangan to'liq hujjat.
Har bir funksiya uchun: maqsad, kirish, chiqish, xato holatlari, UI, API.
Chiqish: Texnik_Hujjat_v2_AB.pdf
"""

import datetime
from pdf_engine import Doc, render

d = Doc()


def feature(num, title, purpose, actor, inputs, outputs, errors, ui, api):
    """Bitta funksiyani standart formatda yozadi."""
    d.h1(f"{num}. {title}")
    d.para(purpose)
    d.h3("Asosiy aktor")
    d.para(actor)
    d.h3("Kirish (input)")
    for it in inputs:
        d.bullet(it)
    d.h3("Chiqish (output)")
    for it in outputs:
        d.bullet(it)
    d.h3("Xato holatlari")
    for it in errors:
        d.bullet(it)
    d.h3("UI ko'rinishi")
    d.para(ui)
    d.h3("API")
    d.code(api)


# --- Title ---
d.blank(110)
d.title("PARTNYOR PUL O'TKAZMALARI")
d.title("MONITORING TIZIMI")
d.blank(10)
d.title("FUNKSIYALAR SPESIFIKATSIYASI", size=15)
d.blank(14)
d.center("To'liq texnik hujjat - F1 dan F14 gacha batafsil",
         size=13, color=(0.3, 0.3, 0.3), font="F2")
d.blank(40)
d.center("Tashkilot turi: kommertsiya banki")
d.center("Asosiy foydalanuvchi: bek-ofis operatori")
d.center("Partnyorlar soni: 3-4 ta")
d.center("Backend: .NET 10  |  Frontend: Vue 3  |  DB: PostgreSQL")
d.blank(30)
d.center("Sana: " + datetime.date.today().strftime("%d.%m.%Y"),
         size=10, color=(0.3, 0.3, 0.3))
d.newpage()

# --- Mundarija ---
d.h1("Mundarija")
toc = [
    "Kirish va belgilanishlar",
    "Mavjud funksiyalar (boshliq ko'rgan):",
    "  F1.  Yagona tranzaksiyalar ro'yxati",
    "  F2.  Filtr",
    "  F3.  Qidiruv",
    "  F4.  Tafsilot modali",
    "  F5.  Xatolar paneli",
    "  F6.  Xato yozuvlar ro'yxati",
    "  F7.  Excel eksport",
    "  F8.  Foydalanuvchi va partnyor boshqaruvi",
    "Qo'shimcha funksiyalar (boshliq talabi bo'yicha):",
    "  F9.  Retry / qayta yuborish",
    "  F10. Bosh sahifa dashboard widgetlari",
    "  F11. Izoh va status tarixi",
    "  F12. Audit jurnali (lite)",
    "  F13. Bildirishnoma (threshold alert)",
    "  F14. Parol o'zgartirish va 2FA",
    "Yangi DB jadvallari (jamlanma)",
    "Yangilangan bajarilish rejasi",
]
for t in toc:
    d.bullet(t, size=10.5)
d.newpage()

# --- Kirish ---
d.h1("Kirish va belgilanishlar")
d.para("Ushbu hujjat asosiy Texnik_Hujjat.pdf ning funksiyalarini batafsil "
       "ochib beradi va boshliq talabi bo'yicha qo'shilgan yangi "
       "funksiyalarni (F9-F14) qo'shadi. Har bir funksiya bir xil "
       "formatda yozilgan: maqsad, aktor, kirish, chiqish, xato holatlari, "
       "UI va API.")
d.h3("Rollar")
d.bullet("operator - bek-ofis xodimi, asosiy foydalanuvchi.")
d.bullet("admin - foydalanuvchi va partnyor boshqaruvi, sozlamalar.")
d.bullet("auditor - faqat o'qish (audit jurnali). F12 da paydo bo'ladi.")
d.h3("Status qiymatlari")
d.pre("created, sent, pending, paid, cancelled, failed")
d.h3("Xato toifalari (error_category)")
d.pre("KYC_FAIL, INSUFFICIENT_FUNDS, BENEFICIARY_NOT_FOUND,\n"
      "LIMIT_EXCEEDED, TIMEOUT, CANCELLED_BY_SENDER, OTHER")
d.newpage()

# ===================================================================
#  MAVJUD FUNKSIYALAR F1-F8
# ===================================================================
d.h1("MAVJUD FUNKSIYALAR (F1 - F8)")
d.para("Quyidagi funksiyalar asosiy hujjatda qisqa berilgan edi - bu yerda "
       "batafsil ochib berilgan.")

feature(
    "F1", "Yagona tranzaksiyalar ro'yxati",
    "Barcha 3-4 partnyordan kelgan o'tkazmalarni bitta jadvalda ko'rsatadi. "
    "Bu tizimning asosiy ish ekrani. Standart holatda bugungi yozuvlar, "
    "eng yangisi yuqorida.",
    "operator",
    ["So'rov parametrlari: sahifa (page), bir sahifadagi soni (limit, "
     "standart 50), saralash (sent_at bo'yicha kamayuvchi).",
     "Filtr va qidiruv parametrlari F2, F3 dan keladi."],
    ["Jadval. Ustunlar: sana (sent_at), partnyor, status, yo'nalish "
     "(INCOMING/OUTGOING), summa va valyuta, mijoz F.I.Sh, error_category.",
     "Sahifalash: jami soni, joriy sahifa, oldingi/keyingi.",
     "Status rangli belgi: paid - yashil, failed - qizil, pending - sariq."],
    ["Ma'lumot yo'q bo'lsa: 'Yozuv topilmadi' xabari.",
     "DB xatosi bo'lsa: 500 va umumiy xato xabari, log yoziladi."],
    "PaymentsView.vue. Yuqorida filtr paneli, ostida jadval, pastda "
    "sahifalash. Qatorerga bosilsa F4 modal ochiladi.",
    "GET /api/payments?page=&limit=        -- rol: operator")

feature(
    "F2", "Filtr",
    "Operatorga ro'yxatni partnyor, status, sana oralig'i va valyuta "
    "bo'yicha toraytirishga yordam beradi. Filtrlar birga ishlaydi (AND).",
    "operator",
    ["partner - partnyor ID yoki kodi.",
     "status - bir yoki bir nechta status.",
     "from / to - sana oralig'i (sent_at bo'yicha).",
     "currency - valyuta kodi (USD, RUB, UZS, ...)."],
    ["Filtrga mos yozuvlar (F1 formatida).",
     "Faol filtrlar 'chip' ko'rinishida ko'rinadi, bittalab o'chiriladi."],
    ["Noto'g'ri sana formati: 400 va tushuntirish.",
     "from > to bo'lsa: 400 'sana oralig'i noto'g'ri'."],
    "Filtr paneli jadval ustida. 'Tozalash' tugmasi barcha filtrni oladi. "
    "Filtr o'zgarsa ro'yxat avtomatik yangilanadi.",
    "GET /api/payments?partner=&status=&from=&to=&currency=")

feature(
    "F3", "Qidiruv",
    "Bitta o'tkazmani tez topish uchun. PaymentRef, MTCN, telefon yoki "
    "F.I.Sh bo'yicha qidiradi.",
    "operator",
    ["q - qidiruv matni (bitta qator).",
     "Tizim q ni payment_ref, mtcn, partner_txn_id, sender/receiver phone "
     "va full_name bo'yicha qidiradi."],
    ["Mos yozuvlar ro'yxati (F1 formatida).",
     "Aniq bitta mos kelsa, to'g'ridan-to'g'ri F4 modal ochilishi mumkin."],
    ["Bo'sh so'rov: filtrsiz ro'yxat qaytadi.",
     "Hech narsa topilmasa: 'Topilmadi' xabari."],
    "Jadval ustidagi qidiruv qatori (lupa belgisi). Enter bosilsa qidiradi.",
    "GET /api/payments?q=901234567        -- rol: operator")

feature(
    "F4", "Tafsilot modali",
    "Bitta o'tkazmaning barcha maydonlarini ko'rsatadi: summa, valyuta, "
    "jo'natuvchi va qabul qiluvchi, status, xato kodi va matni.",
    "operator",
    ["Yo'l parametri: o'tkazma id."],
    ["O'tkazmaning to'liq ma'lumotlari.",
     "PII (passport, telefon) maskalangan: +998 90 *** ** 67.",
     "Xato bo'lsa: error_category, error_code, error_message ko'rinadi."],
    ["id topilmasa: 404.",
     "Ruxsat bo'lmasa: 403."],
    "PaymentDetailModal.vue - markaziy modal oyna. Bo'limlar: umumiy, "
    "jo'natuvchi, qabul qiluvchi, xato, vaqtlar. 'Yopish' tugmasi.",
    "GET /api/payments/{id}              -- rol: operator")

feature(
    "F5", "Xatolar paneli",
    "Barcha xato o'tkazmalarni toifa x partnyor kesimida jadval ko'rinishida "
    "ko'rsatadi. Qaysi partnyorda qaysi sababdan nechta xato borligini bir "
    "qarashda ko'rsatadi.",
    "operator",
    ["from / to - sana oralig'i (standart: oxirgi 14 kun).",
     "partner - ixtiyoriy, bitta partnyorga toraytirish."],
    ["Toifa x partnyor jadvali: har yacheyka - xato soni.",
     "Har toifa bo'yicha jami va foiz.",
     "Umumiy jami xatolar soni."],
    ["Tanlangan oraliqda xato yo'q: 'Xatolar yo'q' xabari (ijobiy holat)."],
    "ErrorsDashboardView.vue. Yuqorida sana va partnyor filtri, o'rtada "
    "matritsa jadval. Yacheykaga yoki toifa nomiga bosilsa F6 ochiladi.",
    "GET /api/errors/stats?from=&to=&partner=   -- rol: operator")

feature(
    "F6", "Xato yozuvlar ro'yxati",
    "F5 da tanlangan kesim (masalan, Partnyor 2 ning TIMEOUT xatolari) "
    "bo'yicha aniq yozuvlar ro'yxati.",
    "operator",
    ["error_cat - toifa.",
     "partner - partnyor (ixtiyoriy).",
     "from / to - sana oralig'i."],
    ["Shu kesimdagi xato o'tkazmalar (F1 formatida + error_message ustuni)."],
    ["Mos yozuv yo'q: bo'sh ro'yxat."],
    "F5 ostida ochiladigan panel yoki alohida ro'yxat. Qatorga bosilsa "
    "F4 modal.",
    "GET /api/payments?error_cat=TIMEOUT&partner=2&from=&to=")

feature(
    "F7", "Excel eksport",
    "Joriy filtr va qidiruvga mos o'tkazmalarni .xlsx faylga chiqaradi. "
    "Kunlik yoki oraliq hisobot uchun.",
    "operator",
    ["Joriy filtr parametrlari (F2, F3 dagidek)."],
    ["XLSX fayl: barcha ustunlar, sarlavha qatori, sana bilan nomlangan.",
     "PII maskalangan (xavfsizlik)."],
    ["Juda katta hajm (>50000 qator): ogohlantirish, oraliqni toraytirish "
     "taklifi."],
    "Jadval ustida 'Excel' tugmasi. Bosilganda joriy filtr bilan fayl "
    "yuklab olinadi.",
    "GET /api/payments/export.xlsx?partner=&status=&from=&to=")

feature(
    "F8", "Foydalanuvchi va partnyor boshqaruvi",
    "Admin foydalanuvchilarni (yaratish, rol berish, faolsizlantirish) va "
    "partnyorlarni (qo'shish, nom o'zgartirish) boshqaradi.",
    "admin",
    ["Foydalanuvchi: login, F.I.Sh, rol, parol.",
     "Partnyor: kod, nom, faol/nofaol."],
    ["Foydalanuvchilar va partnyorlar ro'yxati va CRUD natijasi."],
    ["Login takrorlansa: 400 'bunday login bor'.",
     "Oxirgi adminni o'chirishga urinish: 400 bloklaydi."],
    "AdminView.vue - 2 tab: Foydalanuvchilar va Partnyorlar. Jadval + "
    "qo'shish/tahrirlash formasi.",
    "GET/POST /api/admin/users    PUT /api/admin/partners/{id}  -- admin")

# ===================================================================
#  QO'SHIMCHA FUNKSIYALAR F9-F14
# ===================================================================
d.newpage()
d.h1("QO'SHIMCHA FUNKSIYALAR (F9 - F14)")
d.para("Boshliq talabi bo'yicha qo'shilgan yangi funksiyalar. Bular yangi "
       "DB jadvallari va endpointlarni talab qiladi.")

feature(
    "F9", "Retry / qayta yuborish",
    "Texnik sabab (TIMEOUT) bilan to'xtagan o'tkazmani operator bitta "
    "tugma bilan partnyorga qayta yuboradi. Mantiqiy xatolar (KYC_FAIL, "
    "AML) retry qilinmaydi.",
    "operator",
    ["Yo'l parametri: o'tkazma id.",
     "Tugma faqat error_category texnik (TIMEOUT/OTHER) bo'lganda faol."],
    ["Yangi yuborish urinishi; status 'pending' ga o'tadi.",
     "retry_count oshadi, last_retry_at yangilanadi."],
    ["retry_count limitdan oshgan (>3): 400 'limit tugadi'.",
     "Mantiqiy xato yozuvga retry: 400 'bu xato qayta yuborilmaydi'."],
    "F4 modalida 'Qayta yuborish' tugmasi. Tasdiqlash dialogi bilan.",
    "POST /api/payments/{id}/retry        -- rol: operator\n"
    "-- DB: ALTER TABLE payments ADD retry_count, last_retry_at")

feature(
    "F10", "Bosh sahifa dashboard widgetlari",
    "Operator kirganda bosh sahifada kun holatini 4 ta widgetda ko'rsatadi: "
    "bugungi o'tkazmalar soni, xatolar soni va foizi, top xato sababi, eng "
    "ko'p xato qilgan partnyor. Pastda 7 kunlik trend grafigi.",
    "operator",
    ["date - sana (standart: bugun).",
     "days - trend uchun kunlar soni (standart 7)."],
    ["4 ta ko'rsatkich (summary) va trend nuqtalari massivi."],
    ["Ma'lumot yo'q kun: widgetlar 0 ko'rsatadi."],
    "HomeView.vue (yangi). 4 ta karta + chiziqli grafik (Chart.js yoki "
    "Element Plus). Kartaga bosilsa tegishli ekranga o'tadi.",
    "GET /api/dashboard/summary?date=     -- rol: operator\n"
    "GET /api/dashboard/trend?days=7      -- rol: operator")

feature(
    "F11", "Izoh va status tarixi",
    "Operator o'tkazmaga ichki izoh yozadi va statusning o'zgarish tarixini "
    "ko'radi (created -> sent -> failed -> retry -> paid).",
    "operator",
    ["Izoh uchun: payment_id, matn.",
     "Tarix uchun: payment_id."],
    ["Izohlar ro'yxati (kim, qachon, matn).",
     "Status tarixi: har bosqich vaqti va manbasi (import/retry/manual)."],
    ["Bo'sh izoh: 400.",
     "payment_id topilmasa: 404."],
    "F4 modalida 2 ta yangi blok: 'Izohlar' (yozish maydoni bilan) va "
    "'Status tarixi' (vaqt chizig'i ko'rinishida).",
    "GET/POST /api/payments/{id}/notes    -- rol: operator\n"
    "GET      /api/payments/{id}/history  -- rol: operator\n"
    "-- DB: payment_notes, payment_status_history jadvallari")

feature(
    "F12", "Audit jurnali (lite)",
    "Tizimdagi muhim harakatlar yoziladi: login, eksport, retry, izoh "
    "qo'shish, foydalanuvchi o'zgartirish. Sodda jurnal - operatorlar "
    "harakatini kuzatish uchun (to'liq 7 yillik audit emas).",
    "admin, auditor",
    ["user - foydalanuvchi bo'yicha filtr.",
     "action - harakat turi.",
     "from / to - sana oralig'i."],
    ["Jurnal yozuvlari: vaqt, foydalanuvchi, harakat, obyekt, IP.",
     "Eksport imkoni (Excel)."],
    ["Auditor faqat o'qiy oladi - yozish/o'chirish yo'q."],
    "AuditView.vue (yangi). Filtr + jadval. Yozuvlar o'chirilmaydi.",
    "GET /api/audit?user=&action=&from=&to=   -- rol: admin, auditor\n"
    "-- DB: audit_log jadvali")

feature(
    "F13", "Bildirishnoma (threshold alert)",
    "Xatolar soni belgilangan chegaradan oshsa, tizim avtomatik email yoki "
    "Telegram orqali xabar yuboradi. Operator kutmasdan muammodan xabardor "
    "bo'ladi.",
    "admin (qoidalarni sozlaydi)",
    ["Qoida: partnyor (ixtiyoriy), toifa (ixtiyoriy), chegara, vaqt oynasi "
     "(daqiqa), kanal (email/telegram), manzil."],
    ["Chegara oshganda: ogohlantirish yuboriladi.",
     "Cooldown: bir xil ogohlantirish takror yuborilmaydi."],
    ["Noto'g'ri kanal/manzil: 400.",
     "Yuborish xatosi: log yoziladi, keyingi tsiklda qayta urinadi."],
    "AdminView.vue ga 'Ogohlantirishlar' tab. Background service har "
    "10-15 daqiqada tekshiradi.",
    "GET/POST /api/admin/alert-rules      -- rol: admin\n"
    "PUT      /api/admin/alert-rules/{id} -- rol: admin\n"
    "-- DB: alert_rules jadvali")

feature(
    "F14", "Parol o'zgartirish va 2FA",
    "Foydalanuvchi o'z parolini o'zgartiradi. Ixtiyoriy 2FA (TOTP - Google "
    "Authenticator) qo'llab-quvvatlanadi; admin uni majburiy qilishi mumkin.",
    "hammasi",
    ["Parol: eski parol, yangi parol.",
     "2FA setup: foydalanuvchi tasdiqlaydi.",
     "Login: parol + 6 raqamli kod (agar 2FA yoqilgan bo'lsa)."],
    ["Parol yangilanadi (BCrypt hash).",
     "2FA yoqilganda QR kod va zaxira kodlar beriladi."],
    ["Eski parol noto'g'ri: 400.",
     "Yangi parol kuchsiz: 400 talablar bilan.",
     "2FA kod noto'g'ri: 401."],
    "ProfileView.vue (yangi): parol o'zgartirish va 2FA sozlash. LoginView "
    "2 bosqichli bo'ladi.",
    "POST /api/auth/change-password       -- rol: hammasi\n"
    "POST /api/auth/2fa/setup             -- rol: hammasi\n"
    "POST /api/auth/2fa/verify            -- login paytida\n"
    "-- DB: ALTER TABLE users ADD totp_secret, totp_enabled")

# ===================================================================
#  YANGI DB JADVALLARI
# ===================================================================
d.newpage()
d.h1("Yangi DB jadvallari (jamlanma)")
d.para("F9-F14 quyidagi DB o'zgarishlarini talab qiladi. Bular asosiy 4 ta "
       "jadval (roles, users, partners, payments) ustiga qo'shiladi.")
d.code(
"-- F9: payments ga ustunlar\n"
"ALTER TABLE payments ADD COLUMN retry_count   SMALLINT DEFAULT 0;\n"
"ALTER TABLE payments ADD COLUMN last_retry_at TIMESTAMP;\n\n"
"-- F11: izoh va status tarixi\n"
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
"    source VARCHAR(20)\n"
");")
d.code(
"-- F12: audit jurnali\n"
"CREATE TABLE audit_log (\n"
"    id BIGSERIAL PRIMARY KEY,\n"
"    ts TIMESTAMP DEFAULT now(),\n"
"    user_id INT REFERENCES users(id),\n"
"    user_login VARCHAR(100),\n"
"    action VARCHAR(40) NOT NULL,\n"
"    entity_type VARCHAR(40),\n"
"    entity_id VARCHAR(64),\n"
"    ip_address VARCHAR(45)\n"
");\n\n"
"-- F13: ogohlantirish qoidalari\n"
"CREATE TABLE alert_rules (\n"
"    id SERIAL PRIMARY KEY,\n"
"    partner_id INT REFERENCES partners(id),\n"
"    error_category VARCHAR(40),\n"
"    threshold INT NOT NULL,\n"
"    window_minutes INT NOT NULL DEFAULT 60,\n"
"    channel VARCHAR(20) NOT NULL,\n"
"    target VARCHAR(200) NOT NULL,\n"
"    is_active BOOLEAN DEFAULT true\n"
");\n\n"
"-- F14: users ga 2FA ustunlari\n"
"ALTER TABLE users ADD COLUMN totp_secret  VARCHAR(255);\n"
"ALTER TABLE users ADD COLUMN totp_enabled BOOLEAN DEFAULT false;")

# ===================================================================
#  YANGILANGAN REJA
# ===================================================================
d.h1("Yangilangan bajarilish rejasi")
d.pre(
"Asosiy qism (F1-F8):                        4 hafta\n"
"\nQo'shimcha funksiyalar (F9-F14):\n"
"  F9   Retry / qayta yuborish               2-3 kun\n"
"  F10  Dashboard widgetlari                 2-3 kun\n"
"  F11  Izoh va status tarixi                2-3 kun\n"
"  F12  Audit jurnali (lite)                 2 kun\n"
"  F13  Bildirishnoma                        3-4 kun\n"
"  F14  Parol o'zgartirish va 2FA            3-4 kun\n"
"  -----------------------------------------------\n"
"  Qo'shimcha jami:                          ~2.5-3 hafta\n"
"\nYakuniy taxminiy muddat:                    6.5-7 hafta")

d.blank(8)
d.para("Eslatma: F9-F14 ni asosiy qismdan keyin alohida bosqich sifatida "
       "yoki ba'zilarini parallel ravishda qilish mumkin. Boshliq "
       "muhimligiga qarab tartibni belgilashi mumkin.")

d.blank(10)
d.para("--- Hujjat yakuni ---")

pages, size = render(d.lines, "Texnik_Hujjat_v2_AB.pdf")
print(f"A+B variant yaratildi: Texnik_Hujjat_v2_AB.pdf | "
      f"sahifalar: {pages} | hajmi: {size} bayt")
