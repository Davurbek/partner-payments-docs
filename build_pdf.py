# -*- coding: utf-8 -*-
"""
Texnik hujjatni PDF qilib chiqaruvchi skript (tashqi kutubxonasiz).
Mazmun: bank uchun xalqaro pul o'tkazmalari sverka tizimi.
"""

import textwrap, datetime

PAGE_W, PAGE_H = 595.276, 841.890
ML, MR, MT, MB = 55, 50, 60, 55
CONTENT_W = PAGE_W - ML - MR

lines = []


def max_chars(size, extra=0):
    return max(1, int((CONTENT_W - extra) // (size * 0.6)))


def add_blank(h=6): lines.append({"blank": h})
def add_rule():     lines.append({"rule": True})


def add_h1(text):
    add_blank(10)
    lines.append({"text": text, "font": "F2", "size": 15,
                  "color": (0.10, 0.20, 0.50)})
    add_rule(); add_blank(5)


def add_h2(text):
    add_blank(9)
    lines.append({"text": text, "font": "F2", "size": 12,
                  "color": (0.14, 0.18, 0.42)})
    add_blank(4)


def add_h3(text):
    add_blank(5)
    lines.append({"text": text, "font": "F2", "size": 10.5,
                  "color": (0, 0, 0)})
    add_blank(2)


def add_para(text, size=10):
    width = max_chars(size)
    for seg in (textwrap.wrap(text, width=width) or [""]):
        lines.append({"text": seg, "font": "F1", "size": size,
                      "color": (0, 0, 0)})
    add_blank(4)


def add_bullet(text, size=10):
    width = max_chars(size, extra=size * 0.6 * 2)
    wrapped = textwrap.wrap(text, width=width) or [""]
    for i, seg in enumerate(wrapped):
        prefix = "- " if i == 0 else "  "
        lines.append({"text": prefix + seg, "font": "F1", "size": size,
                      "color": (0, 0, 0)})


def add_code(code, size=8.5):
    add_blank(3)
    for ln in code.split("\n"):
        lines.append({"text": ln, "font": "F1", "size": size,
                      "color": (0.10, 0.10, 0.10), "code": True})
    add_blank(3)


def add_pre(block, size=8.5):
    add_blank(3)
    for ln in block.split("\n"):
        lines.append({"text": ln, "font": "F1", "size": size,
                      "color": (0, 0, 0)})
    add_blank(3)


# ===================================================================
#  HUJJAT MAZMUNI
# ===================================================================

# --- Title page ---
add_blank(110)
lines.append({"text": "XALQARO PUL O'TKAZMALARI", "font": "F2", "size": 20,
              "color": (0.10, 0.20, 0.50), "center": True})
lines.append({"text": "BIRLASHTIRILGAN MONITORING VA", "font": "F2",
              "size": 20, "color": (0.10, 0.20, 0.50), "center": True})
lines.append({"text": "SVERKA TIZIMI", "font": "F2", "size": 20,
              "color": (0.10, 0.20, 0.50), "center": True})
add_blank(14)
lines.append({"text": "Bank bek-ofisi uchun texnik hujjat (TZ)",
              "font": "F2", "size": 13, "color": (0.3, 0.3, 0.3),
              "center": True})
add_blank(40)
lines.append({"text": "Tashkilot turi: kommertsiya banki", "font": "F1",
              "size": 11, "color": (0, 0, 0), "center": True})
lines.append({"text": "Asosiy foydalanuvchi: bek-ofis / sverka xodimi",
              "font": "F1", "size": 11, "color": (0, 0, 0),
              "center": True})
lines.append({"text": "Backend: .NET 10  |  Frontend: Vue 3  |  DB: PostgreSQL",
              "font": "F1", "size": 11, "color": (0, 0, 0),
              "center": True})
add_blank(30)
lines.append({"text": "Sana: " + datetime.date.today().strftime("%d.%m.%Y"),
              "font": "F1", "size": 10, "color": (0.3, 0.3, 0.3),
              "center": True})
lines.append({"newpage": True})

# --- Mundarija ---
add_h1("Mundarija")
toc = [
    "1.  Loyihaning maqsadi",
    "2.  Hal qilinadigan muammolar",
    "3.  Tizim foydalanuvchilari va rollari",
    "4.  Foydalanuvchi senariylari (use-case)",
    "5.  Funksional talablar",
    "6.  Xalqaro o'tkazmaning ma'lumot maydonlari",
    "7.  Sverka (reconciliation) oqimi",
    "8.  Xato o'tkazmalar bilan ishlash",
    "9.  Audit jurnali va NBU hisoboti",
    "10. Tizim arxitekturasi",
    "11. Ma'lumotlar bazasi (SQL)",
    "12. Backend modellar (.NET 10)",
    "13. API endpointlar",
    "14. Frontend (Vue 3)",
    "15. Xavfsizlik va kirish nazorati",
    "16. Bajarilish ketma-ketligi (rejasi)",
    "17. Loyihani ishga tushirish",
]
for t in toc:
    add_bullet(t, size=10.5)
lines.append({"newpage": True})

# --- 1. Maqsad ---
add_h1("1. Loyihaning maqsadi")
add_para(
    "Bank bek-ofisi har kuni 8 ta xalqaro pul o'tkazma tizimi bilan ishlaydi: "
    "Western Union, MoneyGram, KoronaPay, Unistream, Contact, Ria, "
    "Zolotaya Korona va Asia Express. Har bir tizimning o'z portali, o'z "
    "hisobot fayli va o'z formati bor. Bu vaziyatda kunlik sverka, xatolarni "
    "tahlil qilish va NBU hisobotini tayyorlash o'ta mehnattalab.")
add_para(
    "Loyihaning maqsadi - barcha partnyor tizimlardan kelgan o'tkazmalarni "
    "yagona ma'lumotlar bazasida to'plash va bek-ofis xodimiga bitta veb "
    "interfeys orqali ko'rish, qidirish, sverka qilish va hisobot olish "
    "imkonini beradigan ichki bank tizimini yaratish.")

add_h2("Asosiy g'oya")
add_pre(
"  Western Union --\\\n"
"  MoneyGram     --|\n"
"  KoronaPay     --|     +---------------------+      +-----------+\n"
"  Unistream     --| ==> | Yagona o'tkazmalar  | <==> | Bek-ofis  |\n"
"  Contact       --|     | bazasi (PostgreSQL) |      | xodimi    |\n"
"  Ria           --|     +----------+----------+      +-----+-----+\n"
"  Z. Korona     --|                |                       |\n"
"  Asia Express  --/                v                       v\n"
"                          NBU hisobotlari        Sverka, xatolar,\n"
"                          va audit jurnali        qidiruv, modal")

# --- 2. Muammolar ---
add_h1("2. Hal qilinadigan muammolar")
add_para("Hujjatdagi har bir funksiya quyidagi 3 ta asosiy muammodan bittasini "
         "yechadi. Ro'yxat aniq:")

add_h2("Muammo 1. Sverka (reconciliation) qo'lda qilinmoqda")
add_pre(
"Hozirgi holat:\n"
"  - Har kuni har bir partnyordan Excel/CSV fayl yuklanadi.\n"
"  - Xodim qo'lda ABS bilan solishtiradi: PaymentRef, summa, sana.\n"
"  - 1 partnyor uchun ~200-500 ta o'tkazma, 8 partnyor x 1-2 soat.\n"
"  - Inson xatosi yuqori, farqlarni topish kech bo'ladi.\n\n"
"Yechim (tizim):\n"
"  - Partnyor faylini yuklab, avtomatik moslash (matching).\n"
"  - 'Faqat partnyorda bor', 'faqat bizda bor', 'summa farq qiladi'\n"
"    kategoriyalari avtomatik ajraladi.\n"
"  - Sverka aktiga 1 tugma bilan tayyor PDF/Excel chiqaradi.")

add_h2("Muammo 2. Xato o'tkazmalarni kuzatish qiyin")
add_pre(
"Hozirgi holat:\n"
"  - Xato bo'lgan o'tkazmalar har bir partnyor portalida alohida.\n"
"  - Xato sabablari turli formatda (kod, matn, til).\n"
"  - Mijozga javob berish uchun xodim har bir portalga qaraydi.\n\n"
"Yechim (tizim):\n"
"  - Barcha xato o'tkazmalar yagona dashboardda.\n"
"  - Xato sabablari me'yorlashtirilgan toifaga ajratiladi:\n"
"    KYC_FAIL, AML_HOLD, BENEFICIARY_NOT_FOUND, LIMIT_EXCEEDED,\n"
"    TECH_TIMEOUT, CANCELLED_BY_SENDER va h.k.\n"
"  - Statistika: qaysi partnyorda nechta, qaysi sababdan ko'p.")

add_h2("Muammo 3. Audit / NBU hisoboti uchun tarix yo'q")
add_pre(
"Hozirgi holat:\n"
"  - Tarix har bir partnyor portalida 30-90 kun saqlanadi.\n"
"  - Eski o'tkazmalarni topish uchun partnyorga so'rov yuboriladi.\n"
"  - NBU forma 402 va shubhali operatsiyalar (AML) hisoboti uchun\n"
"    ma'lumot yig'ish kunlab vaqt oladi.\n\n"
"Yechim (tizim):\n"
"  - O'tkazmalar bizning bazada 7 yil saqlanadi (NBU talabi).\n"
"  - Har qanday o'zgarish (status, sverka holati) audit jurnalida\n"
"    yoziladi: kim, qachon, nima qildi.\n"
"  - NBU hisoboti tugma orqali tayyor formatda chiqariladi.")

# --- 3. Foydalanuvchilar ---
add_h1("3. Tizim foydalanuvchilari va rollari")
add_pre(
"+----------------+--------------------------+--------------------------+\n"
"| Rol            | Kim                      | Asosiy harakatlar        |\n"
"+----------------+--------------------------+--------------------------+\n"
"| sverka_officer | Bek-ofis sverka xodimi   | Ro'yxat, modal, sverka,  |\n"
"|                | (asosiy aktor)           | partnyor fayl yuklash,   |\n"
"|                |                          | farqlarni hal qilish.    |\n"
"|                |                          |                          |\n"
"| compliance     | Compliance/AML xodimi    | Xato/shubhali o'tkazma   |\n"
"|                |                          | tahlili, AML hisoboti.   |\n"
"|                |                          |                          |\n"
"| auditor        | Ichki audit / NBU bilan  | Faqat o'qish; tarix,     |\n"
"|                | bog'lovchi               | jurnal, hisobot eksport. |\n"
"|                |                          |                          |\n"
"| admin          | IT administrator         | Foydalanuvchi, partnyor  |\n"
"|                |                          | va tizim sozlamalari.    |\n"
"+----------------+--------------------------+--------------------------+")
add_para("Eslatma: Mijozga to'g'ridan-to'g'ri ko'rinish bermaymiz - bu ichki "
         "bank tizimi.")

# --- 4. Use-case ---
add_h1("4. Foydalanuvchi senariylari (use-case)")

add_h2("UC-1. Kunlik sverka")
add_pre(
"Aktor: sverka_officer\n"
"Boshlanish: ish kuni boshida (08:30).\n"
"Qadamlar:\n"
"  1. Tizimga kiradi.\n"
"  2. 'Sverka' bo'limini ochadi, partnyorni tanlaydi (mas. KoronaPay).\n"
"  3. Partnyordan kelgan kunlik faylni (CSV/Excel) yuklaydi.\n"
"  4. Tizim avtomatik moslashtiradi va 4 ta toifaga ajratadi:\n"
"     - moslashgan (matched)\n"
"     - faqat partnyorda (missing_in_bank)\n"
"     - faqat bankda (missing_in_partner)\n"
"     - summa/sana farq qiladi (mismatch)\n"
"  5. Har bir nomoslash uchun izoh yozadi yoki 'tekshiruvga' belgilaydi.\n"
"  6. Sverka aktini PDF qilib chiqaradi va imzolaydi.\n"
"Natija: kunlik sverka 1-2 soat o'rniga 10-15 daqiqada bajariladi.")

add_h2("UC-2. Xato o'tkazma sababini topish")
add_pre(
"Aktor: compliance / sverka_officer\n"
"Boshlanish: mijoz qo'ng'iroq qildi yoki dashboardda xato ko'rindi.\n"
"Qadamlar:\n"
"  1. Asosiy ekranda 'Xatolar' filtrini yoqadi.\n"
"  2. PaymentRef yoki MTCN bo'yicha qidiradi.\n"
"  3. Modal ochadi - xato kodi, sababi, partnyor javobi ko'rinadi.\n"
"  4. Agar AML_HOLD bo'lsa, compliance bo'limiga yuboradi.\n"
"  5. Agar texnik bo'lsa, qayta yuborish (retry) tugmasi.\n"
"Natija: xatoning sababi 1 ekranda, partnyor portaliga kirish shart emas.")

add_h2("UC-3. NBU hisoboti tayyorlash")
add_pre(
"Aktor: auditor\n"
"Boshlanish: oy oxirida, NBU forma 402 talab qilinadi.\n"
"Qadamlar:\n"
"  1. 'Hisobotlar' bo'limiga kiradi.\n"
"  2. 'NBU 402' shablonini tanlaydi.\n"
"  3. Sana oralig'ini, valyutani belgilaydi.\n"
"  4. Tizim jamlagan ma'lumotni Excel formatida chiqaradi.\n"
"Natija: hisobot 2-3 kun o'rniga 5 daqiqada tayyor.")

# --- 5. Funksional talablar ---
add_h1("5. Funksional talablar")
add_para("Quyidagi har bir funksiya qaysi muammoni yechishi izohi bilan "
         "berilgan (M1=sverka, M2=xato tahlili, M3=audit/NBU).")
add_pre(
"+----+---------------------------------------+--------+------------------+\n"
"| #  | Funksiya                              | Yechim | Asosiy aktor     |\n"
"+----+---------------------------------------+--------+------------------+\n"
"| F1 | Yagona o'tkazmalar ro'yxati (jadval)  | M1, M2 | sverka_officer   |\n"
"| F2 | Filtr: partnyor, status, sana, valuta | M1, M2 | sverka_officer   |\n"
"| F3 | Qidiruv: PaymentRef / MTCN / passport | M2     | compliance       |\n"
"| F4 | Modal: o'tkazma to'liq tafsiloti      | M2     | sverka_officer   |\n"
"| F5 | Partnyor fayl yuklash (CSV/Excel)     | M1     | sverka_officer   |\n"
"| F6 | Avtomatik moslash + farqlar ro'yxati  | M1     | sverka_officer   |\n"
"| F7 | Sverka aktini PDF qilib chiqarish     | M1, M3 | sverka_officer   |\n"
"| F8 | Xato statistikasi (sabab/partnyor)    | M2     | compliance       |\n"
"| F9 | Audit jurnali (ko'rish, eksport)      | M3     | auditor          |\n"
"| F10| NBU forma 402 hisoboti (Excel)        | M3     | auditor          |\n"
"| F11| Foydalanuvchi va partnyor boshqaruvi  | -      | admin            |\n"
"+----+---------------------------------------+--------+------------------+")

# --- 6. Maydonlar ---
add_h1("6. Xalqaro o'tkazmaning ma'lumot maydonlari")
add_para("Xalqaro pul o'tkazmasi mahalliy o'tkazmadan farq qiladi: korridor, "
         "valyuta jufti, MTCN/Reference, o'tkazma yo'nalishi (kiruvchi yoki "
         "chiquvchi), tomon banki/agenti kabi maydonlar bor.")
add_pre(
"+--------------------------+----------------------------------------------+\n"
"| Maydon                   | Tavsif                                       |\n"
"+--------------------------+----------------------------------------------+\n"
"| payment_ref              | Bizning ichki ID (UUID)                      |\n"
"| partner_code             | WU, MGR, KP, UNI, CON, RIA, ZK, ASE          |\n"
"| partner_txn_id           | Partnyordagi original ID                     |\n"
"| mtcn                     | Money Transfer Control Number (WU/MGR)       |\n"
"| direction                | INCOMING / OUTGOING                          |\n"
"| status                   | created, sent, pending, paid, cancelled,     |\n"
"|                          | failed, refunded                             |\n"
"| corridor_from / _to      | Davlat ISO kodlari (UZ, RU, US, TR, ...)     |\n"
"| send_currency / amount   | Jo'natilgan valyuta va summa                 |\n"
"| recv_currency / amount   | Qabul valyutasi va summa                     |\n"
"| amount_uzs               | UZSga o'girilgan ekvivalent                  |\n"
"| fx_rate                  | Qo'llanilgan kurs                            |\n"
"| usd_rate                 | NBU/CBU dollar kursi                         |\n"
"| commission               | Komissiya (jo'natuvchi tomonidan)            |\n"
"| sender_*                 | F.I.Sh, passport seriya/raqam, telefon,      |\n"
"|                          | tug'ilgan sana, fuqarolik, manzil            |\n"
"| receiver_*               | F.I.Sh, passport, telefon, fuqarolik         |\n"
"| sender_country           | Jo'natuvchi davlati                          |\n"
"| receiver_country         | Qabul qiluvchi davlati                       |\n"
"| purpose_code             | O'tkazma maqsadi (oilaviy, savdo, ...)       |\n"
"| sanctions_check          | clean / flagged / blocked                    |\n"
"| aml_score                | 0-100                                        |\n"
"| error_code / message     | Xato kodi va matni (me'yorlashgan)           |\n"
"| sent_at / paid_at        | Sanalar                                      |\n"
"| recon_status             | not_checked, matched, mismatch, missing      |\n"
"| recon_batch_id           | Sverka partiyasi ID                          |\n"
"+--------------------------+----------------------------------------------+")

# --- 7. Sverka oqimi ---
add_h1("7. Sverka (reconciliation) oqimi")
add_pre(
"  [1. Partnyor fayli (CSV/Excel)]\n"
"            |\n"
"            v\n"
"  [2. Parser - partnyor formatiga maxsus]\n"
"     - WU adapteri          - Unistream adapteri\n"
"     - MoneyGram adapteri   - Contact adapteri\n"
"     - KoronaPay adapteri   - Ria, Z. Korona, Asia Express\n"
"            |\n"
"            v\n"
"  [3. Matching engine]\n"
"     kalit: partner_txn_id YOKI mtcn\n"
"     to'lqinlar:\n"
"       a) bir xil ID + summa + sana   -> matched\n"
"       b) bir xil ID, summa farqi     -> amount_mismatch\n"
"       c) faqat partnyorda             -> missing_in_bank\n"
"       d) faqat bankda                 -> missing_in_partner\n"
"            |\n"
"            v\n"
"  [4. Sverka partiyasi (recon_batch)]\n"
"     - sana: 11.06.2026\n"
"     - partnyor: KoronaPay\n"
"     - jami: 412 ta yozuv\n"
"     - matched: 405, mismatch: 3, missing_in_bank: 2,\n"
"       missing_in_partner: 2\n"
"            |\n"
"            v\n"
"  [5. Xodim har bir farqga izoh yozadi yoki tekshiruvga yuboradi]\n"
"            |\n"
"            v\n"
"  [6. Sverka akti (PDF) - imzo va arxiv]")

# --- 8. Xato o'tkazmalar ---
add_h1("8. Xato o'tkazmalar bilan ishlash")
add_para("Har bir partnyorning o'z xato kodi bo'ladi. Tizim ularni ichki, "
         "me'yorlashgan toifalarga moslab oladi - xodim faqat toifa bo'yicha "
         "ishlasa bo'ladi.")
add_pre(
"+----------------------+-------------------------------------------------+\n"
"| Ichki toifa          | Tavsif va misol                                 |\n"
"+----------------------+-------------------------------------------------+\n"
"| KYC_FAIL             | Mijoz hujjati notog'ri / muddati o'tgan         |\n"
"| AML_HOLD             | AML/sanksiya ro'yxati - compliance ko'radi      |\n"
"| BENEFICIARY_NOT_FOUND| Qabul qiluvchi topilmadi yoki MTCN yaroqsiz     |\n"
"| LIMIT_EXCEEDED       | Kunlik/oylik limit oshib ketdi                  |\n"
"| INSUFFICIENT_FUNDS   | Mablag' yetmadi (chiquvchida)                   |\n"
"| TECH_TIMEOUT         | Texnik xato, partnyor javobi yo'q               |\n"
"| CANCELLED_BY_SENDER  | Jo'natuvchi bekor qildi                         |\n"
"| FX_RATE_MISMATCH     | Kurs farqi limitdan oshdi                       |\n"
"| OTHER                | Boshqa (matn ichida saqlanadi)                  |\n"
"+----------------------+-------------------------------------------------+")
add_h3("Statistika ko'rinishi")
add_bullet("Partnyor x toifa kesimida xato soni (oxirgi 30 kun).")
add_bullet("Trend grafigi - kun bo'yicha xato foizi.")
add_bullet("Top 10 takrorlanuvchi xato matni (asl, partnyor matni).")

# --- 9. Audit / NBU ---
add_h1("9. Audit jurnali va NBU hisoboti")
add_h2("9.1. Audit jurnali (audit_log jadvali)")
add_para("Tizimdagi har qanday muhim harakat yoziladi. Hech qanday yozuv "
         "o'chirilmaydi yoki o'zgartirilmaydi - faqat yangi yozuv qo'shiladi.")
add_pre(
"audit_log:\n"
"  - id, timestamp, user_id, user_login\n"
"  - action: LOGIN, VIEW_PAYMENT, EXPORT_REPORT, RUN_RECON,\n"
"            RESOLVE_DIFF, RETRY_PAYMENT, CHANGE_USER, ...\n"
"  - entity_type, entity_id  (qaysi obyekt ustida)\n"
"  - details_json            (eski va yangi qiymat)\n"
"  - ip_address")

add_h2("9.2. NBU hisobotlari (chiqariladigan formatlar)")
add_bullet("Forma 402 - xalqaro o'tkazmalar bo'yicha kunlik hisobot (Excel).")
add_bullet("AML hisoboti - flagged va blocked o'tkazmalar (PDF + Excel).")
add_bullet("Korridor kesimida statistik hisobot (kelgan/ketgan, davlat).")
add_bullet("Saqlash muddati: 7 yil (NBU talabi); arxivga ko'chiriladi.")

# --- 10. Arxitektura ---
add_h1("10. Tizim arxitekturasi")
add_pre(
"  Partnyor ma'lumot manbalari\n"
"  ============================\n"
"  - Avtomatik: API/Webhook (qaerda mavjud bo'lsa)\n"
"  - Yarim avtomatik: SFTP/elektron pochta orqali kunlik fayl\n"
"  - Qo'lda: xodim tomonidan UI orqali yuklash\n"
"            |\n"
"            v\n"
"  +-------------------------------+\n"
"  | Integration / Import qatlami  |  (.NET 10 background services)\n"
"  | - WU adapter                  |\n"
"  | - MoneyGram adapter           |\n"
"  | - KoronaPay adapter           |\n"
"  | - Unistream / Contact / Ria / |\n"
"  |   Z. Korona / Asia Express    |\n"
"  +-------------+-----------------+\n"
"                |  yagona ichki model (Payment)\n"
"                v\n"
"  +-------------------------------+         +-------------------------+\n"
"  | Domain qatlami                | <-----> | PostgreSQL (asosiy DB)  |\n"
"  | - Reconciliation engine       |         |  payments, partners,    |\n"
"  | - Error normalizer            |         |  recon_batches,         |\n"
"  | - Audit logger                |         |  recon_diffs, audit_log |\n"
"  | - Report generator (NBU)      |         +-------------------------+\n"
"  +-------------+-----------------+\n"
"                |\n"
"                v\n"
"  +-------------------------------+\n"
"  | API qatlami (.NET 10 Web API) |  JWT, RBAC\n"
"  +-------------+-----------------+\n"
"                |\n"
"                v\n"
"  +-------------------------------+\n"
"  | Vue 3 SPA (bek-ofis xodimi)   |  jadval, modal, sverka, hisobot\n"
"  +-------------------------------+")

# --- 11. SQL ---
add_h1("11. Ma'lumotlar bazasi (SQL)")
add_para("Asosiy jadvallar (PostgreSQL). Maxfiy maydonlar shifrlanadi (PII).")
add_code(
"CREATE TABLE roles (\n"
"    id SERIAL PRIMARY KEY,\n"
"    name VARCHAR(40) UNIQUE NOT NULL\n"
"      -- 'sverka_officer','compliance','auditor','admin'\n"
");\n\n"
"CREATE TABLE partners (\n"
"    id SERIAL PRIMARY KEY,\n"
"    code VARCHAR(10) UNIQUE NOT NULL,   -- WU, MGR, KP, UNI, CON, RIA, ZK, ASE\n"
"    name VARCHAR(100) NOT NULL,\n"
"    is_active BOOLEAN DEFAULT true\n"
");\n\n"
"CREATE TABLE users (\n"
"    id SERIAL PRIMARY KEY,\n"
"    login VARCHAR(100) UNIQUE NOT NULL,\n"
"    password_hash VARCHAR(255) NOT NULL,\n"
"    full_name VARCHAR(150),\n"
"    role_id INT NOT NULL REFERENCES roles(id),\n"
"    is_active BOOLEAN DEFAULT true,\n"
"    created_at TIMESTAMP DEFAULT now()\n"
");")
add_code(
"CREATE TABLE payments (\n"
"    id BIGSERIAL PRIMARY KEY,\n"
"    payment_ref      VARCHAR(64) UNIQUE NOT NULL, -- ichki UUID\n"
"    partner_id       INT NOT NULL REFERENCES partners(id),\n"
"    partner_txn_id   VARCHAR(100),\n"
"    mtcn             VARCHAR(40),                 -- WU/MGR\n"
"    direction        VARCHAR(10) NOT NULL,        -- INCOMING/OUTGOING\n"
"    status           VARCHAR(20) NOT NULL,\n"
"    -- korridor / valyuta\n"
"    corridor_from    CHAR(2),                     -- ISO: UZ, RU\n"
"    corridor_to      CHAR(2),\n"
"    send_currency    CHAR(3),  send_amount    NUMERIC(18,2),\n"
"    recv_currency    CHAR(3),  recv_amount    NUMERIC(18,2),\n"
"    amount_uzs       NUMERIC(18,2),\n"
"    fx_rate          NUMERIC(14,6),\n"
"    usd_rate         NUMERIC(14,4),\n"
"    commission       NUMERIC(18,2),\n"
"    -- jo'natuvchi (PII shifrlanadi)\n"
"    sender_full_name VARCHAR(200),\n"
"    sender_passport  VARCHAR(40),\n"
"    sender_phone     VARCHAR(20),\n"
"    sender_country   CHAR(2),\n"
"    -- qabul qiluvchi\n"
"    receiver_full_name VARCHAR(200),\n"
"    receiver_passport  VARCHAR(40),\n"
"    receiver_phone     VARCHAR(20),\n"
"    receiver_country   CHAR(2),\n"
"    -- compliance\n"
"    purpose_code     VARCHAR(20),\n"
"    sanctions_check  VARCHAR(20) DEFAULT 'clean',\n"
"    aml_score        SMALLINT,\n"
"    -- xato\n"
"    error_category   VARCHAR(40),  -- KYC_FAIL, AML_HOLD ...\n"
"    error_code       VARCHAR(50),\n"
"    error_message    TEXT,\n"
"    -- sverka\n"
"    recon_status     VARCHAR(20) DEFAULT 'not_checked',\n"
"    recon_batch_id   BIGINT,\n"
"    -- vaqt\n"
"    sent_at          TIMESTAMP,\n"
"    paid_at          TIMESTAMP,\n"
"    created_at       TIMESTAMP DEFAULT now(),\n"
"    updated_at       TIMESTAMP DEFAULT now()\n"
");\n\n"
"CREATE INDEX ix_payments_partner   ON payments(partner_id);\n"
"CREATE INDEX ix_payments_mtcn      ON payments(mtcn);\n"
"CREATE INDEX ix_payments_status    ON payments(status);\n"
"CREATE INDEX ix_payments_sent_at   ON payments(sent_at);\n"
"CREATE INDEX ix_payments_recon     ON payments(recon_status, recon_batch_id);")
add_code(
"-- Sverka partiyalari va farqlari\n"
"CREATE TABLE recon_batches (\n"
"    id BIGSERIAL PRIMARY KEY,\n"
"    partner_id INT NOT NULL REFERENCES partners(id),\n"
"    business_date DATE NOT NULL,\n"
"    file_name VARCHAR(255),\n"
"    total_partner INT, total_bank INT,\n"
"    matched INT, mismatch INT,\n"
"    missing_in_bank INT, missing_in_partner INT,\n"
"    status VARCHAR(20) DEFAULT 'open', -- open/closed/signed\n"
"    created_by INT REFERENCES users(id),\n"
"    created_at TIMESTAMP DEFAULT now()\n"
");\n\n"
"CREATE TABLE recon_diffs (\n"
"    id BIGSERIAL PRIMARY KEY,\n"
"    batch_id BIGINT NOT NULL REFERENCES recon_batches(id),\n"
"    payment_id BIGINT REFERENCES payments(id),\n"
"    diff_type VARCHAR(30) NOT NULL,\n"
"        -- amount_mismatch / missing_in_bank / missing_in_partner\n"
"    partner_record_json JSONB,\n"
"    bank_record_json    JSONB,\n"
"    resolution VARCHAR(20),  -- pending/accepted/disputed\n"
"    note TEXT,\n"
"    resolved_by INT REFERENCES users(id),\n"
"    resolved_at TIMESTAMP\n"
");\n\n"
"CREATE TABLE audit_log (\n"
"    id BIGSERIAL PRIMARY KEY,\n"
"    ts TIMESTAMP DEFAULT now(),\n"
"    user_id INT REFERENCES users(id),\n"
"    user_login VARCHAR(100),\n"
"    action VARCHAR(40) NOT NULL,\n"
"    entity_type VARCHAR(40),\n"
"    entity_id VARCHAR(64),\n"
"    details JSONB,\n"
"    ip_address VARCHAR(45)\n"
");")

# --- 12. .NET modellar ---
add_h1("12. Backend modellar (.NET 10)")
add_para("Loyiha tuzilishi:")
add_pre(
"InternationalTransfers.Api/\n"
" |- Domain/\n"
" |   |- Entities/   (Payment, Partner, User, Role,\n"
" |   |              ReconBatch, ReconDiff, AuditLog)\n"
" |   |- Enums/      (Direction, PaymentStatus, ReconStatus,\n"
" |   |              ErrorCategory, DiffType)\n"
" |   |- Services/   (ReconciliationService, ImportService,\n"
" |                   ErrorNormalizer, ReportService, AuditService)\n"
" |- Infrastructure/\n"
" |   |- Persistence/    (AppDbContext, EF Core configs)\n"
" |   |- Adapters/       (WuAdapter, MoneyGramAdapter, ...)\n"
" |- Application/\n"
" |   |- Dtos/, Queries/, Commands/\n"
" |- Api/\n"
" |   |- Controllers/    (PaymentsController, ReconciliationController,\n"
" |                       ReportsController, AuthController)\n"
" |   |- Program.cs\n"
" |- appsettings.json")
add_h3("Asosiy entity: Payment.cs (qisqartma)")
add_code(
"public class Payment\n"
"{\n"
"    public long Id { get; set; }\n"
"    public string PaymentRef { get; set; } = default!;\n"
"    public int PartnerId { get; set; }\n"
"    public Partner? Partner { get; set; }\n"
"    public string? PartnerTxnId { get; set; }\n"
"    public string? Mtcn { get; set; }\n"
"    public Direction Direction { get; set; }\n"
"    public PaymentStatus Status { get; set; }\n\n"
"    public string? CorridorFrom { get; set; }\n"
"    public string? CorridorTo { get; set; }\n"
"    public string? SendCurrency { get; set; }\n"
"    public decimal? SendAmount { get; set; }\n"
"    public string? RecvCurrency { get; set; }\n"
"    public decimal? RecvAmount { get; set; }\n"
"    public decimal? AmountUzs { get; set; }\n"
"    public decimal? FxRate { get; set; }\n"
"    public decimal? UsdRate { get; set; }\n"
"    public decimal? Commission { get; set; }\n\n"
"    // jo'natuvchi va qabul qiluvchi PII (shifrlanadi)\n"
"    public string? SenderFullName { get; set; }\n"
"    public string? SenderPassport { get; set; }\n"
"    public string? SenderPhone { get; set; }\n"
"    public string? SenderCountry { get; set; }\n"
"    public string? ReceiverFullName { get; set; }\n"
"    public string? ReceiverPassport { get; set; }\n"
"    public string? ReceiverPhone { get; set; }\n"
"    public string? ReceiverCountry { get; set; }\n\n"
"    public string? PurposeCode { get; set; }\n"
"    public string SanctionsCheck { get; set; } = \"clean\";\n"
"    public short? AmlScore { get; set; }\n\n"
"    public ErrorCategory? ErrorCategory { get; set; }\n"
"    public string? ErrorCode { get; set; }\n"
"    public string? ErrorMessage { get; set; }\n\n"
"    public ReconStatus ReconStatus { get; set; } = ReconStatus.NotChecked;\n"
"    public long? ReconBatchId { get; set; }\n\n"
"    public DateTime? SentAt { get; set; }\n"
"    public DateTime? PaidAt { get; set; }\n"
"    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;\n"
"    public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;\n"
"}")
add_h3("ReconBatch.cs va ReconDiff.cs")
add_code(
"public class ReconBatch\n"
"{\n"
"    public long Id { get; set; }\n"
"    public int PartnerId { get; set; }\n"
"    public DateOnly BusinessDate { get; set; }\n"
"    public string? FileName { get; set; }\n"
"    public int TotalPartner { get; set; }\n"
"    public int TotalBank { get; set; }\n"
"    public int Matched { get; set; }\n"
"    public int Mismatch { get; set; }\n"
"    public int MissingInBank { get; set; }\n"
"    public int MissingInPartner { get; set; }\n"
"    public string Status { get; set; } = \"open\";\n"
"    public int? CreatedBy { get; set; }\n"
"    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;\n"
"    public List<ReconDiff> Diffs { get; set; } = new();\n"
"}\n\n"
"public class ReconDiff\n"
"{\n"
"    public long Id { get; set; }\n"
"    public long BatchId { get; set; }\n"
"    public long? PaymentId { get; set; }\n"
"    public DiffType DiffType { get; set; }\n"
"    public string? PartnerRecordJson { get; set; }\n"
"    public string? BankRecordJson { get; set; }\n"
"    public string Resolution { get; set; } = \"pending\";\n"
"    public string? Note { get; set; }\n"
"}")
add_h3("Enumlar")
add_code(
"public enum Direction { Incoming, Outgoing }\n\n"
"public enum PaymentStatus {\n"
"    Created, Sent, Pending, Paid, Cancelled, Failed, Refunded\n"
"}\n\n"
"public enum ReconStatus {\n"
"    NotChecked, Matched, AmountMismatch,\n"
"    MissingInBank, MissingInPartner\n"
"}\n\n"
"public enum ErrorCategory {\n"
"    KYC_FAIL, AML_HOLD, BENEFICIARY_NOT_FOUND, LIMIT_EXCEEDED,\n"
"    INSUFFICIENT_FUNDS, TECH_TIMEOUT, CANCELLED_BY_SENDER,\n"
"    FX_RATE_MISMATCH, OTHER\n"
"}\n\n"
"public enum DiffType {\n"
"    AmountMismatch, MissingInBank, MissingInPartner\n"
"}")

# --- 13. API ---
add_h1("13. API endpointlar")
add_pre(
"+--------+------------------------------------+----------------------+\n"
"| Metod  | URL                                | Rol(lar)             |\n"
"+--------+------------------------------------+----------------------+\n"
"| POST   | /api/auth/login                    | hammasi              |\n"
"| GET    | /api/payments                      | sverka, compliance,  |\n"
"|        |   ?partner=&status=&from=&to=&q=   | auditor              |\n"
"|        |   &recon=&error_cat=&page=&limit=  |                      |\n"
"| GET    | /api/payments/{id}                 | sverka, compliance,  |\n"
"|        |                                    | auditor              |\n"
"| POST   | /api/payments/{id}/retry           | sverka, compliance   |\n"
"| GET    | /api/errors/stats                  | compliance           |\n"
"|        |   ?from=&to=&partner=              |                      |\n"
"| POST   | /api/recon/upload                  | sverka               |\n"
"|        |   (multipart: file + partner_id)   |                      |\n"
"| GET    | /api/recon/batches                 | sverka, auditor      |\n"
"| GET    | /api/recon/batches/{id}            | sverka, auditor      |\n"
"| GET    | /api/recon/batches/{id}/diffs      | sverka               |\n"
"| POST   | /api/recon/diffs/{id}/resolve      | sverka               |\n"
"| POST   | /api/recon/batches/{id}/sign       | sverka               |\n"
"| GET    | /api/recon/batches/{id}/act.pdf    | sverka, auditor      |\n"
"| GET    | /api/reports/nbu-402.xlsx          | auditor              |\n"
"|        |   ?from=&to=                       |                      |\n"
"| GET    | /api/reports/aml.xlsx              | compliance, auditor  |\n"
"| GET    | /api/audit                         | auditor              |\n"
"|        |   ?user=&action=&from=&to=         |                      |\n"
"+--------+------------------------------------+----------------------+")

# --- 14. Frontend ---
add_h1("14. Frontend (Vue 3)")
add_para("SPA, Composition API, Pinia + Vue Router. Asosiy sahifalar:")
add_pre(
"frontend/src/views/\n"
"  LoginView.vue\n"
"  PaymentsView.vue          (F1, F2, F3 - asosiy ish ekrani)\n"
"  PaymentModalView.vue      (F4 - to'liq tafsilot)\n"
"  ReconciliationView.vue    (F5, F6, F7 - sverka)\n"
"    |- ReconUpload.vue\n"
"    |- ReconBatchList.vue\n"
"    |- ReconBatchDetail.vue\n"
"  ErrorsDashboard.vue       (F8 - xato statistikasi)\n"
"  ReportsView.vue           (F10 - NBU 402, AML)\n"
"  AuditView.vue             (F9 - audit jurnali)\n"
"  AdminView.vue             (F11 - foydalanuvchilar, partnyorlar)")

# --- 15. Xavfsizlik ---
add_h1("15. Xavfsizlik va kirish nazorati")
add_bullet("RBAC - har bir endpoint rol(lar)i bilan himoyalangan; tekshiruv "
           "serverda.")
add_bullet("Parol BCrypt hash, JWT amal qilish muddati 8 soat.")
add_bullet("PII (passport, telefon) ma'lumotlar bazasida shifrlanadi "
           "(AES-256, kalit Vault yoki AWS KMS'da).")
add_bullet("Modal'da karta/passport maskalangan; to'liq qiymat faqat "
           "compliance va sverka rolida ko'rinadi.")
add_bullet("Audit_log o'chirilmaydi; faqat append. Saqlash 7 yil.")
add_bullet("Sanksiya ro'yxati (OFAC/EU/NBU) bilan har bir o'tkazma "
           "tekshiriladi.")
add_bullet("CORS faqat ishonchli ichki domenga ochiq, HTTPS majburiy.")

# --- 16. Reja ---
add_h1("16. Bajarilish ketma-ketligi (rejasi)")
add_pre(
"Sprint 1 (yadro, 2 hafta):\n"
"  - .NET 10 va Vue 3 skelet, JWT, RBAC.\n"
"  - DB migratsiyalari (payments, partners, users, roles, audit_log).\n"
"  - Login, foydalanuvchilar va partnyorlar boshqaruvi.\n"
"\nSprint 2 (asosiy ko'rish, 2 hafta):  -> M2 ning bir qismini yopadi\n"
"  - Yagona o'tkazmalar ro'yxati (F1).\n"
"  - Filtr va qidiruv (F2, F3).\n"
"  - To'liq tafsilot modali (F4).\n"
"\nSprint 3 (sverka, 2-3 hafta):  -> M1 ni yopadi\n"
"  - Partnyor adapterlari (kamida 3 ta partnyor uchun parser).\n"
"  - Matching engine, recon_batches, recon_diffs.\n"
"  - Fayl yuklash UI, farqlar ekrani, izoh va resolve.\n"
"  - Sverka akti PDF.\n"
"\nSprint 4 (xatolar va NBU, 2 hafta):  -> M2 va M3 ni yopadi\n"
"  - Xato me'yorlashtiruvchi, statistika dashboardi (F8).\n"
"  - NBU 402 va AML hisobotlari (F10).\n"
"  - Audit jurnali ekrani (F9).\n"
"\nSprint 5 (qolgan partnyor adapterlari + qattiqlash, 1-2 hafta):\n"
"  - Qolgan partnyor adapterlari.\n"
"  - PII shifrlash, sanksiya integratsiyasi, yuklamani sinash.\n"
"\nUmumiy taxminiy muddat: 9-11 hafta.")

# --- 17. Ishga tushirish ---
add_h1("17. Loyihani ishga tushirish")
add_h3("Backend (.NET 10)")
add_code(
"dotnet new webapi -n InternationalTransfers.Api\n"
"cd InternationalTransfers.Api\n"
"dotnet add package Microsoft.EntityFrameworkCore\n"
"dotnet add package Npgsql.EntityFrameworkCore.PostgreSQL\n"
"dotnet add package Microsoft.AspNetCore.Authentication.JwtBearer\n"
"dotnet add package BCrypt.Net-Next\n"
"dotnet add package ClosedXML        # Excel hisobot\n"
"dotnet add package QuestPDF         # PDF (sverka akti)\n\n"
"dotnet ef migrations add Init\n"
"dotnet ef database update\n"
"dotnet run")
add_h3("Frontend (Vue 3)")
add_code(
"npm create vite@latest frontend -- --template vue\n"
"cd frontend\n"
"npm install axios pinia vue-router element-plus\n"
"npm run dev   # http://localhost:5173")
add_h3("appsettings.json (namuna)")
add_code(
"{\n"
"  \"ConnectionStrings\": {\n"
"    \"Default\": \"Host=localhost;Port=5432;Database=intl_transfers;\" +\n"
"               \"Username=postgres;Password=postgres\"\n"
"  },\n"
"  \"Jwt\": { \"Key\": \"BU_YERGA_KUCHLI_MAXFIY_KALIT_QOYING_32+\" },\n"
"  \"Encryption\": { \"PiiKeyId\": \"vault://kv/pii-key\" }\n"
"}")
add_blank(10)
add_para("--- Hujjat yakuni ---")


# ===================================================================
#  PDF GENERATSIYA
# ===================================================================

def esc(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


pages = []
cur = []
y = PAGE_H - MT

for ln in lines:
    if ln.get("newpage"):
        pages.append(cur); cur = []; y = PAGE_H - MT; continue
    if "blank" in ln:
        h = ln["blank"]
        if y - h < MB:
            pages.append(cur); cur = []; y = PAGE_H - MT
        else:
            y -= h
        continue
    if ln.get("rule"):
        h = 8
        if y - h < MB:
            pages.append(cur); cur = []; y = PAGE_H - MT
        cur.append({"rule": True, "y": y - 4})
        y -= h
        continue
    size = ln["size"]; h = size * 1.5
    if y - h < MB:
        pages.append(cur); cur = []; y = PAGE_H - MT
    item = dict(ln); item["baseline"] = y - size
    cur.append(item)
    y -= h

if cur:
    pages.append(cur)


def build_content(items):
    out = []
    for it in items:
        if it.get("rule"):
            out.append("0.55 0.6 0.75 RG")
            out.append("0.6 w")
            out.append(f"{ML:.2f} {it['y']:.2f} m "
                       f"{ML + CONTENT_W:.2f} {it['y']:.2f} l S")
            continue
        size = it["size"]; font = it["font"]
        col = it.get("color", (0, 0, 0)); text = it["text"]
        if it.get("center"):
            tw = len(text) * size * 0.6
            x = ML + (CONTENT_W - tw) / 2
        else:
            x = ML
        if it.get("code"):
            out.append("0.85 0.88 0.95 RG")
            out.append("1.5 w")
            out.append(f"{ML - 6:.2f} {it['baseline'] - 2:.2f} m "
                       f"{ML - 6:.2f} {it['baseline'] + size:.2f} l S")
        out.append("BT")
        out.append(f"/{font} {size:.2f} Tf")
        out.append(f"{col[0]:.3f} {col[1]:.3f} {col[2]:.3f} rg")
        out.append(f"{x:.2f} {it['baseline']:.2f} Td")
        out.append(f"({esc(text)}) Tj")
        out.append("ET")
    return "\n".join(out)


objects = []
catalog_id, pages_id = 1, 2
font1_id, font2_id = 3, 4
page_obj_ids, content_obj_ids = [], []
next_id = 5
for _ in pages:
    page_obj_ids.append(next_id); next_id += 1
    content_obj_ids.append(next_id); next_id += 1

objects.append((catalog_id,
    f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode("latin-1")))
kids = " ".join(f"{p} 0 R" for p in page_obj_ids)
objects.append((pages_id,
    f"<< /Type /Pages /Kids [{kids}] /Count {len(page_obj_ids)} >>"
    .encode("latin-1")))
objects.append((font1_id,
    b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier "
    b"/Encoding /WinAnsiEncoding >>"))
objects.append((font2_id,
    b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier-Bold "
    b"/Encoding /WinAnsiEncoding >>"))

for i, items in enumerate(pages):
    pid = page_obj_ids[i]; cid = content_obj_ids[i]
    page_dict = (
        f"<< /Type /Page /Parent {pages_id} 0 R "
        f"/MediaBox [0 0 {PAGE_W:.2f} {PAGE_H:.2f}] "
        f"/Resources << /Font << /F1 {font1_id} 0 R "
        f"/F2 {font2_id} 0 R >> >> /Contents {cid} 0 R >>"
    )
    objects.append((pid, page_dict.encode("latin-1")))
    stream = build_content(items).encode("latin-1")
    body = (b"<< /Length " + str(len(stream)).encode() +
            b" >>\nstream\n" + stream + b"\nendstream")
    objects.append((cid, body))

objects.sort(key=lambda o: o[0])
buf = bytearray()
buf += b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
offsets = {}
for oid, body in objects:
    offsets[oid] = len(buf)
    buf += f"{oid} 0 obj\n".encode("latin-1")
    buf += body
    buf += b"\nendobj\n"

xref_pos = len(buf)
n = len(objects) + 1
buf += f"xref\n0 {n}\n".encode("latin-1")
buf += b"0000000000 65535 f \n"
for oid in range(1, n):
    buf += f"{offsets[oid]:010d} 00000 n \n".encode("latin-1")

buf += b"trailer\n"
buf += f"<< /Size {n} /Root {catalog_id} 0 R >>\n".encode("latin-1")
buf += b"startxref\n"
buf += f"{xref_pos}\n".encode("latin-1")
buf += b"%%EOF\n"

with open("Texnik_Hujjat.pdf", "wb") as f:
    f.write(buf)

print(f"PDF yaratildi: Texnik_Hujjat.pdf | sahifalar: {len(pages)} | "
      f"hajmi: {len(buf)} bayt")
