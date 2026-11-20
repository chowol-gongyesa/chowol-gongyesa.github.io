"""나무 고르기 페이지의 나뭇결 견본 그림 8가지 (가로 견본 + 세로로 세운 동자용). Claude 작업 환경(numpy+Pillow)에서 실행.
결과: public/tex/woods/<key>.webp (480x240), <key>-v.webp (96x800, 결이 세로). 색은 src/data/woods.ts의 colors와 같게."""
from pathlib import Path

import numpy as np
from PIL import Image

OUT = Path(__file__).resolve().parent.parent / 'public/tex/woods'
OUT.mkdir(parents=True, exist_ok=True)

def hexrgb(h):
    h = h.lstrip('#')
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float)

def pnoise(W, H, sx, sy, seed):
    r = np.random.default_rng(seed)
    F = np.fft.fft2(r.standard_normal((H, W)))
    ky = np.fft.fftfreq(H)[:, None] * H
    kx = np.fft.fftfreq(W)[None, :] * W
    filt = np.exp(-(kx / sx) ** 2 - (ky / sy) ** 2)
    filt[0, 0] = 0
    n = np.real(np.fft.ifft2(F * filt))
    return (n - n.mean()) / n.std()

# key: (밝은색, 어두운색, 결 개수, 휘어짐, 늦은재 세기, 물관, 섬유, 씨앗)
SPEC = {
    'zelkova':   ('#c9925a', '#8a5a32', 9, 1.1, 0.75, 0.30, 0.06, 1),
    'oak':       ('#c8a374', '#8f6b42', 11, 0.45, 0.6, 0.45, 0.07, 2),
    'walnut':    ('#7a5236', '#3f2717', 10, 0.8, 0.5, 0.22, 0.05, 3),
    'ash':       ('#dcc49c', '#a88a5e', 10, 0.4, 0.65, 0.30, 0.05, 4),
    'cherry':    ('#b8774c', '#7d4527', 14, 0.6, 0.35, 0.05, 0.04, 5),
    'maple':     ('#ecd8b4', '#c2a679', 16, 0.5, 0.25, 0.03, 0.03, 6),
    'pine':      ('#e2bf85', '#b48447', 7, 0.9, 0.95, 0.0, 0.04, 7),
    'paulownia': ('#e6d3b3', '#bfa37c', 8, 0.7, 0.3, 0.05, 0.03, 8),
}

def grain(W, H, light, dark, cycles, warp_amt, late_amt, pore_amt, fib_amt, seed):
    w1 = pnoise(W, H, 2.0, 1.4, seed * 10 + 1)
    w2 = pnoise(W, H, 6, 4, seed * 10 + 2)
    y = np.arange(H)[:, None] / H
    phase = y * cycles + warp_amt * w1 + 0.25 * warp_amt * w2
    ring = phase - np.floor(phase)
    late = np.clip((ring - 0.6) / 0.4, 0, 1) ** 1.7
    fib = pnoise(W, H, 14, 260, seed * 10 + 3)
    pores = np.clip((pnoise(W, H, 90, 420, seed * 10 + 4) - 1.9) / 0.8, 0, 1)
    broad = pnoise(W, H, 1.3, 1.1, seed * 10 + 5)
    t = 0.72 - late_amt * 0.62 * late + fib_amt * fib - pore_amt * pores + 0.05 * broad
    t = np.clip(t, 0, 1)[..., None]
    L, D = hexrgb(light), hexrgb(dark)
    rgb = D + (L - D) * t
    return np.clip(rgb, 0, 255).astype(np.uint8)

for key, (lc, dc, cyc, warp, late, pore, fib, seed) in SPEC.items():
    a = grain(960, 480, lc, dc, cyc, warp, late, pore, fib, seed)
    Image.fromarray(a).resize((480, 240), Image.LANCZOS).save(OUT / f'{key}.webp', quality=80, method=6)
    # 세로 결 (동자에 입힘): 가로 그림을 90도 돌려서 길게
    b = grain(1600, 192, lc, dc, cyc * 0.6, warp * 0.5, late, pore, fib, seed + 50)
    Image.fromarray(b).rotate(90, expand=True).resize((96, 800), Image.LANCZOS).save(OUT / f'{key}-v.webp', quality=80, method=6)
print('ok')
