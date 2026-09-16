# -*- coding: utf-8 -*-
"""
批量生成第5-32课mBlock截图
基于课程steps精确匹配积木内容
"""
import sys, os, json, re
sys.path.insert(0, r"D:\PROJECTS\_AI\AIBook_CyberPi")
from _mblock_renderer import draw_mblock_interface, COLORS

BASE_DIR = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\blocks"

def parse_steps_to_blocks(steps):
    """从步骤描述中解析出积木列表"""
    blocks = []
    for step in steps:
        s = step.strip()
        # 跳过上传验证步骤
        if '点击上传' in s or '烧录' in s or '验证' in s:
            continue
        
        # 事件类积木
        if '启动' in s or '开机' in s:
            blocks.append({'type':'event', 'text':'当童芯派启动时', 'shape':'hat', 'color':COLORS['event']})
        elif '按钮 A' in s or '按键A' in s or '按A' in s:
            blocks.append({'type':'event', 'text':'当按键 A ▼ 按下时', 'shape':'hat', 'color':COLORS['event']})
        elif '按钮 B' in s or '按键B' in s or '按B' in s:
            blocks.append({'type':'event', 'text':'当按键 B ▼ 按下时', 'shape':'hat', 'color':COLORS['event']})
        elif '摇杆' in s:
            blocks.append({'type':'event', 'text':'当摇杆 向上拨动 ▼ 时', 'shape':'hat', 'color':COLORS['event']})
        
        # 变量类积木
        elif '建立变量' in s or '变量' in s and '设为' in s:
            var_name = '变量'
            m = re.search(r'「([^」]+)」', s)
            if m: var_name = m.group(1)
            if '增加' in s or '+1' in s or '加 1' in s:
                blocks.append({'type':'variable', 'text':f'将 {var_name} ▼ 增加 1', 'shape':'stack', 'color':COLORS['variable']})
            elif '设为0' in s or '设为 0' in s or '初始为0' in s or '清零' in s:
                blocks.append({'type':'variable', 'text':f'将 {var_name} ▼ 设为 0', 'shape':'stack', 'color':COLORS['variable']})
            else:
                blocks.append({'type':'variable', 'text':f'将 {var_name} ▼ 设为 0', 'shape':'stack', 'color':COLORS['variable']})
        elif '变量' in s and '增加' in s:
            blocks.append({'type':'variable', 'text':'将 变量 ▼ 增加 1', 'shape':'stack', 'color':COLORS['variable']})
        
        # 控制类积木
        elif '重复' in s or '循环' in s:
            times = '3'
            m = re.search(r'(\d+)\s*次', s)
            if m: times = m.group(1)
            inner = []
            if '灯' in s or '闪' in s:
                inner.append({'text':'RGB灯 亮起 红色', 'color':COLORS['light']})
                inner.append({'text':'等待 0.2 秒', 'color':COLORS['control']})
            blocks.append({'type':'control', 'text':f'重复执行 {times} 次', 'shape':'repeat', 'color':COLORS['control'], 'inner_blocks':inner})
        elif '如果' in s or '判断' in s or '条件' in s:
            blocks.append({'type':'control', 'text':'如果 ... 那么 ... 否则', 'shape':'c', 'color':COLORS['control'],
                          'inner_blocks':[{'text':'显示标签  条件成立', 'color':COLORS['display']}]})
        elif '等待' in s:
            blocks.append({'type':'control', 'text':'等待 0.5 秒', 'shape':'stack', 'color':COLORS['control']})
        
        # 显示类积木
        elif '清空屏幕' in s or '清屏' in s:
            blocks.append({'type':'display', 'text':'清空屏幕', 'shape':'stack', 'color':COLORS['display']})
        elif '像素点' in s or '像素' in s or '画' in s:
            blocks.append({'type':'display', 'text':'绘制像素点  x:10 y:10', 'shape':'stack', 'color':COLORS['display']})
        elif '显示' in s or '屏幕显示' in s or '显示标签' in s:
            text = s[:20] if len(s) > 20 else s
            blocks.append({'type':'display', 'text':f'显示标签  {text}', 'shape':'stack', 'color':COLORS['display']})
        elif '打印' in s:
            blocks.append({'type':'display', 'text':'打印 makeblock 并换行', 'shape':'stack', 'color':COLORS['display']})
        
        # 灯光类积木
        elif 'RGB灯' in s or '灯亮' in s or '亮起' in s or '灯灭' in s or '熄灭' in s:
            if '灭' in s:
                blocks.append({'type':'light', 'text':'RGB灯 熄灭', 'shape':'stack', 'color':COLORS['light']})
            else:
                color = '绿色'
                if '黄' in s: color = '黄色'
                elif '红' in s: color = '红色'
                elif '蓝' in s: color = '蓝色'
                blocks.append({'type':'light', 'text':f'RGB灯 亮起 {color}', 'shape':'stack', 'color':COLORS['light']})
        elif 'LED' in s or 'led' in s:
            blocks.append({'type':'light', 'text':'RGB灯 亮起 红色', 'shape':'stack', 'color':COLORS['light']})
        
        # 播放/声音类
        elif '播放' in s or '声音' in s or '音乐' in s or '蜂鸣' in s:
            blocks.append({'type':'play', 'text':'播放 嗨 ▼ 直到结束', 'shape':'stack', 'color':COLORS['play']})
        
        # 感知/传感器类
        elif '光线' in s or '环境光' in s or '传感器' in s:
            blocks.append({'type':'sensing', 'text':'环境光强度', 'shape':'stack', 'color':COLORS['sensing']})
        elif '温度' in s:
            blocks.append({'type':'sensing', 'text':'温度', 'shape':'stack', 'color':COLORS['sensing']})
        elif '加速度' in s or '陀螺仪' in s or '姿态' in s:
            blocks.append({'type':'motion', 'text':'加速度 x轴', 'shape':'stack', 'color':COLORS['motion']})
        
        # 运算类
        elif '运算' in s or '计算' in s or '+' in s or '-' in s or '×' in s or '÷' in s:
            blocks.append({'type':'operator', 'text':'1 + 1', 'shape':'stack', 'color':COLORS['operator']})
        
        # AI类
        elif '识别' in s or 'AI' in s or '人工智能' in s or '模型' in s or '训练' in s:
            blocks.append({'type':'ai', 'text':'识别图像 结果', 'shape':'stack', 'color':COLORS['ai']})
        
        # 默认：显示类积木
        else:
            text = s[:20] if len(s) > 20 else s
            blocks.append({'type':'stack', 'text':text, 'shape':'stack', 'color':COLORS['display']})
    
    return blocks

def generate_lesson_screenshots(lesson_data):
    """为单课生成4张截图"""
    lid = lesson_data['id']
    steps = lesson_data['steps']
    
    # 解析所有步骤对应的积木
    all_blocks = parse_steps_to_blocks(steps)
    
    # 确保至少有启动事件
    if not any(b.get('shape') == 'hat' for b in all_blocks):
        all_blocks.insert(0, {'type':'event', 'text':'当童芯派启动时', 'shape':'hat', 'color':COLORS['event']})
    
    # step-02: 前1/3的积木
    n = len(all_blocks)
    cut1 = max(1, n // 3)
    cut2 = max(2, 2 * n // 3)
    
    step02 = all_blocks[:cut1]
    step03 = all_blocks[:cut2]
    step04 = all_blocks[:]
    full = all_blocks[:]
    
    # 生成截图
    lesson_dir = os.path.join(BASE_DIR, f"lesson-{lid:02d}")
    os.makedirs(lesson_dir, exist_ok=True)
    
    for name, config in [('step-02', step02), ('step-03', step03), ('step-04', step04), ('full-program', full)]:
        img = draw_mblock_interface(config, lid, name)
        out_path = os.path.join(lesson_dir, f"{name}.png")
        img.save(out_path)
    
    return True

def main():
    # 读取课程数据
    with open(r"D:\PROJECTS\_AI\AIBook_CyberPi\_lessons_data.json", encoding='utf-8') as f:
        lessons_data = json.load(f)
    
    count = 0
    for ld in lessons_data:
        lid = ld['id']
        if lid < 5:
            continue  # 1-4课已有真实截图
        
        try:
            generate_lesson_screenshots(ld)
            print(f"✓ 第{lid}课 {ld['title']} - 4张截图已生成")
            count += 1
        except Exception as e:
            print(f"✗ 第{lid}课失败: {e}")
    
    print(f"\n完成！共生成 {count} 课 × 4张 = {count*4} 张截图")

if __name__ == '__main__':
    main()
