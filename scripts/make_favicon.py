"""파비콘(브라우저 탭 아이콘) 만들기: 붉은 낙관 '초월' (상호 시안 B의 낙관과 같은 모양).
결과: src/assets/favicons/favicon.ico · favicon.svg · apple-touch-icon.png
필요한 것: Python 3 + Pillow, Noto Serif CJK 글꼴. python3 scripts/make_favicon.py
"""
import base64
import io
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FAV = ROOT / 'src/assets/favicons'
FONT = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Black.ttc'
RED, CREAM = (179, 59, 43), (255, 243, 232)


def seal(size, radius=0.12, full=False):
    S = 4  # 크게 그린 뒤 줄임
    n = size * S
    im = Image.new('RGBA', (n, n), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    pad = 0 if full else int(n * 0.04)
    d.rounded_rectangle([pad, pad, n - 1 - pad, n - 1 - pad], radius=int(n * radius), fill=RED + (255,))
    b = int(n * 0.085)
    d.rounded_rectangle([pad + b, pad + b, n - 1 - pad - b, n - 1 - pad - b], radius=int(n * radius * 0.6),
                        outline=CREAM + (235,), width=max(2, int(n * 0.035)))
    font = ImageFont.truetype(FONT, int(n * 0.36), index=1)
    for k, ch in enumerate('초월'):
        d.text((n / 2, n * (0.32 + 0.37 * k)), ch, font=font, fill=CREAM + (255,), anchor='mm')
    return im.resize((size, size), Image.LANCZOS)


seal(180, full=True).convert('RGB').save(FAV / 'apple-touch-icon.png')
seal(256).save(FAV / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
buf = io.BytesIO()
seal(128).save(buf, 'PNG')
(FAV / 'favicon.svg').write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 128 128">'
    f'<image width="128" height="128" xlink:href="data:image/png;base64,{base64.b64encode(buf.getvalue()).decode()}"/></svg>')
prev = Image.new('RGB', (300, 140), (238, 232, 222))
for i, sz in enumerate((128, 48, 32, 16)):
    im = seal(sz)
    prev.paste(im, (6 + [0, 140, 200, 245][i], 6), im)
prev.save('/tmp/favicon_preview.png')
print('favicons ok')
