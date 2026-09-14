# -*- coding: utf-8 -*-
import io, sys

path = r"D:\PROJECTS\_AI\AIBook_CyberPi\AI编程探险课_CyberPi\index.html"
with io.open(path, 'r', encoding='utf-8') as f:
    src = f.read()

# === 1. 在 switchTab 后添加 goNextTab 和 nextStageBtn 函数 ===
old1 = """  document.getElementById('panel-'+key).classList.add('active');
}

/* ---- 面板：课程导入 ---- */"""

new1 = """  document.getElementById('panel-'+key).classList.add('active');
  window.scrollTo({top:document.getElementById('view-course').offsetTop - 70, behavior:'smooth'});
}
function goNextTab(){
  var tabs = document.querySelectorAll('#courseTabs .tab-btn');
  var activeIdx = 0;
  tabs.forEach(function(b, i){ if(b.classList.contains('active')) activeIdx = i; });
  if(activeIdx < tabs.length - 1){ switchTab(tabs[activeIdx + 1]); }
}
function nextStageBtn(label){
  return '<div style="margin-top:24px;display:flex;justify-content:flex-end"><button class="btn" onclick="goNextTab()" style="display:inline-flex;align-items:center;gap:8px;padding:12px 26px;font-size:15px;font-weight:700;border-radius:14px;background:var(--primary);color:#fff;box-shadow:0 6px 18px -6px hsl(214 77% 46% / .5)">'+label+' <span style="font-size:18px">→</span></button></div>';
}

/* ---- 面板：课程导入 ---- */"""

if old1 in src:
    src = src.replace(old1, new1, 1)
    print("OK: added goNextTab + nextStageBtn")
else:
    print("FAIL: old1 not found")
    # debug: find nearby
    idx = src.find("面板：课程导入")
    print("context around 课程导入:", repr(src[idx-80:idx+20]))

# === 2. panelIntro 末尾加"下一环节：学知识"按钮 ===
old2 = """    }).join('') + '</div></div>';
}

/* ---- 面板：AI 知识点 ---- */"""
new2 = """    }).join('') + '</div>' + nextStageBtn('下一环节：学知识') + '</div>';
}

/* ---- 面板：AI 知识点 ---- */"""
if old2 in src:
    src = src.replace(old2, new2, 1)
    print("OK: panelIntro next button")
else:
    print("FAIL: old2 not found")

# === 3. panelKnow 末尾加"下一环节：看积木"按钮 ===
old3 = """    }).join('') + '</div></div>';
}

/* ---- 面板：编程积木 ---- */"""
new3 = """    }).join('') + '</div>' + nextStageBtn('下一环节：看积木') + '</div>';
}

/* ---- 面板：编程积木 ---- */"""
if old3 in src:
    src = src.replace(old3, new3, 1)
    print("OK: panelKnow next button")
else:
    print("FAIL: old3 not found")

# === 4. panelBlocks 末尾加"下一环节：看演示"按钮 ===
old4 = """'<div class="tip-box">在 mBlock 5 中选择「CyberPi」设备，从对应分类里拖出这些积木，像拼乐高一样把它们接起来。</div></div>';
}

/* ---- 面板：CyberPi 演示 ---- */"""
new4 = """'<div class="tip-box">在 mBlock 5 中选择「CyberPi」设备，从对应分类里拖出这些积木，像拼乐高一样把它们接起来。</div>' + nextStageBtn('下一环节：看演示') + '</div>';
}

/* ---- 面板：CyberPi 演示 ---- */"""
if old4 in src:
    src = src.replace(old4, new4, 1)
    print("OK: panelBlocks next button")
else:
    print("FAIL: old4 not found")

# === 5. panelDemo 末尾加"下一环节：做挑战"按钮 ===
old5 = """'<div class="hw-chips">'+ l.hardware.map(function(h){ return '<span class="hw-chip">'+esc(h)+'</span>'; }).join('') + '</div></div>';
}

/* ---- 面板：动手挑战 ---- */"""
new5 = """'<div class="hw-chips">'+ l.hardware.map(function(h){ return '<span class="hw-chip">'+esc(h)+'</span>'; }).join('') + '</div>' + nextStageBtn('下一环节：做挑战') + '</div>';
}

/* ---- 面板：动手挑战 ---- */"""
if old5 in src:
    src = src.replace(old5, new5, 1)
    print("OK: panelDemo next button")
else:
    print("FAIL: old5 not found")

# === 6. panelChallenge 末尾加"下一环节：答问题"按钮 ===
old6 = """(l.tip ? '<div class="tip-box"><b>老师小贴士：</b>'+esc(l.tip)+'</div>' : '') + '</div>';
}

/* ---- 面板：知识问答 ---- */"""
new6 = """(l.tip ? '<div class="tip-box"><b>老师小贴士：</b>'+esc(l.tip)+'</div>' : '') + nextStageBtn('下一环节：答问题') + '</div>';
}

/* ---- 面板：知识问答 ---- */"""
if old6 in src:
    src = src.replace(old6, new6, 1)
    print("OK: panelChallenge next button")
else:
    print("FAIL: old6 not found")

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(src)
print("DONE: file saved")
