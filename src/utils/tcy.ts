/** 세로쓰기 글씨에서 숫자(예: 40)를 옆으로 눕히지 않고 한 칸에 세워 쓰도록 감쌈 (set:html 용, 사이트 문구에만 사용) */
export const tcy = (text: string) =>
  text.replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' })[c] as string).replace(/(\d+)/g, '<span class="tcy">$1</span>');
