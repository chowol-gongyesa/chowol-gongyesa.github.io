"""(예전 시안) 초월공예사 로고 그림 만들기 — '나무로 깎은 글자' + '나이테 원판'.
2026-11-21에 상호를 '먹 붓글씨 + 붉은 낙관'(public/brand/name-brush.svg)으로 바꿔서, 여기서 만드는 그림은 지금 사이트에서 쓰지 않습니다.
파비콘은 scripts/make_favicon.py 가 만듭니다 (이 파일을 다시 돌려도 파비콘은 건드리지 않음).

결과 (public/brand/):
  wordmark.webp        나무를 깎아 만든 것 같은 '초월공예사' 글자 (투명 바탕)
  wordmark-mask.webp   로고 위 반짝임 효과용 글자 모양 (흰색)
  emblem.webp, logo-h.webp, logo-mask.webp  나이테 원판과 원판+글자 가로형
필요한 것: Python 3 + numpy + scipy + Pillow, Noto Serif CJK 글꼴. Claude 작업 환경(리눅스)에서 만들었습니다.
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from scipy import ndimage

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public/brand'
OUT.mkdir(parents=True, exist_ok=True)
FONT = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Black.ttc'
KR = 1  # 글꼴 묶음 안의 한국어(KR) 순서
rng = np.random.default_rng(7)


def noise(h, w, sx, sy, seed):
    r = np.random.default_rng(seed)
    F = np.fft.fft2(r.standard_normal((h, w)))
    ky = np.fft.fftfreq(h)[:, None] * h
    kx = np.fft.fftfreq(w)[None, :] * w
    filt = np.exp(-(kx / sx) ** 2 - (ky / sy) ** 2)
    filt[0, 0] = 0
    n = np.real(np.fft.ifft2(F * filt))
    return (n - n.mean()) / (n.std() + 1e-9)


def wood_texture(h, w, light, dark, cycles, seed, warp=0.9):
    """가로결 나무 무늬 (0~255 RGB)"""
    w1 = noise(h, w, 2.0, 1.5, seed)
    w2 = noise(h, w, 7, 5, seed + 1)
    y = np.arange(h)[:, None] / h
    phase = y * cycles + warp * w1 + 0.3 * w2
    ring = phase - np.floor(phase)
    late = np.clip((ring - 0.6) / 0.4, 0, 1) ** 1.7
    fib = noise(h, w, 18, 340, seed + 2)
    t = np.clip(0.74 - 0.5 * late + 0.06 * fib, 0, 1)[..., None]
    L, D = np.array(light, float), np.array(dark, float)
    return D + (L - D) * t


def shade(mask, bevel, light=(-0.5, -0.62, 0.6), dome=0.12):
    """마스크(0~1)에서 깎아 낸 듯한 높이와 빛을 계산 → (diffuse, spec, height)"""
    inside = mask > 0.5
    dist = ndimage.distance_transform_edt(inside)
    hgt = np.clip(dist / bevel, 0, 1)
    hgt = np.sin(hgt * np.pi / 2) + dome * np.clip(dist / (bevel * 6), 0, 1)
    hgt = ndimage.gaussian_filter(hgt, bevel * 0.08)
    gy, gx = np.gradient(hgt * bevel * 1.1)
    nz = np.ones_like(gx)
    n = np.stack([-gx, -gy, nz], -1)
    n /= np.linalg.norm(n, axis=-1, keepdims=True)
    l = np.array(light) / np.linalg.norm(light)
    diff = np.clip((n * l).sum(-1), 0, 1)
    hvec = l + np.array([0, 0, 1.0])
    hvec /= np.linalg.norm(hvec)
    spec = np.clip((n * hvec).sum(-1), 0, 1) ** 40
    return diff, spec, hgt


def carved(mask, wood, bevel):
    """나무 무늬 + 깎은 빛 + 그림자 + 가는 어두운 테두리를 입힌 RGBA"""
    diff, spec, hgt = shade(mask, bevel)
    ao = 0.78 + 0.22 * np.clip(hgt, 0, 1)
    rgb = wood * (0.5 + 0.62 * diff[..., None]) * ao[..., None] + 255 * 0.14 * spec[..., None]
    rgb = np.clip(rgb, 0, 255)
    h, w = mask.shape
    # 그림자 (오른쪽 아래로 부드럽게)
    sh = ndimage.gaussian_filter(mask, bevel * 0.9)
    sh = np.roll(np.roll(sh, int(bevel * 0.55), 0), int(bevel * 0.3), 1)
    # 가는 어두운 테두리 (밝은 배경에서도 모양이 보이게)
    edge = ndimage.binary_dilation(mask > 0.5, iterations=max(2, int(bevel * 0.18))).astype(float)
    edge = ndimage.gaussian_filter(edge, 1.2)
    out = np.zeros((h, w, 4))
    # 그림자 → 테두리 → 글자 순으로 겹침
    a_sh = np.clip(sh * 0.75, 0, 1)
    out[..., :3] = np.array([10, 6, 3]) * 1.0
    out[..., 3] = a_sh
    a_edge = np.clip(edge, 0, 1) * 0.95
    out[..., :3] = out[..., :3] * (1 - a_edge[..., None]) + np.array([22, 14, 8]) * a_edge[..., None]
    out[..., 3] = a_edge + out[..., 3] * (1 - a_edge)
    a = np.clip(mask, 0, 1)
    out[..., :3] = out[..., :3] * (1 - a[..., None]) + rgb * a[..., None]
    out[..., 3] = a + out[..., 3] * (1 - a)
    return out


def to_img(arr):
    a = arr.copy()
    a[..., :3] = np.clip(a[..., :3], 0, 255)
    a[..., 3] = np.clip(a[..., 3] * 255, 0, 255)
    return Image.fromarray(a.astype(np.uint8), 'RGBA')


def trim(img, pad=0):
    bbox = img.getchannel('A').point(lambda v: 255 if v > 6 else 0).getbbox()
    l, t, r, b = bbox
    return img.crop((max(0, l - pad), max(0, t - pad), min(img.width, r + pad), min(img.height, b + pad)))


# ── 1) 글자 '초월공예사'
S = 3  # 크게 그린 뒤 줄여서 매끈하게
size = 260 * S
font = ImageFont.truetype(FONT, size, index=KR)
text = '초월공예사'
l, t, r, b = font.getbbox(text)
W, H = r - l + 80 * S, b - t + 80 * S
m = Image.new('L', (W, H), 0)
ImageDraw.Draw(m).text((40 * S - l, 40 * S - t), text, font=font, fill=255)
mask = np.array(m).astype(float) / 255
wood = wood_texture(H, W, (240, 204, 146), (176, 122, 68), cycles=7, seed=11, warp=1.1)
word = to_img(carved(mask, wood, bevel=6 * S))
word = trim(word, pad=6 * S)
word_s = word.resize((word.width // S, word.height // S), Image.LANCZOS)
word_s.save(OUT / 'wordmark.webp', quality=88, method=6)
wmask = Image.new('RGBA', word_s.size, (255, 255, 255, 0))
wmask.putalpha(word_s.getchannel('A').point(lambda v: 255 if v > 200 else 0))
wmask.save(OUT / 'wordmark-mask.webp', quality=90, method=6)

# ── 2) 나이테 원판
R = 300 * S
D = 2 * R + 60 * S
yy, xx = np.mgrid[0:D, 0:D].astype(float)
cx = cy = D / 2
dx, dy = xx - cx, yy - cy
rad = np.sqrt(dx ** 2 + dy ** 2)
ang = np.arctan2(dy, dx)
edge_n = 1 + 0.022 * np.sin(ang * 3 + 0.7) + 0.012 * np.sin(ang * 7 + 2.1) + 0.006 * np.sin(ang * 13)
r_norm = rad / (R * edge_n)
disc = np.clip((1 - r_norm) * R / 2.0, 0, 1)  # 가장자리 부드럽게
# 나이테: 가운데(심)에서 멀어질수록 간격이 조금씩 좁아짐, 살짝 일그러짐
warp = 0.05 * noise(D, D, 3, 3, 21) + 0.02 * np.sin(ang * 2 + 0.5)
rr = np.clip(r_norm + warp * r_norm, 0, 2)
rings = 18 * rr ** 0.85
ring = rings - np.floor(rings)
late = np.clip((ring - 0.68) / 0.32, 0, 1) ** 1.6
fib = noise(D, D, 30, 30, 23)
tone = np.clip(0.78 - 0.42 * late + 0.05 * fib - 0.12 * np.clip(r_norm - 0.85, 0, 1) / 0.15, 0, 1)
L, Dk = np.array((238, 202, 142), float), np.array((176, 120, 66), float)
rgb = Dk + (L - Dk) * tone[..., None]
# 심(가운데 작은 점)과 갈라진 금
pith = np.exp(-(rad / (R * 0.035)) ** 2)
rgb = rgb * (1 - 0.55 * pith[..., None])
crack = np.exp(-((ang - 0.9) * rad / (R * 0.012)) ** 2) * np.clip((r_norm - 0.45) / 0.4, 0, 1) * np.clip((0.97 - r_norm) / 0.05, 0, 1)
rgb = rgb * (1 - 0.5 * crack[..., None])
# 껍질 테
bark = np.clip((r_norm - 0.9) / 0.04, 0, 1)
bark_tex = 0.55 + 0.25 * noise(D, D, 60, 60, 25)
bark_rgb = np.array((70, 44, 26), float)[None, None, :] * bark_tex[..., None]
rgb = rgb * (1 - bark[..., None]) + bark_rgb * bark[..., None]
# 둥근 판의 빛 (위쪽 왼편이 밝게) + 가장자리 깎은 빛
dmask = (r_norm < 1).astype(float)
diff, spec, hgt = shade(dmask, bevel=14 * S, dome=0.25)
rgb = rgb * (0.5 + 0.62 * diff[..., None]) + 255 * 0.18 * spec[..., None]
arr = np.zeros((D, D, 4))
sh = ndimage.gaussian_filter(dmask, 10 * S)
sh = np.roll(np.roll(sh, 8 * S, 0), 4 * S, 1)
arr[..., :3] = np.array([10, 6, 3])
arr[..., 3] = sh * 0.7
a = disc
arr[..., :3] = arr[..., :3] * (1 - a[..., None]) + np.clip(rgb, 0, 255) * a[..., None]
arr[..., 3] = a + arr[..., 3] * (1 - a)
emblem = trim(to_img(arr), pad=4 * S)
emblem_s = emblem.resize((emblem.width // S, emblem.height // S), Image.LANCZOS)
emblem_s.save(OUT / 'emblem.webp', quality=88, method=6)

# ── 3) 가로형: 원판 + 글자
eh = int(word_s.height * 1.08)
em = emblem_s.resize((int(emblem_s.width * eh / emblem_s.height), eh), Image.LANCZOS)
gap = int(word_s.height * 0.22)
canvas = Image.new('RGBA', (em.width + gap + word_s.width, max(em.height, word_s.height)), (0, 0, 0, 0))
canvas.alpha_composite(em, (0, (canvas.height - em.height) // 2))
canvas.alpha_composite(word_s, (em.width + gap, (canvas.height - word_s.height) // 2))
canvas.save(OUT / 'logo-h.webp', quality=88, method=6)
# 반짝임용 모양 (글자만 흰색)
mask_img = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
wm = Image.new('RGBA', word_s.size, (255, 255, 255, 0))
wm.putalpha(word_s.getchannel('A').point(lambda v: 255 if v > 200 else 0))
mask_img.alpha_composite(wm, (em.width + gap, (canvas.height - word_s.height) // 2))
mask_img.save(OUT / 'logo-mask.webp', quality=90, method=6)

# 확인용 미리보기 (어두운 바탕·밝은 바탕)
prev = Image.new('RGB', (canvas.width + 80, canvas.height * 2 + 120), (18, 13, 9))
ImageDraw.Draw(prev).rectangle([0, canvas.height + 60, prev.width, prev.height], fill=(238, 232, 222))
prev.paste(canvas, (40, 30), canvas)
prev.paste(canvas, (40, canvas.height + 90), canvas)
prev.save('/tmp/logo_preview.jpg', quality=90)
print('wordmark', word_s.size, 'emblem', emblem_s.size, 'logo-h', canvas.size)


# ── 4) 파비콘: 상호 첫 글자 '초'를 짙은 바탕에
def favicon():
    import base64
    import io
    a = np.array(word_s.getchannel('A'))
    cols = (a > 40).sum(axis=0)
    x0 = int(np.argmax(cols > 0))
    x1 = x0 + int(np.argmax(cols[x0:] == 0))
    ys = np.nonzero((a[:, x0:x1] > 40).sum(axis=1))[0]
    g = word_s.crop((x0, ys[0], x1, ys[-1] + 1))

    def icon(size, pad, radius=0.22):
        im = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        mk = Image.new('L', (size, size), 0)
        ImageDraw.Draw(mk).rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * radius), fill=255)
        im.paste((24, 16, 10, 255), (0, 0), mk)
        s = (size - 2 * pad) / max(g.width, g.height)
        gg = g.resize((max(1, round(g.width * s)), max(1, round(g.height * s))), Image.LANCZOS)
        im.alpha_composite(gg, ((size - gg.width) // 2, (size - gg.height) // 2))
        return im

    fav = ROOT / 'src/assets/favicons'
    icon(180, 26, 0).convert('RGB').save(fav / 'apple-touch-icon.png')
    icon(256, 30).save(fav / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
    buf = io.BytesIO()
    icon(128, 14).save(buf, 'PNG')
    b64 = base64.b64encode(buf.getvalue()).decode()
    (fav / 'favicon.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 128 128">'
        f'<image width="128" height="128" xlink:href="data:image/png;base64,{b64}"/></svg>')


# favicon()  # 예전 파비콘('초' 한 글자). 지금 파비콘은 scripts/make_favicon.py
