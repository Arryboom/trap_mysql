#coding:utf-8
import pymysql as sql
import uuid
import random
from pypinyin import lazy_pinyin
import string
from hashlib import md5
import datetime
import time
import sys


def randtrade_count():
    return str(random.randint(0,986))
def randaccounttype():
    return random.choice(['A','B','C','D','E'])
def randcid():
    m=md5()
    m.update(str(uuid.uuid4()))
    return m.hexdigest()


def randcustomer_id():
    return str(uuid.uuid4())
def cx_coin():
    return str(random.randint(0,99999))
def randgender():
    return str(random.randint(1,2))
def randstatus():
    x=random.randint(1,1000)
    if x<=100:
        return str(0)
    else:
        return str(1)
def randtxnid():
    xs=''.join ([random.choice(string.ascii_letters) for _ in range(5)])
    xa=uuid.uuid4()
    tx=md5()
    tx.update(str(xa)+xs)
    return tx.hexdigest()
def randomname():
    xing = [
        '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
        '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
        '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
        '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
        '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
        '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
        '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']

    ming = [
        '的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
        '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
        '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都', '好',
        '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开', '美',
        '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意', '动',
        '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知',
        '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正', '感',
        '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走',
        '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真', '打',
        '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界', '门',
        '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性', '马',
        '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让', '母',
        '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英', '军',
        '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快', '原',
        '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条', '呢',
        '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片', '罗',
        '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合', '反',
        '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运', '及',
        '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司', '巴',
        '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形', '影',
        '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈', '容',
        '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计', '您',
        '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻', '统',
        '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示', '愿',
        '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社', '算',
        '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息', '功',
        '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图', '具',
        '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引', '食',
        '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试', '怀',
        '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除', '跑',
        '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳', '验',
        '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿', '睡',
        '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店', '否',
        '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河', '续',
        '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪', '索',
        '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族', '低',
        '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅', '街',
        '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀', '律',
        '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职', '属',
        '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉', '遗',
        '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳', '差',
        '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府', '压',
        '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童', '顶',
        '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯', '巨',
        '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层', '付',
        '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀', '营',
        '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊', '降',
        '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙', '杰',
        '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡', '预',
        '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误',
        '乾', '坤']
    two_three=random.randint(2,3)
    if two_three==2:
        x = random.randint(0, len(xing)-1)
        m1 = random.randint(0, len(ming)-1)
        name=xing[x] + ming[m1]
    else:
        x = random.randint(0, len(xing)-1)
        m1 = random.randint(0, len(ming)-1)
        m2=random.randint(0,len(ming)-1)
        name=xing[x] + ming[m1]+ming[m2]
    return name
def randengname(male):
    ALL_ENG_NAMES = [
        "fAaliyah", "mAaron", "fAarushi", "fAbagail", "fAbbey", "fAbbi", "fAbbie", "fAbby", "mAbdul", "mAbdullah"
        , "mAbe", "mAbel", "fAbi", "fAbia", "fAbigail", "mAbraham", "mAbram", "fAbrianna", "mAbriel", "fAbrielle"
        , "fAby", "fAcacia", "mAce", "fAda", "fAdalia", "fAdalyn", "mAdam", "mAdan", "fAddie", "mAddison"
        , "fAddison", "mAde", "fAdelaide", "fAdele", "fAdelene", "fAdelia", "fAdelina", "fAdeline", "mAden", "mAdnan"
        , "mAdonis", "fAdreanna", "mAdrian", "fAdriana", "fAdrianna", "fAdrianne", "mAdriel", "fAdrienne", "fAerona",
        "fAgatha"
        , "fAggie", "fAgnes", "mAhmad", "mAhmed", "fAida", "mAidan", "mAiden", "fAileen", "fAilsa", "fAimee"
        , "fAine", "fAinsleigh", "fAinsley", "mAinsley", "fAisha", "fAisling", "fAislinn", "mAjay", "mAl", "mAlain"
        , "fAlaina", "mAlan", "fAlana", "fAlanis", "fAlanna", "fAlannah", "fAlaska", "mAlastair", "fAlayah", "fAlayna"
        , "fAlba", "mAlbert", "fAlberta", "mAlberto", "mAlbie", "mAlden", "mAldo", "fAleah", "mAlec", "fAlecia"
        , "fAleisha", "fAlejandra", "mAlejandro", "mAlen", "fAlena", "mAlesandro", "fAlessandra", "fAlessia", "mAlex",
        "fAlex"
        , "fAlexa", "mAlexander", "fAlexandra", "fAlexandria", "fAlexia", "fAlexis", "mAlexis", "fAlexus", "mAlfie",
        "mAlfonso"
        , "mAlfred", "mAlfredo", "mAli", "fAli", "fAlia", "fAlice", "fAlicia", "fAlina", "fAlisa", "fAlisha"
        , "fAlison", "fAlissa", "mAlistair", "fAlivia", "fAliyah", "fAliza", "fAlize", "fAlka", "mAllan", "mAllen"
        , "fAllie", "fAllison", "fAlly", "fAllyson", "fAlma", "fAlondra", "mAlonzo", "mAloysius", "mAlphonso", "mAlton"
        , "mAlvin", "fAlycia", "fAlyshialynn", "fAlyson", "fAlyssa", "fAlyssia", "fAmalia", "fAmanda", "fAmani",
        "fAmara"
        , "mAmari", "fAmari", "fAmaris", "fAmaya", "fAmber", "fAmberly", "fAmelia", "fAmelie", "fAmerica", "fAmethyst"
        , "fAmie", "fAmina", "mAmir", "fAmirah", "mAmit", "fAmity", "mAmos", "fAmy", "fAmya", "fAna"
        , "fAnabel", "fAnabelle", "fAnahi", "fAnais", "fAnamaria", "mAnand", "fAnanya", "fAnastasia", "mAnderson",
        "fAndie"
        , "mAndre", "fAndrea", "mAndreas", "mAndres", "mAndrew", "fAndromeda", "mAndy", "mAngel", "fAngel", "fAngela"
        , "fAngelia", "fAngelica", "fAngelina", "fAngeline", "fAngelique", "mAngelo", "fAngie", "mAngus", "fAnika",
        "fAnisa"
        , "fAnita", "fAniya", "fAniyah", "fAnjali", "fAnn", "fAnna", "fAnnabel", "fAnnabella", "fAnnabelle", "fAnnabeth"
        , "fAnnalisa", "fAnnalise", "fAnne", "fAnneke", "fAnnemarie", "fAnnette", "fAnnie", "fAnnika", "fAnnmarie",
        "mAnsel"
        , "mAnson", "fAnthea", "mAnthony", "fAntoinette", "mAnton", "fAntonia", "mAntonio", "mAntony", "fAnuja",
        "fAnusha"
        , "fAnushka", "fAnya", "fAoibhe", "fAoibheann", "fAoife", "fAphrodite", "mApollo", "fApple", "fApril", "fAqua"
        , "fArabella", "fArabelle", "mAran", "mArcher", "mArchie", "mAri", "fAria", "fAriadne", "fAriana", "fArianna"
        , "fArianne", "fAriel", "fAriella", "fArielle", "fArisha", "mArjun", "fArleen", "fArlene", "fArlette", "mArlo"
        , "mArman", "mArmando", "mArnold", "mAron", "mArran", "mArrie", "mArt", "fArtemis", "mArthur", "mArturo"
        , "mArun", "fArwen", "mArwin", "fArya", "mAsa", "mAsad", "mAsh", "fAsha", "fAshanti", "mAshby"
        , "mAsher", "fAshlee", "fAshleigh", "fAshley", "mAshley", "fAshlie", "fAshlyn", "fAshlynn", "mAshton", "fAshton"
        , "fAshvini", "fAsia", "fAsma", "mAspen", "fAspen", "mAston", "fAstrid", "mAthan", "fAthena", "fAthene"
        , "mAtticus", "fAubreanna", "fAubree", "fAubrey", "mAubrey", "fAudra", "fAudrey", "fAudrina", "mAudwin",
        "mAugust"
        , "fAugustina", "mAugustus", "fAurelia", "fAurora", "mAusten", "mAustin", "fAutumn", "fAva", "fAvalon", "mAvery"
        , "fAvery", "fAvril", "mAxel", "fAya", "mAyaan", "fAyana", "fAyanna", "mAyden", "fAyesha", "fAyisha"
        , "fAyla", "fAzalea", "fAzaria", "fAzariah", "fBailey", "mBailey", "mBarack", "fBarbara", "fBarbie", "mBarclay"
        , "mBarnaby", "mBarney", "mBarrett", "mBarron", "mBarry", "mBart", "mBartholomew", "mBasil", "mBastian",
        "mBaxter"
        , "mBay", "fBay", "fBaylee", "mBaylor", "fBea", "mBear", "fBeatrice", "fBeatrix", "mBeau", "fBecca"
        , "fBeccy", "mBeck", "mBeckett", "fBecky", "fBelinda", "fBella", "mBellamy", "fBellatrix", "fBelle", "mBen"
        , "mBenedict", "fBenita", "mBenjamin", "mBenji", "mBenjy", "mBennett", "mBennie", "mBenny", "mBenson",
        "mBentley"
        , "mBently", "fBernadette", "mBernard", "mBernardo", "fBernice", "mBernie", "mBert", "fBertha", "mBertie",
        "mBertram"
        , "fBeryl", "fBess", "fBeth", "fBethan", "fBethanie", "fBethany", "fBetsy", "fBettina", "fBetty", "mBev"
        , "mBevan", "fBeverly", "fBeyonce", "fBianca", "mBill", "fBillie", "mBilly", "mBjorn", "mBladen", "mBlain"
        , "mBlaine", "mBlair", "fBlair", "fBlaire", "mBlaise", "mBlake", "fBlake", "fBlakely", "fBlanche", "fBlaze"
        , "mBlaze", "fBlessing", "fBliss", "fBloom", "fBlossom", "mBlue", "fBlythe", "mBob", "fBobbi", "fBobbie"
        , "fBobby", "mBobby", "mBodie", "fBonita", "fBonnie", "fBonquesha", "mBoris", "mBoston", "mBowen", "mBoyd"
        , "mBrad", "mBraden", "mBradford", "mBradley", "mBradwin", "mBrady", "mBraeden", "fBraelyn", "mBram", "mBranden"
        , "fBrandi", "mBrandon", "fBrandy", "mBrantley", "mBraxton", "mBrayan", "mBrayden", "mBraydon", "fBraylee",
        "mBraylon"
        , "fBrea", "fBreanna", "fBree", "fBreeze", "fBrenda", "mBrendan", "mBrenden", "mBrendon", "fBrenna", "mBrennan"
        , "mBrent", "mBrenton", "mBret", "mBrett", "mBrevin", "mBrevyn", "fBria", "mBrian", "fBriana", "fBrianna"
        , "fBrianne", "fBriar", "mBrice", "fBridget", "fBridgette", "mBridie", "fBridie", "fBriella", "fBrielle",
        "mBrighton"
        , "fBrigid", "fBriley", "fBrinley", "mBrinley", "fBriony", "fBrisa", "fBristol", "fBritney", "fBritt",
        "fBrittany"
        , "fBrittney", "mBrock", "mBrodie", "mBrody", "mBrogan", "fBrogan", "fBronagh", "mBronson", "fBronte",
        "fBronwen"
        , "fBronwyn", "fBrook", "fBrooke", "fBrooklyn", "fBrooklynn", "mBrooks", "mBruce", "mBruno", "mBryan",
        "fBryanna"
        , "mBryant", "mBryce", "mBryden", "mBrydon", "fBrylee", "fBryn", "fBrynlee", "fBrynn", "mBryon", "fBryony"
        , "mBryson", "mBuck", "mBuddy", "fBunty", "mBurt", "mBurton", "mBuster", "mButch", "mByron", "mCadby"
        , "mCade", "mCaden", "fCadence", "mCael", "mCaelan", "mCaesar", "mCai", "mCaiden", "fCailin", "mCain"
        , "fCaitlan", "fCaitlin", "fCaitlyn", "mCaius", "mCal", "mCale", "mCaleb", "fCaleigh", "mCalhoun", "fCali"
        , "fCalista", "mCallan", "mCallen", "fCallie", "fCalliope", "fCallista", "mCallum", "mCalum", "mCalvin",
        "fCalypso"
        , "mCam", "fCambria", "mCamden", "mCameron", "fCameron", "fCami", "fCamila", "fCamilla", "fCamille", "mCampbell"
        , "mCamron", "fCamryn", "fCandace", "fCandice", "fCandis", "fCandy", "fCaoimhe", "fCaprice", "fCara", "mCarey"
        , "fCarina", "fCaris", "fCarissa", "mCarl", "fCarla", "fCarlene", "fCarley", "fCarlie", "mCarlisle", "mCarlos"
        , "mCarlton", "fCarly", "fCarlynn", "fCarmel", "fCarmela", "fCarmen", "fCarol", "fCarole", "fCarolina",
        "fCaroline"
        , "fCarolyn", "fCarrie", "mCarsen", "mCarson", "mCarter", "fCarter", "mCary", "fCarys", "fCasey", "mCasey"
        , "mCash", "mCason", "mCasper", "fCassandra", "fCassia", "fCassidy", "fCassie", "mCassius", "mCastiel",
        "mCastor"
        , "fCat", "fCatalina", "fCate", "fCaterina", "mCathal", "fCathalina", "fCatherine", "fCathleen", "fCathy",
        "fCatlin"
        , "mCato", "fCatrina", "fCatriona", "mCavan", "mCayden", "mCaydon", "fCayla", "fCece", "fCecelia", "mCecil"
        , "fCecilia", "fCecily", "mCedric", "fCeleste", "fCelestia", "fCelestine", "fCelia", "fCelina", "fCeline",
        "fCelise"
        , "fCerise", "fCerys", "mCesar", "mChad", "mChance", "mChandler", "fChanel", "fChanelle", "mChanning",
        "fChantal"
        , "fChantelle", "fCharis", "fCharissa", "fCharity", "fCharlene", "mCharles", "fCharley", "mCharley", "mCharlie",
        "fCharlie"
        , "fCharlize", "fCharlotte", "mCharlton", "fCharmaine", "mChase", "fChastity", "mChaz", "mChe", "fChelsea",
        "fChelsey"
        , "fChenai", "fChenille", "fCher", "fCheri", "fCherie", "fCherry", "fCheryl", "mChesney", "mChester", "mChevy"
        , "fCheyanne", "fCheyenne", "fChiara", "mChip", "fChloe", "mChris", "fChris", "fChrissy", "fChrista",
        "fChristabel"
        , "fChristal", "fChristen", "fChristi", "mChristian", "fChristiana", "fChristie", "fChristina", "fChristine",
        "mChristopher", "fChristy"
        , "fChrystal", "mChuck", "mCian", "fCiara", "mCiaran", "fCici", "fCiel", "fCierra", "mCillian", "fCindy"
        , "fClaire", "mClancy", "fClara", "fClarabelle", "fClare", "mClarence", "fClarice", "fClaris", "fClarissa",
        "fClarisse"
        , "fClarity", "mClark", "fClary", "mClaude", "fClaudette", "fClaudia", "fClaudine", "mClay", "mClayton", "fClea"
        , "mClement", "fClementine", "fCleo", "fCleopatra", "mCliff", "mClifford", "mClifton", "mClint", "mClinton",
        "mClive"
        , "fClodagh", "fClotilde", "fClover", "mClyde", "mCoby", "fCoco", "mCody", "mCohen", "mColby", "mCole"
        , "fColette", "mColin", "fColleen", "mCollin", "mColm", "mColt", "mColton", "mConan", "mConner", "fConnie"
        , "mConnor", "mConor", "mConrad", "fConstance", "mConstantine", "mCooper", "fCora", "fCoral", "fCoralie",
        "fCoraline"
        , "mCorbin", "fCordelia", "mCorey", "fCori", "fCorina", "fCorinne", "mCormac", "fCornelia", "mCornelius",
        "fCorra"
        , "mCory", "fCosette", "fCourtney", "mCraig", "fCressida", "fCristal", "mCristian", "fCristina", "mCristobal",
        "mCrosby"
        , "mCruz", "fCrystal", "mCullen", "mCurt", "mCurtis", "mCuthbert", "fCyndi", "fCynthia", "mCyril", "mCyrus"
        , "mDacey", "fDagmar", "fDahlia", "mDaire", "fDaisy", "fDakota", "mDakota", "mDale", "mDallas", "mDalton"
        , "mDamian", "mDamien", "mDamion", "mDamon", "mDan", "fDana", "mDana", "mDane", "fDanette", "fDani"
        , "fDanica", "mDaniel", "fDaniela", "fDaniella", "fDanielle", "fDanika", "mDanny", "mDante", "fDaphne", "mDara"
        , "fDara", "mDaragh", "fDarby", "fDarcey", "fDarcie", "mDarcy", "fDarcy", "mDaren", "fDaria", "mDarian"
        , "mDarin", "mDario", "mDarius", "fDarla", "fDarlene", "mDarnell", "mDarragh", "mDarrel", "mDarrell", "mDarren"
        , "mDarrin", "mDarryl", "mDarryn", "mDarwin", "mDaryl", "mDash", "mDashawn", "fDasia", "mDave", "mDavid"
        , "fDavida", "mDavin", "fDavina", "mDavion", "mDavis", "fDawn", "mDawson", "mDax", "mDaxter", "mDaxton"
        , "fDayna", "fDaysha", "mDayton", "mDeacon", "mDean", "fDeana", "fDeandra", "mDeandre", "fDeann", "fDeanna"
        , "fDeanne", "fDeb", "fDebbie", "fDebby", "fDebora", "fDeborah", "fDebra", "mDeclan", "fDee", "fDeedee"
        , "fDeena", "mDeepak", "fDeidre", "fDeirdre", "fDeja", "fDelaney", "fDelanie", "fDelany", "mDelbert", "fDelia"
        , "fDelilah", "fDella", "fDelores", "fDelphine", "fDemetria", "mDemetrius", "fDemi", "fDena", "mDenis",
        "fDenise"
        , "mDennis", "fDenny", "mDenver", "mDenzel", "mDeon", "mDerek", "mDermot", "mDerrick", "mDeshaun", "mDeshawn"
        , "fDesiree", "mDesmond", "fDestinee", "fDestiny", "mDev", "mDevin", "mDevlin", "mDevon", "mDewayne", "mDewey"
        , "mDexter", "fDiamond", "fDiana", "fDiane", "fDianna", "fDianne", "mDiarmuid", "mDick", "fDido", "mDiego"
        , "mDilan", "mDillon", "mDimitri", "fDina", "mDinesh", "mDino", "mDion", "fDionne", "fDior", "mDirk"
        , "fDixie", "mDjango", "mDmitri", "fDolly", "fDolores", "mDominic", "mDominick", "fDominique", "mDon", "mDonald"
        , "fDonna", "mDonnie", "mDonovan", "fDora", "fDoreen", "mDorian", "fDoris", "fDorothy", "fDot", "mDoug"
        , "mDouglas", "mDoyle", "mDrake", "mDrew", "fDrew", "mDuane", "mDuke", "fDulce", "mDuncan", "mDustin"
        , "mDwayne", "mDwight", "mDylan", "fEabha", "mEamon", "mEarl", "mEarnest", "mEason", "mEaston", "fEbony"
        , "fEcho", "mEd", "mEddie", "mEddy", "fEden", "mEden", "mEdgar", "fEdie", "mEdison", "fEdith"
        , "mEdmund", "fEdna", "mEdouard", "mEdric", "mEdsel", "mEduardo", "mEdward", "mEdwardo", "mEdwin", "fEdwina"
        , "fEffie", "mEfrain", "mEfren", "mEgan", "mEgon", "fEileen", "fEilidh", "fEimear", "fElaina", "fElaine"
        , "fElana", "fEleanor", "fElectra", "fElektra", "fElena", "mEli", "fEliana", "mElias", "mElijah", "fElin"
        , "fElina", "fElinor", "mEliot", "fElisa", "fElisabeth", "fElise", "mElisha", "fEliza", "fElizabeth", "fElla"
        , "fElle", "fEllen", "fEllery", "fEllie", "mEllington", "mElliot", "mElliott", "fEllis", "mEllis", "fElly"
        , "mElmer", "mElmo", "fElodie", "fEloise", "fElora", "fElsa", "fElsie", "fElspeth", "mElton", "fElva"
        , "fElvira", "mElvis", "mElwyn", "fElysia", "fElyza", "mEmanuel", "fEmanuela", "fEmber", "fEmelda", "fEmely"
        , "fEmer", "fEmerald", "mEmerson", "fEmerson", "mEmery", "mEmet", "mEmil", "fEmilee", "fEmilia", "mEmiliano"
        , "fEmilie", "mEmilio", "fEmily", "fEmma", "fEmmalee", "fEmmaline", "fEmmalyn", "mEmmanuel", "fEmmanuelle",
        "fEmmeline"
        , "mEmmerson", "mEmmet", "mEmmett", "fEmmie", "fEmmy", "fEnid", "mEnnio", "mEnoch", "mEnrique", "fEnya"
        , "mEnzo", "mEoghan", "mEoin", "mEric", "fErica", "mErick", "mErik", "fErika", "fErin", "fEris"
        , "mErnest", "mErnesto", "mErnie", "mErrol", "mErvin", "mErwin", "fEryn", "fEsmay", "fEsme", "fEsmeralda"
        , "fEsparanza", "fEsperanza", "mEsteban", "fEstee", "fEstelle", "fEster", "fEsther", "fEstrella", "mEthan",
        "fEthel"
        , "mEthen", "mEtienne", "mEuan", "mEuen", "mEugene", "fEugenie", "fEunice", "mEustace", "fEva", "mEvan"
        , "fEvangelina", "fEvangeline", "mEvangelos", "fEve", "fEvelin", "fEvelyn", "mEvelyn", "mEverett", "fEverly",
        "fEvie"
        , "fEvita", "mEwan", "mEzekiel", "mEzio", "mEzra", "mFabian", "mFabio", "fFabrizia", "mFaisal", "fFaith"
        , "fFallon", "fFanny", "fFarah", "mFarley", "fFarrah", "fFatima", "fFawn", "fFay", "fFaye", "mFebian"
        , "fFelicia", "fFelicity", "mFelipe", "mFelix", "mFergus", "fFern", "mFernand", "fFernanda", "mFernando",
        "fFfion"
        , "mFidel", "fFifi", "mFinbar", "mFinlay", "mFinley", "mFinn", "mFinnian", "mFinnigan", "fFiona", "mFionn"
        , "mFletcher", "fFleur", "fFlick", "fFlo", "fFlora", "fFlorence", "mFloyd", "mFlynn", "mFord", "mForest"
        , "mForrest", "mFoster", "mFox", "fFran", "fFrances", "fFrancesca", "mFrancesco", "fFrancine", "mFrancis",
        "mFrancisco"
        , "mFrank", "fFrankie", "mFrankie", "mFranklin", "mFranklyn", "mFraser", "mFred", "fFreda", "mFreddie",
        "mFreddy"
        , "mFrederick", "mFredrick", "fFreya", "fFrida", "mFritz", "fGabby", "mGabe", "mGabriel", "fGabriela",
        "fGabriella"
        , "fGabrielle", "mGael", "mGaelan", "mGage", "fGail", "mGale", "mGalen", "mGannon", "mGareth", "mGarman"
        , "fGarnet", "mGarrett", "mGarrison", "mGarry", "mGarth", "mGary", "mGaston", "mGavin", "fGayle", "fGaynor"
        , "fGeena", "fGemma", "fGena", "mGene", "fGenesis", "fGenevieve", "mGeoff", "mGeoffrey", "mGeorge", "fGeorgette"
        , "fGeorgia", "fGeorgie", "fGeorgina", "mGeraint", "mGerald", "fGeraldine", "mGerard", "mGerardo", "mGermain",
        "mGerry"
        , "fGert", "fGertrude", "fGia", "mGian", "fGianna", "mGibson", "mGideon", "fGigi", "mGil", "mGilbert"
        , "mGilberto", "mGiles", "fGillian", "fGina", "fGinger", "fGinny", "mGino", "mGiorgio", "fGiovanna", "mGiovanni"
        , "fGisela", "fGiselle", "fGisselle", "fGladys", "mGlen", "fGlenda", "mGlenn", "fGlenys", "fGloria", "mGlyndwr"
        , "fGlynis", "mGodfrey", "mGodric", "mGodwin", "fGolda", "fGoldie", "mGonzalo", "mGordon", "fGrace", "fGracelyn"
        , "fGracie", "mGrady", "mGraeme", "mGraham", "fGrainne", "mGrant", "mGrayson", "mGreg", "mGregg", "mGregor"
        , "mGregory", "fGreta", "fGretchen", "mGrey", "mGreyson", "mGriffin", "fGriselda", "fGuadalupe", "mGuillermo",
        "fGuinevere"
        , "mGunnar", "mGunner", "mGus", "mGustav", "mGustavo", "mGuy", "fGwen", "fGwendolyn", "fGwyneth", "fHabiba"
        , "mHaden", "fHadley", "mHaiden", "fHailee", "fHailey", "mHal", "fHaleigh", "fHaley", "fHalle", "fHallie"
        , "mHamish", "mHan", "mHank", "fHanna", "fHannah", "mHans", "mHarlan", "fHarley", "mHarley", "fHarmony"
        , "mHarold", "fHarper", "fHarriet", "mHarris", "mHarrison", "mHarry", "mHarvey", "mHassan", "fHattie", "fHaven"
        , "mHayden", "fHayden", "mHayes", "fHaylee", "fHayley", "fHazel", "fHazeline", "mHeath", "fHeather", "fHeaven"
        , "mHector", "fHeidi", "fHelen", "fHelena", "fHelene", "fHelga", "fHelina", "mHendrik", "mHendrix", "mHenley"
        , "mHenri", "fHenrietta", "mHenry", "fHepsiba", "fHera", "mHerbert", "mHerman", "fHermione", "fHester",
        "mHeston"
        , "fHetty", "fHilary", "mHilary", "fHilda", "fHillary", "mHolden", "fHollie", "fHolly", "mHomer", "fHonesty"
        , "fHoney", "fHonor", "fHonour", "fHope", "mHorace", "mHoratio", "mHoward", "mHubert", "mHudson", "mHugh"
        , "mHugo", "mHumberto", "mHumphrey", "mHunter", "mHuw", "fHyacinth", "mHywel", "mIain", "mIan", "fIanthe"
        , "mIanto", "mIbrahim", "fIda", "mIdris", "mIeuan", "mIggy", "mIgnacio", "mIgor", "mIke", "fIla"
        , "fIlene", "fIliana", "fIlona", "fIlse", "fImani", "fImelda", "fImogen", "mImran", "fIndia", "mIndiana"
        , "fIndie", "fIndigo", "fIndira", "fInes", "fIngrid", "mInigo", "fIona", "mIra", "fIra", "fIrene"
        , "fIrina", "fIris", "fIrma", "mIrvin", "mIrving", "mIrwin", "fIsa", "mIsaac", "fIsabel", "fIsabell"
        , "fIsabella", "fIsabelle", "fIsadora", "mIsaiah", "fIsha", "mIsiah", "mIsidore", "fIsis", "fIsla", "mIsmael"
        , "fIsobel", "fIsolde", "mIsrael", "mIssac", "fItzel", "mIvan", "fIvana", "mIvor", "fIvy", "fIyanna"
        , "fIzabella", "fIzidora", "fIzzie", "fIzzy", "mJace", "fJacinda", "fJacinta", "mJack", "mJackie", "fJackie"
        , "mJackson", "mJacob", "mJacoby", "fJacqueline", "fJacquelyn", "mJacques", "fJada", "fJade", "fJaden", "mJaden"
        , "mJadon", "fJadyn", "fJaelynn", "mJagger", "mJago", "mJai", "fJaida", "mJaiden", "fJaime", "mJaime"
        , "mJak", "mJake", "mJakob", "mJalen", "mJamal", "mJames", "mJameson", "mJamie", "fJamie", "mJamison"
        , "fJamiya", "fJan", "mJan", "fJana", "fJancis", "fJane", "fJanelle", "fJanessa", "fJanet", "fJanette"
        , "fJania", "fJanice", "fJanie", "fJanine", "fJanis", "fJaniya", "fJanuary", "fJaqueline", "mJared", "mJarod"
        , "mJarrett", "mJarrod", "mJarvis", "mJase", "fJasmin", "fJasmine", "mJason", "mJasper", "mJavier", "mJavon"
        , "mJax", "mJaxon", "mJaxson", "mJay", "fJaya", "mJayce", "fJayda", "mJayden", "fJayden", "mJaydon"
        , "fJayla", "mJaylen", "fJaylene", "mJaylin", "fJaylinn", "mJaylon", "fJaylynn", "fJayne", "mJayson", "fJazlyn"
        , "fJazmin", "fJazmine", "fJazz", "fJean", "fJeanette", "fJeanine", "fJeanne", "fJeannette", "fJeannie",
        "fJeannine"
        , "mJeb", "mJebediah", "mJed", "mJediah", "mJedidiah", "mJeff", "mJefferson", "mJeffery", "mJeffrey", "mJeffry"
        , "fJemima", "fJemma", "fJen", "fJena", "fJenelle", "fJenessa", "fJenna", "fJennette", "fJenni", "fJennie"
        , "fJennifer", "fJenny", "fJensen", "mJensen", "mJenson", "mJerald", "mJeremiah", "mJeremy", "fJeri", "mJericho"
        , "mJermaine", "mJerome", "fJerri", "mJerry", "fJess", "fJessa", "mJesse", "fJessica", "mJessie", "fJessie"
        , "mJesus", "fJet", "mJet", "mJethro", "mJett", "fJewel", "fJill", "fJillian", "mJim", "mJimmie"
        , "mJimmy", "fJo", "mJoachim", "fJoan", "fJoann", "fJoanna", "fJoanne", "mJoaquin", "fJocelyn", "fJodi"
        , "fJodie", "fJody", "mJody", "mJoe", "mJoel", "fJoelle", "mJoey", "mJohan", "fJohanna", "mJohn"
        , "mJohnathan", "mJohnathon", "mJohnnie", "mJohnny", "fJoleen", "fJolene", "fJolie", "mJon", "mJonah", "mJonas"
        , "mJonathan", "mJonathon", "fJoni", "mJonty", "mJordan", "fJordan", "fJordana", "mJordon", "mJordy", "fJordyn"
        , "mJorge", "fJorja", "mJose", "fJoselyn", "mJoseph", "fJosephine", "mJosh", "mJoshua", "mJosiah", "fJosie"
        , "mJosue", "mJovan", "fJoy", "fJoyce", "mJuan", "fJuanita", "mJudah", "mJudas", "mJudd", "fJude"
        , "mJude", "fJudith", "fJudy", "fJules", "fJulia", "mJulian", "fJuliana", "fJulianna", "fJulianne", "fJulie"
        , "fJulienne", "fJuliet", "fJuliette", "mJulio", "fJulissa", "mJulius", "fJuly", "fJune", "fJuniper", "fJuno"
        , "fJustice", "mJustice", "mJustin", "fJustina", "fJustine", "fKacey", "mKade", "mKaden", "fKadence", "mKai"
        , "mKaiden", "fKaidence", "fKailey", "fKailyn", "mKaine", "fKaitlin", "fKaitlyn", "fKaitlynn", "mKale", "fKalea"
        , "mKaleb", "fKaleigh", "fKali", "fKalia", "fKalista", "fKallie", "fKamala", "mKameron", "fKamryn", "mKane"
        , "fKara", "fKaren", "fKari", "fKarin", "fKarina", "fKarissa", "mKarl", "fKarla", "fKarlee", "fKarly"
        , "fKarolina", "mKarson", "fKaryn", "fKasey", "mKash", "mKasper", "fKassandra", "fKassidy", "fKassie", "fKat"
        , "fKatara", "fKatarina", "fKate", "fKatelyn", "fKatelynn", "fKaterina", "fKatharine", "fKatherine",
        "fKathleen", "fKathryn"
        , "fKathy", "fKatia", "fKatie", "fKatlyn", "fKatniss", "fKatrina", "fKaty", "fKatya", "fKay", "fKaya"
        , "mKayden", "fKaye", "fKayla", "fKaylee", "fKayleigh", "mKaylen", "fKayley", "fKaylie", "fKaylin", "mKayson"
        , "mKeanu", "fKeara", "mKeaton", "mKedrick", "mKeegan", "fKeeley", "fKeely", "mKeenan", "fKeira", "fKeisha"
        , "mKeith", "fKelis", "mKellan", "mKellen", "fKelley", "fKelli", "fKellie", "mKellin", "mKelly", "fKelly"
        , "fKelsey", "fKelsie", "mKelvin", "mKen", "fKendall", "mKendall", "fKendra", "mKendrick", "fKenna", "fKennedy"
        , "mKennedy", "mKenneth", "mKenny", "mKent", "mKenton", "fKenzie", "fKera", "fKeri", "fKerian", "fKerri"
        , "fKerry", "mKerry", "mKevin", "mKhalid", "mKhalil", "fKia", "mKian", "fKiana", "fKiara", "mKiefer"
        , "fKiera", "mKieran", "mKieron", "fKierra", "fKiersten", "fKiki", "fKiley", "mKillian", "fKim", "mKim"
        , "fKimberlee", "fKimberley", "fKimberly", "fKimbriella", "fKimmy", "mKingsley", "mKingston", "fKinley",
        "fKinsey", "fKinsley"
        , "mKip", "fKira", "mKiran", "mKirby", "mKirk", "fKirsten", "fKirstin", "fKirsty", "mKit", "fKitty"
        , "fKizzy", "mKlaus", "mKlay", "fKloe", "mKnox", "mKobe", "mKoby", "mKody", "mKolby", "fKora"
        , "fKori", "fKourtney", "mKris", "fKris", "mKrish", "fKrista", "fKristen", "fKristi", "mKristian", "fKristie"
        , "fKristin", "fKristina", "fKristine", "mKristoff", "mKristopher", "fKristy", "fKrystal", "mKurt", "mKurtis",
        "mKye"
        , "fKyla", "mKylar", "mKyle", "fKylee", "fKyleigh", "mKylen", "mKyler", "fKylie", "fKyra", "mKyran"
        , "mKyrin", "mKyron", "fLacey", "mLacey", "mLachlan", "fLacie", "fLacy", "fLadonna", "fLaila", "fLainey"
        , "mLake", "fLakyn", "fLala", "mLamar", "mLamont", "fLana", "mLance", "mLanden", "mLandon", "mLandyn"
        , "mLane", "fLaney", "mLangdon", "mLangston", "fLara", "fLarissa", "mLarry", "mLars", "fLatoya", "fLaura"
        , "fLaurel", "fLauren", "mLaurence", "fLaurie", "mLaurie", "fLauryn", "fLavana", "fLavender", "fLavinia",
        "mLawrence"
        , "mLawson", "fLayla", "mLayne", "mLayton", "fLea", "mLeaf", "fLeah", "fLeandra", "mLeandro", "fLeann"
        , "fLeanna", "fLeanne", "mLebron", "fLee", "mLee", "fLeela", "fLeena", "fLeia", "mLeigh", "fLeigh"
        , "mLeighton", "fLeila", "fLeilani", "fLela", "mLeland", "fLena", "mLennie", "mLennon", "mLennox", "mLenny"
        , "fLenore", "mLeo", "mLeon", "fLeona", "mLeonard", "mLeonardo", "mLeonel", "fLeonie", "mLeopold", "fLeora"
        , "mLeroy", "mLes", "fLesley", "mLeslie", "fLeslie", "fLesly", "mLester", "fLeticia", "fLetitia", "fLettie"
        , "mLeuan", "mLev", "mLeven", "mLevi", "mLewis", "mLex", "fLexi", "fLexia", "fLexie", "fLexis"
        , "fLeyla", "fLia", "mLiam", "fLiana", "fLianne", "fLibbie", "fLibby", "fLiberty", "fLidia", "mLief"
        , "fLiesl", "fLila", "fLilac", "fLilah", "fLili", "fLilian", "fLiliana", "fLilita", "fLilith", "fLillia"
        , "fLillian", "fLillie", "fLilly", "fLily", "fLina", "mLincoln", "fLinda", "fLindsay", "fLindsey", "fLindy"
        , "mLink", "mLinus", "mLionel", "fLisa", "mLisandro", "fLisette", "fLiv", "fLivia", "fLivvy", "fLiz"
        , "fLiza", "fLizbeth", "fLizette", "fLizzie", "fLizzy", "mLloyd", "mLochlan", "mLogan", "fLogan", "fLois"
        , "mLoki", "fLola", "fLolita", "fLondon", "mLondon", "mLonnie", "fLora", "fLoran", "mLorcan", "fLorelei"
        , "mLoren", "fLoren", "fLorena", "mLorenzo", "fLoretta", "fLori", "fLorie", "mLoris", "fLorna", "fLorraine"
        , "fLorri", "fLorrie", "fLottie", "fLotus", "fLou", "mLou", "fLouella", "mLouie", "mLouis", "fLouisa"
        , "fLouise", "mLowell", "fLuann", "mLuca", "mLucas", "fLucia", "mLucian", "fLuciana", "mLuciano", "fLucie"
        , "fLucille", "fLucinda", "fLucky", "fLucy", "mLuigi", "mLuis", "fLuisa", "mLukas", "mLuke", "fLulu"
        , "fLuna", "fLupita", "mLuther", "fLuz", "fLydia", "fLyla", "mLyle", "fLynda", "mLyndon", "fLyndsey"
        , "fLynette", "mLynn", "fLynn", "fLynne", "fLynnette", "fLynsey", "fLyra", "fLyric", "mLysander", "fMabel"
        , "fMacey", "fMacie", "mMack", "fMackenzie", "fMacy", "fMadalyn", "fMaddie", "fMaddison", "mMaddox", "fMaddy"
        , "fMadeleine", "fMadeline", "fMadelyn", "fMadison", "fMadisyn", "fMadonna", "fMadyson", "fMae", "fMaeve",
        "fMagda"
        , "fMagdalena", "fMagdalene", "fMaggie", "mMagnus", "fMaia", "fMaire", "fMairead", "fMaisie", "mMaison",
        "fMaisy"
        , "fMaja", "fMakayla", "fMakenna", "fMakenzie", "mMalachi", "mMalakai", "mMalcolm", "fMalia", "mMalik",
        "fMalina"
        , "fMalinda", "fMallory", "mMalloy", "fMalory", "fMandy", "mManny", "mManuel", "fManuela", "fMara", "mMarc"
        , "mMarcel", "fMarcela", "fMarcella", "fMarcelle", "fMarci", "fMarcia", "fMarcie", "mMarco", "mMarcos",
        "mMarcus"
        , "fMarcy", "fMargaret", "fMargarita", "fMargaux", "fMarge", "fMargie", "fMargo", "fMargot", "fMargret",
        "fMaria"
        , "fMariah", "fMariam", "fMarian", "fMariana", "fMarianna", "fMarianne", "fMaribel", "fMarie", "fMariela",
        "fMariella"
        , "mMarik", "fMarilyn", "fMarina", "mMario", "mMarion", "fMarion", "fMarisa", "fMarisol", "fMarissa", "fMaritza"
        , "fMarjorie", "mMark", "fMarla", "fMarlee", "fMarlena", "fMarlene", "mMarley", "fMarley", "mMarlon", "fMarnie"
        , "mMarquis", "fMarsha", "mMarshall", "fMartha", "mMartin", "fMartina", "mMarty", "mMartyn", "mMarvin", "fMary"
        , "fMaryam", "fMaryann", "fMarybeth", "fMasie", "mMason", "mMassimo", "mMat", "mMateo", "mMathew", "fMatilda"
        , "mMatt", "mMatthew", "mMatthias", "fMaude", "fMaura", "fMaureen", "mMaurice", "mMauricio", "mMaverick",
        "fMavis"
        , "mMax", "mMaxim", "mMaximilian", "mMaximus", "fMaxine", "mMaxwell", "fMay", "fMaya", "fMazie", "fMckayla"
        , "fMckenna", "fMckenzie", "fMea", "fMeadow", "fMeagan", "fMeera", "fMeg", "fMegan", "fMeghan", "mMehdi"
        , "mMehtab", "fMei", "mMekhi", "mMel", "fMel", "fMelanie", "fMelina", "fMelinda", "fMelissa", "fMelody"
        , "mMelvin", "fMercedes", "fMercy", "fMeredith", "mMerick", "fMerida", "mMervyn", "fMeryl", "fMia", "mMicah"
        , "mMichael", "fMichaela", "mMicheal", "fMichele", "fMichelle", "mMick", "mMickey", "mMiguel", "fMika",
        "fMikaela"
        , "fMikayla", "mMike", "mMikey", "fMikhaela", "fMila", "mMilan", "fMildred", "fMilena", "mMiles", "fMiley"
        , "mMiller", "fMillicent", "fMillie", "fMilly", "mMilo", "mMilton", "fMimi", "fMina", "fMindy", "fMinerva"
        , "fMinnie", "fMira", "fMirabel", "fMirabelle", "fMiracle", "fMiranda", "fMiriam", "fMirielle", "mMisha",
        "fMissie"
        , "fMisty", "mMitch", "mMitchell", "mMitt", "fMitzi", "mMoe", "mMohamed", "mMohammad", "mMohammed", "fMoira"
        , "mMoises", "fMollie", "fMolly", "fMona", "fMonica", "fMonika", "fMonique", "fMontana", "mMonte", "fMontserrat"
        , "mMonty", "mMordecai", "mMorgan", "fMorgan", "fMorgana", "mMorris", "mMoses", "fMoya", "mMuhammad", "fMuriel"
        , "mMurphy", "mMurray", "fMya", "fMyfanwy", "fMyla", "mMyles", "fMyra", "fMyrna", "mMyron", "fMyrtle"
        , "fNadene", "fNadia", "fNadine", "fNaja", "fNala", "fNana", "fNancy", "fNanette", "fNaomi", "mNash"
        , "mNasir", "fNatalia", "fNatalie", "fNatasha", "mNate", "mNath", "mNathan", "mNathanael", "mNathaniel", "fNaya"
        , "fNayeli", "mNeal", "mNed", "mNehemiah", "mNeil", "fNell", "fNellie", "fNelly", "mNelson", "fNena"
        , "fNerissa", "mNesbit", "fNessa", "mNestor", "fNevaeh", "fNeve", "mNeville", "mNevin", "fNia", "mNiall"
        , "fNiamh", "fNichola", "mNicholas", "fNichole", "mNick", "fNicki", "mNickolas", "fNicky", "mNicky", "mNico"
        , "fNicola", "mNicolas", "fNicole", "fNicolette", "fNieve", "mNigel", "fNiki", "fNikita", "fNikki", "mNiklaus"
        , "mNikolai", "mNikolas", "fNila", "mNile", "mNils", "fNina", "fNishka", "mNoah", "mNoe", "mNoel"
        , "fNoelle", "fNoemi", "fNola", "mNolan", "fNora", "fNorah", "mNorbert", "fNoreen", "fNorma", "mNorman"
        , "fNova", "fNyla", "mOakes", "mOakley", "fOasis", "fOcean", "fOctavia", "mOctavio", "fOdalis", "fOdalys"
        , "fOdele", "fOdelia", "fOdette", "mOisin", "mOlaf", "fOlga", "mOli", "fOlive", "mOliver", "fOlivia"
        , "mOllie", "mOlly", "mOmar", "fOona", "fOonagh", "fOpal", "fOphelia", "fOprah", "mOran", "fOriana"
        , "fOrianna", "mOrion", "fOrla", "fOrlaith", "mOrlando", "mOrson", "mOscar", "mOsvaldo", "mOswald", "mOtis"
        , "mOtto", "mOwen", "mOzzie", "mOzzy", "mPablo", "mPaco", "mPaddy", "mPadraig", "fPage", "fPaige"
        , "fPaisley", "mPalmer", "fPaloma", "fPam", "fPamela", "fPandora", "fPansy", "fPaola", "mPaolo", "fParis"
        , "mParker", "mPascal", "mPat", "fPatience", "fPatrice", "fPatricia", "mPatrick", "fPatsy", "fPatti", "fPatty"
        , "mPaul", "fPaula", "fPaulette", "fPaulina", "fPauline", "mPaxton", "fPayton", "mPayton", "fPeace", "mPearce"
        , "fPearl", "mPedro", "fPeggy", "fPenelope", "fPenny", "mPercy", "fPerla", "fPerrie", "mPerry", "fPersephone"
        , "mPetar", "mPete", "mPeter", "fPetra", "fPetunia", "fPeyton", "mPeyton", "mPhebian", "mPhil", "mPhilip"
        , "mPhilippe", "mPhillip", "fPhillipa", "fPhilomena", "mPhineas", "fPhoebe", "fPhoenix", "mPhoenix", "fPhyllis",
        "mPierce"
        , "mPiers", "mPip", "fPiper", "fPippa", "fPixie", "fPolly", "fPollyanna", "fPoppy", "mPorter", "fPortia"
        , "mPoul", "mPrakash", "fPrecious", "fPresley", "fPreslie", "mPreston", "fPrimrose", "mPrince", "fPrincess",
        "mPrinceton"
        , "fPriscilla", "fPriya", "fPromise", "fPrudence", "fPrue", "fQueenie", "mQuentin", "fQuiana", "mQuincy",
        "mQuinlan"
        , "fQuinn", "mQuinn", "mQuinton", "mQuintrell", "fRabia", "fRachael", "fRachel", "fRachelle", "fRae", "fRaegan"
        , "fRaelyn", "mRafael", "mRafferty", "mRaheem", "mRahul", "mRaiden", "fRaina", "fRaine", "mRaj", "mRajesh"
        , "mRalph", "mRam", "mRameel", "mRamon", "fRamona", "mRamsey", "fRamsha", "mRandal", "mRandall", "fRandi"
        , "mRandolph", "mRandy", "fRani", "fRania", "mRaoul", "mRaphael", "fRaquel", "mRashad", "mRashan", "mRashid"
        , "mRaul", "fRaven", "mRavi", "mRay", "fRaya", "mRaylan", "mRaymond", "fRayna", "fRayne", "fReagan"
        , "fReanna", "fReanne", "fRebecca", "fRebekah", "mReece", "mReed", "mReef", "fReese", "mReese", "fRegan"
        , "mReggie", "fRegina", "mReginald", "mRehan", "mReid", "mReilly", "fReilly", "fReina", "mRemco", "fRemi"
        , "mRemington", "mRemy", "mRen", "fRena", "fRenata", "mRene", "fRene", "fRenee", "fRenesmee", "mReuben"
        , "mRex", "fReyna", "mReynaldo", "mReza", "fRhea", "mRhett", "fRhian", "fRhianna", "fRhiannon", "fRhoda"
        , "fRhona", "fRhonda", "mRhys", "fRia", "mRian", "fRianna", "mRicardo", "mRich", "mRichard", "mRichie"
        , "mRick", "mRickey", "fRicki", "mRickie", "mRicky", "mRico", "mRider", "fRihanna", "mRik", "mRiker"
        , "fRikki", "mRiley", "fRiley", "mRio", "fRita", "mRiver", "fRiver", "fRiya", "mRoan", "fRoanne"
        , "mRob", "mRobbie", "mRobby", "mRobert", "fRoberta", "mRoberto", "fRobin", "mRobin", "fRobyn", "mRocco"
        , "fRochelle", "fRocio", "mRock", "mRocky", "mRod", "mRoderick", "mRodger", "mRodney", "mRodolfo", "mRodrigo"
        , "mRogelio", "mRoger", "mRohan", "fRoisin", "mRoland", "fRolanda", "mRolando", "mRoman", "mRomeo", "mRon"
        , "mRonald", "mRonan", "fRonda", "fRoni", "mRonnie", "mRonny", "mRoosevelt", "mRory", "fRosa", "fRosalie"
        , "fRosalina", "fRosalind", "fRosalinda", "fRosalynn", "fRosanna", "mRoscoe", "fRose", "fRoseanne", "fRosella",
        "fRosemarie"
        , "fRosemary", "fRosetta", "fRosie", "mRoss", "fRosy", "fRowan", "mRowan", "fRowena", "fRoxana", "fRoxanne"
        , "fRoxie", "fRoxy", "mRoy", "mRoyce", "fRozlynn", "mRuairi", "mRuben", "mRubin", "fRuby", "mRudolph"
        , "mRudy", "fRue", "mRufus", "mRupert", "mRuss", "mRussell", "mRusty", "fRuth", "fRuthie", "mRyan"
        , "fRyanne", "fRydel", "mRyder", "mRyker", "mRylan", "mRyland", "fRylee", "fRyleigh", "mRyley", "fRylie"
        , "fSabina", "fSabine", "fSable", "fSabrina", "mSacha", "fSade", "fSadhbh", "fSadie", "fSaffron", "fSafire"
        , "fSafiya", "fSage", "fSahara", "mSaid", "fSaige", "fSaira", "fSally", "fSalma", "fSalome", "mSalvador"
        , "mSalvatore", "mSam", "fSam", "fSamantha", "fSamara", "fSamia", "mSamir", "fSamira", "fSammie", "fSammy"
        , "mSammy", "mSamson", "mSamuel", "mSandeep", "fSandra", "fSandy", "mSandy", "fSania", "mSanjay", "mSantiago"
        , "fSaoirse", "fSapphire", "fSara", "fSarah", "fSarina", "fSariya", "fSascha", "fSasha", "mSasha", "fSaskia"
        , "mSaul", "fSavanna", "fSavannah", "mSawyer", "fScarlet", "fScarlett", "mScot", "mScott", "mScottie", "mScotty"
        , "mSeamus", "mSean", "mSeb", "mSebastian", "fSebastianne", "mSebastien", "mSebestian", "fSelah", "fSelena",
        "fSelene"
        , "fSelina", "fSelma", "fSenuri", "fSeptember", "fSeren", "fSerena", "fSerenity", "mSergio", "mSeth",
        "mShadrach"
        , "fShakira", "fShana", "mShane", "fShania", "mShannon", "fShannon", "fShari", "fSharon", "fShary", "mShaun"
        , "fShauna", "mShawn", "fShawn", "fShawna", "fShawnette", "mShay", "fShayla", "fShayna", "mShayne", "fShea"
        , "mShea", "fSheba", "fSheena", "fSheila", "fShelby", "mSheldon", "fShelia", "fShelley", "fShelly", "mShelton"
        , "fSheri", "fSheridan", "mSherlock", "mSherman", "fSherri", "fSherrie", "fSherry", "fSheryl", "mShiloh",
        "fShirley"
        , "fShivani", "fShona", "fShonagh", "fShreya", "fShyla", "fSian", "mSid", "fSidney", "mSidney", "fSienna"
        , "fSierra", "fSigourney", "mSilas", "fSilvia", "mSimeon", "mSimon", "fSimone", "fSimran", "fSinead", "fSiobhan"
        , "fSky", "mSky", "fSkye", "mSkylar", "fSkylar", "mSkyler", "fSkyler", "mSlade", "fSloane", "fSnow"
        , "fSofia", "fSofie", "mSol", "mSolomon", "fSondra", "fSonia", "fSonja", "mSonny", "fSonya", "fSophia"
        , "fSophie", "fSophy", "mSoren", "fSorrel", "mSpencer", "mSpike", "fSpring", "mStacey", "fStacey", "fStaci"
        , "fStacie", "mStacy", "fStacy", "mStan", "mStanley", "fStar", "fStarla", "mStefan", "fStefanie", "fStella"
        , "fSteph", "mStephan", "fStephanie", "mStephen", "mSterling", "mSteve", "mSteven", "mStevie", "mStewart",
        "mStone"
        , "mStorm", "mStuart", "fSue", "mSufyan", "fSugar", "fSuki", "mSullivan", "fSummer", "fSusan", "fSusanna"
        , "fSusannah", "fSusanne", "fSusie", "fSutton", "fSuzanna", "fSuzanne", "fSuzette", "fSuzie", "fSuzy", "mSven"
        , "fSybil", "fSydney", "mSylvester", "fSylvia", "fSylvie", "fTabatha", "fTabitha", "mTadhg", "fTahlia", "fTala"
        , "fTalia", "fTalitha", "fTaliyah", "fTallulah", "mTalon", "mTam", "fTamara", "fTamera", "fTami", "fTamia"
        , "fTamika", "fTammi", "fTammie", "fTammy", "fTamra", "fTamsin", "fTania", "fTanika", "fTanisha", "mTanner"
        , "fTanya", "fTara", "mTariq", "mTarquin", "fTaryn", "fTasha", "fTasmin", "mTate", "fTatiana", "fTatum"
        , "fTawana", "fTaya", "fTayah", "fTayla", "fTaylah", "fTayler", "mTaylor", "fTaylor", "fTeagan", "mTed"
        , "mTeddy", "fTeegan", "fTegan", "fTeigan", "fTenille", "mTeo", "mTerence", "fTeresa", "fTeri", "mTerrance"
        , "mTerrell", "mTerrence", "fTerri", "fTerrie", "fTerry", "mTerry", "fTess", "fTessa", "mTevin", "mTex"
        , "mThad", "mThaddeus", "fThalia", "fThea", "fThelma", "mTheo", "fTheodora", "mTheodore", "mTheophilus",
        "fTheresa"
        , "fTherese", "mThomas", "fThomasina", "mThor", "fTia", "mTiago", "fTiana", "mTiberius", "fTiegan", "fTiffany"
        , "mTiger", "fTilly", "mTim", "mTimmy", "mTimothy", "fTina", "fTisha", "mTito", "mTitus", "mTobias"
        , "mTobin", "mToby", "mTod", "mTodd", "mTom", "mTomas", "mTommie", "mTommy", "fToni", "fTonia"
        , "mTony", "fTonya", "fTori", "mTorin", "mToryn", "mTrace", "fTracey", "mTracey", "fTraci", "fTracie"
        , "mTracy", "fTracy", "mTravis", "mTray", "mTremaine", "mTrent", "mTrenton", "mTrevon", "mTrevor", "mTrey"
        , "fTricia", "fTrina", "fTrinity", "fTrish", "fTrisha", "fTrista", "mTristan", "mTristen", "mTriston", "fTrixie"
        , "fTrixy", "mTroy", "fTrudy", "mTruman", "mTucker", "fTula", "fTulip", "mTy", "mTyler", "fTyra"
        , "mTyrese", "mTyrone", "mTyson", "fUlrica", "mUlysses", "fUma", "mUmar", "fUna", "mUriah", "mUriel"
        , "fUrsula", "mUsama", "mValentin", "fValentina", "mValentine", "mValentino", "fValeria", "fValerie", "fValery",
        "mVan"
        , "mVance", "fVanessa", "mVasco", "mVaughn", "fVeda", "fVelma", "fVenetia", "fVenus", "fVera", "fVerity"
        , "mVernon", "fVeronica", "fVicki", "fVickie", "fVicky", "mVictor", "fVictoria", "fVienna", "mVihan", "mVijay"
        , "mVikram", "mVince", "mVincent", "mVinnie", "fViola", "fViolet", "fVioletta", "mVirgil", "fVirginia",
        "mVishal"
        , "fVivian", "mVivian", "fViviana", "fVivien", "fVivienne", "mVlad", "mVladimir", "mWade", "mWalker", "mWallace"
        , "fWallis", "mWalter", "fWanda", "mWarren", "fWaverley", "mWaylon", "mWayne", "mWendell", "fWendi", "fWendy"
        , "mWes", "mWesley", "mWeston", "fWhitney", "mWilbert", "mWilbur", "mWiley", "mWilfred", "mWilhelm",
        "fWilhelmina"
        , "mWill", "fWilla", "mWillam", "mWillard", "mWillem", "mWilliam", "mWillie", "mWillis", "fWillow", "fWilma"
        , "mWilson", "fWinnie", "fWinnifred", "fWinona", "mWinston", "fWinter", "mWolfgang", "mWoody", "mWyatt",
        "mXander"
        , "fXandra", "fXanthe", "mXavier", "fXaviera", "fXena", "mXerxes", "fXia", "fXimena", "fXochil", "fXochitl"
        , "mYahir", "mYardley", "fYasmin", "fYasmine", "fYazmin", "mYehudi", "fYelena", "fYesenia", "mYestin",
        "fYolanda"
        , "mYork", "fYsabel", "fYulissa", "mYuri", "mYusuf", "fYvaine", "mYves", "fYvette", "fYvonne", "mZac"
        , "mZach", "mZachariah", "mZachary", "mZachery", "mZack", "mZackary", "mZackery", "fZada", "fZaheera", "fZahra"
        , "mZaiden", "mZain", "mZaine", "fZaira", "mZak", "fZakia", "fZali", "mZander", "mZane", "fZara"
        , "fZaria", "fZaya", "mZayden", "fZayla", "mZayn", "mZayne", "mZeb", "mZebulon", "mZed", "mZeke"
        , "fZelda", "fZelida", "fZelina", "fZena", "fZendaya", "mZeph", "fZia", "mZiggy", "fZina", "mZion"
        , "fZiva", "fZoe", "fZoey", "fZola", "mZoltan", "fZora", "fZoya", "fZula", "fZuri", "mZuriel"
        , "fZyana", "mZylen",
    ]
    size = len(ALL_ENG_NAMES) - 1
    while True:
        idx_name = random.randint(0, size)
        if male and ALL_ENG_NAMES[idx_name][0] == 'm':
            return ALL_ENG_NAMES[idx_name][1:]
        if not male and ALL_ENG_NAMES[idx_name][0] == 'f':
            return ALL_ENG_NAMES[idx_name][1:]
def randomuuid():
    return str(uuid.uuid4())
def nametopinyin(xname):
    pydict=lazy_pinyin(xname)
    pinyin=""
    for x in pydict:
        pinyin=pinyin+x
    pinyin=pinyin.strip()
    return pinyin
def randompass(xsalt):
    minlength=5
    maxlength = 25
    length = random.randint(minlength,maxlength)
    letters = string.ascii_letters + string.digits
    yyy= ''.join([random.choice(letters) for _ in range(length)])
    xxx=md5()
    yyy=yyy+xsalt
    xxx.update(yyy)
    return xxx.hexdigest()
def randompaypass(xsalt):
    x= ''.join([random.choice(string.digits) for _ in range(6)] )
    x=xsalt+x
    m=md5()
    m.update(x)
    return m.hexdigest()
def salt():
    letters = string.ascii_letters + string.digits
    return ''.join([random.choice(letters) for _ in range(6)])
def randommail(pyname,phone,gg):
    maybepm=random.randint(1,1500)
    if maybepm<=300:
        prl=['163.com','126.com','qq.com','vip.163.com','vip.126.com','gmail.com']
        return phone+"@"+random.choice(prl)
    qqor=random.randint(1,2)
    if qqor==1:
        leg=random.randint(1,5000)
        if leg<=1000:
            leng=8
        elif leg<=4500:
            leng=9
        elif leg<=4900:
            leng=10
        else:
            leng=11
        qqn=''.join ([random.choice(string.digits) for _ in range(leng)])
        return qqn+"@qq.com"
    else:
        leg=random.randint(1,5000)
        if leg<=1000:
            leng=8
        elif leg<=4500:
            leng=9
        elif leg<=4900:
            leng=10
        else:
            leng=11
        qqn=''.join ([random.choice(string.digits) for _ in range(leng)])
        xname=randengname(gg)
        randpaddingloc=random.randint(1,2)
        if randpaddingloc==1:
            rap=''.join ([random.choice(["6","8","1","5","9","a","f","d","s","p","r","m","b","y","t"]) for _ in range(random.randint(0,4))])
        else:
            rap=''.join ([random.choice(["6","6","6","8","8","8","8","8","8","1","5","9","a","a","a","f","d","s","p","r","m","b","y","t"]) for _ in range(random.randint(0,4))])
        xp=random.randint(1,1000)
        tailm=random.choice(["163.com","163.com","163.com","126.com"])
        if xp<=150:
            return qqn+"@"+tailm
        elif xp<=370:
            if randpaddingloc==1:
                return rap+pyname+"@"+tailm
            else:
                return pyname+rap+"@"+tailm
        else:
            if randpaddingloc==1:
                return rap+xname+"@"+tailm
            else:
                return xname+rap+"@"+tailm

def randphone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
               "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    tailnumber = ''.join([random.choice(string.digits) for _ in range(8)])
    phone = random.choice(prelist)
    pn = phone + tailnumber
    return pn
def getdistrictcode():
    global districtlist
    for node in districtlist:
        if node[10:11] != ' ':
            state = node[10:].strip()
        if node[10:11] == ' ' and node[12:13] != ' ':
            city = node[12:].strip()
        if node[10:11] == ' ' and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            codelist.append({"state": state, "city": city, "district": district, "code": code})
    return codelist

def cnid():

    global codelist
    codelist = []
    if not codelist:
        codelist=getdistrictcode()
    id = codelist[random.randint(0, len(codelist)-1)]['code']  # 地区项

    id = id + str(random.randint(1930, 2013))  # 年份项
    da = datetime.date.today() + datetime.timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理
    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                 '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
        id = id + checkcode[str(count % 11)]  # 算出校验码
        return id
def randdxr_cr():
    return random.choice(["H","A","C","K","E","D","B","Y","A","R","R","Y","B","O","O","M"])
def randomcreatetime():
    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳
    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    return str(t)
def randomupdatetime(stime):
    end = time.mktime(a2)
    xtime=random.randint(int(stime),end)
    return str(xtime)
class person:
    def __init__(self):
        self.realname = randomname()
        self.username = nametopinyin(self.realname.decode("utf-8"))
        self.salt = salt()
        self.account_id = randomuuid()
        self.password = randompass(self.salt)
        self.gender = randgender()
        self.status = randstatus()
        self.cx_coin = cx_coin()
        self.customer_id = randcustomer_id()
        self.cid = randcid()
        self.account_type = randaccounttype()
        self.trade_count = randtrade_count()
        self.txnid = randtxnid()
        self.phone = randphone()
        self.pay_pass = randompaypass(self.salt)
        self.CNID = cnid()
        self.mail = randommail(self.username, self.phone, self.gender)
        self.dxr_cr=randdxr_cr()
        self.create_date=randomcreatetime()
        self.update_date=randomupdatetime(self.create_date)
if __name__=="__main__":
    reload(sys)
    sys.setdefaultencoding("utf-8")
    global a1
    global a2
    a1 = (2018, 7, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
    a2 = (2018, 7, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（1990-12-31 23：59：59）
    global districtlist
    DC_PATH = "districtcode.txt"
    with open(DC_PATH) as file:
        data = file.read()
        districtlist = data.split('\n')
    xsql=sql.connect(host="localhost",user="root",
 	password="123456",db="test",port=3306,charset="utf8")
    conn=xsql.cursor()
    m=1
    for _ in range(1,random.randint(12335,33225)):
        px=person()
        m=m+1
        conn.execute("insert into trap_users(account_id,username,password,mail,salt,create_date,update_date,CNID,realname,pay_pass,phone,txnid,gender,status,cx_coin,customer_id,cid,account_type,dxr_cr,trade_count) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(px.account_id,px.username,px.password,px.mail,px.salt,px.create_date,px.update_date,px.CNID,px.realname,px.pay_pass,px.phone,px.txnid,px.gender,px.status,px.cx_coin,px.customer_id,px.cid,px.account_type,px.dxr_cr,px.trade_count))
        xsql.commit()
        del px
        print m