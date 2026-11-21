"""공유 미리보기 이미지(카톡·SNS에 주소를 보낼 때 보이는 그림) 만들기.

결과: src/assets/images/og/og-ko|en|ja|zh.jpg (1200x630)
필요한 것: Python 3 + Pillow, Noto Sans/Serif CJK 글꼴 (아래 FONT_DIR). Claude 작업 환경(리눅스)에서 만들었습니다.
홈페이지와 같은 '먹감나무 공방' 모양: 짙은 호두나무 결 바탕, 검은 액자에 넣은 대표 사진, 붉은 낙관,
붓글씨 상호 그림(public/brand/name-brush.svg, 나눔손글씨 붓 글꼴의 글자 모양). rsvg-convert가 필요합니다.
전화번호나 문구가 바뀌면 TXT를 고치고 다시 실행하세요:  python3 scripts/make_og.py
"""
import io
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = Path('/usr/share/fonts/opentype/noto')
F_BOLD, F_MED = (str(FONT_DIR / n) for n in ('NotoSansCJK-Bold.ttc', 'NotoSansCJK-Medium.ttc'))
F_SERIF_B, F_SERIF_K = str(FONT_DIR / 'NotoSerifCJK-Bold.ttc'), str(FONT_DIR / 'NotoSerifCJK-Black.ttc')
IDX = {'ko': 1, 'ja': 0, 'zh': 2, 'en': 1}  # Sans 글꼴 묶음 안의 언어 순서
SIDX = {'ko': 1, 'ja': 0, 'zh': 2, 'en': 1}  # Serif 글꼴 묶음 안의 언어 순서 (JP, KR, SC, TC, HK)
BG = (18, 13, 9)
IVORY, IVORY2 = (243, 233, 216), (216, 202, 177)
GOLD, GOLD2, GOLD3 = (205, 167, 99), (232, 201, 140), (142, 107, 52)
SEAL = (179, 59, 43)

TXT = {
    # 연수(40년)는 해마다 바뀌므로 그림에 넣지 않음
    'ko': dict(name='', pill='로구로 전문', t1='같은 모양을', t2='한결같이', tel='상담전화 010-8548-7264', addr='경기도 광주시 초월읍 · 로구로 전문 공방'),
    'en': dict(name='Chowol Craft', pill='Woodturning', t1='The same shape,', t2='every single time', tel='Order line +82 10-8548-7264', addr='Chowol-eup, Gwangju, Gyeonggi-do, Korea · Woodturning workshop'),
    'ja': dict(name='チョウォル工芸社', pill='木工ろくろ専門', t1='同じかたちを、', t2='何度でも', tel='ご注文・ご相談 +82 10-8548-7264', addr='韓国 京畿道 広州市 草月邑 · 木工ろくろ専門工房'),
    'zh': dict(name='Chowol 工艺社', pill='专业木工车削', t1='同一个形状，', t2='始终如一', tel='咨询专线 +82 10-8548-7264', addr='韩国 京畿道 广州市 草月邑 · 专业木工车削工坊'),
}


def gold_text(size_font, text, pad=8):
    """금박 글씨: 위는 밝고 아래로 짙어지는 금색 (투명 바탕 RGBA)"""
    font = size_font
    l, t, r, b = font.getbbox(text)
    w, h = r - l + pad * 2, b - t + pad * 2
    mask = Image.new('L', (w, h), 0)
    ImageDraw.Draw(mask).text((pad - l, pad - t), text, font=font, fill=255)
    grad = Image.new('RGB', (1, h))
    for y in range(h):
        k = y / max(1, h - 1)
        if k < 0.55:
            a, c, kk = (246, 223, 166), GOLD, k / 0.55
        else:
            a, c, kk = GOLD, GOLD3, (k - 0.55) / 0.45
        grad.putpixel((0, y), tuple(round(a[i] + (c[i] - a[i]) * kk) for i in range(3)))
    grad = grad.resize((w, h))
    out = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    out.paste(grad, (0, 0), mask)
    return out


def make(lang, t, photo, wood):
    W, H = 1200, 630
    # 바탕: 호두나무 결 + 짙은 덮개 + 왼쪽 위에서 비추는 따뜻한 빛
    im = ImageOps.fit(wood, (W, H), Image.LANCZOS)
    im = Image.blend(im, Image.new('RGB', (W, H), BG), 0.84)
    glow = Image.new('L', (W, H), 0)
    ImageDraw.Draw(glow).ellipse([-300, -420, 900, 380], fill=110)
    glow = glow.filter(ImageFilter.GaussianBlur(170))
    im = Image.composite(Image.new('RGB', (W, H), (70, 50, 26)), im, glow)
    d = ImageDraw.Draw(im)

    # 오른쪽: 검은 매트 액자 + 안쪽 금선 + 따뜻하게 보정한 대표 사진
    pw, ph = 372, 466
    px, py = W - pw - 78, (H - ph) // 2
    mat = 12
    d.rectangle([px - mat, py - mat, px + pw + mat - 1, py + ph + mat - 1], fill=(0, 0, 0))
    d.rectangle([px - mat - 1, py - mat - 1, px + pw + mat, py + ph + mat], outline=(60, 50, 38), width=1)
    pic = ImageOps.fit(photo, (pw, ph), Image.LANCZOS, centering=(0.5, 0.3))
    pic = ImageEnhance.Color(pic).enhance(0.85)
    pic = ImageEnhance.Brightness(pic).enhance(0.96)
    im.paste(pic, (px, py))
    d.rectangle([px, py, px + pw - 1, py + ph - 1], outline=(117, 96, 62), width=1)

    # 붉은 낙관 (액자 왼쪽 아래 모서리에 걸쳐)
    ss = 76
    seal = Image.new('RGBA', (ss, ss), (0, 0, 0, 0))
    sd = ImageDraw.Draw(seal)
    sd.rounded_rectangle([0, 0, ss - 1, ss - 1], radius=4, fill=SEAL + (255,))
    sd.rounded_rectangle([5, 5, ss - 6, ss - 6], radius=3, outline=(255, 243, 232, 220), width=2)
    fs = ImageFont.truetype(F_SERIF_K, 27, index=SIDX['ko'])
    for k, ch in enumerate('초월'):
        sd.text((ss / 2, 23 + k * 30), ch, font=fs, fill=(255, 243, 232), anchor='mm')
    seal = seal.rotate(-3, resample=Image.BICUBIC, expand=True)
    im.paste(seal, (px - 46, py + ph - 52), seal)

    # 왼쪽: 붓글씨 상호 그림(public/brand/name-brush.svg) + 띠
    x0, limit = 76, px - 70
    png = subprocess.run(['rsvg-convert', '-h', '104', str(ROOT / 'public/brand/name-brush.svg')], capture_output=True, check=True).stdout
    brand = Image.open(io.BytesIO(png)).convert('RGBA')
    shadow = Image.new('RGBA', brand.size, (0, 0, 0, 0))
    shadow.putalpha(brand.getchannel('A').filter(ImageFilter.GaussianBlur(3)).point(lambda v: int(v * 0.8)))
    im.paste((0, 0, 0), (x0 - 4, 52 + 3), shadow)
    im.paste(brand, (x0 - 6, 52), brand)
    d = ImageDraw.Draw(im)
    fp = ImageFont.truetype(F_BOLD, 21, index=IDX[lang])
    pl = d.textlength(t['pill'], font=fp)
    bx = x0 + brand.width + 6
    if bx + pl + 28 > limit:  # 상호 옆에 안 들어가면 아래 줄로
        bx, by = x0, 58 + brand.height + 6
    else:
        by = 58 + brand.height // 2 - 17
    d.rectangle([bx, by, bx + pl + 26, by + 34], outline=GOLD, width=1)
    d.text((bx + 13, by + 4), t['pill'], font=fp, fill=GOLD2)
    y = 58 + brand.height + 4
    if t['name']:
        d.text((x0, max(y, by + 40)), t['name'], font=ImageFont.truetype(F_MED, 24, index=IDX[lang]), fill=IVORY2)

    # 큰 제목 (명조)
    hs = 70
    fh = ImageFont.truetype(F_SERIF_B, hs, index=SIDX[lang])
    while max(d.textlength(t['t1'], font=fh), d.textlength(t['t2'], font=fh)) > limit - x0:
        hs -= 2
        fh = ImageFont.truetype(F_SERIF_B, hs, index=SIDX[lang])
    ty = 238
    d.text((x0, ty), t['t1'], font=fh, fill=IVORY)
    d.text((x0, ty + hs + 14), t['t2'], font=fh, fill=IVORY)

    # 금색 짧은 선 + 전화 + 주소
    ly = ty + 2 * hs + 58
    d.line([(x0, ly), (x0 + 64, ly)], fill=GOLD, width=2)
    ft = ImageFont.truetype(F_BOLD, 30, index=IDX[lang])
    while d.textlength(t['tel'], font=ft) > limit - x0 and ft.size > 22:
        ft = ImageFont.truetype(F_BOLD, ft.size - 1, index=IDX[lang])
    d.text((x0, ly + 18), t['tel'], font=ft, fill=IVORY)
    fa = ImageFont.truetype(F_MED, 22, index=IDX[lang])
    while d.textlength(t['addr'], font=fa) > limit - x0 and fa.size > 16:
        fa = ImageFont.truetype(F_MED, fa.size - 1, index=IDX[lang])
    d.text((x0, ly + 62), t['addr'], font=fa, fill=IVORY2)

    out = ROOT / 'src/assets/images/og' / f'og-{lang}.jpg'
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, quality=86, optimize=True, progressive=True)
    print(out.relative_to(ROOT))


if __name__ == '__main__':
    photo = Image.open(ROOT / 'src/assets/images/works/chowol-owner-2.jpg').convert('RGB')
    wood = Image.open(ROOT / 'public/tex/walnut.webp').convert('RGB')
    for lang, t in TXT.items():
        make(lang, t, photo, wood)
