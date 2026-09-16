# -*- coding: utf-8 -*-
"""
mBlock界面截图精确生成引擎
为每课生成精确匹配积木内容的mBlock界面截图
"""
from PIL import Image, ImageDraw, ImageFont
import json, os, re

# ============ 颜色定义（精确匹配mBlock） ============
COLORS = {
    'event': '#FFAB19',       # 事件 - 黄色
    'control': '#FFAB19',     # 控制 - 橙色
    'display': '#9966FF',     # 显示 - 紫色
    'light': '#CF63CF',       # 灯光 - 紫色(偏红)
    'play': '#CF63CF',        # 播放 - 紫色
    'variable': '#FF8C1A',    # 变量 - 深橙
    'operator': '#59C059',    # 运算 - 绿色
    'sensing': '#FFAB19',     # 感知 - 橙色
    'motion': '#FFAB19',      # 体感 - 橙色
    'ai': '#59C059',          # 人工智能 - 绿色
    'iot': '#0FBD8C',         # 物联网 - 青绿
    'lan': '#0FBD8C',         # 局域网 - 青绿
    'music': '#CF63CF',       # 音乐 - 紫色
    'myblock': '#FF6680',     # 自制积木 - 红色
}

# 分类栏配置
CATEGORIES = [
    ('搜索', '#4C97FC', '🔍'),
    ('播放', '#CF63CF', '▶'),
    ('灯光', '#CF63CF', '💡'),
    ('显示', '#9966FF', '📺'),
    ('体感', '#FFAB19', '📱'),
    ('感知', '#FFAB19', '👁'),
    ('局域网', '#0FBD8C', '🌐'),
    ('人工智能', '#59C059', '🤖'),
    ('物联网', '#0FBD8C', '📡'),
    ('事件', '#FFAB19', '⚡'),
    ('控制', '#FFAB19', '🔄'),
    ('运算', '#59C059', '➕'),
    ('变量', '#FF8C1A', '📦'),
    ('自制积木', '#FF6680', '🧩'),
]

def get_font(size=14):
    """获取中文字体"""
    font_paths = [
        r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\simsun.ttc",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except:
                continue
    return ImageFont.load_default()

def draw_hat_block(draw, x, y, text, color='#FFAB19', width=240):
    """绘制事件帽子积木（顶部弧形）"""
    h = 42
    # 主体
    draw.rounded_rectangle([x, y+8, x+width, y+h], radius=6, fill=color)
    # 顶部弧形
    draw.pieslice([x+10, y, x+50, y+20], 180, 360, fill=color)
    draw.rectangle([x+30, y, x+width-10, y+10], fill=color)
    # 底部凹槽
    draw.rectangle([x+12, y+h-2, x+32, y+h+4], fill='#FFFFFF')
    # 文字
    font = get_font(14)
    draw.text((x+15, y+14), text, fill='#FFFFFF', font=font)
    return h + 4

def draw_stack_block(draw, x, y, text, color='#9966FF', width=240, inputs=None):
    """绘制普通堆叠积木"""
    h = 42
    # 顶部凸口
    draw.rectangle([x+12, y-2, x+32, y+4], fill=color)
    # 主体
    draw.rectangle([x, y, x+width, y+h], fill=color)
    # 底部凹槽
    draw.rectangle([x+12, y+h-2, x+32, y+h+4], fill='#FFFFFF')
    # 文字
    font = get_font(14)
    draw.text((x+12, y+12), text, fill='#FFFFFF', font=font)
    # 输入框（如果有）
    if inputs:
        ix = x + 12 + font.getlength(text) + 10
        for inp in inputs:
            iw = inp.get('width', 40)
            draw.rounded_rectangle([ix, y+8, ix+iw, y+h-8], radius=4, fill='#FFFFFF')
            if inp.get('text'):
                draw.text((ix+5, y+12), inp['text'], fill='#333333', font=get_font(12))
            ix += iw + 8
    return h + 4

def draw_c_block(draw, x, y, text, color='#FFAB19', width=260, inner_blocks=None):
    """绘制C形积木（如果...那么...否则）"""
    h = 100
    # 顶部凸口
    draw.rectangle([x+12, y-2, x+32, y+4], fill=color)
    # 顶部横条
    draw.rectangle([x, y, x+width, y+35], fill=color)
    # 左侧竖条
    draw.rectangle([x, y+35, x+20, y+h-35], fill=color)
    # 中间横条（那么/否则分隔）
    draw.rectangle([x, y+h-35, x+width, y+h], fill=color)
    # 底部凹槽
    draw.rectangle([x+12, y+h-2, x+32, y+h+4], fill='#FFFFFF')
    # 文字
    font = get_font(14)
    draw.text((x+12, y+8), text, fill='#FFFFFF', font=font)
    # 内部积木
    if inner_blocks:
        iy = y + 40
        for ib in inner_blocks:
            draw_stack_block(draw, x+25, iy, ib.get('text',''), ib.get('color','#9966FF'), width-50)
            iy += 46
    return h + 4

def draw_repeat_block(draw, x, y, text, color='#FFAB19', width=260, inner_blocks=None):
    """绘制重复执行C形积木"""
    h = 90
    draw.rectangle([x+12, y-2, x+32, y+4], fill=color)
    draw.rectangle([x, y, x+width, y+35], fill=color)
    draw.rectangle([x, y+35, x+20, y+h], fill=color)
    draw.rectangle([x, y+h-5, x+width, y+h], fill=color)
    draw.rectangle([x+12, y+h-2, x+32, y+h+4], fill='#FFFFFF')
    font = get_font(14)
    draw.text((x+12, y+8), text, fill='#FFFFFF', font=font)
    if inner_blocks:
        iy = y + 40
        for ib in inner_blocks:
            draw_stack_block(draw, x+25, iy, ib.get('text',''), ib.get('color','#CF63CF'), width-50)
            iy += 46
    return h + 4

def draw_mblock_interface(blocks_config, lesson_id=5, step_name='step'):
    """
    绘制完整的mBlock界面
    blocks_config: 积木配置列表，每个元素是 {'type','text','shape','color','inner_blocks','inputs'}
    """
    W, H = 1519, 891
    img = Image.new('RGB', (W, H), '#FFFFFF')
    draw = ImageDraw.Draw(img)
    font = get_font(14)
    font_small = get_font(12)
    font_title = get_font(16)
    
    # ===== 顶部导航栏 =====
    draw.rectangle([0, 0, W, 50], fill='#4C97FC')
    draw.text((15, 15), 'makeblock | mBlock', fill='#FFFFFF', font=font_title)
    # 文件菜单
    draw.text((180, 15), '📁 文件', fill='#FFFFFF', font=font)
    draw.text((260, 15), '无标题', fill='#333333', font=font)
    draw.rectangle([250, 10, 370, 38], fill='#FFFFFF', outline='#DDDDDD')
    draw.text((260, 15), '无标题', fill='#333333', font=font)
    draw.text((400, 15), '💾 保存', fill='#FFFFFF', font=font)
    # 右侧
    draw.text((W-300, 15), '📖 使用文档  📚 示例程序  💬 反馈  ⚙ 设置', fill='#FFFFFF', font=font_small)
    
    # ===== 左侧设备面板 =====
    draw.rectangle([0, 50, 200, H], fill='#F7F8FA')
    # 童芯派图标区域
    draw.rectangle([10, 70, 190, 250], fill='#FFFFFF', outline='#E0E0E0')
    draw.ellipse([60, 90, 140, 170], fill='#FFFFFF', outline='#333333', width=2)
    # 熊猫图标简化
    draw.ellipse([75, 100, 95, 120], fill='#333333')
    draw.ellipse([105, 100, 125, 120], fill='#333333')
    draw.ellipse([80, 125, 120, 160], fill='#FFFFFF', outline='#333333')
    draw.text((70, 180), '童芯派', fill='#333333', font=font)
    # 设备标签
    draw.text((15, 270), '设备', fill='#4C97FC', font=font)
    draw.text((70, 270), '角色', fill='#999999', font=font)
    draw.text((125, 270), '背景', fill='#999999', font=font)
    # 连接方式
    draw.text((15, 320), '🔗 切换至mLink', fill='#666666', font=font_small)
    draw.text((15, 350), '连接方式', fill='#999999', font=font_small)
    draw.rounded_rectangle([15, 370, 90, 400], radius=4, fill='#E8E8E8')
    draw.text((25, 378), '蓝牙直连', fill='#999999', font=font_small)
    draw.rounded_rectangle([95, 370, 170, 400], radius=4, fill='#E8E8E8')
    draw.text((105, 378), '串口直连', fill='#999999', font=font_small)
    # 模式切换
    draw.text((15, 420), '模式切换', fill='#999999', font=font_small)
    draw.rounded_rectangle([15, 440, 90, 470], radius=4, fill='#4C97FC')
    draw.text((35, 448), '上传', fill='#FFFFFF', font=font_small)
    draw.rounded_rectangle([95, 440, 170, 470], radius=4, fill='#FFFFFF', outline='#E0E0E0')
    draw.text((115, 448), '在线', fill='#999999', font=font_small)
    # 底部提示
    draw.text((15, 500), '请连接设备', fill='#999999', font=font_small)
    draw.text((15, 520), '怎么使用设备？', fill='#4C97FC', font=font_small)
    
    # ===== 中间积木分类栏 =====
    draw.rectangle([200, 50, 445, H], fill='#FFFFFF')
    draw.line([445, 50, 445, H], fill='#E0E0E0')
    # 搜索框
    draw.rounded_rectangle([215, 65, 425, 95], radius=4, fill='#F5F5F5')
    draw.text((225, 72), '🔍 搜索', fill='#999999', font=font)
    # 分类列表
    for i, (name, color, icon) in enumerate(CATEGORIES):
        y = 110 + i * 48
        # 图标圆点
        draw.ellipse([220, y+5, 240, y+25], fill=color)
        # 文字
        draw.text((250, y+8), name, fill='#333333', font=font)
    # 添加扩展
    draw.rounded_rectangle([215, H-50, 425, H-20], radius=4, fill='#4C97FC')
    draw.text((280, H-43), '➕ 添加扩展', fill='#FFFFFF', font=font)
    
    # ===== 右侧代码区 =====
    draw.rectangle([445, 50, W, H], fill='#FFFFFF')
    # 网格点背景
    for gx in range(460, W, 22):
        for gy in range(60, H, 22):
            draw.point([gx, gy], fill='#EEEEEE')
    # 积木/Python切换标签
    draw.rounded_rectangle([W-160, 60, W-80, 90], radius=4, fill='#E8F3FF')
    draw.text((W-140, 68), '积木', fill='#4C97FC', font=font)
    draw.rounded_rectangle([W-80, 60, W-20, 90], radius=4, fill='#FFFFFF')
    draw.text((W-65, 68), 'Python', fill='#999999', font=font)
    
    # ===== 绘制积木 =====
    bx = 650
    by = 120
    for block in blocks_config:
        btype = block.get('type', 'stack')
        text = block.get('text', '')
        color = block.get('color', COLORS.get(block.get('category','event'), '#FFAB19'))
        shape = block.get('shape', 'stack')
        inner = block.get('inner_blocks', None)
        inputs = block.get('inputs', None)
        
        if shape == 'hat':
            dh = draw_hat_block(draw, bx, by, text, color, block.get('width', 240))
        elif shape == 'c':
            dh = draw_c_block(draw, bx, by, text, color, block.get('width', 260), inner)
        elif shape == 'repeat':
            dh = draw_repeat_block(draw, bx, by, text, color, block.get('width', 260), inner)
        else:
            dh = draw_stack_block(draw, bx, by, text, color, block.get('width', 240), inputs)
        by += dh + 8
    
    # 底部提示条
    draw.rectangle([0, H-30, W, H], fill='#F0F0F0')
    draw.text((400, H-22), '当前环境可能存在兼容性问题，部分功能可能无法正常使用。点击"环境检测"了解更多', fill='#666666', font=font_small)
    
    return img

print("mBlock截图生成引擎已加载")
print("可用函数: draw_mblock_interface, draw_hat_block, draw_stack_block, draw_c_block, draw_repeat_block")
