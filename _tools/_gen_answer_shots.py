# -*- coding: utf-8 -*-
"""渲染32课任务答案截图 task-answer.png（复用 Coding 版渲染器）"""
import sys, os, json
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT_DIR, "_tools"))
from _batch_gen_coding import build_lesson_blocks, segments_to_config
from _mblock_renderer import draw_mblock_interface

BASE_DIR = os.path.join(ROOT_DIR, "AI编程探险课_CyberPi", "assets", "blocks")

def generate_answer_screenshot(lid, flat_blocks):
    segs = build_lesson_blocks(flat_blocks)
    blocks_cfg = segments_to_config(segs)
    img = draw_mblock_interface(blocks_cfg, lid, 'task-answer')
    lesson_dir = os.path.join(BASE_DIR, f"lesson-{lid:02d}")
    os.makedirs(lesson_dir, exist_ok=True)
    img.save(os.path.join(lesson_dir, "task-answer.png"))

def main():
    answers = json.load(open(os.path.join(ROOT_DIR, "_tools", "lesson_answers.json"), encoding='utf-8'))
    # 补充：第3/19/20课等答案里用了「控制 否则」，检查渲染器对 else 分支支持
    ok = 0
    for k in sorted(answers, key=int):
        lid = int(k)
        try:
            generate_answer_screenshot(lid, answers[k])
            print(f"✓ 第{lid:2d}课 task-answer.png 已生成")
            ok += 1
        except Exception as e:
            print(f"✗ 第{lid}课失败: {e}")
            import traceback; traceback.print_exc()
    print(f"\n完成！{ok} 张答案截图")

if __name__ == '__main__':
    main()
