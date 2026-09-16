# -*- coding: utf-8 -*-
"""
批量生成全部32课mBlock截图（V2 - 精确匹配版）
基于修正后的课程数据，精确解析每步积木内容
"""
import sys, os, json, re
sys.path.insert(0, r"D:\PROJECTS\_AI\AIBook_CyberPi\_tools")
from _mblock_renderer import draw_mblock_interface, COLORS

BASE_DIR = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\assets\blocks"

def extract_var_name(s):
    """从步骤描述中提取变量名"""
    m = re.search(r'「([^」]+)」', s)
    if m: return m.group(1)
    m = re.search(r'变量[「"]?([^」"\s,，]+)', s)
    if m: return m.group(1)
    return '变量'

def parse_step_blocks(step):
    """从单个步骤描述中解析出积木列表（可能多个）"""
    blocks = []
    s = step.strip()
    
    # 跳过上传验证步骤
    if '点击上传' in s or '烧录' in s or '验证运行效果' in s:
        return blocks
    
    # 按分号或逗号分割多个积木操作
    parts = re.split(r'[；;]', s)
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
        
        # 事件类积木（帽子积木）
        if re.search(r'当.*启动时|当.*开机时', part):
            blocks.append({'type':'event', 'text':'当童芯派启动时', 'shape':'hat', 'color':COLORS['event']})
            continue
        if re.search(r'当按钮\s*A.*按下时|当按键\s*A.*按下时', part):
            blocks.append({'type':'event', 'text':'当按键 A ▼ 按下时', 'shape':'hat', 'color':COLORS['event']})
            continue
        if re.search(r'当按钮\s*B.*按下时|当按键\s*B.*按下时', part):
            blocks.append({'type':'event', 'text':'当按键 B ▼ 按下时', 'shape':'hat', 'color':COLORS['event']})
            continue
        if re.search(r'当摇杆.*时', part):
            blocks.append({'type':'event', 'text':'当摇杆 向上拨动 ▼ 时', 'shape':'hat', 'color':COLORS['event']})
            continue
        
        # 自制积木定义
        if '自制积木' in part or re.search(r'^「[^」]+」\s*：', part):
            m = re.search(r'「([^」]+)」', part)
            name = m.group(1) if m else '自制积木'
            blocks.append({'type':'myblock', 'text':f'定义 {name}', 'shape':'hat', 'color':COLORS['myblock']})
            continue
        
        # 调用自制积木
        if re.search(r'调用.*「[^」]+」|放面包|放肉饼|放蔬菜|第一层|第二层|第三层', part) and '自制' not in part:
            m = re.search(r'「([^」]+)」', part)
            name = m.group(1) if m else '积木'
            blocks.append({'type':'myblock', 'text':name, 'shape':'stack', 'color':COLORS['myblock']})
            continue
        
        # 变量类积木
        if '建立变量' in part:
            vars_found = re.findall(r'「([^」]+)」', part)
            for v in vars_found[:2]:
                blocks.append({'type':'variable', 'text':f'建立变量 {v}', 'shape':'stack', 'color':COLORS['variable']})
            continue
        
        if '变量' in part or re.search(r'「[^」]+」.*设为|「[^」]+」.*增加|「[^」]+」.*减少', part):
            var_name = extract_var_name(part)
            if '增加' in part or '+1' in part or '加 1' in part or '加1' in part:
                # 检查增加的值
                m = re.search(r'增加\s*(\d+)', part)
                val = m.group(1) if m else '1'
                blocks.append({'type':'variable', 'text':f'将 {var_name} ▼ 增加 {val}', 'shape':'stack', 'color':COLORS['variable']})
            elif '减少' in part or '-1' in part or '减 1' in part:
                m = re.search(r'减少\s*(\d+)', part)
                val = m.group(1) if m else '1'
                blocks.append({'type':'variable', 'text':f'将 {var_name} ▼ 减少 {val}', 'shape':'stack', 'color':COLORS['variable']})
            elif '设为' in part or '=' in part:
                m = re.search(r'设为\s*([^，,。\s]+)', part)
                val = m.group(1) if m else '0'
                # 处理运算表达式
                if '1 -' in val or '1-' in val:
                    val = '1 - 开关'
                blocks.append({'type':'variable', 'text':f'将 {var_name} ▼ 设为 {val}', 'shape':'stack', 'color':COLORS['variable']})
            elif '清零' in part or '设为0' in part or '设为 0' in part:
                blocks.append({'type':'variable', 'text':f'将 {var_name} ▼ 设为 0', 'shape':'stack', 'color':COLORS['variable']})
            else:
                blocks.append({'type':'variable', 'text':f'将 {var_name} ▼ 设为 0', 'shape':'stack', 'color':COLORS['variable']})
            continue
        
        # 控制类：重复执行
        if re.search(r'重复执行\s*(\d+)?\s*次|重复执行直到', part):
            m = re.search(r'重复执行\s*(\d+)\s*次', part)
            times = m.group(1) if m else ''
            if times:
                text = f'重复执行 {times} 次'
            else:
                text = '重复执行'
            # 解析内部积木
            inner = []
            if '显示' in part:
                inner.append({'text':'显示标签  剩余时间', 'color':COLORS['display']})
            if '等待' in part:
                inner.append({'text':'等待 1 秒', 'color':COLORS['control']})
            if '减少' in part or '减1' in part:
                inner.append({'text':'将 剩余时间 ▼ 减少 1', 'color':COLORS['variable']})
            if '灯' in part and '亮' in part:
                inner.append({'text':'RGB灯 亮起 红色', 'color':COLORS['light']})
            if not inner:
                inner.append({'text':'（循环内容）', 'color':COLORS['control']})
            blocks.append({'type':'control', 'text':text, 'shape':'repeat', 'color':COLORS['control'], 'inner_blocks':inner})
            continue
        
        # 控制类：如果...那么...否则
        if re.search(r'如果.*那么.*否则|如果\s*…', part):
            # 解析条件
            cond = ''
            if '环境光' in part and '<' in part:
                cond = '环境光强度 < 30'
            elif '环境光' in part and '>' in part:
                cond = '环境光强度 > 30'
            elif '声音' in part and '>' in part:
                cond = '声音强度 > 60'
            elif '加速度' in part and '<' in part:
                cond = '加速度 x轴 < -1'
            elif '加速度' in part and '>' in part:
                cond = '加速度 x轴 > 1'
            elif '开关' in part and '=' in part:
                cond = '开关 = 1'
            elif '且' in part:
                cond = '光线 > 50 且 声音 > 60'
            elif '线索计数' in part:
                cond = '线索计数 = 1'
            elif '输入序列' in part:
                cond = '输入序列 = 112'
            elif '随机数' in part and '≤' in part:
                cond = '随机数 ≤ 50'
            else:
                cond = '条件'
            
            # 解析那么分支
            then_inner = []
            if '红灯' in part or '红色' in part:
                then_inner.append({'text':'RGB灯 亮起 红色', 'color':COLORS['light']})
            if '绿灯' in part or '绿色' in part:
                then_inner.append({'text':'RGB灯 亮起 绿色', 'color':COLORS['light']})
            if '黄灯' in part or '黄色' in part:
                then_inner.append({'text':'RGB灯 亮起 黄色', 'color':COLORS['light']})
            if '蓝灯' in part or '蓝色' in part:
                then_inner.append({'text':'RGB灯 亮起 蓝色', 'color':COLORS['light']})
            if '白灯' in part or '白色' in part:
                then_inner.append({'text':'RGB灯 亮起 白色', 'color':COLORS['light']})
            if '显示' in part and '开灯' in part:
                then_inner.append({'text':'显示标签  开灯啦！', 'color':COLORS['display']})
            elif '显示' in part and '白天' in part:
                then_inner.append({'text':'显示标签  白天好', 'color':COLORS['display']})
            elif '显示' in part and '大声' in part:
                then_inner.append({'text':'显示标签  大声！', 'color':COLORS['display']})
            elif '显示' in part and '晴天' in part:
                then_inner.append({'text':'显示标签  预测：晴天！', 'color':COLORS['display']})
            elif '显示' in part and '下雨' in part:
                then_inner.append({'text':'显示标签  要下雨带伞', 'color':COLORS['display']})
            elif '显示' in part and '激活' in part:
                then_inner.append({'text':'显示标签  神经元激活！', 'color':COLORS['display']})
            elif '显示' in part and '收到' in part:
                then_inner.append({'text':'显示标签  收到1条线索', 'color':COLORS['display']})
            elif '显示' in part:
                then_inner.append({'text':'显示标签  条件成立', 'color':COLORS['display']})
            if '增加' in part and '大声组' in part:
                then_inner.append({'text':'将 大声组 ▼ 增加 1', 'color':COLORS['variable']})
            if '增加' in part and '正确' in part:
                then_inner.append({'text':'将 正确数 ▼ 增加 1', 'color':COLORS['variable']})
            if '播放' in part:
                then_inner.append({'text':'播放 嗨 ▼ 直到结束', 'color':COLORS['play']})
            if not then_inner:
                then_inner.append({'text':'（那么分支）', 'color':COLORS['control']})
            
            blocks.append({'type':'control', 'text':f'如果 {cond} 那么 ... 否则', 'shape':'c', 'color':COLORS['control'],
                          'inner_blocks':then_inner})
            continue
        
        # 控制类：等待
        if '等待' in part:
            m = re.search(r'等待\s*([\d.]+)\s*秒', part)
            sec = m.group(1) if m else '0.5'
            blocks.append({'type':'control', 'text':f'等待 {sec} 秒', 'shape':'stack', 'color':COLORS['control']})
            continue
        
        # 显示类：清空屏幕
        if '清空屏幕' in part or '清屏' in part:
            blocks.append({'type':'display', 'text':'清空屏幕', 'shape':'stack', 'color':COLORS['display']})
            # 检查是否还有其他操作
            if '绘制像素点' in part or '画爱心' in part or '画' in part:
                pass  # 会在下面处理
            else:
                continue
        
        # 显示类：绘制像素点
        if '绘制像素点' in part or '像素点' in part:
            # 提取所有坐标
            coords = re.findall(r'x\s*[=:]\s*(\d+)\s*[,，]?\s*y\s*[=:]\s*(\d+)', part)
            if coords:
                for x, y in coords[:4]:  # 最多显示4个
                    blocks.append({'type':'display', 'text':f'绘制像素点  x:{x} y:{y}', 'shape':'stack', 'color':COLORS['display']})
            else:
                blocks.append({'type':'display', 'text':'绘制像素点  x:2 y:2', 'shape':'stack', 'color':COLORS['display']})
            continue
        
        # 显示类：显示标签/显示文字
        if '显示标签' in part or '显示' in part or '屏幕显示' in part:
            # 提取显示内容
            text = ''
            m = re.search(r'显示[标签文字]*[「"]?([^」"]+)[」"]?', part)
            if m:
                text = m.group(1)
            elif '显示' in part:
                idx = part.find('显示')
                text = part[idx+2:idx+20].strip('：:「」""，,。')
            
            if not text:
                text = '显示内容'
            
            # 处理变量拼接
            if '+' in part and ('变量' in part or '光线' in part or '声音' in part or '综合分' in part):
                text = text[:15] + '...'
            
            if len(text) > 18:
                text = text[:18] + '..'
            
            blocks.append({'type':'display', 'text':f'显示标签  {text}', 'shape':'stack', 'color':COLORS['display']})
            continue
        
        # 灯光类
        if 'RGB灯' in part or '灯亮' in part or '亮起' in part or '灯灭' in part or '熄灭' in part:
            if '灭' in part or '熄灭' in part:
                blocks.append({'type':'light', 'text':'RGB灯 熄灭', 'shape':'stack', 'color':COLORS['light']})
            else:
                color = '绿色'
                if '黄' in part: color = '黄色'
                elif '红' in part: color = '红色'
                elif '蓝' in part: color = '蓝色'
                elif '白' in part: color = '白色'
                elif '紫' in part: color = '紫色'
                # 处理RGB值
                if 'R' in part and 'G' in part and 'B' in part:
                    blocks.append({'type':'light', 'text':'RGB灯 亮起 R红 G绿 B蓝', 'shape':'stack', 'color':COLORS['light']})
                else:
                    blocks.append({'type':'light', 'text':f'RGB灯 亮起 {color}', 'shape':'stack', 'color':COLORS['light']})
            continue
        
        # 播放/声音类
        if '播放' in part or '声音' in part or '音乐' in part or '蜂鸣' in part or '喇叭' in part:
            if '完成' in part or '刷完' in part:
                blocks.append({'type':'play', 'text':'播放 完成 ▼ 直到结束', 'shape':'stack', 'color':COLORS['play']})
            else:
                blocks.append({'type':'play', 'text':'播放 嗨 ▼ 直到结束', 'shape':'stack', 'color':COLORS['play']})
            continue
        
        # 感知/传感器类（作为值积木，通常嵌入其他积木中）
        if '环境光强度' in part or '光线强度' in part:
            blocks.append({'type':'sensing', 'text':'环境光强度', 'shape':'stack', 'color':COLORS['sensing']})
            continue
        if '声音强度' in part:
            blocks.append({'type':'sensing', 'text':'声音强度', 'shape':'stack', 'color':COLORS['sensing']})
            continue
        if '加速度' in part:
            axis = 'x轴'
            if 'Y' in part or 'y' in part: axis = 'y轴'
            blocks.append({'type':'motion', 'text':f'加速度 {axis}', 'shape':'stack', 'color':COLORS['motion']})
            continue
        if '温度' in part:
            blocks.append({'type':'sensing', 'text':'温度', 'shape':'stack', 'color':COLORS['sensing']})
            continue
        if '摇杆' in part and ('位置' in part or 'x' in part or 'y' in part):
            blocks.append({'type':'sensing', 'text':'摇杆 y位置', 'shape':'stack', 'color':COLORS['sensing']})
            continue
        
        # 运算类
        if re.search(r'[+\-×÷=]', part) and ('计算' in part or '综合分' in part or '平均' in part or '总和' in part):
            if '÷' in part or '平均' in part:
                blocks.append({'type':'operator', 'text':'总和 ÷ 3', 'shape':'stack', 'color':COLORS['operator']})
            elif '×' in part or '权重' in part:
                blocks.append({'type':'operator', 'text':'光线 × 权重1 + 声音 × 权重2', 'shape':'stack', 'color':COLORS['operator']})
            else:
                blocks.append({'type':'operator', 'text':'1 + 1', 'shape':'stack', 'color':COLORS['operator']})
            continue
        
        # 随机数
        if '随机数' in part or '随机' in part:
            m = re.search(r'随机数\s*(\d+)\s*[-~到]\s*(\d+)', part)
            if m:
                blocks.append({'type':'operator', 'text':f'随机数 {m.group(1)} 到 {m.group(2)}', 'shape':'stack', 'color':COLORS['operator']})
            else:
                blocks.append({'type':'operator', 'text':'随机数 1 到 10', 'shape':'stack', 'color':COLORS['operator']})
            continue
        
        # 读取传感器（作为独立积木）
        if '读取' in part:
            if '光线' in part or '环境光' in part:
                blocks.append({'type':'sensing', 'text':'环境光强度', 'shape':'stack', 'color':COLORS['sensing']})
            elif '声音' in part:
                blocks.append({'type':'sensing', 'text':'声音强度', 'shape':'stack', 'color':COLORS['sensing']})
            elif '加速度' in part:
                blocks.append({'type':'motion', 'text':'加速度 x轴', 'shape':'stack', 'color':COLORS['motion']})
            continue
        
        # 概念步骤（在线训练、讨论等）- 用显示积木代替
        if '在线' in part or '训练' in part or '概念' in part or '讨论' in part or '准备' in part or '阅读' in part or '对比' in part or '总结' in part:
            text = part[:18] + '..' if len(part) > 18 else part
            blocks.append({'type':'display', 'text':f'显示标签  {text}', 'shape':'stack', 'color':COLORS['display']})
            continue
        
        # 默认：显示类积木
        text = part[:18] + '..' if len(part) > 18 else part
        blocks.append({'type':'stack', 'text':text, 'shape':'stack', 'color':COLORS['display']})
    
    return blocks

def generate_lesson_screenshots(lid, steps):
    """为单课生成4张截图"""
    # 解析所有步骤对应的积木
    all_blocks = []
    for step in steps:
        step_blocks = parse_step_blocks(step)
        all_blocks.extend(step_blocks)
    
    # 确保至少有启动事件
    if not any(b.get('shape') == 'hat' for b in all_blocks):
        all_blocks.insert(0, {'type':'event', 'text':'当童芯派启动时', 'shape':'hat', 'color':COLORS['event']})
    
    # 限制积木数量，避免截图过长
    if len(all_blocks) > 12:
        all_blocks = all_blocks[:12]
    
    # step-02: 前1/3的积木
    n = len(all_blocks)
    cut1 = max(2, n // 3)
    cut2 = max(3, 2 * n // 3)
    
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
    
    return len(all_blocks)

def main():
    # 读取修正后的课程数据
    with open(r"D:\PROJECTS\_AI\AIBook_CyberPi\_tools\_lessons_data_fixed.json", encoding='utf-8') as f:
        lessons_fixed = json.load(f)
    
    count = 0
    total_blocks = 0
    for lid_str in sorted(lessons_fixed.keys(), key=int):
        lid = int(lid_str)
        data = lessons_fixed[lid_str]
        steps = data['steps']
        
        try:
            n_blocks = generate_lesson_screenshots(lid, steps)
            print(f"✓ 第{lid:2d}课 - {n_blocks:2d}个积木 - 4张截图已生成")
            count += 1
            total_blocks += n_blocks
        except Exception as e:
            print(f"✗ 第{lid}课失败: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n完成！共生成 {count} 课 × 4张 = {count*4} 张截图")
    print(f"平均每课 {total_blocks/count:.1f} 个积木")

if __name__ == '__main__':
    main()
