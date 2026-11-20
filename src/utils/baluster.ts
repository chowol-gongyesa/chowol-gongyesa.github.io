// 난간 동자 모양 — 첫 화면 난간, 입장 화면, 복제 장면, 공유 이미지(scripts/make_og.py)가 같은 모양을 씁니다.
// r(y): 높이 y(0~300)에서의 반지름. 숫자를 바꾸면 모든 곳의 동자 모양이 함께 바뀝니다.
export const profile = (y: number): number => {
  if (y < 40) return 14; // 위쪽 네모 머리
  if (y < 44) return 14 - (y - 40); // 깎아 들어감
  if (y < 58) return 10 + 3.5 * Math.sin((Math.PI * (y - 44)) / 14); // 구슬
  if (y < 66) return 9 - ((y - 58) / 8) * 2.5; // 목
  if (y < 232) return 6.5 + 9.5 * Math.sin(Math.PI * Math.pow((y - 66) / 166, 1.6)); // 배불뚝이 몸통
  if (y < 236) return 6.5 + ((y - 232) / 4) * 3.5;
  if (y < 248) return 10 + 3.5 * Math.sin((Math.PI * (y - 236)) / 12); // 아래 구슬
  if (y < 252) return 10 + ((y - 248) / 4) * 4;
  return 14; // 아래쪽 네모 받침
};

/** 세로로 선 동자 (viewBox 0 0 36 300). step: 몇 픽셀마다 점을 찍을지 (작을수록 매끈하지만 HTML이 커짐) */
export const verticalPath = (step = 2): string => {
  const left: string[] = [];
  const right: string[] = [];
  for (let y = 0; y <= 300; y += step) {
    const r = profile(y);
    left.push(`${(18 - r).toFixed(1)} ${y}`);
    right.unshift(`${(18 + r).toFixed(1)} ${y}`);
  }
  return `M${left.join(' L')} L${right.join(' L')} Z`;
};

/** 로구로에 가로로 물린 동자: x0에서 길이 len, 가운데 선 cy, 굵기 배율 k */
export const horizontalPath = (x0: number, len: number, cy: number, k: number): string => {
  const top: string[] = [];
  const bottom: string[] = [];
  for (let i = 0; i <= 150; i += 1) {
    const y = (i / 150) * 300;
    const r = profile(y) * k;
    const x = x0 + (i / 150) * len;
    top.push(`${x.toFixed(1)} ${(cy - r).toFixed(1)}`);
    bottom.unshift(`${x.toFixed(1)} ${(cy + r).toFixed(1)}`);
  }
  return `M${top.join(' L')} L${bottom.join(' L')} Z`;
};
