"""어두운 호두나무 결 바탕 그림 (가로·세로 이어 붙여도 이음매가 없게 FFT 노이즈로). Claude 작업 환경(numpy+Pillow)에서 실행.
결과: public/tex/walnut.webp (사이트 .sec-wood 바탕)"""
from pathlib import Path

import numpy as np
from PIL import Image

W, H = 2048, 1024


def pnoise(sx, sy, seed):
    r = np.random.default_rng(seed)
    w = r.standard_normal((H, W))
    F = np.fft.fft2(w)
    ky = np.fft.fftfreq(H)[:, None] * H
    kx = np.fft.fftfreq(W)[None, :] * W
    filt = np.exp(-(kx / sx) ** 2 - (ky / sy) ** 2)
    filt[0, 0] = 0
    n = np.real(np.fft.ifft2(F * filt))
    return (n - n.mean()) / n.std()


warp = pnoise(2.2, 1.6, 11)
warp2 = pnoise(7, 5, 12)
warp3 = pnoise(22, 14, 13)
cycles = 44
y = np.arange(H)[:, None] / H
phase = y * cycles + 1.35 * warp + 0.35 * warp2 + 0.07 * warp3
ring = phase - np.floor(phase)
# 늦은재(짙은 띠): 한 주기 끝쪽에 좁고 진하게, 경계는 부드럽게
late = np.clip((ring - 0.62) / 0.38, 0, 1) ** 1.8
late = late * (0.75 + 0.25 * np.clip(pnoise(6, 40, 14), -2, 2) / 2)
fibers = pnoise(18, 520, 15)          # 가로로 긴 섬유 결
fibers2 = pnoise(60, 900, 16)
pores_n = pnoise(120, 700, 17)
pores = np.clip((pores_n - 2.0) / 0.8, 0, 1)   # 드문드문 짧은 물관(호두나무의 점)
broad = pnoise(1.5, 1.2, 18)           # 판 전체의 큰 색 차이

L = 0.58 - 0.42 * late + 0.06 * fibers + 0.04 * fibers2 - 0.25 * pores + 0.07 * broad
L = np.clip(L, 0, 1)

dark = np.array([18, 12, 8], float)
mid = np.array([78, 55, 36], float)
light = np.array([128, 92, 60], float)
t = L[..., None]
rgb = np.where(t < 0.5, dark + (mid - dark) * (t / 0.5), mid + (light - mid) * ((t - 0.5) / 0.5))
# 붉은 기 살짝 (호두나무)
rgb[..., 0] *= 1.03
img = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))
img.save(Path(__file__).resolve().parent.parent / 'public/tex/walnut.webp', quality=62, method=6)
print('mean', rgb.reshape(-1, 3).mean(0))
