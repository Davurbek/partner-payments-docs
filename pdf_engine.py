# -*- coding: utf-8 -*-
"""
Umumiy PDF generatsiya dvigateli (tashqi kutubxonasiz).
build_pdf.py, build_pdf_B.py va build_pdf_AB.py shu modulni ishlatadi.
"""

import textwrap

PAGE_W, PAGE_H = 595.276, 841.890
ML, MR, MT, MB = 55, 50, 60, 55
CONTENT_W = PAGE_W - ML - MR


class Doc:
    """Hujjat kontenti uchun yig'uvchi."""

    def __init__(self):
        self.lines = []

    def max_chars(self, size, extra=0):
        return max(1, int((CONTENT_W - extra) // (size * 0.6)))

    def blank(self, h=6):
        self.lines.append({"blank": h})

    def rule(self):
        self.lines.append({"rule": True})

    def newpage(self):
        self.lines.append({"newpage": True})

    def h1(self, text):
        self.blank(10)
        self.lines.append({"text": text, "font": "F2", "size": 15,
                           "color": (0.10, 0.20, 0.50)})
        self.rule(); self.blank(5)

    def h2(self, text):
        self.blank(9)
        self.lines.append({"text": text, "font": "F2", "size": 12,
                           "color": (0.14, 0.18, 0.42)})
        self.blank(4)

    def h3(self, text):
        self.blank(5)
        self.lines.append({"text": text, "font": "F2", "size": 10.5,
                           "color": (0, 0, 0)})
        self.blank(2)

    def para(self, text, size=10):
        width = self.max_chars(size)
        for seg in (textwrap.wrap(text, width=width) or [""]):
            self.lines.append({"text": seg, "font": "F1", "size": size,
                               "color": (0, 0, 0)})
        self.blank(4)

    def bullet(self, text, size=10):
        width = self.max_chars(size, extra=size * 0.6 * 2)
        wrapped = textwrap.wrap(text, width=width) or [""]
        for i, seg in enumerate(wrapped):
            prefix = "- " if i == 0 else "  "
            self.lines.append({"text": prefix + seg, "font": "F1",
                               "size": size, "color": (0, 0, 0)})

    def code(self, code, size=8.5):
        self.blank(3)
        for ln in code.split("\n"):
            self.lines.append({"text": ln, "font": "F1", "size": size,
                               "color": (0.10, 0.10, 0.10), "code": True})
        self.blank(3)

    def pre(self, block, size=8.5):
        self.blank(3)
        for ln in block.split("\n"):
            self.lines.append({"text": ln, "font": "F1", "size": size,
                               "color": (0, 0, 0)})
        self.blank(3)

    def title(self, text, size=20):
        self.lines.append({"text": text, "font": "F2", "size": size,
                           "color": (0.10, 0.20, 0.50), "center": True})

    def center(self, text, size=11, color=(0, 0, 0), font="F1"):
        self.lines.append({"text": text, "font": font, "size": size,
                           "color": color, "center": True})


def _esc(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def render(lines, out_path):
    """lines ro'yxatidan PDF yasaydi va out_path ga yozadi."""
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
            out.append(f"({_esc(text)}) Tj")
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

    with open(out_path, "wb") as f:
        f.write(buf)

    return len(pages), len(buf)
