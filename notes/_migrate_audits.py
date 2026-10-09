# -*- coding: utf-8 -*-
import io, json

def load(n):
    p = 'notes/semantic-audits/第%s章-语义审计.json' % n
    return p, json.load(io.open(p, encoding='utf-8'))

def save(p, d):
    io.open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

def setq(items, idx, quote, **kw):
    it = items[idx]
    it['quote'] = quote
    for k, v in kw.items():
        it[k] = v

# ---- ch4 ----
p, d = load('004')
setq(d['claims'], 3, "回想两天都是加班到十一点半，我从公司走回去，路上固定会经过两辆卖炒粉的三轮车和一家通宵亮着的便利店。")
setq(d['claims'], 4, "东平码头那边的物流仓上班，夜班调度，两班倒。")
setq(d['claims'], 5, "“你已被移出群聊”")
d['dialogueExposition']['entries'][0]['quote'] = "他退钱，是因为你是个麻烦，不是因为你赢了。"
d['cognition'][1]['citedInfo'] = "他退钱，是因为你是个麻烦，不是因为你赢了。"
d['joins']['auditedToNext']['nextHeadQuote'] = "手机在桌角震起来，屏幕上两个字：周敏。"
save(p, d)

# ---- ch6 ----
p, d = load('006')
d['joins']['prevToAudited']['prevTailQuote'] = "两个数看着一样真。这一趟，就是去把其中一个划掉的。"
save(p, d)

# ---- ch7 ----
p, d = load('007')
setq(d['claims'], 12, "我看了眼地图。从物流园南三门到这家便利店，绕行距离三点二公里。")
setq(d['claims'], 13, "剩下能用的，一张一张编号，每张后面贴上拍摄时间：路面封堵一点零一，涵洞出口一点四十，便利店一点五十五。")
setq(d['claims'], 14, "“记着就行。”他把手套往下扒了一半，“下回要是顺路，你说话。要是专门为你跑远路，那就另说。”",
     type="制度与流程")
d['cognition'][2]['citedInfo'] = "欠下一趟了"
d['cognition'][2]['sourceQuote'] = "“今晚这一趟，我记着。”"
save(p, d)

# ---- ch8 ----
p, d = load('008')
setq(d['claims'], 2, "他陪我蹲在桥洞底下冻的那半个钟头")
setq(d['claims'], 10, "这一下按出去，欠杜勇的那一趟、那两公里没灯的路、他陪我蹲在桥洞底下冻的那半个钟头，就")
d['cognition'][1]['citedInfo'] = "“发吧。”它说，“就算只有十个人看，有一个人今晚少掉进坑里，你这半宿就没白熬。”"
d['cognition'][1]['sourceQuote'] = "欠下一趟了"
save(p, d)

# ---- ch9 ----
p, d = load('009')
setq(d['claims'], 0, "五点十五我摸黑看过一次，那会儿还是1。杜勇回那个“转”字的时候我没当真，现在看来是真转了")
setq(d['claims'], 9, "欠杜勇的那一趟，他陪我吹的半宿江风，换回来的就是这三十七双眼睛随手一扫。")
setq(d['claims'], 10, "账上还欠着杜勇一趟没还")
save(p, d)
print('quotes migrated')
