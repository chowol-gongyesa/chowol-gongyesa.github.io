// 가게 기본 정보 — 전화번호·주소가 바뀌면 이 파일과 src/i18n/ 의 각 언어 파일(shop 부분)을 고치세요.
import { useT, type Lang } from '~/i18n';

export const SHOP = {
  name: '초월공예사', // 간판 표기 (명함·사업자등록증은 '초월공예'지만 사이트는 '초월공예사'로 — 사용자 확인 2026-11-20)
  prefix: '', // 상호 위에 얹는 호(성창공예는 '거목'). 표시는 BrandCrown.astro — TODO: 쓸지 정하기
  nameEn: 'CHOWOL CRAFT', // TODO: 영문 표기 사장님께 확인
  owner: '정영순', // 대표 (명함·사업자등록증)
  address: '경기도 광주시 초월읍 경충대로963번길 35',
  addressShort: '경기 광주시 초월읍 경충대로963번길 35',
  hours: '월~토 08:00~18:00', // 성창공예와 같음 (사용자 확인 2026-11-20)
  closed: '일요일·공휴일 휴무',
  // ⚠️ 사장님이 청각장애가 있으셔서, 사이트의 '전화' 단추·링크는 모두 상담전화(성창공예 사장님이 주문을 대신 받아 주심)로 걸려야 함
  tel: { label: '010-8548-7264', href: 'tel:01085487264' }, // 상담전화 — 큰 '전화하기' 단추
  tel2: { label: '031-797-0783', href: 'tel:0317970783' }, // 가게 유선 (명함)
  fax: '031-797-0784', // 팩스 (명함) — 도면 보내기 안내에 쓰기
  // 사장님 휴대폰 — 전화도 되지만 '문자 주세요'를 앞세워 안내. 주문서 문자도 이 번호로 감
  mobile: { label: '010-5216-4554', href: 'tel:01052164554', sms: 'sms:01052164554' },
};

// 해외에서도 걸리는 국제 번호 (외국어 페이지에서 사용)
const INTL = {
  tel: 'tel:+821085487264',
  tel2: 'tel:+82317970783',
  mobile: 'tel:+821052164554',
  sms: 'sms:+821052164554',
};

/** 언어에 맞는 가게 정보 (주소·영업시간 문구, 전화 표기) */
export const shopFor = (lang: Lang) => {
  const t = useT(lang).shop;
  const ko = lang === 'ko';
  return {
    name: SHOP.name,
    nameEn: SHOP.nameEn,
    address: t.address,
    addressShort: t.addressShort,
    hours: t.hours,
    closed: t.closed,
    tel: { label: t.telLabel, href: ko ? SHOP.tel.href : INTL.tel },
    tel2: { label: t.telLabel2, href: ko ? SHOP.tel2.href : INTL.tel2 },
    mobile: { label: t.mobileLabel, href: ko ? SHOP.mobile.href : INTL.mobile, sms: ko ? SHOP.mobile.sms : INTL.sms },
  };
};

const q = encodeURIComponent(SHOP.addressShort);
const MAP_HL: Record<Lang, string> = { ko: 'ko', en: 'en', ja: 'ja', zh: 'zh-CN' };

// 사장님 블로그 등 (바닥글, 소개 페이지에서 연결) — TODO: 있으면 넣기
export const BLOG_URL = '';

export const MAP_LINKS = {
  // TODO: 네이버 지도·카카오맵에서 초월공예사 가게 화면 주소를 찾아 넣기
  naver: '',
  naverReview: '',
  kakao: '',
  google: `https://www.google.com/maps/search/?api=1&query=${q}`,
  embed: `https://maps.google.com/maps?q=${q}&hl=ko&z=17&output=embed`,
};
export const mapEmbed = (lang: Lang) => `https://maps.google.com/maps?q=${q}&hl=${MAP_HL[lang]}&z=17&output=embed`;

// 작업 분야 4가지. 이름과 설명은 src/i18n/ 의 각 언어 파일 services 부분에 있습니다.
export const SERVICES = [
  { key: 'lathe', icon: 'tabler:rotate-clockwise-2' },
  { key: 'column', icon: 'tabler:ruler-measure' },
  { key: 'custom', icon: 'tabler:school' },
  { key: 'furniture', icon: 'tabler:hammer' },
] as const;
export type ServiceKey = (typeof SERVICES)[number]['key'];
