// 가게 기본 정보 — 전화번호·주소가 바뀌면 이 파일과 src/i18n/ 의 각 언어 파일(shop 부분)을 고치세요.
import { useT, type Lang } from '~/i18n';

export const SHOP = {
  name: '초월공예사',
  prefix: '', // 상호 위에 얹는 호(성창공예는 '거목'). 표시는 BrandCrown.astro — TODO: 쓸지 정하기
  nameEn: 'CHOWOL CRAFT', // TODO: 영문 표기 사장님께 확인
  owner: '', // TODO: 대표 이름
  address: '', // TODO: 주소
  addressShort: '',
  hours: '', // TODO: 영업시간
  closed: '', // TODO: 휴무일
  tel: { label: '', href: '' }, // TODO: 가게 전화 (예: { label: '02-000-0000', href: 'tel:020000000' })
  tel2: { label: '', href: '' }, // 두 번째 전화가 없으면 이 항목과 쓰는 곳을 지우기
  mobile: { label: '', href: '', sms: '' }, // TODO: 휴대폰
};

// 해외에서도 걸리는 국제 번호 (외국어 페이지에서 사용) — TODO
const INTL = {
  tel: '',
  tel2: '',
  mobile: '',
  sms: '',
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
