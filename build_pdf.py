# -*- coding: utf-8 -*-
"""
Texnik hujjatni PDF qilib chiqaruvchi skript (tashqi kutubxonasiz).
Mazmun: bank ichki dashboardi - 3-4 ta partnyor pul o'tkazmalari
monitoringi va xatolar paneli.
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
lines.append({"text": "PARTNYOR PUL O'TKAZMALARI", "font": "F2", "size": 20,
              "color": (0.10, 0.20, 0.50), "center": True})
lines.append({"text": "MONITORING TIZIMI", "font": "F2",
              "size": 20, "color": (0.10, 0.20, 0.50), "center": True})
add_blank(14)
lines.append({"text": "Bank ichki dashboardi uchun texnik hujjat (TZ)",
              "font": "F2", "size": 13, "color": (0.3, 0.3, 0.3),
              "center": True})
add_blank(40)
lines.append({"text": "Tashkilot turi: kommertsiya banki", "font": "F1",
              "size": 11, "color": (0, 0, 0), "center": True})
lines.append({"text": "Asosiy foydalanuvchi: bek-ofis operatori",
              "font": "F1", "size": 11, "color": (0, 0, 0),
              "center": True})
lines.append({"text": "Partnyorlar soni: 3-4 ta",
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
    "2.  Hozirgi muammo va taklif etilayotgan yechim",
    "3.  Tizim foydalanuvchilari va rollari",
    "4.  Foydalanuvchi senariylari (use-case)",
    "5.  Funksional talablar",
    "6.  O'tkazmaning ma'lumot maydonlari",
    "7.  Xato toifalari va xatolar paneli",
    "8.  Tizim arxitekturasi",
    "9.  Ma'lumotlar bazasi (PostgreSQL)",
    "10. Backend modellar (.NET 10)",
    "11. API endpointlar",
    "12. Frontend ekranlar (Vue 3)",
    "13. Xavfsizlik va kirish nazorati",
    "14. Bajarilish rejasi va ishga tushirish",
]
for t in toc:
    add_bullet(t, size=10.5)
lines.append({"newpage": True})

# --- 1. Maqsad ---
add_h1("1. Loyihaning maqsadi")
add_para(
    "Bank o'zining 3-4 ta partnyori orqali pul o'tkazmalarini amalga "
    "oshiradi. Har bir partnyorning o'z portali va o'z formati bor. "
    "Bek-ofis operatori har kuni har bir portalga alohida kirib, "
    "tranzaksiyalarni va xato yozuvlarni qo'lda kuzatishga majbur. Bu "
    "vaqt oladi va xatolarni o'z vaqtida topishga to'sqinlik qiladi.")
add_para(
    "Loyihaning maqsadi - 3-4 ta partnyordan kelgan o'tkazmalarni yagona "
    "bazaga to'plash va bek-ofis operatoriga bitta veb interfeys orqali "
    "kunlik kuzatuv hamda xatolarni darhol ko'rish imkonini beradigan "
    "ichki bank dashboardini yaratish.")

add_h2("Aniq cheklov (scope)")
add_bullet("Bu - ichki bank tizimi. Partnyorlar va mijozlar tashqaridan "
           "kira olmaydi.")
add_bullet("Foydalanuvchi - faqat bank xodimi: bek-ofis operatori va admin.")
add_bullet("Tizim 2 ta asosiy ekrandan iborat: tranzaksiyalar ro'yxati va "
           "xatolar paneli.")
add_bullet("Birinchi versiyada sverka, NBU 402 va AML hisobotlari "
           "kiritilmagan. Kerak bo'lsa keyingi versiyalarda qo'shiladi.")

add_h2("Asosiy g'oya")
add_pre(
"  Partnyor 1 --\\\n"
"  Partnyor 2 --|     +---------------------+      +------------+\n"
"  Partnyor 3 --| ==> | Yagona o'tkazmalar  | <==> | Bek-ofis   |\n"
"  Partnyor 4 --/     | bazasi (PostgreSQL) |      | operatori  |\n"
"                     +----------+----------+      +-----+------+\n"
"                                |                       |\n"
"                                v                       v\n"
"                          Excel eksport         Tranzaksiyalar va\n"
"                          (kunlik/oraliq)        xatolar dashboardi")

# --- 2. Muammo va yechim ---
add_h1("2. Hozirgi muammo va taklif etilayotgan yechim")

add_h2("Muammo")
add_pre(
"Hozirgi holat:\n"
"  - Har bir partnyorning o'z portali bor (3-4 ta alohida tizim).\n"
"  - Operator har kuni har biriga alohida login qiladi va\n"
"    o'tkazmalarni qo'lda ko'rib chiqadi.\n"
"  - Xato bo'lgan yozuvlar har bir portalda alohida joylashgan,\n"
"    xato sabablari turli formatda yoziladi.\n"
"  - Mijozga javob berish uchun operator har bir portalga qaraydi -\n"
"    bu vaqt oladi va xatolarga olib keladi.\n"
"  - 'Qaysi partnyorda qancha xato bor, qaysi sababdan ko'p?' degan\n"
"    savolga tezda javob bera olmaydi.")

add_h2("Yechim")
add_pre(
"Yangi tizim:\n"
"  - 3-4 ta partnyordan kelgan o'tkazmalarni yagona bazada to'playdi.\n"
"  - Bek-ofis operatoriga 1 ta dashboardda hammasini ko'rish imkonini\n"
"    beradi.\n"
"  - Xatolarni alohida 'Xatolar paneli' ekranida toifa bo'yicha\n"
"    ko'rsatadi: KYC_FAIL, INSUFFICIENT_FUNDS, TIMEOUT va h.k.\n"
"  - Filtr va qidiruv: partnyor, status, sana, payment_ref, MTCN,\n"
"    telefon, F.I.Sh.\n"
"  - Excel eksport - kunlik yoki oraliq hisobot uchun.")

# --- 3. Foydalanuvchilar ---
add_h1("3. Tizim foydalanuvchilari va rollari")
add_pre(
"+----------+--------------------------+----------------------------+\n"
"| Rol      | Kim                      | Asosiy harakatlar          |\n"
"+----------+--------------------------+----------------------------+\n"
"| operator | Bek-ofis xodimi          | Tranzaksiyalar ro'yxati,   |\n"
"|          | (asosiy aktor)           | filtr, qidiruv, tafsilot,  |\n"
"|          |                          | xatolar paneli, eksport.   |\n"
"|          |                          |                            |\n"
"| admin    | IT/bek-ofis administra-  | Foydalanuvchilarni va      |\n"
"|          | tori                     | partnyorlarni boshqarish.  |\n"
"+----------+--------------------------+----------------------------+")
add_para("Tizim faqat bank ichida ishlaydi. Partnyorlar va mijozlar uchun "
         "tashqi kirish nazarda tutilmagan.")

# --- 4. Use-case ---
add_h1("4. Foydalanuvchi senariylari (use-case)")

add_h2("UC-1. Kunlik tranzaksiya kuzatuvi")
add_pre(
"Aktor: operator\n"
"Boshlanish: ish kuni boshida (08:30).\n"
"Qadamlar:\n"
"  1. Tizimga kiradi (login + parol).\n"
"  2. 'Tranzaksiyalar' ekrani avtomatik ochiladi - bugungi yozuvlar.\n"
"  3. Partnyor yoki status bo'yicha filtr qo'yadi (kerak bo'lsa).\n"
"  4. Yangi yozuvlarni ko'rib chiqadi.\n"
"Natija: 4 ta portal o'rniga 1 ekrandan barcha o'tkazmalar ko'rinadi.\n"
"        Vaqt: ~10 daqiqa (avval ~1 soat).")

add_h2("UC-2. Xatolarni tahlil qilish")
add_pre(
"Aktor: operator\n"
"Boshlanish: dashboardda xato yozuvlar ko'rindi yoki mijoz qo'ng'iroq qildi.\n"
"Qadamlar:\n"
"  1. 'Xatolar paneli' bo'limini ochadi.\n"
"  2. Toifalar bo'yicha jadval ochiladi: qaysi partnyorda nechta\n"
"     KYC_FAIL, INSUFFICIENT_FUNDS, TIMEOUT va h.k.\n"
"  3. Toifa nomi yoki yacheykaga bosadi - shu kesimdagi xato\n"
"     yozuvlar ro'yxati ochiladi.\n"
"  4. Bitta yozuvga bosadi - to'liq tafsilot, partnyor xato matni.\n"
"  5. Mijozga javob beradi yoki tegishli bo'limga yo'naltiradi.\n"
"Natija: xato sababi 1 ekranda, partnyor portaliga kirish shart emas.")

add_h2("UC-3. Bitta o'tkazmani topish")
add_pre(
"Aktor: operator\n"
"Boshlanish: mijoz qo'ng'iroq qildi va o'tkazma raqamini aytdi.\n"
"Qadamlar:\n"
"  1. Yuqoridagi qidiruv qatoriga PaymentRef yoki MTCN kiritadi.\n"
"  2. Tegishli yozuv chiqadi.\n"
"  3. Tafsilot modalini ochib barcha maydonlarni ko'radi.\n"
"Natija: 4 ta portalda qidirish o'rniga 1 sekundda topiladi.")

# --- 5. Funksional talablar ---
add_h1("5. Funksional talablar")
add_pre(
"+----+-----------------------------------------------+--------------+\n"
"| #  | Funksiya                                      | Asosiy aktor |\n"
"+----+-----------------------------------------------+--------------+\n"
"| F1 | Yagona tranzaksiyalar ro'yxati (jadval)       | operator     |\n"
"| F2 | Filtr: partnyor, status, sana, valyuta        | operator     |\n"
"| F3 | Qidiruv: PaymentRef / MTCN / telefon / F.I.Sh | operator     |\n"
"| F4 | Tafsilot modali (bitta o'tkazma)              | operator     |\n"
"| F5 | Xatolar paneli (toifa x partnyor jadvali)     | operator     |\n"
"| F6 | Xato yozuvlar ro'yxati (filtrlangan)          | operator     |\n"
"| F7 | Excel eksport (kunlik / oraliq)               | operator     |\n"
"| F8 | Foydalanuvchi va partnyor boshqaruvi          | admin        |\n"
"+----+-----------------------------------------------+--------------+")
add_para("Eslatma: birinchi versiyada sverka motori, NBU 402 hisoboti, AML "
         "tahlili va to'liq audit jurnali kiritilmagan. Bular keyingi "
         "versiyalarda, kerak bo'lsa, qo'shiladi.")

# --- 6. Maydonlar ---
add_h1("6. O'tkazmaning ma'lumot maydonlari")
add_para("O'tkazma yozuvi quyidagi maydonlardan iborat. Maxfiy maydonlar "
         "(passport, telefon) ma'lumotlar bazasida shifrlanadi va UI'da "
         "maskalangan ko'rinishda chiqariladi.")
add_pre(
"+--------------------------+----------------------------------------------+\n"
"| Maydon                   | Tavsif                                       |\n"
"+--------------------------+----------------------------------------------+\n"
"| payment_ref              | Bizning ichki ID (UUID)                      |\n"
"| partner_id / partner_code| Partnyor (1, 2, 3, 4)                        |\n"
"| partner_txn_id           | Partnyordagi original ID                     |\n"
"| mtcn                     | Money Transfer Control Number (mavjud bo'lsa)|\n"
"| direction                | INCOMING / OUTGOING                          |\n"
"| status                   | created, sent, pending, paid, cancelled,     |\n"
"|                          | failed                                       |\n"
"| send_currency / amount   | Jo'natilgan valyuta va summa                 |\n"
"| recv_currency / amount   | Qabul qilingan valyuta va summa              |\n"
"| amount_uzs               | UZSga ekvivalenti                            |\n"
"| sender_full_name         | Jo'natuvchining F.I.Sh                       |\n"
"| sender_phone             | Jo'natuvchi telefoni (shifrlanadi)           |\n"
"| sender_country           | Jo'natuvchi davlati (ISO kod)                |\n"
"| receiver_full_name       | Qabul qiluvchi F.I.Sh                        |\n"
"| receiver_phone           | Qabul qiluvchi telefoni (shifrlanadi)        |\n"
"| receiver_country         | Qabul qiluvchi davlati                       |\n"
"| error_category           | Ichki toifa - 7-bo'limda batafsil            |\n"
"| error_code               | Partnyor xato kodi (asl)                     |\n"
"| error_message            | Partnyor xato matni                          |\n"
"| sent_at                  | O'tkazma jo'natilgan vaqt                    |\n"
"| paid_at                  | Qabul qilingan vaqt                          |\n"
"| created_at               | Bizning bazaga kirib kelgan vaqt             |\n"
"+--------------------------+----------------------------------------------+")

# --- 7. Xato toifalari ---
add_h1("7. Xato toifalari va xatolar paneli")
add_para("Har bir partnyorning o'z xato kodi va xato matni bor. Tizim "
         "ularni yagona ichki toifaga moslab oladi - operator faqat "
         "toifa bo'yicha ishlaydi.")

add_h2("7.1. Xato toifalari ro'yxati")
add_pre(
"+----------------------+-------------------------------------------------+\n"
"| Ichki toifa          | Tavsif va misol                                 |\n"
"+----------------------+-------------------------------------------------+\n"
"| KYC_FAIL             | Mijoz hujjati notog'ri / muddati o'tgan         |\n"
"| INSUFFICIENT_FUNDS   | Mablag' yetmadi                                 |\n"
"| BENEFICIARY_NOT_FOUND| Qabul qiluvchi topilmadi yoki MTCN yaroqsiz     |\n"
"| LIMIT_EXCEEDED       | Kunlik yoki oylik limit oshib ketdi             |\n"
"| TIMEOUT              | Texnik xato, partnyor javobi yo'q yoki kech     |\n"
"| CANCELLED_BY_SENDER  | Jo'natuvchi bekor qildi                         |\n"
"| OTHER                | Boshqa (asl matn saqlanadi)                     |\n"
"+----------------------+-------------------------------------------------+")
add_para("Yangi toifalar zarurat tug'ilsa qo'shiladi. Toifaga tushmagan "
         "barcha xatolar OTHER ga yoziladi - keyinchalik tahlil qilinib, "
         "yangi toifa qo'shilishi mumkin.")

add_h2("7.2. Xatolar paneli ko'rinishi (F5)")
add_para("Yuqorida - sana oraligi va partnyor filtri. O'rtada - toifa x "
         "partnyor jadvali. Yacheykaga bosilsa - shu kesimdagi xato "
         "yozuvlar ro'yxati pastda ochiladi.")
add_pre(
"+--------------+------+------+------+------+--------+--------+\n"
"| Toifa        | P1   | P2   | P3   | P4   | Jami   | %      |\n"
"+--------------+------+------+------+------+--------+--------+\n"
"| KYC_FAIL     |  12  |   4  |   8  |   1  |   25   |  31 %  |\n"
"| INSUF_FUNDS  |   3  |   6  |   2  |   0  |   11   |  14 %  |\n"
"| BENEFICIARY  |   2  |   1  |   5  |   0  |    8   |  10 %  |\n"
"| LIMIT_EXCD   |   1  |   0  |   2  |   0  |    3   |   4 %  |\n"
"| TIMEOUT      |   7  |  11  |   4  |   2  |   24   |  30 %  |\n"
"| CANCELLED    |   2  |   1  |   1  |   0  |    4   |   5 %  |\n"
"| OTHER        |   1  |   2  |   2  |   1  |    6   |   8 %  |\n"
"+--------------+------+------+------+------+--------+--------+\n"
"  Sana oraligi: 01.06.2026 - 14.06.2026\n"
"  Jami xatolar: 81 ta\n"
"  Toifa nomiga bosilsa - shu toifadagi barcha xato yozuvlar.\n"
"  Yacheykaga bosilsa - shu partnyor x toifa kesimidagi yozuvlar.")

# --- 8. Arxitektura ---
add_h1("8. Tizim arxitekturasi")
add_pre(
"  Partnyor manbalari (3-4 ta)\n"
"  ============================\n"
"  - API/Webhook (qaerda mavjud bo'lsa)\n"
"  - Yarim avtomatik: SFTP / pochta orqali kunlik fayl\n"
"  - Qo'lda: operator UI orqali yuklash\n"
"            |\n"
"            v\n"
"  +-------------------------------+\n"
"  | Import qatlami                |  (.NET 10 background services)\n"
"  | - Partnyor 1 adapter          |\n"
"  | - Partnyor 2 adapter          |\n"
"  | - Partnyor 3 adapter          |\n"
"  | - Partnyor 4 adapter          |\n"
"  | -> yagona ichki Payment model |\n"
"  +-------------+-----------------+\n"
"                |\n"
"                v\n"
"  +-------------------------------+         +-------------------------+\n"
"  | Domain qatlami                | <-----> | PostgreSQL              |\n"
"  | - ErrorNormalizer             |         |  partners, payments,    |\n"
"  | - StatsService                |         |  users, roles           |\n"
"  | - ExportService (Excel)       |         +-------------------------+\n"
"  +-------------+-----------------+\n"
"                |\n"
"                v\n"
"  +-------------------------------+\n"
"  | API qatlami (.NET 10 Web API) |  JWT autentifikatsiya, RBAC\n"
"  +-------------+-----------------+\n"
"                |\n"
"                v\n"
"  +-------------------------------+\n"
"  | Vue 3 SPA (operator)          |  Tranzaksiyalar, xatolar paneli\n"
"  +-------------------------------+")

# --- 9. Database ---
add_h1("9. Ma'lumotlar bazasi (PostgreSQL)")
add_para("Tizim 4 ta jadvaldan iborat. Maxfiy maydonlar (passport, telefon) "
         "AES-256 bilan shifrlanadi.")
add_code(
"CREATE TABLE roles (\n"
"    id SERIAL PRIMARY KEY,\n"
"    name VARCHAR(40) UNIQUE NOT NULL\n"
"      -- 'operator', 'admin'\n"
");\n\n"
"CREATE TABLE users (\n"
"    id SERIAL PRIMARY KEY,\n"
"    login VARCHAR(100) UNIQUE NOT NULL,\n"
"    password_hash VARCHAR(255) NOT NULL,\n"
"    full_name VARCHAR(150),\n"
"    role_id INT NOT NULL REFERENCES roles(id),\n"
"    is_active BOOLEAN DEFAULT true,\n"
"    created_at TIMESTAMP DEFAULT now()\n"
");\n\n"
"CREATE TABLE partners (\n"
"    id SERIAL PRIMARY KEY,\n"
"    code VARCHAR(20) UNIQUE NOT NULL,\n"
"    name VARCHAR(100) NOT NULL,\n"
"    is_active BOOLEAN DEFAULT true\n"
");")

add_code(
"CREATE TABLE payments (\n"
"    id BIGSERIAL PRIMARY KEY,\n"
"    payment_ref      VARCHAR(64) UNIQUE NOT NULL,\n"
"    partner_id       INT NOT NULL REFERENCES partners(id),\n"
"    partner_txn_id   VARCHAR(100),\n"
"    mtcn             VARCHAR(40),\n"
"    direction        VARCHAR(10) NOT NULL,   -- INCOMING/OUTGOING\n"
"    status           VARCHAR(20) NOT NULL,\n"
"    -- summa va valyuta\n"
"    send_currency    CHAR(3),  send_amount    NUMERIC(18,2),\n"
"    recv_currency    CHAR(3),  recv_amount    NUMERIC(18,2),\n"
"    amount_uzs       NUMERIC(18,2),\n"
"    -- jo'natuvchi va qabul qiluvchi\n"
"    sender_full_name VARCHAR(200),\n"
"    sender_phone     VARCHAR(20),\n"
"    sender_country   CHAR(2),\n"
"    receiver_full_name VARCHAR(200),\n"
"    receiver_phone     VARCHAR(20),\n"
"    receiver_country   CHAR(2),\n"
"    -- xato\n"
"    error_category   VARCHAR(40),\n"
"    error_code       VARCHAR(50),\n"
"    error_message    TEXT,\n"
"    -- vaqt\n"
"    sent_at          TIMESTAMP,\n"
"    paid_at          TIMESTAMP,\n"
"    created_at       TIMESTAMP DEFAULT now(),\n"
"    updated_at       TIMESTAMP DEFAULT now()\n"
");\n\n"
"CREATE INDEX ix_payments_partner   ON payments(partner_id);\n"
"CREATE INDEX ix_payments_status    ON payments(status);\n"
"CREATE INDEX ix_payments_sent_at   ON payments(sent_at);\n"
"CREATE INDEX ix_payments_error_cat ON payments(error_category);")

# --- 10. Backend ---
add_h1("10. Backend modellar (.NET 10)")
add_para("Loyiha tuzilishi:")
add_pre(
"PartnerPayments.Api/\n"
" |- Domain/\n"
" |   |- Entities/   (Payment, Partner, User, Role)\n"
" |   |- Enums/      (Direction, PaymentStatus, ErrorCategory)\n"
" |   |- Services/   (ImportService, ErrorNormalizer,\n"
" |                   StatsService, ExportService)\n"
" |- Infrastructure/\n"
" |   |- Persistence/    (AppDbContext, EF Core configs)\n"
" |   |- Adapters/       (Partner1Adapter, Partner2Adapter,\n"
" |                       Partner3Adapter, Partner4Adapter)\n"
" |- Application/\n"
" |   |- Dtos/, Queries/, Commands/\n"
" |- Api/\n"
" |   |- Controllers/    (PaymentsController, ErrorsController,\n"
" |                       AuthController, AdminController)\n"
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
"    public string? SendCurrency { get; set; }\n"
"    public decimal? SendAmount { get; set; }\n"
"    public string? RecvCurrency { get; set; }\n"
"    public decimal? RecvAmount { get; set; }\n"
"    public decimal? AmountUzs { get; set; }\n\n"
"    // PII (shifrlanadi)\n"
"    public string? SenderFullName { get; set; }\n"
"    public string? SenderPhone { get; set; }\n"
"    public string? SenderCountry { get; set; }\n"
"    public string? ReceiverFullName { get; set; }\n"
"    public string? ReceiverPhone { get; set; }\n"
"    public string? ReceiverCountry { get; set; }\n\n"
"    public ErrorCategory? ErrorCategory { get; set; }\n"
"    public string? ErrorCode { get; set; }\n"
"    public string? ErrorMessage { get; set; }\n\n"
"    public DateTime? SentAt { get; set; }\n"
"    public DateTime? PaidAt { get; set; }\n"
"    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;\n"
"    public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;\n"
"}")

add_h3("Enumlar")
add_code(
"public enum Direction { Incoming, Outgoing }\n\n"
"public enum PaymentStatus {\n"
"    Created, Sent, Pending, Paid, Cancelled, Failed\n"
"}\n\n"
"public enum ErrorCategory {\n"
"    KYC_FAIL, INSUFFICIENT_FUNDS, BENEFICIARY_NOT_FOUND,\n"
"    LIMIT_EXCEEDED, TIMEOUT, CANCELLED_BY_SENDER, OTHER\n"
"}")

# --- 11. API ---
add_h1("11. API endpointlar")
add_pre(
"+--------+------------------------------------+----------------------+\n"
"| Metod  | URL                                | Rol(lar)             |\n"
"+--------+------------------------------------+----------------------+\n"
"| POST   | /api/auth/login                    | hammasi              |\n"
"| GET    | /api/payments                      | operator             |\n"
"|        |   ?partner=&status=&from=&to=&q=   |                      |\n"
"|        |   &error_cat=&page=&limit=         |                      |\n"
"| GET    | /api/payments/{id}                 | operator             |\n"
"| GET    | /api/payments/export.xlsx          | operator             |\n"
"|        |   ?partner=&status=&from=&to=      |                      |\n"
"| GET    | /api/errors/stats                  | operator             |\n"
"|        |   ?from=&to=&partner=              |                      |\n"
"| GET    | /api/partners                      | operator, admin      |\n"
"| GET    | /api/admin/users                   | admin                |\n"
"| POST   | /api/admin/users                   | admin                |\n"
"| PUT    | /api/admin/partners/{id}           | admin                |\n"
"+--------+------------------------------------+----------------------+")

add_h3("GET /api/errors/stats javobi (namuna)")
add_code(
'{\n'
'  "from": "2026-06-01",\n'
'  "to":   "2026-06-14",\n'
'  "total": 81,\n'
'  "by_category": [\n'
'    {\n'
'      "category": "KYC_FAIL",\n'
'      "count": 25,\n'
'      "by_partner": { "P1": 12, "P2": 4, "P3": 8, "P4": 1 }\n'
'    },\n'
'    {\n'
'      "category": "TIMEOUT",\n'
'      "count": 24,\n'
'      "by_partner": { "P1": 7, "P2": 11, "P3": 4, "P4": 2 }\n'
'    }\n'
'    /* ... qolgan toifalar ... */\n'
'  ]\n'
'}')

# --- 12. Frontend ---
add_h1("12. Frontend ekranlar (Vue 3)")
add_para("SPA, Composition API, Pinia + Vue Router. UI kutubxonasi: "
         "Element Plus.")
add_pre(
"frontend/src/views/\n"
"  LoginView.vue\n"
"  PaymentsView.vue          (F1, F2, F3 - asosiy ish ekrani)\n"
"  PaymentDetailModal.vue    (F4 - tafsilot)\n"
"  ErrorsDashboardView.vue   (F5, F6 - xatolar paneli)\n"
"  AdminView.vue             (F8 - admin uchun)")

add_h3("Asosiy ekranlar")
add_bullet("LoginView: login va parol; muvaffaqiyatdan keyin /payments ga "
           "yo'naltiradi.")
add_bullet("PaymentsView: jadval. Ustunlar - sana, partnyor, status, "
           "yo'nalish, summa va valyuta, mijoz F.I.Sh, error_category. "
           "Yuqorida filtr va qidiruv qatori, sahifalash (pagination).")
add_bullet("PaymentDetailModal: barcha maydonlar; partnyor xato matni; "
           "passport va telefon maskalangan ko'rinishda.")
add_bullet("ErrorsDashboardView: yuqorida toifa x partnyor jadvali "
           "(7-bo'limdagidek); pastda - tanlangan kesim bo'yicha xato "
           "yozuvlar ro'yxati.")
add_bullet("AdminView: foydalanuvchilar va partnyorlarni boshqarish (CRUD).")

# --- 13. Xavfsizlik ---
add_h1("13. Xavfsizlik va kirish nazorati")
add_bullet("RBAC - har bir endpoint rol bilan himoyalangan; tekshiruv "
           "serverda bajariladi.")
add_bullet("Parol BCrypt hash bilan saqlanadi, JWT amal qilish muddati "
           "8 soat.")
add_bullet("PII (passport, telefon) ma'lumotlar bazasida AES-256 bilan "
           "shifrlanadi (kalit Vault yoki AWS KMS'da).")
add_bullet("Modal'da telefon va passport maskalangan; to'liq qiymat "
           "rolga bog'liq holda ko'rinadi.")
add_bullet("CORS faqat ichki domenga ochiq, HTTPS majburiy.")
add_bullet("Login va eksport harakatlari logga yoziladi (oddiy log fayl).")

# --- 14. Reja va ishga tushirish ---
add_h1("14. Bajarilish rejasi va ishga tushirish")

add_h2("14.1. Sprintlar bo'yicha reja")
add_pre(
"Sprint 1 (skelet, 1 hafta):\n"
"  - .NET 10 va Vue 3 skeletlari, JWT, RBAC.\n"
"  - DB migratsiyalari (partners, users, roles, payments).\n"
"  - Login va admin: foydalanuvchilar va partnyorlarni boshqarish.\n"
"  - 1 ta partnyor adapteri + import (test ma'lumotlar).\n"
"\nSprint 2 (asosiy ko'rish, 1 hafta):\n"
"  - F1 - tranzaksiyalar ro'yxati (jadval, sahifalash).\n"
"  - F2, F3 - filtr va qidiruv.\n"
"  - F4 - tafsilot modali.\n"
"  - F7 - Excel eksport.\n"
"\nSprint 3 (xatolar paneli, 1 hafta):\n"
"  - F5 - xatolar paneli (toifa x partnyor jadvali).\n"
"  - F6 - tanlangan kesim bo'yicha xato yozuvlar ro'yxati.\n"
"  - ErrorNormalizer servisi.\n"
"  - Qolgan partnyor adapterlari (3-4 ta jami).\n"
"\nSprint 4 (sayqal va qabul, 1 hafta):\n"
"  - PII shifrlash, real ma'lumotlar bilan sinov.\n"
"  - Xavfsizlik tekshiruvi (CORS, JWT, RBAC).\n"
"  - Foydalanuvchi qabuli (UAT), boshliq tomonidan qabul.\n"
"\nUmumiy taxminiy muddat: 4 hafta.")

add_h2("14.2. Backend (.NET 10)")
add_code(
"dotnet new webapi -n PartnerPayments.Api\n"
"cd PartnerPayments.Api\n"
"dotnet add package Microsoft.EntityFrameworkCore\n"
"dotnet add package Npgsql.EntityFrameworkCore.PostgreSQL\n"
"dotnet add package Microsoft.AspNetCore.Authentication.JwtBearer\n"
"dotnet add package BCrypt.Net-Next\n"
"dotnet add package ClosedXML        # Excel eksport\n\n"
"dotnet ef migrations add Init\n"
"dotnet ef database update\n"
"dotnet run")

add_h2("14.3. Frontend (Vue 3)")
add_code(
"npm create vite@latest frontend -- --template vue\n"
"cd frontend\n"
"npm install axios pinia vue-router element-plus\n"
"npm run dev   # http://localhost:5173")

add_h2("14.4. appsettings.json (namuna)")
add_code(
"{\n"
"  \"ConnectionStrings\": {\n"
"    \"Default\": \"Host=localhost;Port=5432;Database=partner_payments;\"\n"
"               + \"Username=postgres;Password=postgres\"\n"
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
