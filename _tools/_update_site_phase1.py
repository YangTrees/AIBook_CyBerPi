# -*- coding: utf-8 -*-
"""
Coding分支网站全面更新：
1. 首页文案（编程学习定位）
2. CHAPTERS（4个新章节）
3. LESSONS_1~4（32课全新数据）
4. CURRICULUM_REFINEMENTS（32课）
5. SAMPLE_CONTENT（32课）
"""
import json, os, re, shutil, time

BASE = r"D:\AI\_AIBook\AIBook_Offline_CyberPi"
HTML = os.path.join(BASE, "AI编程探险课_CyberPi", "index.html")
DATA = os.path.join(BASE, "_tools", "lessons_coding.json")

# 备份
bak = HTML + f".bak_{time.strftime('%H%M%S')}"
shutil.copy2(HTML, bak)
print(f"已备份 → {os.path.basename(bak)}")

with open(DATA, encoding='utf-8') as f:
    lessons = json.load(f)
assert len(lessons) == 32, f"课程数错误: {len(lessons)}"

with open(HTML, encoding='utf-8') as f:
    content = f.read()

# ============ 1. 首页文案 ============
repls = [
    # 品牌
    ('<div class="brand-name">AI逻辑与硬件交互课程（CyberPi）</div>',
     '<div class="brand-name">CyberPi 积木编程探险课</div>'),
    ('<div class="brand-sub">AI硬件编程 · 在线积木实践</div>',
     '<div class="brand-sub">mBlock 积木编程 · CyberPi 动手实践</div>'),
    # hero
    ('<div class="hero-kicker">AI LOGIC × HARDWARE × CODING</div>',
     '<div class="hero-kicker">BLOCK CODING × HARDWARE × CREATION</div>'),
    ('<h1><span class="hero-title-main">AI逻辑与硬件交互课程 <small>（CyBerPi）</small></span><em>让AI连接真实世界</em></h1>',
     '<h1><span class="hero-title-main">CyberPi 积木编程探险课 <small>（6–9 岁）</small></span><em>像搭积木一样学会编程</em></h1>'),
    ('<p class="lead">团团和点点把绘本里的 AI 问题带进创客课堂。孩子通过在线积木编程完成每一节AI任务，再用 CyberPi 感知环境、执行程序、反馈结果。</p>',
     '<p class="lead">团团和点点在 CyberPi 上一步步学习积木编程：从屏幕显示、灯光声音，到事件循环、条件变量，再到自制积木和AI语音。每课都在真实设备上运行验证。</p>'),
    ('<div class="hero-proof"><span>每课都有编程任务</span><span>真实运行与调试</span><span>与原绘本一一呼应</span></div>',
     '<div class="hero-proof"><span>每课都有编程任务</span><span>真机运行与调试</span><span>递进式编程成长路径</span></div>'),
    # 按钮样板课
    ('<button class="btn ghost big" onclick="go(\'#/course/17\')">查看样板课</button>',
     '<button class="btn ghost big" onclick="go(\'#/course/18\')">查看样板课</button>'),
    # float chips
    ('故事 → 编程 → 测试', '编程 → 上传 → 验证'),
    ('AI硬件编程全程实践', '积木编程全程真机实践'),
    # stats
    ('<div class="stat-card"><div class="num">8</div><div class="lab">个 AI 主题</div></div>',
     '<div class="stat-card"><div class="num">9</div><div class="lab">类编程积木</div></div>'),
    # studio strip
    ('<div class="studio-step"><span class="no">01</span><div><b>在绘本中发现问题</b><p>用熟悉的故事建立AI概念入口</p></div></div>',
     '<div class="studio-step"><span class="no">01</span><div><b>认识新积木</b><p>先了解本课会用到的积木分类和功能</p></div></div>'),
    ('<div class="studio-step"><span class="no">02</span><div><b>在线搭建AI程序</b><p>连接积木、运行、观察并找到错误</p></div></div>',
     '<div class="studio-step"><span class="no">02</span><div><b>搭建积木程序</b><p>按步骤连接积木，在 mBlock 中完成程序</p></div></div>'),
    ('<div class="studio-step"><span class="no">03</span><div><b>用 CyberPi 验证</b><p>让程序连接真实世界的输入与输出</p></div></div>',
     '<div class="studio-step"><span class="no">03</span><div><b>上传到 CyberPi 验证</b><p>把程序烧录进设备，观察灯光、屏幕和声音</p></div></div>'),
    # legend
    ('<span class="lg"><span class="sw" style="background:var(--ch1)"></span>第一章 信息与感知（1–8 课）</span>',
     '<span class="lg"><span class="sw" style="background:var(--ch1)"></span>第一章 初识CyberPi（1–8 课）</span>'),
    ('<span class="lg"><span class="sw" style="background:var(--ch2)"></span>第二章 算法与思维（9–16 课）</span>',
     '<span class="lg"><span class="sw" style="background:var(--ch2)"></span>第二章 事件与控制（9–16 课）</span>'),
    ('<span class="lg"><span class="sw" style="background:var(--ch3)"></span>第三章 机器学习（17–24 课）</span>',
     '<span class="lg"><span class="sw" style="background:var(--ch3)"></span>第三章 逻辑与智慧（17–24 课）</span>'),
    ('<span class="lg"><span class="sw" style="background:var(--ch4)"></span>第四章 AI 创造与未来（25–32 课）</span>',
     '<span class="lg"><span class="sw" style="background:var(--ch4)"></span>第四章 创意项目工坊（25–32 课）</span>'),
    # 全部课程
    ('<span class="chip" style="margin-left:auto">和绘本课一一呼应</span>',
     '<span class="chip" style="margin-left:auto">编程能力递进 · 32 课</span>'),
    # featured cards
    ('<article class="featured-card"><span class="tag">入门样板 · 第 01 课</span><h3>信息怎么走？</h3><p>从“按键—判断—反馈”理解输入、处理与输出，并完成第一个可运行程序。</p><button onclick="go(\'#/course/1\')">查看课程设计 →</button></article>',
     '<article class="featured-card"><span class="tag">入门样板 · 第 01 课</span><h3>你好，CyberPi！</h3><p>从屏幕显示开始，学习顺序结构，完成第一个可运行程序。</p><button onclick="go(\'#/course/1\')">查看课程设计 →</button></article>'),
    ('<article class="featured-card"><span class="tag">核心样板 · 第 17 课</span><h3>让模型接受新题考试</h3><p>在在线积木编程环境中区分训练样本与测试样本，用新数据验证模型是否真的学会。</p><button onclick="go(\'#/course/17\')">查看课程设计 →</button></article>',
     '<article class="featured-card"><span class="tag">核心样板 · 第 18 课</span><h3>智能夜灯</h3><p>用光线和声音两个条件实现自动判断，感受程序如何感知环境。</p><button onclick="go(\'#/course/18\')">查看课程设计 →</button></article>'),
    ('<article class="featured-card"><span class="tag">素养样板 · 第 30 课</span><h3>公平要用实验说话</h3><p>用随机抽签和多轮统计观察差异，讨论数据、规则与结果之间的关系。</p><button onclick="go(\'#/course/30\')">查看课程设计 →</button></article>',
     '<article class="featured-card"><span class="tag">AI 样板 · 第 29 课</span><h3>会说话的CyberPi</h3><p>连接网络，让 CyberPi 用语音合成朗读文字，体验 AI 语音能力。</p><button onclick="go(\'#/course/29\')">查看课程设计 →</button></article>'),
    # hw-feats
    ('<div><b>读故事</b><p>每课先回看同名 AI 绘本课的故事，带着问题进入编程</p></div>',
     '<div><b>看积木</b><p>每课先认识本课要用的积木分类和它们的功能</p></div>'),
    ('<div><b>搭积木</b><p>通过在线积木编程学习顺序、条件、循环、变量与AI扩展</p></div>',
     '<div><b>搭程序</b><p>从顺序到事件、循环、条件、变量、自制积木，递进式学习</p></div>'),
    ('<div><b>看效果</b><p>程序上传到 CyberPi，灯亮、屏显、发声，AI 知识现场演示</p></div>',
     '<div><b>真机验证</b><p>程序上传到 CyberPi，灯光、屏幕、声音和传感器全部真实运行</p></div>'),
    ('<div><b>做挑战</b><p>每课一个动手挑战 + 随堂问答，答对点亮勋章</p></div>',
     '<div><b>做挑战</b><p>每课一个动手挑战 + 随堂问答，答对点亮勋章</p></div>'),
]
for old, new in repls:
    if old in content:
        content = content.replace(old, new)
    else:
        print(f"⚠ 未找到: {old[:50]}...")

# 标题
content = content.replace(
    '<title>AI逻辑与硬件交互课程（CyberPi）</title>',
    '<title>CyberPi 积木编程探险课</title>'
)

# ============ 2. CHAPTERS ============
chapter_pattern = re.compile(r'var CHAPTERS = \[.*?\];', re.DOTALL)
new_chapters = '''var CHAPTERS = [
  {id:1, name:'初识CyberPi', range:'第 1–8 课', desc:'认识设备 · 顺序执行 · 屏幕/灯光/声音输出', color:'var(--ch1)',
   icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="14" rx="3"/><path d="M7 9h10M7 13h4"/><circle cx="16" cy="13" r="1.6"/></svg>'},
  {id:2, name:'事件与控制', range:'第 9–16 课', desc:'按键/摇杆事件 · 循环结构 · 灯光动画', color:'var(--ch2)',
   icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4.5 13.5H11L9.5 22 19 10h-6.5L13 2z"/></svg>'},
  {id:3, name:'逻辑与智慧', range:'第 17–24 课', desc:'条件判断 · 变量运算 · 多传感器联动', color:'var(--ch3)',
   icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="5" cy="6" r="2.4"/><circle cx="19" cy="6" r="2.4"/><circle cx="12" cy="18" r="2.4"/><path d="M6.8 7.4 10.8 16M17.2 7.4 13.2 16M7.4 6h9.2"/></svg>'},
  {id:4, name:'创意项目工坊', range:'第 25–32 课', desc:'自制积木 · 综合项目 · AI语音体验', color:'var(--ch4)',
   icon:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.8 4.6L18.5 9l-4.7 1.4L12 15l-1.8-4.6L5.5 9l4.7-1.4L12 3z"/><path d="M19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9L19 15z"/></svg>'}
];'''
content, n = chapter_pattern.subn(new_chapters, content, count=1)
print(f"CHAPTERS 替换: {'✓' if n else '✗'}")

# ============ 3. LESSONS_1~4 数据 ============
def lesson_to_js(l):
    qs = ','.join(
        '{q:"%s",o:[%s],a:%d,exp:"%s"}' % (
            lq['q'].replace('"','\\"'),
            ','.join('"%s"' % o.replace('"','\\"') for o in lq['o']),
            lq['a'], lq['exp'].replace('"','\\"'))
        for lq in l['quiz'])
    return '''{
  id:%d, ch:%d, title:"%s", theme:"%s",
  echoId:%d, echoTitle:"%s", echoBrief:"%s",
  story:"%s",
  knowledge:[%s],
  blocks:[%s],
  projName:"%s",
  projEff:"%s",
  steps:[%s],
  challenge:"%s",
  tip:"%s",
  hardware:[%s],
  quiz:[%s]
}''' % (
    l['id'], l['ch'], l['title'], l['theme'],
    l['id'], l['echoTitle'], l['echoBrief'],
    l['story'],
    ','.join('"%s"' % k.replace('"','\\"') for k in l['knowledge']),
    ','.join('["%s","%s"]' % (b[0].replace('"','\\"'), b[1].replace('"','\\"')) for b in l['blocks']),
    l['projName'].replace('"','\\"'), l['projEff'].replace('"','\\"'),
    ','.join('"%s"' % s.replace('"','\\"') for s in l['steps']),
    l['challenge'].replace('"','\\"'), l['tip'].replace('"','\\"'),
    ','.join('"%s"' % h.replace('"','\\"') for h in l['hardware']),
    qs)

# 按章节分组
ch1 = [l for l in lessons if l['ch']==1]
ch2 = [l for l in lessons if l['ch']==2]
ch3 = [l for l in lessons if l['ch']==3]
ch4 = [l for l in lessons if l['ch']==4]

def build_lessons_block(ch_lessons):
    inner = ',\n'.join(lesson_to_js(l) for l in ch_lessons)
    return 'const LESSONS = [\n' + inner + '\n];'

# 找到并替换 LESSONS_1 到 LESSONS_4（在 const LESSONS_1 到 CURRICULUM_REFINEMENTS 前）
lessons_start = content.find('const LESSONS_1')
refine_start = content.find('const CURRICULUM_REFINEMENTS')
if lessons_start < 0 or refine_start < 0:
    print(f"✗ 定位失败: LESSONS_1={lessons_start}, REFINE={refine_start}")
else:
    new_lessons = '\n/* ============ 课程数据（Coding 版） ============ */\n'
    for i, ch_lessons in enumerate([ch1, ch2, ch3, ch4], 1):
        inner = ',\n'.join(lesson_to_js(l) for l in ch_lessons)
        new_lessons += f'const LESSONS_{i} = [\n{inner}\n];\n\n'
    content = content[:lessons_start] + new_lessons + content[refine_start:]
    print("✓ LESSONS_1~4 已替换")

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print("\n第一阶段完成：首页文案 + CHAPTERS + LESSONS_1~4")
print(f"备份文件: {os.path.basename(bak)}")
