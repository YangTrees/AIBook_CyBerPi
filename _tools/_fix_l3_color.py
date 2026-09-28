# -*- coding: utf-8 -*-
"""第3课：RGB灯亮起 黄色 -> 红色（积木、步骤、效果描述、目标、driving/deliverable）"""
import io

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

pairs = [
    # blocks 积木（仅第3课，含重复执行+等待0.5秒上下文）
    ('["控制","重复执行"],["灯","RGB灯亮起 黄色"],["等待","等待0.5秒"]',
     '["控制","重复执行"],["灯","RGB灯亮起 红色"],["等待","等待0.5秒"]'),
    # steps 第4步
    ('循环内放入「RGB灯亮起 黄色」', '循环内放入「RGB灯亮起 红色」'),
    # projEff + driving + deliverable（3处相同文本）
    ('反复亮起黄色、熄灭，形成一闪一闪的星星效果', '反复亮起红色、熄灭，形成一闪一闪的星星效果'),
    # curriculum 3 goal
    ('反复亮起黄色、熄灭，形成一闪一闪的效果', '反复亮起红色、熄灭，形成一闪一闪的效果'),
]
for old, new in pairs:
    n = s.count(old)
    print('count=%d  %s' % (n, old[:26]))
    s = s.replace(old, new)

io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('done')
