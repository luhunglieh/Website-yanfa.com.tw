export interface SiteConfig {
  name: string;
  title: string;
  description: string;
  companyName: string;
  address: string;
  phone: string;
  fax: string;
  email: string;
  mapUrl: string;
  navItems: { label: string; href: string }[];
  googleAnalyticsId?: string;
}

export const siteConfig: SiteConfig = {
  name: '仰發科技',
  title: '仰發科技有限公司 | 專業半導體及電子零件代理與經銷商',
  description: '仰發科技成立於西元2007年，專營代理經銷國內外知名半導體零件產品，包含全系列 MOSFET、電晶體、二極體、三極體、電解電容、固態電容、LED、第三代半導體 SiC 等。',
  companyName: '仰發科技有限公司',
  address: '235 新北市中和區建八路181號2樓',
  phone: '02-2228-6936',
  fax: '02-2228-1776',
  email: 'jane.sun@yanfa.com.tw',
  mapUrl: 'https://goo.gl/maps/A827R63W6FQ11LiMA',
  googleAnalyticsId: 'G-TQDJH1PPH4',
  navItems: [
    { label: '關於我們', href: '/' },
    { label: '代理品牌', href: '/brands/' },
    { label: '經銷服務', href: '/dealer/' }
  ]
};
