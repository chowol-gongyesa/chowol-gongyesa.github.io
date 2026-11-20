"""공유 미리보기 이미지(카톡·SNS에 주소를 보낼 때 보이는 그림) 만들기.

결과: src/assets/images/og/og-ko|en|ja|zh.jpg (1200x630)
필요한 것: Python 3 + Pillow, Noto Sans/Serif CJK 글꼴 (아래 FONT_DIR). Claude 작업 환경(리눅스)에서 만들었습니다.
홈페이지와 같은 '쪽빛 공방' 모양: 밤 작업장 쪽빛 바탕, 원목 액자에 넣은 대표 사진, 주홍 낙관, 아래쪽 난간.
전화번호나 문구가 바뀌면 TXT를 고치고 다시 실행하세요:  python3 scripts/make_og.py
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = Path('/usr/share/fonts/opentype/noto')
F_BLACK, F_BOLD, F_MED = (str(FONT_DIR / n) for n in ('NotoSansCJK-Black.ttc', 'NotoSansCJK-Bold.ttc', 'NotoSansCJK-Medium.ttc'))
F_SERIF = str(FONT_DIR / 'NotoSerifCJK-Bold.ttc')
IDX = {'ko': 1, 'ja': 0, 'zh': 2, 'en': 1}  # Sans 글꼴 묶음 안의 언어 순서
SIDX = {'ko': 4, 'ja': 2, 'zh': 0, 'en': 4}  # Serif 글꼴 묶음 안의 언어 순서 (SC, TC, JP, HK, KR)
NIGHT, NIGHT2, PAPER, VERM, WOOD = (14, 22, 38), (31, 53, 102), (242, 234, 219), (196, 67, 47), (230, 207, 166)

TXT = {
    'ko': dict(brand='초월공예사', pill='로구로 전문', t1='같은 모양을', t2='한결같이', tel='상담전화 010-8548-7264', addr='경기 광주시 초월읍, 로구로 40년'),
    'en': dict(brand='Chowol Craft', pill='Woodturning', t1='The same shape,', t2='every single time', tel='Call +82 10-8548-7264', addr='Gwangju, Korea. 40 years at the lathe'),
    'ja': dict(brand='チョウォル工芸社', pill='ろくろ専門', t1='同じかたちを、', t2='ひとすじに', tel='ご相談 +82 10-8548-7264', addr='韓国 京畿道 広州市、ろくろ一筋40年'),
    'zh': dict(brand='Chowol 工艺社', pill='木工车床专营', t1='同一个形状，', t2='始终如一', tel='咨询 +82 10-8548-7264', addr='韩国 京畿道 广州市，木工车床40年'),
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


def tile(tex, w, h):
    """나무 결 그림을 (w, h) 크기로 이어 붙임"""
    out = Image.new('RGB', (w, h))
    for x in range(0, w, tex.width):
        for y in range(0, h, tex.height):
            out.paste(tex, (x, y))
    return out


def make(lang, t, photo, wood_light, wood_dark):
    W, H = 1200, 630
    # 밤 작업장 쪽빛: 위쪽 가운데가 조금 밝은 둥근 빛
    im = Image.new('RGB', (W, H), NIGHT)
    glow = Image.new('L', (W, H), 0)
    ImageDraw.Draw(glow).ellipse([-200, -380, 1100, 420], fill=150)
    glow = glow.filter(ImageFilter.GaussianBlur(160))
    im = Image.composite(Image.new('RGB', (W, H), NIGHT2), im, glow)
    d = ImageDraw.Draw(im)
    # 원목 액자에 넣은 사진
    pw, ph = 380, 470
    px, py = W - pw - 70, 44
    frame = tile(wood_dark, pw + 28, ph + 28)
    im.paste(frame, (px - 14, py - 14))
    im.paste(ImageOps.fit(photo, (pw, ph), Image.LANCZOS, centering=(0.5, 0.35)), (px, py))
    # 낙관
    sx, sy, ss = px - 58, py + ph - 70, 84
    seal = Image.new('RGBA', (ss, ss), (0, 0, 0, 0))
    sd = ImageDraw.Draw(seal)
    sd.rounded_rectangle([0, 0, ss - 1, ss - 1], radius=6, fill=VERM + (255,))
    sd.rounded_rectangle([5, 5, ss - 6, ss - 6], radius=4, outline=(255, 243, 232, 230), width=3)
    fs = ImageFont.truetype(F_SERIF, 30, index=SIDX['ko'])
    for k, ch in enumerate('초월'):
        sd.text((ss / 2, 26 + k * 33), ch, font=fs, fill=(255, 243, 232), anchor='mm')
    seal = seal.rotate(4, resample=Image.BICUBIC, expand=True)
    im.paste(seal, (sx, sy), seal)
    # 아래쪽 난간: 원목 난간대 + 똑같은 동자들
    by = H - 74
    rail = tile(wood_light, W, 12)
    im.paste(rail, (0, by - 12))
    mask = Image.new('L', (W, H), 0)
    md = ImageDraw.Draw(mask)
    n, s_ = 26, 0.22
    for k in range(n):
        cx = 22 + k * (W - 44) / (n - 1)
        pts = [(cx - r(y) * s_, by + y * s_) for y in range(0, 301, 2)] + [(cx + r(y) * s_, by + y * s_) for y in range(300, -1, -2)]
        md.polygon(pts, fill=255)
    im = Image.composite(tile(wood_light, W, H), im, mask)
    d = ImageDraw.Draw(im)
    # 상호 + 띠
    idx, sidx = IDX[lang], SIDX[lang]
    x0, y0, limit = 70, 64, px - 90
    size = 56
    while True:
        fb = ImageFont.truetype(F_BLACK, size, index=idx)
        fp = ImageFont.truetype(F_BOLD, max(18, round(size * 0.4)), index=idx)
        bw = d.textlength(t['brand'], font=fb)
        pwid = d.textlength(t['pill'], font=fp) + 32
        if x0 + bw + 16 + pwid <= limit or size <= 40:
            break
        size -= 2
    d.text((x0, y0), t['brand'], font=fb, fill=(255, 255, 255))
    pxl, pyl = x0 + bw + 16, y0 + round(size * 0.36)
    ph_ = round(size * 0.7)
    d.rounded_rectangle([pxl, pyl, pxl + pwid, pyl + ph_], radius=ph_ // 2, fill=(255, 255, 255))
    d.text((pxl + 16, pyl + round(ph_ * 0.06)), t['pill'], font=fp, fill=VERM)
    # 큰 제목 (명조)
    hs = 76
    fh = ImageFont.truetype(F_SERIF, hs, index=sidx)
    while max(d.textlength(t['t1'], font=fh), d.textlength(t['t2'], font=fh)) > limit - x0:
        hs -= 2
        fh = ImageFont.truetype(F_SERIF, hs, index=sidx)
    d.text((x0, 182), t['t1'], font=fh, fill=PAPER)
    d.text((x0, 182 + hs + 16), t['t2'], font=fh, fill=PAPER)
    # 자 눈금
    ty = 182 + 2 * hs + 52
    for k in range(0, 31):
        x = x0 + k * 8
        d.line([(x, ty), (x, ty - (12 if k % 5 == 0 else 6))], fill=(230, 207, 166), width=1)
    d.text((x0, ty + 18), t['tel'], font=ImageFont.truetype(F_BOLD, 30, index=idx), fill=(255, 255, 255))
    d.text((x0, ty + 62), t['addr'], font=ImageFont.truetype(F_MED, 24, index=idx), fill=WOOD)
    out = ROOT / 'src/assets/images/og' / f'og-{lang}.jpg'
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, quality=86, optimize=True, progressive=True)
    print(out.relative_to(ROOT))


if __name__ == '__main__':
    photo = Image.open(ROOT / 'src/assets/images/works/chowol-07.jpg').convert('RGB')
    wood_light = Image.open(ROOT / 'public/tex/wood-light.webp').convert('RGB').resize((512, 128))
    wood_dark = Image.open(ROOT / 'public/tex/wood-dark.webp').convert('RGB').resize((512, 128))
    for lang, t in TXT.items():
        make(lang, t, photo, wood_light, wood_dark)
