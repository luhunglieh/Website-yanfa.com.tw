export interface DealerItem {
  id: string;
  name: string;
  fullName: string;
  logo: string;
  description: string;
  officialUrl: string;
  badge?: string;
}

export const dealersData: DealerItem[] = [
  {
    id: 'littelfuse',
    name: 'Littelfuse',
    fullName: 'Littelfuse, Inc.',
    logo: '/src/assets/logos/littelfuse.png',
    description: 'Littelfuse是一家工業技術製造公司，致力於為可持續發展、互聯互通和更安全的世界提供動力。憑藉覆蓋15多個國家的業務和17,000名全球員工，我們與客戶合作設計和交付創新、可靠的解決方案。服務於超過100,000家最終客戶，我們的產品每天應用於世界各地的各種工業、運輸和電子終端市場。 Littelfuse成立於1927年，總部位於美國伊利諾伊斯州芝加哥。',
    officialUrl: 'https://www.littelfuse.com/products.aspx',
    badge: '經銷服務'
  },
  {
    id: 'nichicon',
    name: 'NICHICON',
    fullName: 'NICHICON CORPORATION (尼吉康株式會社)',
    logo: '/src/assets/logos/nichicon.png',
    description: 'NICHICON CORPORATION dedicates ourselves to creating valued products that will contribute to a brighter future for society. Product lines include Aluminum electrolytic capacitors, Plastic film capacitors, Small Li-Ion Rechargeable Batteries, Positive thermistors “Posi-R”, Household energy storage systems, Vehicle-to-Home (V2H) systems, EVs/PHVs Quick Charger.',
    officialUrl: 'https://cn-nichicon.com/products/',
    badge: '經銷服務'
  },
  {
    id: 'nippon-chemicon',
    name: 'NIPPON CHEMI-CON',
    fullName: 'NIPPON CHEMI-CON CORPORATION',
    logo: '/src/assets/logos/nippon-chemicon.png',
    description: 'NIPPON CHEMI-CON即將迎來創業90週年，本公司的電器元件多年來始終默默地為人們的生活和社會的技術革新提供後盾。我們認為，本公司的產品和事業活動之所以廣為社會所認可，不僅因為我們擁有從材料到產品一條龍開發的高技術力，還因為我們在開展事業活動時兼顧為社會發展做貢獻，而本公司的企業理念“貢獻對環境和人類有益的技術”正是這一切的根基。',
    officialUrl: 'https://www.chemi-con.co.jp/en/products/list-condenser.php',
    badge: '經銷服務'
  },
  {
    id: 'panasonic',
    name: 'Panasonic',
    fullName: '松下產業科技股份有限公司 (Panasonic Industry Taiwan Co., Ltd.)',
    logo: '/src/assets/logos/panasonic.png',
    description: '松下產業科技股份有限公司成立以來以『用心、信心、感恩心』的服務信條，貫徹永續經營的目標。並積極培養國際性專業人才，引進最新科技商品，提供台灣電子、電機產業之製造商，促進台灣產業升級。提供的產品有電子零組件與裝置。',
    officialUrl: 'https://industrial.panasonic.com/tw/products/capacitors',
    badge: '經銷服務'
  },
  {
    id: 'toshiba',
    name: 'TOSHIBA',
    fullName: '東芝電子 (Toshiba Electronic Devices & Storage Corporation)',
    logo: '/src/assets/logos/toshiba.png',
    description: 'Toshiba has long positioned this basic commitment as the core text of its corporate philosophy, and we formulate strategies and do business grounded in the following beliefs and to contribute to a better world. Committed to people, Committed to the future.',
    officialUrl: 'https://www.global.toshiba/ww/products-solutions/semi-parts.html',
    badge: '經銷服務'
  }
];
