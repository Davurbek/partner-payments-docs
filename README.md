# Xalqaro pul o'tkazmalari - birlashtirilgan monitoring va sverka tizimi

Kommertsiya banki bek-ofisi uchun ichki tizim. Maqsad: 8 ta xalqaro pul
o'tkazma tizimidan (Western Union, MoneyGram, KoronaPay, Unistream, Contact,
Ria, Zolotaya Korona, Asia Express) keladigan o'tkazmalarni yagona bazada
to'plash va sverka, xato tahlili, NBU/audit hisobotlarini bitta interfeysda
bajarish.

## Hal qilinadigan muammolar

| # | Muammo | Yechim |
|---|--------|--------|
| M1 | Kunlik sverka qo'lda - 8 partnyor x 1-2 soat | Avtomatik moslash, farqlar ro'yxati, sverka akti (PDF) |
| M2 | Xato o'tkazmalar har bir partnyor portalida alohida | Yagona dashboard, me'yorlashtirilgan xato toifalari |
| M3 | NBU/audit uchun tarix yo'q (30-90 kun) | 7 yil saqlash, audit_log, NBU 402 hisobotlari |

## Asosiy foydalanuvchi

Bek-ofis sverka xodimi. Qo'shimcha rollar: compliance/AML, auditor, admin.

## Texnologiyalar

| Qatlam | Texnologiya |
|--------|-------------|
| Backend | .NET 10 (ASP.NET Core Web API) |
| ORM | Entity Framework Core |
| Ma'lumotlar bazasi | PostgreSQL |
| Autentifikatsiya | JWT + BCrypt + RBAC |
| PII shifrlash | AES-256 (kalit Vault/KMS'da) |
| Frontend | Vue 3 (Composition API) + Vite + Pinia |
| Hisobot | ClosedXML (Excel), QuestPDF (PDF) |

## Asosiy funksiyalar

- F1-F4: yagona o'tkazmalar ro'yxati, filtr, qidiruv (PaymentRef/MTCN/passport), modal
- F5-F7: partnyor faylini yuklash, avtomatik moslash, sverka akti
- F8: xato statistikasi (toifa x partnyor)
- F9: audit jurnali
- F10: NBU forma 402 va AML hisobotlari
- F11: foydalanuvchi va partnyor boshqaruvi (admin)

## Repozitoriya tarkibi

| Fayl | Tavsif |
|------|--------|
| `Texnik_Hujjat.pdf` | To'liq texnik hujjat (15 sahifa) |
| `build_pdf.py` | PDF generator (Python, tashqi kutubxonasiz) |

## Hujjatni ko'rish

[`Texnik_Hujjat.pdf`](Texnik_Hujjat.pdf) faylini oching. Ichida:

1. Loyihaning maqsadi
2. Hal qilinadigan muammolar (M1, M2, M3)
3. Tizim foydalanuvchilari va rollari
4. Foydalanuvchi senariylari (use-case)
5. Funksional talablar (F1-F11, har biri qaysi muammoni yechishi)
6. Xalqaro o'tkazmaning ma'lumot maydonlari (MTCN, korridor, valyuta jufti...)
7. Sverka oqimi
8. Xato o'tkazmalar (me'yorlashtirilgan toifalar)
9. Audit jurnali va NBU hisoboti
10. Tizim arxitekturasi
11. Ma'lumotlar bazasi (SQL)
12. .NET 10 modellar
13. API endpointlar
14. Vue 3 frontend tuzilishi
15. Xavfsizlik
16. Bajarilish ketma-ketligi (5 sprint, 9-11 hafta)
17. Loyihani ishga tushirish

## PDF'ni qayta yaratish

Hujjat matni o'zgarsa:

```bash
python3 build_pdf.py
```

Tashqi kutubxona talab qilinmaydi (faqat standart Python).

## Rejalashtirilgan reja (qisqacha)

- Sprint 1 (2 hafta): yadro, JWT, RBAC, asosiy DB
- Sprint 2 (2 hafta): yagona ro'yxat, filtr, qidiruv, modal -> M2 qisman yopiladi
- Sprint 3 (2-3 hafta): partnyor adapterlari, sverka engine -> M1 yopiladi
- Sprint 4 (2 hafta): xato statistikasi, NBU 402, audit -> M2 va M3 yopiladi
- Sprint 5 (1-2 hafta): qolgan partnyorlar, PII shifrlash, sanksiya, sinash

## Holat

- [x] Texnik topshiriq (TZ) - tayyor
- [ ] Backend (.NET 10 API) - rejada
- [ ] Frontend (Vue 3) - rejada
