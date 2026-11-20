// 작업물 사진 목록 — 사진 파일은 src/assets/images/works/ 에 있습니다.
// 새 사진을 올리려면 그 폴더에 파일을 넣고 아래 목록에 한 줄 추가하세요.
// w('파일 이름', '한국어 설명', '영어', '일본어', '중국어') 순서입니다.
// 파일 이름 앞부분이 분류입니다: chowol-(초월공예사에서 찍은 사진), column-(기둥·난간·가구 다리), lathe-(로구로 소품·목기)
// column-·lathe- 사진은 성창공예 홈페이지의 로구로 작업 사진입니다 (두 사장님 허락, 2026-11-20).
import type { Lang } from '~/i18n';

export const CATEGORY_KEYS = ['chowol', 'column', 'lathe'] as const;
export type CategoryKey = (typeof CATEGORY_KEYS)[number];

type Captions = Record<Lang, string>;

const w = (file: string, ko: string, en: string, ja: string, zh: string) => ({
  file,
  src: `~/assets/images/works/${file}.jpg`,
  captions: { ko, en, ja, zh } as Captions,
  category: file.split('-')[0] as CategoryKey,
});

const ALL = [
  // ───── 초월공예사에서 찍은 사진 (2026-11-20 카톡으로 받은 사진·영상에서) ─────
  w(
    'chowol-01',
    '자동 로구로로 깎은 긴 테이퍼 봉',
    'Long tapered rods turned on the automatic lathe',
    '自動ろくろで挽いた細長いテーパー棒',
    '自动车床车削的细长锥形棒'
  ),
  w(
    'chowol-02',
    '크기와 나무가 다른 원목 공',
    'Wooden balls in different sizes and woods',
    'サイズや樹種の異なる木の玉',
    '不同尺寸与木种的原木球'
  ),
  w('chowol-09', '자동 로구로가 깎아 낸 부품', 'A part just cut by the automatic lathe', '自動ろくろが削り出した部品', '自动车床刚车好的零件'),
  w('chowol-11', '자동 로구로에 건 각재', 'A square blank loaded in the automatic lathe', '自動ろくろに取り付けた角材', '装上自动车床的方料'),
  w('chowol-12', '모양대로 깎이는 부품', 'The part being cut to shape', '形どおりに削られていく部品', '正在按形状车削的零件'),
  w(
    'chowol-08',
    '로구로 작업을 기다리는 같은 모양 부재',
    'Identical blanks waiting for the lathe',
    'ろくろ加工を待つ同じ形の部材',
    '等待车削的同款木料'
  ),
  w('chowol-03', '로구로로 깎은 원목 조명 받침', 'Lathe-turned wooden lamp base', 'ろくろで挽いた木の照明台', '车削原木灯座'),
  w(
    'chowol-06',
    '자동 로구로에 나무를 거는 정영순 대표',
    'Owner Jeong Yeong-sun loading wood into the automatic lathe',
    '自動ろくろに木材を取り付けるチョン・ヨンスン代表',
    '店主郑永顺将木料装上自动车床'
  ),
  w(
    'chowol-10',
    '같은 모양을 반복해 깎는 자동 로구로',
    'The automatic lathe repeating the same shape',
    '同じ形をくり返し削る自動ろくろ',
    '重复车削同一形状的自动车床'
  ),
  w(
    'chowol-07',
    '손 로구로로 다리를 깎는 정영순 대표',
    'Owner Jeong Yeong-sun turning a leg on the hand lathe',
    '手ろくろで脚を削るチョン・ヨンスン代表',
    '店主郑永顺用手动车床车削桌腿'
  ),
  w('chowol-04', '초월공예사 작업장', 'The Chowol Craft workshop', 'チョウォル工芸社の工房', 'Chowol 工艺社工坊'),
  w('chowol-05', '파란 초월공예사 간판', 'The blue Chowol Craft sign', '青いチョウォル工芸社の看板', '蓝色的 Chowol 工艺社招牌'),

  // ───── 기둥 · 난간 · 가구 다리 ─────
  w(
      'column-171',
      '한 묶음으로 묶은 구슬 모양 기둥',
      'Bundled bead-turned spindles',
      '束ねた玉形の柱',
      '成捆的串珠形柱子'
    ),
  w(
      'column-182',
      '각재에서 완성까지 — 로구로로 기둥 깎는 순서',
      'From square timber to finished column on the lathe',
      '角材から完成まで — ろくろで柱を削る順序',
      '从方料到成品——车削柱子的步骤'
    ),
  w(
      'column-178',
      '1. 각재를 로구로에 겁니다',
      '1. Mounting the square timber on the lathe',
      '1. 角材をろくろに取り付ける',
      '1. 将方料装上车床'
    ),
  w('column-179', '2. 거친 날로 둥글게 깎습니다', '2. Rough-turning it round', '2. 荒削りで丸くする', '2. 粗车成圆形'),
  w('column-180', '3. 아래쪽 모양을 잡습니다', '3. Shaping the lower end', '3. 下側の形を出す', '3. 车出下端造型'),
  w(
      'column-181',
      '4. 위쪽 턱을 깎아 냅니다',
      '4. Cutting the upper collar',
      '4. 上側の段を削り出す',
      '4. 车出上端凸缘'
    ),
  w(
      'column-152',
      '포장을 마친 난간 동자 — 대량 납품',
      'Balusters bundled for a bulk delivery',
      '梱包を終えた手すり子 — 大量納品',
      '打包完成的栏杆立柱——批量交货'
    ),
  w(
      'column-153',
      '난간 동자 대량 납품 — 옆에서 본 모습',
      'Bulk balusters seen from the side',
      '手すり子の大量納品 — 横から',
      '批量栏杆立柱——侧面'
    ),
  w(
      'column-154',
      '묶음으로 포장한 원목 봉',
      'Turned wooden spindles in bundles',
      '束ねて梱包した木の丸棒',
      '成捆包装的原木车削杆'
    ),
  w('column-155', '난간 엄지기둥 여러 개', 'A batch of newel posts', '親柱をまとめて', '一批栏杆端柱'),
  w(
      'column-156',
      '흰색으로 칠한 원목 난간',
      'White-painted wooden balustrade',
      '白く塗装した木の手すり',
      '白色涂装原木栏杆'
    ),
  w(
      'column-157',
      '배불뚝이 모양 테이블 다리 네 개',
      'Four bulbous table legs',
      'ふくらみのあるテーブル脚 4本',
      '四根鼓腹形桌腿'
    ),
  w('column-158', '묶어 둔 원목 테이블 다리', 'Bundled wooden table legs', '束ねた木のテーブル脚', '捆好的原木桌腿'),
  w(
      'column-159',
      '볼트를 끼운 둥근 원목 가구 발',
      'Round wooden furniture feet with bolts',
      'ボルト付きの丸い木の家具脚',
      '带螺栓的圆形原木家具脚'
    ),
  w(
      'column-160',
      '둥근 원목 가구 발 — 위아래 모습',
      'Round wooden furniture feet, top and bottom',
      '丸い木の家具脚 — 上と下',
      '圆形原木家具脚——正反面'
    ),
  w(
      'column-04',
      '꽈배기·장식 기둥 견본',
      'Twisted and decorative column samples',
      'ねじり・装飾柱の見本',
      '麻花柱与装饰柱样品'
    ),
  w(
      'column-14',
      '로구로에서 깎고 있는 기둥',
      'A column being turned on the lathe',
      'ろくろで加工中の柱',
      '车床上正在加工的柱子'
    ),
  w(
      'column-16',
      '로구로에서 깎고 있는 기둥',
      'A column being turned on the lathe',
      'ろくろで加工中の柱',
      '车床上正在加工的柱子'
    ),
  w('column-12', '테이블 다리 수량 제작', 'Table legs made in volume', 'テーブル脚の量産', '批量制作的桌腿'),
  w('column-13', '난간 동자 수량 제작', 'Balusters made in volume', '手すり子の量産', '批量制作的栏杆柱'),
  w('column-06', '계단 난간 동자', 'Stair balusters', '階段の手すり子', '楼梯栏杆柱'),
  w('column-15', '사각 난간 동자', 'Square balusters', '角形の手すり子', '方形栏杆柱'),
  w('column-29', '난간 동자 출고 준비', 'Balusters ready for shipping', '出荷準備中の手すり子', '待出货的栏杆柱'),
  w('column-49', '난간 동자 적재', 'Stacked balusters', '積み上げた手すり子', '堆放的栏杆柱'),
  w('column-37', '기둥 수량 생산', 'Columns in volume production', '柱の量産', '批量生产的柱子'),
  w('column-19', '테이블 다리 묶음', 'Bundled table legs', '束ねたテーブル脚', '成捆的桌腿'),
  w('column-26', '화병형 가구 다리', 'Vase-shaped furniture legs', '花瓶形の家具脚', '花瓶形家具腿'),
  w('column-32', '가구 다리 견본', 'Furniture leg samples', '家具脚の見本', '家具腿样品'),
  w('column-10', '장식 기둥 머리', 'Decorative column tops', '装飾柱の頭', '装饰柱头'),
  w('column-17', '장식 기둥 머리 세트', 'Set of decorative column tops', '装飾柱の頭 セット', '装饰柱头套装'),
  w('column-36', '금색 장식 기둥 머리', 'Gold-finished column tops', '金色の装飾柱頭', '金色装饰柱头'),
  w('column-43', '금색 볼 장식 봉', 'Rods with gold ball finials', '金色の玉飾り付きの棒', '金色圆球装饰杆'),
  w('column-11', '뾰족 장식 기둥', 'Pointed decorative columns', '先のとがった装飾柱', '尖顶装饰柱'),
  w('column-30', '긴 장식 기둥 묶음', 'Bundle of long decorative columns', '長い装飾柱の束', '成捆的长装饰柱'),
  w('column-09', '긴 원목 기둥', 'Long solid wood columns', '長い無垢材の柱', '长原木柱'),
  w('column-35', '원목 봉 묶음', 'Bundle of wooden rods', '木の丸棒の束', '成捆的原木圆棒'),
  w(
      'column-18',
      '둥근 손잡이 막대 수량 가공',
      'Round handle rods made in volume',
      '丸い取っ手棒の量産加工',
      '批量加工的圆把手棒'
    ),
  w('column-31', '대형 기둥용 원목', 'Timber for large columns', '大きな柱用の原木', '大型柱用原木'),
  w('column-107', '화병형 난간 동자', 'Vase-shaped balusters', '花瓶形の手すり子', '花瓶形栏杆柱'),
  w('column-108', '긴 장식 기둥 한 쌍', 'A pair of tall decorative columns', '背の高い装飾柱（一対）', '一对高装饰柱'),
  w('column-109', '구슬 머리 기둥', 'Columns with ball tops', '玉飾り付きの柱', '圆球柱头的柱子'),
  w('column-110', '묶어 둔 난간 동자', 'Bundled balusters', '束ねた手すり子', '成捆的栏杆柱'),
  w(
      'column-111',
      '로구로에서 깎고 있는 다리',
      'A leg being turned on the lathe',
      'ろくろで挽いている脚',
      '车床上正在车削的腿'
    ),
  w(
      'column-112',
      '로구로에서 깎고 있는 원뿔형 부재',
      'A tapered piece being turned on the lathe',
      'ろくろで挽いている円すい形の部材',
      '车床上正在车削的锥形部件'
    ),
  w(
      'column-113',
      '뾰족 머리 장식 기둥 네 개',
      'Four spire-topped decorative posts',
      'とがった頭の装飾柱 四本',
      '四根尖顶装饰柱'
    ),
  w('column-114', '구슬 이음 기둥 묶음', 'Bundle of bead-turned columns', '玉つなぎの柱の束', '成捆的串珠柱'),
  w(
      'column-115',
      '로구로에 걸린 구슬 장식 봉',
      'A beaded rod on the lathe',
      'ろくろ上の玉飾りの棒',
      '车床上的串珠装饰杆'
    ),
  w('column-116', '홈을 새긴 구슬 장식 봉', 'Beaded rod with carved grooves', '溝を刻んだ玉飾りの棒', '刻槽串珠装饰杆'),
  w('column-117', '흰색 도장 장식 기둥', 'White-painted decorative column', '白塗装の装飾柱', '白色涂装装饰柱'),
  w('column-118', '촛대형 장식 기둥', 'Candlestick-style decorative columns', '燭台形の装飾柱', '烛台形装饰柱'),
  w('column-119', '가구 다리 묶음', 'A batch of furniture legs', '家具脚の束', '一批家具腿'),
  w('column-120', '긴 기둥 다섯 개', 'Five tall columns', '長い柱 五本', '五根长柱'),
  w('column-121', '홈 파인 원형 기둥', 'Fluted round columns', '溝彫りの丸柱', '凹槽圆柱'),
  w(
      'column-122',
      '로구로에서 깎고 있는 굵은 부재',
      'A thick piece being turned on the lathe',
      'ろくろで加工中の太い部材',
      '车床上加工中的粗部件'
    ),
  w(
      'column-123',
      '로구로에서 깎고 있는 봉',
      'A rod being turned on the lathe',
      'ろくろで加工中の棒',
      '车床上加工中的杆'
    ),
  w('column-124', '꽈배기 계단 엄지기둥', 'Twisted stair newel post', 'ねじり形の階段親柱', '麻花楼梯起步柱'),
  w(
      'column-125',
      '구슬 머리 계단 엄지기둥',
      'Ball-topped stair newel posts',
      '玉飾り付きの階段親柱',
      '圆球顶楼梯起步柱'
    ),
  w('column-126', '출고를 기다리는 엄지기둥', 'Newel posts waiting to ship', '出荷を待つ親柱', '待出货的起步柱'),

  // ───── 로구로 소품 · 목기 ─────
  w(
      'lathe-190',
      '같은 모양으로 깎아 속을 뚫은 부품',
      'Identical turned and bored parts',
      '同じ形に挽いて内側をくり抜いた部品',
      '形状相同、内部钻空的车削零件'
    ),
  w(
      'lathe-192',
      '작업장 바닥에 쌓인 부품과 원목 판재',
      'Finished parts and a solid-wood board on the workshop floor',
      '工房の床に積まれた部品と無垢板',
      '工坊地上堆放的零件与原木板'
    ),
  w(
      'lathe-169',
      '로구로에서 속을 파내는 원목 그릇',
      'Hollowing out a wooden bowl on the lathe',
      'ろくろで内側をくり抜く木の器',
      '在车床上掏挖原木碗'
    ),
  w(
      'lathe-170',
      '나뭇결이 살아 있는 깊은 원목 그릇',
      'Deep wooden bowl with rich grain',
      '木目の美しい深い木の器',
      '木纹鲜明的深口原木碗'
    ),
  w(
      'lathe-161',
      '로구로로 깎은 대형 원목 화병',
      'Large lathe-turned wooden vase',
      'ろくろで挽いた大きな木の花瓶',
      '车床旋制的大型原木花瓶'
    ),
  w('lathe-162', '달걀 모양 대형 꼭지 장식', 'Large egg-shaped wooden finial', '卵形の大きな飾り頭', '蛋形大型木顶饰'),
  w('lathe-163', '원목 촛대 세 가지', 'Three wooden candlesticks', '木の燭台 三種', '三款原木烛台'),
  w(
      'lathe-164',
      '원목 촛대 대량 제작',
      'Wooden candlesticks made in quantity',
      '木の燭台をまとめて制作',
      '批量制作的原木烛台'
    ),
  w('lathe-165', '원목 키친타월 걸이', 'Wooden paper towel holder', '木のキッチンペーパーホルダー', '原木厨房纸巾架'),
  w(
      'lathe-166',
      '둥근 받침이 달린 원목 스탠드 두 개',
      'Two wooden stands with round trays',
      '丸いトレイ付きの木のスタンド 2台',
      '两款带圆托盘的原木立架'
    ),
  w('lathe-167', '원목 나무망치 두 자루', 'Two wooden mallets', '木槌 2本', '两把原木木槌'),
  w('lathe-168', '원목 밀대', 'Wooden rolling pin', '木の麺棒', '原木擀面杖'),
  w('lathe-80', '원목 받침대', 'Solid wood stand', '無垢材の台', '原木底座'),
  w(
      'lathe-81',
      '나뭇결을 살린 받침대 한 쌍',
      'A pair of stands showing the grain',
      '木目を生かした台（一対）',
      '保留木纹的底座一对'
    ),
  w('lathe-82', '소나무 결 원목 받침대', 'Pine-grain wooden stand', '松の木目の台', '松木纹原木底座'),
  w(
      'lathe-83',
      '원목 받침대 — 수종별 비교',
      'Wooden stands in different woods',
      '無垢材の台 — 樹種くらべ',
      '原木底座——不同木种对比'
    ),
  w('lathe-84', '원목 받침대 두 가지', 'Two wooden stands', '無垢材の台 二種', '两款原木底座'),
  w('lathe-85', '원목 받침대 — 위에서 본 모습', 'Wooden stands seen from above', '上から見た木の台', '俯视原木底座'),
  w(
      'lathe-25',
      '나팔형 원목 볼 한 쌍',
      'A pair of flared wooden bowls',
      'ラッパ形の木のボウル（一対）',
      '喇叭形原木碗一对'
    ),
  w('lathe-24', '나팔형 원목 볼', 'Flared wooden bowl', 'ラッパ形の木のボウル', '喇叭形原木碗'),
  w('lathe-28', '대형 원목 항아리', 'Large wooden jar', '大きな木の壺', '大型原木罐'),
  w(
      'lathe-21',
      '로구로로 깎은 그릇과 화병',
      'Lathe-turned bowl and vase',
      'ろくろで挽いた器と花瓶',
      '车床旋制的碗与花瓶'
    ),
  w('lathe-27', '원목 접시와 볼', 'Wooden plates and bowls', '木の皿とボウル', '原木盘与碗'),
  w(
      'lathe-23',
      '대리석 무늬 도장 화병',
      'Vase with a marble-pattern finish',
      '大理石模様に塗装した花瓶',
      '大理石纹涂装花瓶'
    ),
  w(
      'lathe-56',
      '대형 후추 그라인더 한 쌍',
      'A pair of large pepper mills',
      '大きなペッパーミル（一対）',
      '大型胡椒研磨器一对'
    ),
  w('lathe-05', '원목 후추 그라인더 세트', 'Wooden pepper mill set', '木のペッパーミル セット', '原木胡椒研磨器套装'),
  w(
      'lathe-01',
      '버섯·조롱박 모양 후추통',
      'Mushroom- and gourd-shaped pepper shakers',
      'キノコ・ひょうたん形のこしょう入れ',
      '蘑菇与葫芦造型胡椒罐'
    ),
  w('lathe-69', '흑색 후추 그라인더', 'Black-finished pepper mill', '黒いペッパーミル', '黑色胡椒研磨器'),
  w('lathe-70', '원목 후추·소금통 세트', 'Wooden salt & pepper set', '木の塩・こしょう入れ セット', '原木胡椒盐罐套装'),
  w('lathe-71', '원목 후추·소금통 세트', 'Wooden salt & pepper set', '木の塩・こしょう入れ セット', '原木胡椒盐罐套装'),
  w('lathe-72', '원목 후추·소금통 세트', 'Wooden salt & pepper set', '木の塩・こしょう入れ セット', '原木胡椒盐罐套装'),
  w(
      'lathe-73',
      '원목 후추·소금통 네 가지',
      'Four wooden salt & pepper shakers',
      '木の塩・こしょう入れ 四種',
      '四款原木胡椒盐罐'
    ),
  w('lathe-74', '원목 후추·소금통 세트', 'Wooden salt & pepper set', '木の塩・こしょう入れ セット', '原木胡椒盐罐套装'),
  w(
      'lathe-75',
      '원목 후추·소금통 네 가지',
      'Four wooden salt & pepper shakers',
      '木の塩・こしょう入れ 四種',
      '四款原木胡椒盐罐'
    ),
  w('lathe-77', '원목 후추·소금통 세트', 'Wooden salt & pepper set', '木の塩・こしょう入れ セット', '原木胡椒盐罐套装'),
  w('lathe-50', '원목 머그잔 세트', 'Wooden mug set', '木のマグ セット', '原木马克杯套装'),
  w('lathe-51', '원목 찻잔과 수저통', 'Wooden teacup and utensil holder', '木の湯のみと箸立て', '原木茶杯与筷筒'),
  w('lathe-55', '원목 공기와 수저', 'Wooden rice bowls and spoons', '木の飯椀とスプーン', '原木饭碗与汤匙'),
  w('lathe-52', '와인잔 원목 받침', 'Wooden wine glass stand', 'ワイングラスの木の台', '原木红酒杯托'),
  w('lathe-02', '원목 찻잔과 받침', 'Wooden teacup and saucer', '木の湯のみと茶托', '原木茶杯与杯托'),
  w('lathe-03', '뚜껑 찻잔 세트', 'Lidded teacup set', 'ふた付き湯のみ セット', '带盖茶杯套装'),
  w('lathe-78', '원목 코스터', 'Wooden coasters', '木のコースター', '原木杯垫'),
  w(
      'lathe-88',
      '원목 나팔형 스마트폰 스피커',
      'Flared wooden smartphone speaker',
      'ラッパ形の木のスマホスピーカー',
      '喇叭形原木手机扩音器'
    ),
  w(
      'lathe-89',
      '원목 나팔형 스마트폰 스피커',
      'Flared wooden smartphone speaker',
      'ラッパ形の木のスマホスピーカー',
      '喇叭形原木手机扩音器'
    ),
  w(
      'lathe-101',
      '로구로 위의 작은 원목 망치들',
      'Small wooden mallets on the lathe',
      'ろくろ台の上の小さな木槌',
      '车床上的小木槌'
    ),
  w(
      'lathe-102',
      '제과점 원목 밀대와 거치대',
      'Wooden rolling pins and rack for a bakery',
      'パン屋の木製めん棒とラック',
      '面包店的原木擀面杖与架子'
    ),
  w(
      'lathe-103',
      '병 모양 원목 소품 수량 제작',
      'Bottle-shaped wooden pieces made in volume',
      '瓶形の木製小物の量産',
      '批量制作的瓶形木件'
    ),
  w('lathe-104', '병 모양 원목 소품', 'Bottle-shaped wooden pieces', '瓶形の木製小物', '瓶形木件'),
  w('lathe-105', '원목 공구 손잡이', 'Wooden tool handle', '木製の工具の柄', '原木工具手柄'),
];

export type Work = { src: string; alt: string; caption: string; category: CategoryKey; file: string };

const localize =
  (lang: Lang) =>
  (item: (typeof ALL)[number]): Work => ({
    file: item.file,
    src: item.src,
    alt: item.captions[lang],
    caption: item.captions[lang],
    category: item.category,
  });

// 가게 소개·찾아오는 길에만 쓰고 작업물 갤러리에는 넣지 않는 사진
const NOT_IN_GALLERY = ['chowol-04', 'chowol-05'];
const GALLERY_ITEMS = ALL.filter((item) => !NOT_IN_GALLERY.includes(item.file));
export const WORKS_COUNT = GALLERY_ITEMS.length;
export const worksIn = (lang: Lang = 'ko'): Work[] => ALL.map(localize(lang));
export const worksBy = (key: CategoryKey, lang: Lang = 'ko') =>
  GALLERY_ITEMS.map(localize(lang)).filter((item) => item.category === key);

export const pick = (files: string[], lang: Lang = 'ko') =>
  files.map((file) => worksIn(lang).find((item) => item.file === file)!).filter(Boolean);
export const photo = (file: string, lang: Lang = 'ko') => pick([file], lang)[0];

// 같은 물건을 구도만 바꿔 찍은 사진 묶음. 갤러리에는 맨 앞 사진 하나만 보이고,
// 누르면 묶음 안의 사진을 넘겨 볼 수 있습니다. 설명도 맨 앞 사진의 것을 씁니다.
export const GROUPS: string[][] = [
  ['chowol-06', 'chowol-10'],
  ['chowol-09', 'chowol-11', 'chowol-12'],
  ['lathe-190', 'lathe-192'],
  ['column-182', 'column-178', 'column-179', 'column-180', 'column-181'],
  ['column-152', 'column-153'],
  ['column-159', 'column-160'],
  ['lathe-163', 'lathe-164'],
  ['lathe-70', 'lathe-71', 'lathe-72', 'lathe-73', 'lathe-74', 'lathe-75', 'lathe-77', 'lathe-05', 'lathe-01', 'lathe-56', 'lathe-69'],
  ['lathe-83', 'lathe-80', 'lathe-81', 'lathe-82', 'lathe-84', 'lathe-85'],
  ['lathe-03', 'lathe-02', 'lathe-51'],
  ['lathe-25', 'lathe-24'],
  ['lathe-89', 'lathe-88'],
  ['lathe-103', 'lathe-104'],
  ['lathe-27', 'lathe-21'],
  ['column-14', 'column-16', 'column-111', 'column-112', 'column-122', 'column-123'],
  ['column-114', 'column-115', 'column-116'],
  ['column-13', 'column-12', 'column-107', 'column-119', 'column-37'],
  ['column-29', 'column-06', 'column-15', 'column-49', 'column-110'],
  ['column-19', 'column-30', 'column-26', 'column-32'],
  ['column-125', 'column-126', 'column-17', 'column-109'],
  ['column-09', 'column-11', 'column-35', 'column-120'],
  ['column-36', 'column-43'],
];

export type GalleryWork = Work & { photos: { src: string; alt: string }[] };

/** 갤러리용 목록: 묶음은 하나로 합치고(photos에 묶음 사진 전체), 나머지는 사진 한 장씩 */
export const galleryIn = (lang: Lang = 'ko'): GalleryWork[] => {
  const works = GALLERY_ITEMS.map(localize(lang));
  const byFile = new Map(works.map((w) => [w.file, w]));
  const member = new Map(GROUPS.flatMap((files) => files.map((f) => [f, files] as const)));
  const items: GalleryWork[] = [];
  for (const work of works) {
    const group = member.get(work.file);
    if (!group) {
      items.push({ ...work, photos: [{ src: work.src, alt: work.alt }] });
      continue;
    }
    if (items.some((item) => item.file === group[0])) continue;
    const lead = byFile.get(group[0])!;
    items.push({
      ...lead,
      photos: group.map((f) => byFile.get(f)!).map((w) => ({ src: w.src, alt: w.alt })),
    });
  }
  return items;
};
export const galleryBy = (key: CategoryKey, lang: Lang = 'ko') =>
  galleryIn(lang).filter((item) => item.category === key);
export const GALLERY_COUNT = galleryIn().length;
