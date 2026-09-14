# -*- coding: utf-8 -*-
import io

path = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html"
with io.open(path, 'r', encoding='utf-8') as f:
    src = f.read()

# 替换 finishQuiz 中的星星部分
# 原来：单个大★ emoji
# 新的：根据 quizState.firstTry 显示对应数量的金色SVG星星（最多3颗）

old_star = """  document.getElementById('quizCard').innerHTML =
    '<div class="quiz-done">' +
    '<div class="big-emoji" style="font-size:52px;line-height:1">★</div>' +
    '<h3>本课完成！</h3><p>'+msg+'</p>' +"""

new_star = """  var starCount = Math.min(quizState.firstTry, 3);
  var starSvg = '<svg viewBox="0 0 24 24" width="44" height="44"><defs><linearGradient id="goldGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD93D"/><stop offset="1" stop-color="#F5A623"/></linearGradient></defs><path fill="url(#goldGrad)" stroke="#E8940A" stroke-width="0.8" d="M12 2l2.9 6.26 6.86.72-5.1 4.64 1.42 6.72L12 17.27 5.92 20.34l1.42-6.72-5.1-4.64 6.86-.72z"/></svg>';
  var starEmpty = '<svg viewBox="0 0 24 24" width="44" height="44"><path fill="#E8ECF2" stroke="#D0D7E2" stroke-width="0.8" d="M12 2l2.9 6.26 6.86.72-5.1 4.64 1.42 6.72L12 17.27 5.92 20.34l1.42-6.72-5.1-4.64 6.86-.72z"/></svg>';
  var starsHtml = '<div style="display:flex;gap:10px;justify-content:center;margin-bottom:8px">';
  for(var si=0; si<3; si++){ starsHtml += (si < starCount ? starSvg : starEmpty); }
  starsHtml += '</div>';
  var starLabel = '<div style="font-size:14px;color:var(--ink-2);font-weight:700;margin-bottom:12px">答对 '+quizState.firstTry+' 题，获得 '+starCount+' 颗星星</div>';
  document.getElementById('quizCard').innerHTML =
    '<div class="quiz-done">' +
    starsHtml + starLabel +
    '<h3>本课完成！</h3><p>'+msg+'</p>' +"""

if old_star in src:
    src = src.replace(old_star, new_star, 1)
    print("OK: replaced quiz result stars")
else:
    print("FAIL: old_star not found")
    # debug
    idx = src.find("big-emoji")
    if idx >= 0:
        print("context:", repr(src[idx-60:idx+120]))

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(src)
print("DONE")
