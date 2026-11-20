import { MAP_LINKS, shopFor } from './data/shop';
import { localize, useT, type Lang } from './i18n';

// 상단 메뉴. 소식(블로그)은 꺼 두었습니다 (src/config.yaml의 apps.blog.isEnabled).
export const getHeaderData = (lang: Lang = 'ko') => {
  const t = useT(lang).nav;
  const shop = shopFor(lang);
  return {
    links: [
      { text: t.home, href: localize(lang, '/') },
      { text: t.about, href: localize(lang, '/about') },
      { text: t.services, href: localize(lang, '/services') },
      { text: t.works, href: localize(lang, '/works') },
      { text: t.woods, href: localize(lang, '/woods') },
      { text: t.contact, href: localize(lang, '/contact') },
    ],
    // 전화 단추는 상담전화로 (대표님 청각장애 — src/data/shop.ts 참고)
    actions: [{ variant: 'primary' as const, text: t.call, href: shop.consult.href, icon: 'tabler:phone' }],
  };
};

export const getFooterData = (lang: Lang = 'ko') => {
  const t = useT(lang);
  const shop = shopFor(lang);
  return {
    links: [
      {
        title: t.footer.explore,
        links: [
          { text: t.nav.about, href: localize(lang, '/about') },
          { text: t.nav.services, href: localize(lang, '/services') },
          { text: t.nav.works, href: localize(lang, '/works') },
          { text: t.nav.woods, href: localize(lang, '/woods') },
          { text: t.nav.contact, href: localize(lang, '/contact') },
        ],
      },
      {
        title: t.footer.contact,
        links: [
          { text: `${t.reach.consult} ${shop.consult.label}`, href: shop.consult.href },
          { text: `${t.reach.mobile} ${shop.mobile.label}`, href: shop.mobile.sms },
          { text: `${t.reach.tel} ${shop.tel.label}`, href: shop.tel.href },
          { text: `${t.reach.fax} ${shop.fax}` },
        ],
      },
      {
        title: t.footer.visit,
        links: [
          { text: shop.addressShort, href: lang === 'ko' ? MAP_LINKS.naver : MAP_LINKS.google },
          { text: shop.hours },
          { text: shop.closed },
        ],
      },
    ],
    tagline: t.footer.tagline,
    owner: t.footer.owner,
    footNote: `© ${new Date().getFullYear()} ${shop.name}. ${t.footer.rights}`,
  };
};
