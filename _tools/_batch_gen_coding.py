# -*- coding: utf-8 -*-
"""
Coding版批量截图生成：基于 lessons_coding.json 的结构化 blocks，
推导嵌套容器（重复执行/如果…那么…否则），生成每课 step-02/03/04 + full-program 4张图。
"""
import sys, os, json, re
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT_DIR, "_tools"))
from _mblock_renderer import draw_mblock_interface, COLORS

BASE_DIR = os.path.join(ROOT_DIR, "AI编程探险课_CyberPi", "assets", "blocks")

# 分类 → 渲染参数
CAT_MAP = {
    '事件':   {'shape': 'hat', 'color': COLORS['event']},
    '显示':   {'shape': 'stack', 'color': COLORS['display']},
    '灯':     {'shape': 'stack', 'color': COLORS['light']},
    '声音':   {'shape': 'stack', 'color': COLORS['play']},
    '等待':   {'shape': 'stack', 'color': COLORS['control']},
    '传感':   {'shape': 'stack', 'color': COLORS['sensing']},
    '运算':   {'shape': 'stack', 'color': COLORS['operator']},
    '变量':   {'shape': 'stack', 'color': COLORS['variable']},
    '自制积木': {'shape': 'hat', 'color': COLORS['myblock']},
    'AI':     {'shape': 'stack', 'color': COLORS['ai']},
    '控制':   {'shape': 'stack', 'color': COLORS['control']},
}

def is_hat(cat, desc):
    """判断是否为帽子块（新段开始）"""
    if cat == '事件':
        return True
    if cat == '自制积木' and ('定义' in desc or '自制积木' in desc):
        return True
    return False

def count_top_blocks(seg):
    """统计一段的顶层块数量（帽子1+子块）"""
    n = 1
    for item in seg.get('children', []):
        n += 1
    return n

def build_lesson_blocks(flat_blocks):
    """扁平blocks → 段列表（每段: {hat:..., children:[嵌套块]}）"""
    segments = []
    cur_seg = None
    stack = []  # 容器栈: {'kind':'repeat'|'if', 'node':..., 'branch':'then'|'else'}

    def add_to_current(node):
        if stack:
            top = stack[-1]
            if top['kind'] == 'if' and top['branch'] == 'else':
                top['node']['else_blocks'].append(node)
            else:
                top['node']['inner_blocks'].append(node)
        else:
            cur_seg['children'].append(node)

    for cat, desc in flat_blocks:
        if is_hat(cat, desc):
            # 新段
            text = desc.replace('「', '').replace('」', '')
            if cat == '自制积木':
                if not text.startswith('定义'):
                    text = '定义 ' + text
            seg = {'hat': {'type': 'event', 'shape': 'hat', 'text': text, 'color': CAT_MAP[cat]['color']},
                   'children': []}
            segments.append(seg)
            cur_seg = seg
            stack = []
            continue

        if cat == '控制' and '重复执行' in desc:
            m = re.search(r'重复执行\s*(\d+)\s*次', desc)
            times = m.group(1) if m else ''
            text = f'重复执行 {times} 次' if times else '重复执行'
            node = {'type': 'control', 'shape': 'repeat', 'text': text,
                    'color': COLORS['control'], 'inner_blocks': []}
            add_to_current(node)
            stack.append({'kind': 'repeat', 'node': node})
            continue

        if cat == '控制' and '如果' in desc and '那么' in desc:
            cond = desc.replace('如果', '').replace('那么', '').strip()
            text = f'如果 {cond} 那么'
            node = {'type': 'control', 'shape': 'c', 'text': text,
                    'color': COLORS['control'], 'inner_blocks': [], 'else_blocks': []}
            add_to_current(node)
            stack.append({'kind': 'if', 'node': node, 'branch': 'then'})
            continue

        if cat == '控制' and '否则' in desc:
            if stack and stack[-1]['kind'] == 'if':
                stack[-1]['branch'] = 'else'
            continue

        # 普通块
        cfg = CAT_MAP.get(cat, {'shape': 'stack', 'color': COLORS['display']})
        text = desc.replace('「', '').replace('」', '')
        # 变量操作解析
        node = {'type': cat, 'shape': cfg['shape'], 'text': text, 'color': cfg['color']}
        add_to_current(node)

    return segments

def segments_to_config(segs):
    """段列表 → 渲染配置（把 hat 和 children 平铺，children 作为 inner_blocks 递归）"""
    out = []
    for seg in segs:
        out.append(seg['hat'])
        for child in seg['children']:
            out.append(flatten_child(child))
    return out

def flatten_child(node):
    """递归展开子块（处理嵌套容器）"""
    if 'inner_blocks' in node:
        node = dict(node)
        node['inner_blocks'] = [flatten_child(c) for c in node['inner_blocks']]
        if node.get('else_blocks'):
            node['else_blocks'] = [flatten_child(c) for c in node['else_blocks']]
    return node

def cut_single_seg(seg, top_limit):
    """截取单段的前 top_limit 个顶层子块"""
    import copy
    seg2 = copy.deepcopy(seg)
    seg2['children'] = seg2['children'][:top_limit]
    return seg2

def generate_lesson_screenshots(lid, flat_blocks):
    segs = build_lesson_blocks(flat_blocks)
    n_seg = len(segs)
    total_top = sum(count_top_blocks(s) for s in segs)

    if n_seg >= 2:
        step02 = segs[:1]
        step03 = segs[:2]
    elif n_seg == 1:
        # 单段：step02 = 帽子+前2子块，step03 = 完整段
        step02 = [cut_single_seg(segs[0], 2)]
        step03 = segs[:]
    else:
        step02 = step03 = []
    step04 = segs[:]
    full = segs[:]

    lesson_dir = os.path.join(BASE_DIR, f"lesson-{lid:02d}")
    os.makedirs(lesson_dir, exist_ok=True)

    for name, config in [('step-02', step02), ('step-03', step03), ('step-04', step04), ('full-program', full)]:
        blocks_cfg = segments_to_config(config)
        img = draw_mblock_interface(blocks_cfg, lid, name)
        img.save(os.path.join(lesson_dir, f"{name}.png"))

    return n_seg, total_top

def main():
    with open(os.path.join(ROOT_DIR, "_tools", "lessons_coding.json"), encoding='utf-8') as f:
        lessons = json.load(f)

    count = 0
    for l in lessons:
        lid = l['id']
        try:
            n_seg, total = generate_lesson_screenshots(lid, l['blocks'])
            print(f"✓ 第{lid:2d}课 - {total}块/{n_seg}段 - 4张截图已生成")
            count += 1
        except Exception as e:
            print(f"✗ 第{lid}课失败: {e}")
            import traceback
            traceback.print_exc()

    print(f"\n完成！共生成 {count} 课 × 4张 = {count*4} 张截图")

if __name__ == '__main__':
    main()
