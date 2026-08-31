export interface BrandItem {
  id: string;
  name: string;
  fullName: string;
  logo: string;
  description: string;
  officialUrl: string;
  badge?: string;
}

export const brandsData: BrandItem[] = [
  {
    id: 'jackcon',
    name: 'Jackcon 融欣',
    fullName: 'Jackcon(融欣) Capacitor Electronics Co. Ltd. & Honju Taiwan Co., Ltd.',
    logo: '/src/assets/logos/jackcon.png',
    description: 'Jackcon(融欣) Capacitor Electronics Co. Ltd. & Honju Taiwan Co., Ltd. have driven the top quality, best customer service, vision of innovation and perpetual management since 1983. Providing the high quality products which are all Made In Taiwan is our company tenet throughout the past 35 years till now. To ensure products specs are with customer’s expectations, we adamantly benchmark ourselves to be the new technology-intensive and high value-added industry in Taiwan. Further, by carrying the well reputation, we have been invested to other product lines to provide variety supports to our customers comprehensively.',
    officialUrl: 'https://www.jackcon.com.tw/products.htm',
    badge: '代理品牌'
  },
  {
    id: 'emc',
    name: 'EMC 杰力科技',
    fullName: '杰力科技股份有限公司 (Excelliance MOS Corporation)',
    logo: '/src/assets/logos/emc.png',
    description: '杰力公司成立於民國97年，為一專業功率元件及IC設計公司，產品主要應用於：筆記型電腦、桌上型電腦、電視、電源供應器及其他消費性電子產品等。杰力公司技術及經營團隊擁有豐富的電源系統技術服務、功率半導體元件、製程及封裝設計之學經歷，且具備成功經驗實務，是少數具備垂直整合能力之設計公司。具備整合自身及供應商之技術能力，配合客戶之需求，除提供必要之高效率功率元件IC，更提供使用者快速及完整之解決方案，符合在第一時間將創新及高效能產品推進市場之要求，與上下游成為重要之合作夥伴。主要業務係從事功率元件、電源管理積體電路及電源模組之研究、開發、設計、製造及銷售。',
    officialUrl: 'https://www.excelliancemos.com/products/',
    badge: '代理品牌'
  },
  {
    id: 'niko-sem',
    name: 'NIKO-SEM 尼克森',
    fullName: '尼克森微電子股份有限公司 (NIKO-SEM Microelectronics)',
    logo: '/src/assets/logos/niko-sem.png',
    description: 'NIKO-SEM微電子於1998年總部成立於臺北，為專業之電源管理功率元件及類比IC設計公司，主要產品包括POWER MOSFET功率元件、線性穩壓IC(LDO)、切換型穩壓IC及脈衝控制IC，並廣泛應用於主機板、筆記型電腦、平板電腦等泛PC產品及其週邊電源裝置，以及LED Lighting,車用電子/車充市場,Power Bank 及液晶顯示面板(LCD) 等相關產業領域。NIKO-SEM憑藉著過去在電源系統廠商服務所累積的豐富經驗，堅持在電源管理領域持續深耕，源源不絕地提供國內外系統廠商可靠的產品，並專注實現創新、穩定、高效率及低成本的解決方案。經NIKO-SEM長期努力下，目前已成為少數同時具備低電壓與高電壓高功率元件、類比控制IC、高效率電源供應系統及特殊半導體制程設計能力的IC設計公司，並創造持續穩定的營收成長佳績。',
    officialUrl: 'http://www.niko-sem.com/portal_d743.php',
    badge: '代理品牌'
  },
  {
    id: 'utc',
    name: 'UTC 友順科技',
    fullName: '友順科技股份有限公司 (Unisonic Technologies Co., Ltd.)',
    logo: '/src/assets/logos/utc.png',
    description: '友順科技股份有限公司成立於1990年，專注致力於類比IC及離散式組件Discrete研發、設計、製造、封裝、測試及行銷業務。產品以IC為主(涵蓋Power Management、Amplifier / Comparator、Analog Switches、Hall ICs、Special Application ICs、Logic等)，Discrete為輔(涵蓋Transistors、MOSFETs、TRIACs、SCRs、DIODEs等)，主要產品廣泛應用於通訊產品如行動電話，智慧型電話、LNB、衛星導航裝置、無線通訊設備；消費性電子產品如MP3及PMP、數位相機、可攜式裝置、液晶電視及面板產品等；PC如筆記型電腦、顯示器、鍵盤、無線滑鼠 、主機板、VGA卡、電源供應器、DC FAN、Adapter、外接式硬碟儲存設備及電腦週邊產品等相關市場。',
    officialUrl: 'https://www.unisonic.com.tw/product.htm',
    badge: '代理品牌'
  },
  {
    id: 'brt',
    name: '佰鴻工業',
    fullName: '佰鴻工業股份有限公司 (Bright LED Electronics Corp.)',
    logo: '/src/assets/logos/brt.png',
    description: '佰鴻工業股份有限公司創立於 1981 年7月。客戶群遍及全球各地，在台灣、中國大陸、韓國、東南亞及美洲、歐洲等地都擁有眾多的長期合作客戶，產品被廣泛應用於3C產業、照明市場、車用市場等多個領域。佰鴻生產基地最早建於台灣新北市工業區，主力產品包括發光二極管、顯示模組、紅外線元件模組、貼片型發光二極體及發光二極體應用模組。除了提供給客戶優質及具競爭力的產品外，誠信更是我們與客戶往來一貫秉持的方針，讓佰鴻一直是客戶信賴且願意長期搭配的合作夥伴。此外，佰鴻特別重視與供應商合作的夥伴關係，透過供需雙方的緊密配合及良性溝通，建立穩定而兼顧品質及成本的原物料來源，達到優勢市場競爭力及雙贏的目標。',
    officialUrl: 'https://www.brtled.com//web/product/product.jsp?top_id=none&sub_id=none&oneDm_id=none&upper_id=none',
    badge: '代理品牌'
  },
  {
    id: 'eris',
    name: '德微科技',
    fullName: '德微科技股份有限公司 (Eris Technology Corporation)',
    logo: '/src/assets/logos/eris.png',
    description: '德微科技為一專業 ODM (整流二極體專業供應製造) 廠商，自 1995 年 8 月成立以來，致力於提供整流二極體產品之檢測 Know-How 及提供客戶加值型代工整合服務。為滿足客戶之需求，我們竭力於對二極體的研發、檢測與品保投入相當之心力，因此讓公司之產品極具市場競爭力，未來除維持產品高品質與良率之標準外，我們亦不斷加強研究與專利產品之設計開發，以滿足客戶需求與成為全球二極體專業 OEM 國際大廠的合作夥伴為首要目標。迄今，德微科技之業務範疇已包含整流二極體、蕭特基二極體、TVS 二極體、Zener 二極體、橋式二極體及晶圓，另外也提供 LED 相關產品等零組件之國內外銷售業務。',
    officialUrl: 'https://www.eris.com.tw/product.php',
    badge: '代理品牌'
  },
  {
    id: 'matrix',
    name: 'MATRIX 鑫茂微',
    fullName: '鑫茂微電子 (Matrix Microtech Corp.)',
    logo: '/src/assets/logos/matrix.png',
    description: 'Matrix Microtech intends to provide good performance with cheap cost solutions to local industry. Established in Aug. 2001. We are fabless Power Management company delivering PWM , LDO , MOSFETs , Reset IC and Power Management Solution to consumer and communication markets. Matrix Microtech provide quality & Reliability, competitive cost, flexible lead-time ,better services and make long term partnerships with our customers to multi-win and multi-growth. We bring new solution in manufacturing, and cost reduction without compromising the quality.',
    officialUrl: 'http://www.matrix-microtech.com.tw/products.html',
    badge: '代理品牌'
  },
  {
    id: 'cte',
    name: 'CTE 科特電子',
    fullName: '科特電子 (Coretech Corporation)',
    logo: '/src/assets/logos/cte.png',
    description: '科特電子主要以專業研發製造二三極體/MOSFET晶圓並應用在自有品牌CTE之半導體被動功率元器件為主，堅持著 『專注、創新 、整合、品質、 服務』的經營理念，並提供客戶完整服務。亦提供客製化設計與封裝產品之服務，如TO系列、SMD系列及Axial Lead系列，SOT系列，SOD系列，DFN系列……。經營產品：普通二極體、基納二極體、FRED快恢復二極體、蕭特基二極體、ESD、TVS、BJT、橋堆、MOSFET……等。',
    officialUrl: 'http://www.coretech-corp.com/cpzx/zhengliuqiao/',
    badge: '代理品牌'
  },
  {
    id: 'basic',
    name: 'BASiC 基本半導體',
    fullName: '深圳基本半導體有限公司 (BASiC Semiconductor)',
    logo: '/src/assets/logos/basic.png',
    description: '基本半導體(BASiC)有限公司是中國深圳第三代半導體行業領導企業，專業從事碳化矽功率元件的研發與產業化。公司擁有一支國際化的研發團隊，核心成員包括二十多位來自清華大學、中國科學院、英國劍橋大學、德國阿亨工業大學、瑞典皇家理工學院、瑞士聯邦理工學院等國內外知名高校及研究機構的博士。基本半導體掌握國際領先的碳化矽核心技術，研發覆蓋碳化矽功率元件的材料製備、晶片設計、封裝測試、驅動應用等產業鏈關鍵環節，累計獲得兩百多項專利授權，核心產品包括碳化矽二極體和MOSFET晶片、汽車級碳化矽功率模組、碳化矽驅動晶片等，性能達到國際先進水準，服務于能源儲能、電動汽車、大眾交通、工業控制、智慧電網等領域的全球數百家客戶。',
    officialUrl: 'https://www.basicsemi.com/tcn/h-col-106.html',
    badge: '代理品牌'
  }
];
