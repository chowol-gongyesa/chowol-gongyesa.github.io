// 가게 기본 정보 — 전화번호·주소가 바뀌면 이 파일과 src/i18n/ 의 각 언어 파일(shop 부분)을 고치세요.
import { useT, type Lang } from '~/i18n';

export const SHOP = {
  name: '초월공예사',
  prefix: '', // 상호 위에 얹는 호(성창공예는 '거목'). 표시는 BrandCrown.astro — TODO: 쓸지 정하기
  nameEn: 'CHOWOL CRAFT', // TODO: 영문 표기 사장님께 확인
  owner: '정영순', // 대표 (명함·사업자등록증)
  address: '경기도 광주시 초월읍 경충대로963번길 35',
  addressShort: '경기 광주시 초월읍 경충대로963번길 35',
  hours: '', // TODO: 영업시간
  closed: '', // TODO: 휴무일
  tel: { label: '031-797-0783', href: 'tel:0317970783' }, // 가게 전화 (명함)
  tel2: { label: '', href: '' }, // 두 번째 전화 없음 → 쓰는 곳 정리 필요. 팩스 031-797-0784 (명함)
  mobile: { label: '010-5216-4554', href: 'tel:01052164554', sms: 'sms:01052164554' }, // 명함에 가장 크게 적힌 번호
};

// 해외에서도 걸리는 국제 번호 (외국어 페이지에서 사용) — TODO
const INTL = {
  tel: 'tel:+82317970783',
  tel2: '',
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
