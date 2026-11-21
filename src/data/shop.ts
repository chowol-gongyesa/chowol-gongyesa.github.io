// 가게 기본 정보 — 전화번호·주소가 바뀌면 이 파일과 src/i18n/ 의 각 언어 파일(shop 부분)을 고치세요.
import { useT, type Lang } from '~/i18n';

export const SHOP = {
  name: '초월공예', // 상호: 사업자등록증·명함 기준 '초월공예' (간판에는 '초월공예사'라고 씀 — 간판 안내 문구는 그 글자 그대로) — 사용자 결정 2026-11-21
  nameEn: 'CHOWOL CRAFT', // TODO: 영문 표기 사장님께 확인
  owner: '정영순', // 대표 (명함·사업자등록증)
  address: '경기도 광주시 초월읍 경충대로963번길 35',
  addressShort: '경기 광주시 초월읍 경충대로963번길 35',
  hours: '월~토 08:00~18:00', // 성창공예와 같음 (사용자 확인 2026-11-20)
  closed: '일요일·공휴일 휴무',
  // ⚠️ 대표님이 청각장애가 있으셔서, 사이트의 '전화' 단추는 모두 상담전화(성창공예 사장님이 주문을 대신 받아 주심)로 걸려야 함
  consult: { label: '010-8548-7264', href: 'tel:01085487264' }, // 상담전화 — 큰 '전화하기' 단추
  // 대표님 휴대폰 — 전화도 되지만 '문자 주세요'를 앞세워 안내. 주문서 문자도 이 번호로 감
  mobile: { label: '010-5216-4554', href: 'tel:01052164554', sms: 'sms:01052164554' },
  tel: { label: '031-797-0783', href: 'tel:0317970783' }, // 가게 유선 (명함)
  fax: '031-797-0784', // 팩스 (명함) — 도면 보내기 안내에 씀
};

// 해외에서도 걸리는 국제 번호 (외국어 페이지에서 사용)
const INTL = {
  consult: 'tel:+821085487264',
  mobile: 'tel:+821052164554',
  sms: 'sms:+821052164554',
  tel: 'tel:+82317970783',
};

/** 언어에 맞는 가게 정보 (주소·영업시간 문구, 전화 표기) */
export const shopFor = (lang: Lang) => {
  const all = useT(lang);
  const t = all.shop;
  const ko = lang === 'ko';
  // 문자 앱이 열리면 미리 채워지는 내용 (iPhone·안드로이드 모두 '?&body=' 형식을 알아들음)
  const smsBody = `?&body=${encodeURIComponent(all.reach.smsTemplate)}`;
  return {
    name: t.name,
    address: t.address,
    addressShort: t.addressShort,
    hours: t.hours,
    closed: t.closed,
    consult: { label: t.consultLabel, href: ko ? SHOP.consult.href : INTL.consult },
    mobile: {
      label: t.mobileLabel,
      href: ko ? SHOP.mobile.href : INTL.mobile,
      sms: (ko ? SHOP.mobile.sms : INTL.sms) + smsBody, // 문자 앱이 주문 틀이 채워진 채 열림
      number: (ko ? SHOP.mobile.sms : INTL.sms).replace('sms:', ''), // 번호만 (주문서가 직접 내용을 채울 때)
    },
    tel: { label: t.telLabel, href: ko ? SHOP.tel.href : INTL.tel },
    fax: t.faxLabel,
  };
};

// 네이버·카카오 지도에 아직 가게가 등록되어 있지 않아(2026-11-20 확인) 주소로 검색한 화면을 엽니다.
// 네이버 스마트플레이스에 등록한 뒤에는 가게 화면 주소(map.naver.com/p/entry/place/장소번호)로 바꾸세요.
const q = encodeURIComponent(SHOP.address);
const MAP_HL: Record<Lang, string> = { ko: 'ko', en: 'en', ja: 'ja', zh: 'zh-CN' };

export const MAP_LINKS = {
  naver: `https://map.naver.com/p/search/${q}`,
  kakao: `https://map.kakao.com/link/search/${q}`,
  google: `https://www.google.com/maps/search/?api=1&query=${q}`,
};
export const mapEmbed = (lang: Lang) => `https://maps.google.com/maps?q=${q}&hl=${MAP_HL[lang]}&z=16&output=embed`;

// 깎는 물건 종류. 이름과 설명은 src/i18n/ 의 각 언어 파일 products 부분에 있습니다.
// photo: 대표 사진 (src/data/works.ts의 파일 이름), anchor: 작업물 페이지에서 해당 분류로 이동
export const PRODUCTS = [
  { key: 'rods', photo: 'chowol-01', anchor: 'chowol' },
  { key: 'balusters', photo: 'column-13', anchor: 'column' },
  { key: 'legs', photo: 'column-157', anchor: 'column' },
  { key: 'balls', photo: 'chowol-02', anchor: 'chowol' },
  { key: 'columns', photo: 'column-04', anchor: 'column' },
  { key: 'goods', photo: 'lathe-162', anchor: 'lathe' },
] as const;
export type ProductKey = (typeof PRODUCTS)[number]['key'];
