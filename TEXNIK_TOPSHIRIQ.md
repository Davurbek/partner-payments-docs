# Texnik Topshiriq (TZ): Partnyor o'tkazmalarini ko'rsatish tizimi

## 1. Loyiha haqida qisqacha

Tizimning vazifasi — partnyorlar (Payme, Click, Uzum va h.k.) orqali amalga
oshirilgan pul o'tkazmalarini foydalanuvchilarga ko'rsatish. Ma'lumotlar
tayyor bazada saqlanadi; tizim ularni **o'qib, rol asosida filtrlab,
jadval va modal ko'rinishida** ko'rsatadi.

Asosiy talablar:
1. Foydalanuvchi **login/parol** bilan kiradi.
2. Foydalanuvchiga berilgan **rol** orqali faqat kerakli partnyor
   ma'lumotlari ko'rsatiladi.
3. O'tkazmalar **jadval** ko'rinishida chiqadi.
4. Qatorga bosilganda **modal** ochilib, o'tkazmaning to'liq tafsilotlari
   ko'rsatiladi.

---

## 2. Foydalanuvchi rollari va kirish (autentifikatsiya)

| Rol | Tavsif | Ko'radigan ma'lumot |
|-----|--------|---------------------|
| `admin` | Tizim administratori | Barcha partnyorlarning o'tkazmalari |
| `partner` | Partnyor xodimi | Faqat o'ziga biriktirilgan partnyor o'tkazmalari |

Kirish jarayoni:
1. Foydalanuvchi login va parolni yuboradi.
2. Server parolni tekshiradi (parol **hash** ko'rinishida saqlanadi — bcrypt).
3. Muvaffaqiyatli bo'lsa **JWT token** beriladi (ichida `user_id`, `role`,
   `partner_id`).
4. Keyingi har bir so'rovda token tekshiriladi va rol bo'yicha ma'lumot
   filtrlanadi.

> Xavfsizlik: `partner` roli SQL so'rovda **majburiy** `partner_id` bo'yicha
> cheklanadi. Foydalanuvchi boshqa partnyor ma'lumotini hech qachon ko'ra
> olmaydi (token ichidagi `partner_id` ishlatiladi, frontenddan kelgan
> qiymatga ishonilmaydi).

---

## 3. Funksional talablar

### 3.1. O'tkazmalar ro'yxati (jadval)

Jadvalda quyidagi ustunlar ko'rsatiladi:

| Ustun (ekranda) | Manba maydoni | Izoh |
|-----------------|---------------|------|
| To'lov identifikatori | `payment_ref` | PaymentRef |
| O'tkazma qatnashchilari | `sender_full_name` → `receiver_full_name` | Jo'natuvchi va qabul qiluvchi |
| O'tkazma holati | `status` | success / pending / failed |
| O'tkazma sanasi | `transfer_date` | Sana va vaqt |
| O'tkazma summasi (so'mda) | `amount_uzs` | So'mda formatlanadi (150 000 so'm) |

Qo'shimcha imkoniyatlar:
- Sahifalash (pagination)
- Sana oralig'i, holat va PaymentRef bo'yicha filtr/qidiruv
- Holatni rang bilan ajratish (success = yashil, pending = sariq, failed = qizil)

### 3.2. O'tkazma tafsilotlari (modal)

Jadval qatoriga bosilganda modal ochiladi va quyidagilar ko'rsatiladi:

**Jo'natuvchi:**
- F.I.Sh.
- Passport ma'lumotlari (seriya + raqam)
- Karta raqami (maskalangan, masalan `8600 **** **** 1234`)

**Qabul qiluvchi:**
- F.I.Sh.
- Passport ma'lumotlari (seriya + raqam)
- Karta raqami (maskalangan)

**Summa tafsilotlari:**
- O'tkazilgan summa (asl valyutada)
- So'mga o'girilgan summa
- Dollar kursi
- Komissiya

**Xato (agar mavjud bo'lsa):**
- Xato kodi va xato matni qizil rangda ko'rsatiladi.

---

## 4. Ma'lumotlar bazasi dizayni

### 4.1. ER diagramma (bog'lanishlar)

```
  roles 1 ───< users >─── ? partners 1 ───< payments
                              (partner_id)   (partner_id)

  - roles    (1) ──< (N) users        : bir rolga ko'p foydalanuvchi
  - partners (1) ──< (N) users        : bir partnyorga ko'p xodim
  - partners (1) ──< (N) payments     : bir partnyorga ko'p o'tkazma
```

### 4.2. SQL sxema (PostgreSQL)

```sql
-- Rollar
CREATE TABLE roles (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(50) UNIQUE NOT NULL,   -- 'admin', 'partner'
    description VARCHAR(255),
    created_at  TIMESTAMP DEFAULT now()
);

-- Partnyorlar
CREATE TABLE partners (
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    code       VARCHAR(50) UNIQUE NOT NULL,    -- payme, click, uzum ...
    is_active  BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);

-- Foydalanuvchilar
CREATE TABLE users (
    id            SERIAL PRIMARY KEY,
    login         VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name     VARCHAR(150),
    role_id       INT NOT NULL REFERENCES roles(id),
    partner_id    INT REFERENCES partners(id),  -- admin uchun NULL
    is_active     BOOLEAN DEFAULT true,
    created_at    TIMESTAMP DEFAULT now(),
    updated_at    TIMESTAMP DEFAULT now()
);

-- O'tkazmalar (asosiy jadval)
CREATE TABLE payments (
    id            BIGSERIAL PRIMARY KEY,
    payment_ref   VARCHAR(100) UNIQUE NOT NULL,   -- To'lov identifikatori
    partner_id    INT NOT NULL REFERENCES partners(id),
    status        VARCHAR(30) NOT NULL,           -- success, pending, failed
    transfer_date TIMESTAMP NOT NULL,             -- O'tkazma sanasi
    amount_uzs    NUMERIC(18,2) NOT NULL,         -- Summa (so'mda)

    -- Jo'natuvchi
    sender_full_name       VARCHAR(200),
    sender_passport_series VARCHAR(10),
    sender_passport_number VARCHAR(20),
    sender_card_number     VARCHAR(25),

    -- Qabul qiluvchi
    receiver_full_name       VARCHAR(200),
    receiver_passport_series VARCHAR(10),
    receiver_passport_number VARCHAR(20),
    receiver_card_number     VARCHAR(25),

    -- Summa tafsilotlari
    amount_original   NUMERIC(18,2),   -- o'tkazilgan summa (asl valyuta)
    original_currency VARCHAR(3),      -- USD, RUB ...
    usd_rate          NUMERIC(12,4),   -- dollar kursi
    commission        NUMERIC(18,2),   -- komissiya

    -- Xato
    error_code    VARCHAR(50),
    error_message TEXT,

    created_at TIMESTAMP DEFAULT now()
);

-- Indekslar (tezkor qidiruv uchun)
CREATE INDEX idx_payments_partner ON payments(partner_id);
CREATE INDEX idx_payments_date    ON payments(transfer_date);
CREATE INDEX idx_payments_status  ON payments(status);
CREATE INDEX idx_payments_ref     ON payments(payment_ref);
```

> Eslatma: Agar o'tkazmalar bazasi allaqachon mavjud bo'lsa, `payments`
> jadvali maydonlarini real bazadagi ustun nomlariga moslang. Qolgan
> jadvallar (`roles`, `partners`, `users`) — yangi qo'shiladi.

---

## 5. Modellar (Entity ta'rifi)

### 5.1. User
| Maydon | Tur | Izoh |
|--------|-----|------|
| id | int | PK |
| login | string | unikal |
| password_hash | string | bcrypt hash |
| full_name | string | |
| role_id | int | FK → roles |
| partner_id | int? | FK → partners (admin'da NULL) |
| is_active | bool | |

### 5.2. Role
| Maydon | Tur | Izoh |
|--------|-----|------|
| id | int | PK |
| name | string | admin / partner |
| description | string | |

### 5.3. Partner
| Maydon | Tur | Izoh |
|--------|-----|------|
| id | int | PK |
| name | string | |
| code | string | unikal |
| is_active | bool | |

### 5.4. Payment
| Maydon | Tur | Izoh |
|--------|-----|------|
| id | bigint | PK |
| payment_ref | string | PaymentRef |
| partner_id | int | FK → partners |
| status | string | success/pending/failed |
| transfer_date | datetime | |
| amount_uzs | decimal | so'mdagi summa |
| sender_full_name | string | |
| sender_passport_series | string | |
| sender_passport_number | string | |
| sender_card_number | string | maskalanadi |
| receiver_full_name | string | |
| receiver_passport_series | string | |
| receiver_passport_number | string | |
| receiver_card_number | string | maskalanadi |
| amount_original | decimal | asl valyutadagi summa |
| original_currency | string | USD/RUB |
| usd_rate | decimal | dollar kursi |
| commission | decimal | komissiya |
| error_code | string? | |
| error_message | string? | |

---

## 6. API endpointlar

| Metod | URL | Rol | Tavsif |
|-------|-----|-----|--------|
| POST | `/api/auth/login` | hammasi | Login/parol → JWT token |
| GET | `/api/payments` | admin, partner | O'tkazmalar ro'yxati (filtr + pagination) |
| GET | `/api/payments/:id` | admin, partner | Bitta o'tkazma tafsiloti (modal) |
| GET | `/api/partners` | admin | Partnyorlar ro'yxati (filtr uchun) |

### 6.1. `GET /api/payments` — so'rov parametrlari
- `page`, `limit` — sahifalash
- `status` — holat bo'yicha filtr
- `date_from`, `date_to` — sana oralig'i
- `search` — PaymentRef yoki F.I.Sh. bo'yicha qidiruv

Javob namunasi:
```json
{
  "data": [
    {
      "id": 101,
      "payment_ref": "PR-2026-000101",
      "participants": "Aliyev A. → Valiyev V.",
      "status": "success",
      "transfer_date": "2026-06-11T14:30:00Z",
      "amount_uzs": 150000.00
    }
  ],
  "pagination": { "page": 1, "limit": 20, "total": 354 }
}
```

### 6.2. `GET /api/payments/:id` — modal uchun
```json
{
  "payment_ref": "PR-2026-000101",
  "status": "success",
  "transfer_date": "2026-06-11T14:30:00Z",
  "sender": {
    "full_name": "Aliyev Ali",
    "passport": "AA 1234567",
    "card_number": "8600 **** **** 1234"
  },
  "receiver": {
    "full_name": "Valiyev Vali",
    "passport": "AB 7654321",
    "card_number": "9860 **** **** 5678"
  },
  "amount": {
    "original": 12.50,
    "currency": "USD",
    "uzs": 150000.00,
    "usd_rate": 12000.00,
    "commission": 1500.00
  },
  "error": null
}
```

> Rol filtri: `partner` roli uchun server avtomatik `WHERE partner_id =
> {token.partner_id}` qo'shadi.

---

## 7. UI / UX

### 7.1. Login sahifasi
- Login va parol maydonlari, "Kirish" tugmasi.
- Xato bo'lsa: "Login yoki parol noto'g'ri".

### 7.2. O'tkazmalar jadvali sahifasi
- Yuqorida filtrlar (sana, holat, qidiruv).
- Jadval (5 ta ustun).
- Pastda sahifalash.
- Qatorga bosilsa → modal.

### 7.3. Modal
- Ikki ustun: chapda Jo'natuvchi, o'ngda Qabul qiluvchi.
- Pastda summa tafsilotlari.
- Xato bo'lsa qizil panelda ko'rsatiladi.

---

## 8. Bajarilish ketma-ketligi (bosqichlar)

| # | Bosqich | Natija |
|---|---------|--------|
| 1 | Loyiha skeleti (backend + frontend) | Ishchi muhit tayyor |
| 2 | DB migratsiyalari (`roles`, `partners`, `users`, `payments`) | Jadvallar yaratildi |
| 3 | Seed ma'lumot (1 admin, 1 partner, test o'tkazmalar) | Sinov uchun ma'lumot |
| 4 | Auth: `POST /login`, parol hash, JWT | Foydalanuvchi kira oladi |
| 5 | Rol middleware (token tekshirish + filtr) | Rol bo'yicha himoya |
| 6 | `GET /payments` (filtr, pagination, rol filtri) | Ro'yxat API tayyor |
| 7 | `GET /payments/:id` (modal ma'lumoti) | Tafsilot API tayyor |
| 8 | Frontend: login sahifasi | UI kirish |
| 9 | Frontend: o'tkazmalar jadvali | Ro'yxat ko'rinadi |
| 10 | Frontend: modal | Tafsilotlar ko'rinadi |
| 11 | Karta maskalash, xato ko'rsatish, format (so'm) | Yakuniy ko'rinish |
| 12 | Test va sozlash | Tayyor mahsulot |

---

## 9. Texnologiyalar (taklif)

| Qatlam | Texnologiya (taklif) |
|--------|----------------------|
| Backend | Node.js (Express/NestJS) yoki Laravel (PHP) |
| ORM | Sequelize/Prisma yoki Eloquent |
| Ma'lumotlar bazasi | PostgreSQL / MySQL |
| Auth | JWT + bcrypt |
| Frontend | React (yoki Vue) |
| UI kutubxona | Ant Design / MUI (jadval + modal tayyor) |

> Texnologiyalarni o'zingizning loyihangizga moslab tanlash mumkin.

---

## 10. Xavfsizlik talablari
1. Parollar faqat **hash** (bcrypt) ko'rinishida saqlanadi.
2. Karta raqamlari va passport ma'lumotlari **maskalanadi** (faqat
   ruxsati borlarga to'liq ko'rinadi).
3. Rol bo'yicha cheklov **serverda** amalga oshiriladi.
4. Barcha so'rovlar JWT token bilan himoyalanadi.
5. SQL injection oldini olish uchun parametrlangan so'rovlar ishlatiladi.
```
