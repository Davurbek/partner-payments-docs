# Partnyor o'tkazmalarini ko'rsatish tizimi

Partnyorlar (Payme, Click, Uzum va boshqalar) orqali amalga oshirilgan pul
o'tkazmalarini foydalanuvchilarga **rol asosida** ko'rsatuvchi tizimning
texnik hujjati (TZ).

Bu repozitoriya — **hujjat repozitoriyasi**: tizimning to'liq texnik
topshirig'i, ma'lumotlar bazasi sxemasi, modellar va kod namunalarini
o'z ichiga oladi.

## Loyiha haqida

- Foydalanuvchi login/parol bilan kiradi.
- Roliga qarab kerakli partnyor o'tkazmalari **jadval** ko'rinishida chiqadi.
- Qatorga bosilganda **modal** ochilib, o'tkazmaning to'liq tafsilotlari
  (jo'natuvchi/qabul qiluvchi passport, karta, summa, kurs, komissiya, xato)
  ko'rinadi.

## Texnologiyalar

| Qatlam | Texnologiya |
|--------|-------------|
| Backend | .NET 10 (ASP.NET Core Web API) |
| ORM | Entity Framework Core |
| Ma'lumotlar bazasi | PostgreSQL |
| Autentifikatsiya | JWT + BCrypt |
| Frontend | Vue 3 (Composition API) + Vite |
| State / Routing | Pinia + Vue Router |

## Repozitoriya tarkibi

| Fayl | Tavsif |
|------|--------|
| `Texnik_Hujjat.pdf` | Asosiy texnik hujjat (14 sahifa) |
| `TEXNIK_TOPSHIRIQ.md` | TZ ning markdown versiyasi |
| `build_pdf.py` | PDF'ni qayta yaratuvchi Python skript |

## Hujjatni ko'rish

Asosiy hujjatni [`Texnik_Hujjat.pdf`](Texnik_Hujjat.pdf) faylidan oching.
Ichida: tizim arxitekturasi, rollar, SQL baza sxemasi, C# modellar va
kontrollerlar, Vue 3 komponentlari, xavfsizlik talablari va ishga tushirish
bosqichlari bor.

## PDF'ni qayta yaratish

Hujjat matni o'zgarsa, PDF'ni qayta yaratish uchun (tashqi kutubxona
talab qilinmaydi, faqat Python):

```bash
python3 build_pdf.py
```

## Rollar

| Rol | Ko'radigan ma'lumot |
|-----|---------------------|
| `admin` | Barcha partnyorlar o'tkazmalari |
| `partner` | Faqat o'ziga biriktirilgan partnyor |

## Holat

- [x] Texnik topshiriq (TZ) — tayyor
- [ ] Backend (.NET 10 API) — rejalashtirilgan
- [ ] Frontend (Vue 3) — rejalashtirilgan
