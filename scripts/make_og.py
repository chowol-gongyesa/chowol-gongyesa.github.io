"""공유 미리보기 이미지(카톡·SNS에 주소를 보낼 때 보이는 그림) 만들기.

결과: src/assets/images/og/og-ko|en|ja|zh.jpg (1200x630)
필요한 것: Python 3 + Pillow, Noto Sans CJK 글꼴 (아래 FONT_DIR). Claude 작업 환경(리눅스)에서 만들었습니다.
전화번호나 문구가 바뀌면 TXT를 고치고 다시 실행하세요:  python3 scripts/make_og.py
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = Path('/usr/share/fonts/opentype/noto')
F_BLACK, F_BOLD, F_MED = (str(FONT_DIR / n) for n in ('NotoSansCJK-Black.ttc', 'NotoSansCJK-Bold.ttc', 'NotoSansCJK-Medium.ttc'))
IDX = {'ko': 1, 'ja': 0, 'zh': 2, 'en': 1}  # 글꼴 묶음 안의 언어 순서
SIGN, WHITE, PILL, WOOD = (34, 70, 166), (255, 255, 255), (214, 58, 44), (231, 211, 176)

TXT = {
    'ko': dict(brand='초월공예사', pill='로구로 전문', t1='같은 모양을', t2='몇 개든 똑같이', tel='상담전화 010-8548-7264', addr='경기 광주시 초월읍'),
    'en': dict(brand='Chowol Craft', pill='Woodturning', t1='The same shape,', t2='as many as you need', tel='Call +82 10-8548-7264', addr='Gwangju, Gyeonggi-do, Korea'),
    'ja': dict(brand='チョウォル工芸社', pill='ろくろ専門', t1='同じ形を、', t2='いくつでもそっくりに', tel='ご相談 +82 10-8548-7264', addr='韓国 京畿道 広州市'),
    'zh': dict(brand='Chowol 工艺社', pill='木工车床专营', t1='同样的形状，', t2='要多少，车多少', tel='咨询 +82 10-8548-7264', addr='韩国 京畿道 广州市'),
}


def r(y):
    """난간 동자 모양 (src/components/widgets/Balustrade.astro와 같은 식)"""
    if y < 40: return 14
    if y < 44: return 14 - (y - 40)
    if y < 58: return 10 + 3.5 * math.sin(math.pi * (y - 44) / 14)
    if y < 66: return 9 - ((y - 58) / 8) * 2.5
    if y < 232: return 6.5 + 9.5 * math.sin(math.pi * ((y - 66) / 166) ** 1.6)
    if y < 236: return 6.5 + ((y - 232) / 4) * 3.5
    if y < 248: return 10 + 3.5 * math.sin(math.pi * (y - 236) / 12)
    if y < 252: return 10 + ((y - 248) / 4) * 4
    return 14


def make(lang, t, photo):
    W, H = 1200, 630
    im = Image.new('RGB', (W, H), SIGN)
    d = ImageDraw.Draw(im)
    pw, ph = 400, 500
    px, py = W - pw - 60, 40
    d.rectangle([px - 10, py - 10, px + pw + 10, py + ph + 10], fill=WHITE)
    im.paste(ImageOps.fit(photo, (pw, ph), Image.LANCZOS, centering=(0.5, 0.45)), (px, py))
    by = H - 70
    d.rectangle([0, by - 8, W, by], fill=WOOD)
    n, s = 24, 0.2
    for k in range(n):
        cx = 25 + k * (W - 50) / (n - 1)
        pts = [(cx - r(y) * s, by + y * s) for y in range(0, 301)] + [(cx + r(y) * s, by + y * s) for y in range(300, -1, -1)]
        d.polygon(pts, fill=WOOD)
    idx = IDX[lang]
    x0, y0, limit = 64, 58, px - 40
    size = 64
    while True:
        fb = ImageFont.truetype(F_BLACK, size, index=idx)
        fp = ImageFont.truetype(F_BOLD, max(20, round(size * 0.4)), index=idx)
        bw = d.textlength(t['brand'], font=fb)
        pwid = d.textlength(t['pill'], font=fp) + 36
        if x0 + bw + 18 + pwid <= limit or size <= 44:
            break
        size -= 2
    d.text((x0, y0), t['brand'], font=fb, fill=WHITE)
    pxl, pyl = x0 + bw + 18, y0 + round(size * 0.38)
    ph_ = round(size * 0.69)
    d.rounded_rectangle([pxl, pyl, pxl + pwid, pyl + ph_], radius=ph_ // 2, fill=WHITE)
    d.text((pxl + 18, pyl + round(ph_ * 0.07)), t['pill'], font=fp, fill=PILL)
    hs = 70
    fh = ImageFont.truetype(F_BLACK, hs, index=idx)
    while max(d.textlength(t['t1'], font=fh), d.textlength(t['t2'], font=fh)) > limit - x0:
        hs -= 2
        fh = ImageFont.truetype(F_BLACK, hs, index=idx)
    d.text((x0, 200), t['t1'], font=fh, fill=WHITE)
    d.text((x0, 200 + hs + 14), t['t2'], font=fh, fill=WHITE)
    d.text((x0, 410), t['tel'], font=ImageFont.truetype(F_BOLD, 32, index=idx), fill=WHITE)
    d.text((x0, 458), t['addr'], font=ImageFont.truetype(F_MED, 26, index=idx), fill=(220, 228, 245))
    out = ROOT / 'src/assets/images/og' / f'og-{lang}.jpg'
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, quality=86, optimize=True, progressive=True)
    print(out.relative_to(ROOT))


if __name__ == '__main__':
    photo = Image.open(ROOT / 'src/assets/images/works/chowol-09.jpg').convert('RGB')
    for lang, t in TXT.items():
        make(lang, t, photo)
