# -*- coding: utf-8 -*-
"""
Texnik hujjatni PDF qilib chiqaruvchi skript (tashqi kutubxonasiz, faqat
standart Python). Monospace (Courier) shriftlardan foydalanadi -> matn,
jadval va kod bloklari aniq joylashadi, hech qanday tashqi shrift kerak emas.
"""

import textwrap
import datetime

PAGE_W, PAGE_H = 595.276, 841.890   # A4
ML, MR, MT, MB = 55, 50, 60, 55     # margins
CONTENT_W = PAGE_W - ML - MR

lines = []  # har bir element: matn yoki bo'sh joy yoki chiziq


def max_chars(size, extra_indent=0):
    return max(1, int((CONTENT_W - extra_indent) // (size * 0.6)))


def add_blank(h=6):
    lines.append({"blank": h})


def add_rule():
    lines.append({"rule": True})


def add_h1(text):
    add_blank(10)
    lines.append({"text": text, "font": "F2", "size": 15, "color": (0.10, 0.20, 0.50)})
    add_rule()
    add_blank(5)


def add_h2(text):
    add_blank(9)
    lines.append({"text": text, "font": "F2", "size": 12, "color": (0.14, 0.18, 0.42)})
    add_blank(4)


def add_h3(text):
    add_blank(5)
    lines.append({"text": text, "font": "F2", "size": 10.5, "color": (0.0, 0.0, 0.0)})
    add_blank(2)


def add_para(text, size=10):
    width = max_chars(size)
    for seg in (textwrap.wrap(text, width=width) or [""]):
        lines.append({"text": seg, "font": "F1", "size": size, "color": (0.0, 0.0, 0.0)})
    add_blank(4)


def add_bullet(text, size=10):
    width = max_chars(size, extra_indent=size * 0.6 * 2)
    wrapped = textwrap.wrap(text, width=width) or [""]
    for i, seg in enumerate(wrapped):
        prefix = "- " if i == 0 else "  "
        lines.append({"text": prefix + seg, "font": "F1", "size": size, "color": (0.0, 0.0, 0.0)})


def add_code(code, size=8.5):
    add_blank(3)
    for ln in code.split("\n"):
        lines.append({"text": ln, "font": "F1", "size": size, "color": (0.10, 0.10, 0.10), "code": True})
    add_blank(3)


def add_pre(block, size=8.5):
    add_blank(3)
    for ln in block.split("\n"):
        lines.append({"text": ln, "font": "F1", "size": size, "color": (0.0, 0.0, 0.0)})
    add_blank(3)


# ===================================================================
#  HUJJAT MAZMUNI
# ===================================================================

# --- Sarlavha (title) ---
add_blank(140)
lines.append({"text": "PARTNYOR O'TKAZMALARINI", "font": "F2", "size": 22,
              "color": (0.10, 0.20, 0.50), "center": True})
lines.append({"text": "KO'RSATISH TIZIMI", "font": "F2", "size": 22,
              "color": (0.10, 0.20, 0.50), "center": True})
add_blank(14)
lines.append({"text": "Texnik hujjat (TZ)", "font": "F2", "size": 14,
              "color": (0.3, 0.3, 0.3), "center": True})
add_blank(30)
lines.append({"text": "Backend: .NET 10 (ASP.NET Core Web API)", "font": "F1",
              "size": 11, "color": (0, 0, 0), "center": True})
lines.append({"text": "Frontend: Vue 3", "font": "F1", "size": 11,
              "color": (0, 0, 0), "center": True})
lines.append({"text": "Ma'lumotlar bazasi: PostgreSQL + EF Core", "font": "F1",
              "size": 11, "color": (0, 0, 0), "center": True})
add_blank(40)
lines.append({"text": "Sana: " + datetime.date.today().strftime("%d.%m.%Y"),
              "font": "F1", "size": 10, "color": (0.3, 0.3, 0.3), "center": True})
lines.append({"newpage": True})

# --- Mundarija ---
add_h1("Mundarija")
toc = [
    "1.  Loyiha haqida",
    "2.  Texnologiyalar steki",
    "3.  Tizim arxitekturasi",
    "4.  Rollar va autentifikatsiya",
    "5.  Funksional talablar (jadval va modal)",
    "6.  Ma'lumotlar bazasi (SQL)",
    "7.  Backend: .NET 10 modellar va EF Core",
    "8.  Backend: API endpointlar va JWT",
    "9.  Frontend: Vue 3 (struktura va komponentlar)",
    "10. Bajarilish ketma-ketligi",
    "11. Xavfsizlik talablari",
    "12. Loyihani ishga tushirish",
]
for t in toc:
    add_bullet(t, size=10.5)
lines.append({"newpage": True})

# --- 1. Loyiha haqida ---
add_h1("1. Loyiha haqida")
add_para("Tizimning vazifasi - partnyorlar (Payme, Click, Uzum va boshqalar) "
         "orqali amalga oshirilgan pul o'tkazmalarini foydalanuvchilarga "
         "ko'rsatish. O'tkazmalar tayyor bazada saqlanadi; tizim ularni o'qib, "
         "foydalanuvchining roli asosida filtrlab, jadval va modal ko'rinishida "
         "namoyish etadi.")
add_h3("Asosiy talablar")
add_bullet("Foydalanuvchi login va parol bilan tizimga kiradi.")
add_bullet("Foydalanuvchiga berilgan rol orqali faqat kerakli partnyor "
           "ma'lumotlari ko'rsatiladi.")
add_bullet("O'tkazmalar jadval ko'rinishida chiqadi (5 ta asosiy ustun).")
add_bullet("Jadval qatoriga bosilganda modal ochilib, o'tkazmaning to'liq "
           "tafsilotlari (passport, karta, summa, xato) ko'rsatiladi.")

# --- 2. Texnologiyalar ---
add_h1("2. Texnologiyalar steki")
add_pre(
"+-------------------+--------------------------------------------------+\n"
"| Qatlam            | Texnologiya                                      |\n"
"+-------------------+--------------------------------------------------+\n"
"| Backend           | .NET 10 - ASP.NET Core Web API (C#)              |\n"
"| ORM               | Entity Framework Core 10                         |\n"
"| Ma'lumotlar bazasi| PostgreSQL (Npgsql provayder)                    |\n"
"| Autentifikatsiya  | JWT Bearer + BCrypt (parol hash)                 |\n"
"| Frontend          | Vue 3 (Composition API) + Vite                   |\n"
"| HTTP klient       | Axios                                            |\n"
"| State (holat)     | Pinia                                            |\n"
"| Routing           | Vue Router                                       |\n"
"| UI kutubxona      | (taklif) Element Plus yoki PrimeVue              |\n"
"+-------------------+--------------------------------------------------+")

# --- 3. Arxitektura ---
add_h1("3. Tizim arxitekturasi")
add_para("Umumiy oqim: foydalanuvchi Vue 3 ilovasiga kiradi, .NET API'ga "
         "so'rov yuboradi, API JWT tokenni tekshirib, rol bo'yicha bazadan "
         "ma'lumotni filtrlab qaytaradi.")
add_pre(
"  +-------------------+          HTTPS / JSON          +------------------+\n"
"  |   Vue 3 (SPA)     |  ---------------------------->  |   .NET 10 API    |\n"
"  |  - Login sahifa   |   1. login -> JWT token        |  - AuthController |\n"
"  |  - Jadval         |   2. GET /payments (token)     |  - Payments Ctrl  |\n"
"  |  - Modal          |  <----------------------------  |  - JWT middleware |\n"
"  +-------------------+        ma'lumot (rol bo'yicha)  +--------+---------+\n"
"                                                                 |\n"
"                                                          EF Core | SQL\n"
"                                                                 v\n"
"                                                        +------------------+\n"
"                                                        |   PostgreSQL     |\n"
"                                                        |  roles, partners |\n"
"                                                        |  users, payments |\n"
"                                                        +------------------+")

# --- 4. Rollar ---
add_h1("4. Rollar va autentifikatsiya")
add_pre(
"+-----------+------------------------+-------------------------------------+\n"
"| Rol       | Tavsif                 | Ko'radigan ma'lumot                 |\n"
"+-----------+------------------------+-------------------------------------+\n"
"| admin     | Tizim administratori   | Barcha partnyorlar o'tkazmalari     |\n"
"| partner   | Partnyor xodimi        | Faqat o'ziga biriktirilgan partnyor |\n"
"+-----------+------------------------+-------------------------------------+")
add_h3("Kirish jarayoni")
add_bullet("Foydalanuvchi login va parolni yuboradi.")
add_bullet("Server parolni BCrypt hash bilan solishtiradi.")
add_bullet("To'g'ri bo'lsa JWT token beriladi (ichida userId, role, partnerId).")
add_bullet("Har bir keyingi so'rovda token tekshiriladi.")
add_para("MUHIM (xavfsizlik): partner roli uchun SQL so'rovga server tomonidan "
         "majburiy partnerId sharti qo'shiladi. PartnerId tokendan olinadi, "
         "frontenddan kelgan qiymatga ishonilmaydi - shu sababli foydalanuvchi "
         "boshqa partnyor ma'lumotini hech qachon ko'ra olmaydi.")

# --- 5. Funksional talablar ---
add_h1("5. Funksional talablar")
add_h2("5.1. O'tkazmalar ro'yxati (jadval)")
add_pre(
"+----------------------------+----------------------+---------------------+\n"
"| Ustun (ekranda)            | Manba maydoni        | Izoh                |\n"
"+----------------------------+----------------------+---------------------+\n"
"| To'lov identifikatori      | PaymentRef           | Unikal kod          |\n"
"| O'tkazma qatnashchilari    | Sender -> Receiver   | Jo'nat. / qabul q.  |\n"
"| O'tkazma holati            | Status               | success/pending/... |\n"
"| O'tkazma sanasi            | TransferDate         | Sana va vaqt        |\n"
"| O'tkazma summasi (so'mda)  | AmountUzs            | 150 000 so'm        |\n"
"+----------------------------+----------------------+---------------------+")
add_bullet("Sahifalash (pagination).")
add_bullet("Sana oralig'i, holat va PaymentRef bo'yicha filtr/qidiruv.")
add_bullet("Holat rang bilan ajratiladi (yashil/sariq/qizil).")

add_h2("5.2. O'tkazma tafsilotlari (modal)")
add_para("Jadval qatoriga bosilganda modal ochiladi va quyidagilar ko'rsatiladi:")
add_h3("Jo'natuvchi va Qabul qiluvchi")
add_bullet("F.I.Sh.")
add_bullet("Passport ma'lumotlari (seriya + raqam).")
add_bullet("Karta raqami (maskalangan: 8600 **** **** 1234).")
add_h3("Summa tafsilotlari")
add_bullet("O'tkazilgan summa (asl valyutada).")
add_bullet("So'mga o'girilgan summa.")
add_bullet("Dollar kursi.")
add_bullet("Komissiya.")
add_h3("Xato (agar mavjud bo'lsa)")
add_bullet("Xato kodi va xato matni qizil panelda ko'rsatiladi.")

# --- 6. Baza ---
add_h1("6. Ma'lumotlar bazasi (SQL)")
add_para("To'rtta jadval: roles, partners, users, payments. Quyida PostgreSQL "
         "sxemasi keltirilgan.")
add_code(
"CREATE TABLE roles (\n"
"    id          SERIAL PRIMARY KEY,\n"
"    name        VARCHAR(50) UNIQUE NOT NULL,   -- 'admin' | 'partner'\n"
"    description VARCHAR(255)\n"
");\n\n"
"CREATE TABLE partners (\n"
"    id         SERIAL PRIMARY KEY,\n"
"    name       VARCHAR(100) NOT NULL,\n"
"    code       VARCHAR(50) UNIQUE NOT NULL,    -- payme, click, uzum\n"
"    is_active  BOOLEAN DEFAULT true\n"
");\n\n"
"CREATE TABLE users (\n"
"    id            SERIAL PRIMARY KEY,\n"
"    login         VARCHAR(100) UNIQUE NOT NULL,\n"
"    password_hash VARCHAR(255) NOT NULL,\n"
"    full_name     VARCHAR(150),\n"
"    role_id       INT NOT NULL REFERENCES roles(id),\n"
"    partner_id    INT REFERENCES partners(id),  -- admin uchun NULL\n"
"    is_active     BOOLEAN DEFAULT true\n"
");")
add_code(
"CREATE TABLE payments (\n"
"    id            BIGSERIAL PRIMARY KEY,\n"
"    payment_ref   VARCHAR(100) UNIQUE NOT NULL,  -- PaymentRef\n"
"    partner_id    INT NOT NULL REFERENCES partners(id),\n"
"    status        VARCHAR(30) NOT NULL,          -- success/pending/failed\n"
"    transfer_date TIMESTAMP NOT NULL,\n"
"    amount_uzs    NUMERIC(18,2) NOT NULL,        -- summa (so'mda)\n"
"    -- Jo'natuvchi\n"
"    sender_full_name       VARCHAR(200),\n"
"    sender_passport_series VARCHAR(10),\n"
"    sender_passport_number VARCHAR(20),\n"
"    sender_card_number     VARCHAR(25),\n"
"    -- Qabul qiluvchi\n"
"    receiver_full_name       VARCHAR(200),\n"
"    receiver_passport_series VARCHAR(10),\n"
"    receiver_passport_number VARCHAR(20),\n"
"    receiver_card_number     VARCHAR(25),\n"
"    -- Summa tafsilotlari\n"
"    amount_original   NUMERIC(18,2),  -- asl valyutadagi summa\n"
"    original_currency VARCHAR(3),     -- USD, RUB ...\n"
"    usd_rate          NUMERIC(12,4),  -- dollar kursi\n"
"    commission        NUMERIC(18,2),  -- komissiya\n"
"    -- Xato\n"
"    error_code    VARCHAR(50),\n"
"    error_message TEXT,\n"
"    created_at    TIMESTAMP DEFAULT now()\n"
");\n\n"
"CREATE INDEX idx_payments_partner ON payments(partner_id);\n"
"CREATE INDEX idx_payments_date    ON payments(transfer_date);\n"
"CREATE INDEX idx_payments_status  ON payments(status);")

# --- 7. .NET modellar ---
add_h1("7. Backend: .NET 10 modellar va EF Core")
add_para("Loyiha tuzilishi (Clean / Layered yondashuv):")
add_pre(
"PartnerPayments.Api/\n"
" |- Models/         (Entity klasslar: Role, Partner, User, Payment)\n"
" |- Data/           (AppDbContext)\n"
" |- Dtos/           (PaymentListDto, PaymentDetailDto, LoginDto)\n"
" |- Services/       (AuthService, PaymentService)\n"
" |- Controllers/    (AuthController, PaymentsController)\n"
" |- Program.cs      (DI, JWT, CORS sozlamalari)\n"
" |- appsettings.json")
add_h3("Entity: Payment.cs")
add_code(
"namespace PartnerPayments.Api.Models;\n\n"
"public class Payment\n"
"{\n"
"    public long Id { get; set; }\n"
"    public string PaymentRef { get; set; } = default!;\n"
"    public int PartnerId { get; set; }\n"
"    public Partner? Partner { get; set; }\n"
"    public string Status { get; set; } = \"pending\";\n"
"    public DateTime TransferDate { get; set; }\n"
"    public decimal AmountUzs { get; set; }\n\n"
"    // Jo'natuvchi\n"
"    public string? SenderFullName { get; set; }\n"
"    public string? SenderPassportSeries { get; set; }\n"
"    public string? SenderPassportNumber { get; set; }\n"
"    public string? SenderCardNumber { get; set; }\n\n"
"    // Qabul qiluvchi\n"
"    public string? ReceiverFullName { get; set; }\n"
"    public string? ReceiverPassportSeries { get; set; }\n"
"    public string? ReceiverPassportNumber { get; set; }\n"
"    public string? ReceiverCardNumber { get; set; }\n\n"
"    // Summa tafsilotlari\n"
"    public decimal? AmountOriginal { get; set; }\n"
"    public string? OriginalCurrency { get; set; }\n"
"    public decimal? UsdRate { get; set; }\n"
"    public decimal? Commission { get; set; }\n\n"
"    // Xato\n"
"    public string? ErrorCode { get; set; }\n"
"    public string? ErrorMessage { get; set; }\n"
"    public DateTime CreatedAt { get; set; }\n"
"}")
add_h3("Entity: User, Role, Partner")
add_code(
"public class Role\n"
"{\n"
"    public int Id { get; set; }\n"
"    public string Name { get; set; } = default!;  // admin | partner\n"
"    public string? Description { get; set; }\n"
"}\n\n"
"public class Partner\n"
"{\n"
"    public int Id { get; set; }\n"
"    public string Name { get; set; } = default!;\n"
"    public string Code { get; set; } = default!;\n"
"    public bool IsActive { get; set; } = true;\n"
"}\n\n"
"public class User\n"
"{\n"
"    public int Id { get; set; }\n"
"    public string Login { get; set; } = default!;\n"
"    public string PasswordHash { get; set; } = default!;\n"
"    public string? FullName { get; set; }\n"
"    public int RoleId { get; set; }\n"
"    public Role? Role { get; set; }\n"
"    public int? PartnerId { get; set; }   // admin uchun null\n"
"    public Partner? Partner { get; set; }\n"
"    public bool IsActive { get; set; } = true;\n"
"}")
add_h3("AppDbContext.cs")
add_code(
"using Microsoft.EntityFrameworkCore;\n"
"using PartnerPayments.Api.Models;\n\n"
"public class AppDbContext : DbContext\n"
"{\n"
"    public AppDbContext(DbContextOptions<AppDbContext> o) : base(o) { }\n\n"
"    public DbSet<Role> Roles => Set<Role>();\n"
"    public DbSet<Partner> Partners => Set<Partner>();\n"
"    public DbSet<User> Users => Set<User>();\n"
"    public DbSet<Payment> Payments => Set<Payment>();\n\n"
"    protected override void OnModelCreating(ModelBuilder b)\n"
"    {\n"
"        b.Entity<Payment>().HasIndex(p => p.PaymentRef).IsUnique();\n"
"        b.Entity<Payment>().HasIndex(p => p.PartnerId);\n"
"        b.Entity<User>().HasIndex(u => u.Login).IsUnique();\n"
"        b.Entity<Payment>().Property(p => p.AmountUzs).HasPrecision(18, 2);\n"
"    }\n"
"}")

# --- 8. API ---
add_h1("8. Backend: API endpointlar va JWT")
add_pre(
"+--------+----------------------+-----------------+------------------------+\n"
"| Metod  | URL                  | Rol             | Tavsif                 |\n"
"+--------+----------------------+-----------------+------------------------+\n"
"| POST   | /api/auth/login      | hammasi         | Login -> JWT token     |\n"
"| GET    | /api/payments        | admin, partner  | Ro'yxat (filtr+page)   |\n"
"| GET    | /api/payments/{id}   | admin, partner  | Modal tafsiloti        |\n"
"| GET    | /api/partners        | admin           | Filtr uchun ro'yxat    |\n"
"+--------+----------------------+-----------------+------------------------+")
add_h3("DTO klasslar")
add_code(
"public record LoginDto(string Login, string Password);\n\n"
"public record PaymentListDto(long Id, string PaymentRef,\n"
"    string Participants, string Status, DateTime TransferDate,\n"
"    decimal AmountUzs);\n\n"
"public record AmountDto(decimal? Original, string? Currency,\n"
"    decimal Uzs, decimal? UsdRate, decimal? Commission);\n\n"
"public record PartyDto(string? FullName, string? Passport,\n"
"    string? CardNumber);")
add_h3("PaymentsController.cs (rol bo'yicha filtr)")
add_code(
"[ApiController]\n"
"[Route(\"api/payments\")]\n"
"[Authorize]\n"
"public class PaymentsController : ControllerBase\n"
"{\n"
"    private readonly AppDbContext _db;\n"
"    public PaymentsController(AppDbContext db) => _db = db;\n\n"
"    [HttpGet]\n"
"    public async Task<IActionResult> List(int page = 1, int limit = 20,\n"
"        string? status = null, string? search = null)\n"
"    {\n"
"        var q = _db.Payments.AsQueryable();\n\n"
"        // Rol bo'yicha cheklov: partner faqat o'z ma'lumotini ko'radi\n"
"        var role = User.FindFirst(\"role\")?.Value;\n"
"        if (role == \"partner\")\n"
"        {\n"
"            var pid = int.Parse(User.FindFirst(\"partnerId\")!.Value);\n"
"            q = q.Where(p => p.PartnerId == pid);\n"
"        }\n\n"
"        if (!string.IsNullOrEmpty(status))\n"
"            q = q.Where(p => p.Status == status);\n"
"        if (!string.IsNullOrEmpty(search))\n"
"            q = q.Where(p => p.PaymentRef.Contains(search));\n\n"
"        var total = await q.CountAsync();\n"
"        var items = await q.OrderByDescending(p => p.TransferDate)\n"
"            .Skip((page - 1) * limit).Take(limit)\n"
"            .Select(p => new PaymentListDto(p.Id, p.PaymentRef,\n"
"                (p.SenderFullName ?? \"-\") + \" -> \" +\n"
"                (p.ReceiverFullName ?? \"-\"),\n"
"                p.Status, p.TransferDate, p.AmountUzs))\n"
"            .ToListAsync();\n\n"
"        return Ok(new { data = items,\n"
"            pagination = new { page, limit, total } });\n"
"    }\n\n"
"    [HttpGet(\"{id:long}\")]\n"
"    public async Task<IActionResult> Detail(long id)\n"
"    {\n"
"        var p = await _db.Payments.FindAsync(id);\n"
"        if (p is null) return NotFound();\n\n"
"        var role = User.FindFirst(\"role\")?.Value;\n"
"        if (role == \"partner\")\n"
"        {\n"
"            var pid = int.Parse(User.FindFirst(\"partnerId\")!.Value);\n"
"            if (p.PartnerId != pid) return Forbid();\n"
"        }\n\n"
"        return Ok(new {\n"
"            payment_ref = p.PaymentRef, status = p.Status,\n"
"            transfer_date = p.TransferDate,\n"
"            sender = new PartyDto(p.SenderFullName,\n"
"                $\"{p.SenderPassportSeries} {p.SenderPassportNumber}\",\n"
"                Mask(p.SenderCardNumber)),\n"
"            receiver = new PartyDto(p.ReceiverFullName,\n"
"                $\"{p.ReceiverPassportSeries} {p.ReceiverPassportNumber}\",\n"
"                Mask(p.ReceiverCardNumber)),\n"
"            amount = new AmountDto(p.AmountOriginal, p.OriginalCurrency,\n"
"                p.AmountUzs, p.UsdRate, p.Commission),\n"
"            error = p.ErrorCode == null ? null :\n"
"                new { code = p.ErrorCode, message = p.ErrorMessage }\n"
"        });\n"
"    }\n\n"
"    private static string? Mask(string? c)\n"
"    {\n"
"        if (string.IsNullOrEmpty(c) || c.Length < 8) return c;\n"
"        return c[..4] + \" **** **** \" + c[^4..];\n"
"    }\n"
"}")
add_h3("AuthController.cs (login + JWT)")
add_code(
"[ApiController]\n"
"[Route(\"api/auth\")]\n"
"public class AuthController : ControllerBase\n"
"{\n"
"    private readonly AppDbContext _db;\n"
"    private readonly IConfiguration _cfg;\n"
"    public AuthController(AppDbContext db, IConfiguration cfg)\n"
"        { _db = db; _cfg = cfg; }\n\n"
"    [HttpPost(\"login\")]\n"
"    public async Task<IActionResult> Login(LoginDto dto)\n"
"    {\n"
"        var user = await _db.Users.Include(u => u.Role)\n"
"            .FirstOrDefaultAsync(u => u.Login == dto.Login && u.IsActive);\n"
"        if (user is null ||\n"
"            !BCrypt.Net.BCrypt.Verify(dto.Password, user.PasswordHash))\n"
"            return Unauthorized(new { message = \"Login yoki parol xato\" });\n\n"
"        var claims = new List<Claim> {\n"
"            new(\"userId\", user.Id.ToString()),\n"
"            new(\"role\", user.Role!.Name),\n"
"            new(\"partnerId\", user.PartnerId?.ToString() ?? \"\")\n"
"        };\n"
"        var key = new SymmetricSecurityKey(\n"
"            Encoding.UTF8.GetBytes(_cfg[\"Jwt:Key\"]!));\n"
"        var creds = new SigningCredentials(key,\n"
"            SecurityAlgorithms.HmacSha256);\n"
"        var token = new JwtSecurityToken(claims: claims,\n"
"            expires: DateTime.UtcNow.AddHours(8), signingCredentials: creds);\n"
"        return Ok(new {\n"
"            token = new JwtSecurityTokenHandler().WriteToken(token),\n"
"            role = user.Role.Name });\n"
"    }\n"
"}")
add_h3("Program.cs (JWT + CORS sozlamasi - qisqacha)")
add_code(
"builder.Services.AddDbContext<AppDbContext>(o =>\n"
"    o.UseNpgsql(builder.Configuration.GetConnectionString(\"Default\")));\n\n"
"builder.Services.AddAuthentication(\"Bearer\")\n"
"    .AddJwtBearer(o => o.TokenValidationParameters = new()\n"
"    {\n"
"        ValidateIssuerSigningKey = true,\n"
"        IssuerSigningKey = new SymmetricSecurityKey(\n"
"            Encoding.UTF8.GetBytes(builder.Configuration[\"Jwt:Key\"]!)),\n"
"        ValidateIssuer = false, ValidateAudience = false\n"
"    });\n\n"
"builder.Services.AddCors(o => o.AddDefaultPolicy(p =>\n"
"    p.WithOrigins(\"http://localhost:5173\")\n"
"     .AllowAnyHeader().AllowAnyMethod()));")

# --- 9. Frontend Vue ---
add_h1("9. Frontend: Vue 3")
add_para("Loyiha tuzilishi (Vite + Vue 3 Composition API):")
add_pre(
"frontend/\n"
" |- src/\n"
" |   |- api/         axios.js  (HTTP klient + token)\n"
" |   |- stores/      auth.js   (Pinia - login holati)\n"
" |   |- views/       LoginView.vue, PaymentsView.vue\n"
" |   |- components/  PaymentModal.vue\n"
" |   |- router/      index.js\n"
" |   |- App.vue, main.js\n"
" |- vite.config.js")
add_h3("api/axios.js")
add_code(
"import axios from 'axios'\n\n"
"const api = axios.create({ baseURL: 'http://localhost:5000/api' })\n\n"
"// Har bir so'rovga JWT tokenni qo'shamiz\n"
"api.interceptors.request.use(cfg => {\n"
"  const token = localStorage.getItem('token')\n"
"  if (token) cfg.headers.Authorization = `Bearer ${token}`\n"
"  return cfg\n"
"})\n\n"
"export default api")
add_h3("views/PaymentsView.vue (jadval)")
add_code(
"<script setup>\n"
"import { ref, onMounted } from 'vue'\n"
"import api from '../api/axios'\n"
"import PaymentModal from '../components/PaymentModal.vue'\n\n"
"const items = ref([])\n"
"const selectedId = ref(null)\n"
"const search = ref('')\n\n"
"async function load() {\n"
"  const { data } = await api.get('/payments', {\n"
"    params: { search: search.value, page: 1, limit: 20 }\n"
"  })\n"
"  items.value = data.data\n"
"}\n"
"onMounted(load)\n\n"
"function fmt(n) { return new Intl.NumberFormat('uz-UZ').format(n) }\n"
"</script>\n\n"
"<template>\n"
"  <div class=\"toolbar\">\n"
"    <input v-model=\"search\" placeholder=\"PaymentRef qidirish...\" />\n"
"    <button @click=\"load\">Qidirish</button>\n"
"  </div>\n\n"
"  <table>\n"
"    <thead>\n"
"      <tr>\n"
"        <th>To'lov ID</th><th>Qatnashchilar</th><th>Holat</th>\n"
"        <th>Sana</th><th>Summa (so'm)</th>\n"
"      </tr>\n"
"    </thead>\n"
"    <tbody>\n"
"      <tr v-for=\"p in items\" :key=\"p.id\"\n"
"          @click=\"selectedId = p.id\" class=\"row\">\n"
"        <td>{{ p.paymentRef }}</td>\n"
"        <td>{{ p.participants }}</td>\n"
"        <td><span :class=\"p.status\">{{ p.status }}</span></td>\n"
"        <td>{{ new Date(p.transferDate).toLocaleString() }}</td>\n"
"        <td>{{ fmt(p.amountUzs) }} so'm</td>\n"
"      </tr>\n"
"    </tbody>\n"
"  </table>\n\n"
"  <PaymentModal v-if=\"selectedId\" :id=\"selectedId\"\n"
"      @close=\"selectedId = null\" />\n"
"</template>")
add_h3("components/PaymentModal.vue (tafsilot)")
add_code(
"<script setup>\n"
"import { ref, onMounted } from 'vue'\n"
"import api from '../api/axios'\n\n"
"const props = defineProps({ id: Number })\n"
"const emit = defineEmits(['close'])\n"
"const p = ref(null)\n\n"
"onMounted(async () => {\n"
"  const { data } = await api.get(`/payments/${props.id}`)\n"
"  p.value = data\n"
"})\n"
"</script>\n\n"
"<template>\n"
"  <div class=\"overlay\" @click.self=\"emit('close')\">\n"
"    <div class=\"modal\" v-if=\"p\">\n"
"      <h3>O'tkazma: {{ p.payment_ref }}</h3>\n\n"
"      <div class=\"cols\">\n"
"        <div>\n"
"          <h4>Jo'natuvchi</h4>\n"
"          <p>{{ p.sender.full_name }}</p>\n"
"          <p>Passport: {{ p.sender.passport }}</p>\n"
"          <p>Karta: {{ p.sender.card_number }}</p>\n"
"        </div>\n"
"        <div>\n"
"          <h4>Qabul qiluvchi</h4>\n"
"          <p>{{ p.receiver.full_name }}</p>\n"
"          <p>Passport: {{ p.receiver.passport }}</p>\n"
"          <p>Karta: {{ p.receiver.card_number }}</p>\n"
"        </div>\n"
"      </div>\n\n"
"      <h4>Summa</h4>\n"
"      <p>O'tkazilgan: {{ p.amount.original }} {{ p.amount.currency }}</p>\n"
"      <p>So'mda: {{ p.amount.uzs }} | Kurs: {{ p.amount.usd_rate }}</p>\n"
"      <p>Komissiya: {{ p.amount.commission }}</p>\n\n"
"      <div v-if=\"p.error\" class=\"error\">\n"
"        Xato [{{ p.error.code }}]: {{ p.error.message }}\n"
"      </div>\n\n"
"      <button @click=\"emit('close')\">Yopish</button>\n"
"    </div>\n"
"  </div>\n"
"</template>")

# --- 10. Ketma-ketlik ---
add_h1("10. Bajarilish ketma-ketligi")
add_pre(
"+----+-------------------------------------------+----------------------+\n"
"| #  | Bosqich                                   | Natija               |\n"
"+----+-------------------------------------------+----------------------+\n"
"| 1  | .NET 10 Web API loyihasini yaratish       | Skelet tayyor        |\n"
"| 2  | EF Core + Npgsql ulash, Entity'lar        | Modellar tayyor      |\n"
"| 3  | Migration + Database update               | Jadvallar yaratildi  |\n"
"| 4  | Seed (admin, partner, test o'tkazmalar)   | Sinov ma'lumoti      |\n"
"| 5  | AuthController + JWT + BCrypt             | Login ishlaydi       |\n"
"| 6  | JWT middleware + rol cheklovi             | Himoya o'rnatildi    |\n"
"| 7  | PaymentsController: GET /payments         | Ro'yxat API tayyor   |\n"
"| 8  | GET /payments/{id} + maskalash            | Modal API tayyor     |\n"
"| 9  | Vue 3 loyihasi (Vite) + Pinia + Router    | Frontend skeleti     |\n"
"| 10 | Login sahifa + token saqlash              | Kirish ishlaydi      |\n"
"| 11 | Jadval (PaymentsView)                     | Ro'yxat ko'rinadi    |\n"
"| 12 | Modal (PaymentModal) + format/rang        | Tafsilot ko'rinadi   |\n"
"| 13 | Test va deploy                            | Tayyor mahsulot      |\n"
"+----+-------------------------------------------+----------------------+")

# --- 11. Xavfsizlik ---
add_h1("11. Xavfsizlik talablari")
add_bullet("Parollar faqat BCrypt hash ko'rinishida saqlanadi.")
add_bullet("Karta raqami va passport ma'lumotlari maskalanadi.")
add_bullet("Rol bo'yicha cheklov serverda (token claim'lari asosida) bajariladi.")
add_bullet("Barcha /api/payments so'rovlari [Authorize] bilan himoyalangan.")
add_bullet("EF Core parametrlangan so'rovlar -> SQL injection oldi olinadi.")
add_bullet("CORS faqat ishonchli frontend manzili uchun ochiladi.")
add_bullet("HTTPS majburiy, JWT tokenning amal qilish muddati cheklangan (8 soat).")

# --- 12. Ishga tushirish ---
add_h1("12. Loyihani ishga tushirish")
add_h3("Backend (.NET 10)")
add_code(
"dotnet new webapi -n PartnerPayments.Api\n"
"cd PartnerPayments.Api\n"
"dotnet add package Microsoft.EntityFrameworkCore\n"
"dotnet add package Npgsql.EntityFrameworkCore.PostgreSQL\n"
"dotnet add package Microsoft.AspNetCore.Authentication.JwtBearer\n"
"dotnet add package BCrypt.Net-Next\n\n"
"# migration va baza\n"
"dotnet ef migrations add Init\n"
"dotnet ef database update\n"
"dotnet run")
add_h3("Frontend (Vue 3)")
add_code(
"npm create vite@latest frontend -- --template vue\n"
"cd frontend\n"
"npm install\n"
"npm install axios pinia vue-router\n"
"npm run dev   # http://localhost:5173")
add_h3("appsettings.json (namuna)")
add_code(
"{\n"
"  \"ConnectionStrings\": {\n"
"    \"Default\": \"Host=localhost;Port=5432;Database=payments_db;\" +\n"
"               \"Username=postgres;Password=postgres\"\n"
"  },\n"
"  \"Jwt\": { \"Key\": \"BU_YERGA_KUCHLI_MAXFIY_KALIT_QOYING_32+\" }\n"
"}")
add_blank(10)
add_para("--- Hujjat yakuni ---")


# ===================================================================
#  PDF GENERATSIYA
# ===================================================================

def esc(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


# Layout -> sahifalarga bo'lish
pages = []
cur = []
y = PAGE_H - MT

for ln in lines:
    if ln.get("newpage"):
        pages.append(cur)
        cur = []
        y = PAGE_H - MT
        continue
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
    size = ln["size"]
    h = size * 1.5
    if y - h < MB:
        pages.append(cur); cur = []; y = PAGE_H - MT
    baseline = y - size
    item = dict(ln)
    item["baseline"] = baseline
    cur.append(item)
    y -= h

if cur:
    pages.append(cur)


def build_content(page_items):
    out = []
    for it in page_items:
        if it.get("rule"):
            out.append("0.55 0.6 0.75 RG")
            out.append("0.6 w")
            out.append(f"{ML:.2f} {it['y']:.2f} m {ML + CONTENT_W:.2f} {it['y']:.2f} l S")
            continue
        size = it["size"]
        font = it["font"]
        col = it.get("color", (0, 0, 0))
        text = it["text"]
        if it.get("center"):
            tw = len(text) * size * 0.6
            x = ML + (CONTENT_W - tw) / 2
        else:
            x = ML
        # kod bloklari uchun yengil chap chiziq (vizual ajratish)
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


# PDF obyektlarini yig'ish
objects = []  # (id, bytes)

# 1 Catalog, 2 Pages, 3 Font Courier, 4 Font Courier-Bold
catalog_id = 1
pages_id = 2
font1_id = 3
font2_id = 4

page_obj_ids = []
content_obj_ids = []
next_id = 5
for _ in pages:
    page_obj_ids.append(next_id); next_id += 1
    content_obj_ids.append(next_id); next_id += 1

objects.append((catalog_id,
    f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode("latin-1")))

kids = " ".join(f"{pid} 0 R" for pid in page_obj_ids)
objects.append((pages_id,
    f"<< /Type /Pages /Kids [{kids}] /Count {len(page_obj_ids)} >>".encode("latin-1")))

objects.append((font1_id,
    b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding "
    b"/WinAnsiEncoding >>"))
objects.append((font2_id,
    b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier-Bold /Encoding "
    b"/WinAnsiEncoding >>"))

for i, page_items in enumerate(pages):
    pid = page_obj_ids[i]
    cid = content_obj_ids[i]
    page_dict = (
        f"<< /Type /Page /Parent {pages_id} 0 R "
        f"/MediaBox [0 0 {PAGE_W:.2f} {PAGE_H:.2f}] "
        f"/Resources << /Font << /F1 {font1_id} 0 R /F2 {font2_id} 0 R >> >> "
        f"/Contents {cid} 0 R >>"
    )
    objects.append((pid, page_dict.encode("latin-1")))

    stream = build_content(page_items).encode("latin-1")
    content_obj = (b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n"
                   + stream + b"\nendstream")
    objects.append((cid, content_obj))

# Fayl yozish
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
