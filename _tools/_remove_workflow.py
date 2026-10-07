# -*- coding: utf-8 -*-
"""删除平台统一实施流程模块（函数定义+调用）"""
import io

p = r'D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html'
s = io.open(p, encoding='utf-8').read()

# 1. 删除函数定义（从 function platformWorkflow(l){ 到对应 } 与下一函数之间）
start = s.find('function platformWorkflow(l){')
end = s.find('function sampleTestLab(l){')
assert start != -1 and end != -1 and start < end, (start, end)
s2 = s[:start] + s[end:]
print('函数定义已删除')

# 2. 删除调用
old_call = 'platformWorkflow(l) + sampleTaskLab(l) +'
new_call = 'sampleTaskLab(l) +'
cnt = s2.count(old_call)
assert cnt == 1, cnt
s2 = s2.replace(old_call, new_call)
print('调用已删除')

io.open(p, 'w', encoding='utf-8', newline='').write(s2)

# 验证
import re
left = len(re.findall(r'platformWorkflow', s2))
print('剩余 platformWorkflow 引用:', left)
left2 = len(re.findall(r'MBLOCK → CYBERPI|本课统一实施流程|workflow-head|workflow-grid', s2))
print('剩余流程模块文本/CSS:', left2)
