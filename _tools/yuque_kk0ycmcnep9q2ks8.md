

:::color5
此页面持续更新中，敬请关注！

:::

# 课程1-彩虹灯
## Part 1 学习目标
编写程序并上传，让童芯派开机启动后亮起彩虹灯效。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672885876044-c4f0ad68-1423-46e4-8016-ace6ea04f350.gif)

## Part 2 课前准备
+ <font style="color:#3370ff;"></font>童芯派*1
+ USB数据线（Type-C）*1
+ <font style="color:#3370ff;"></font>一台可以上网的电脑
1. 使用数据线连接童芯派和电脑。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672885955910-3ab4f91c-9e93-4107-94d3-5b0ac31ffba9.gif)

2. 打开慧编程python工具（桌面端、网页端）,在左上方设备区点击“连接”，（**在线模式：可以通过点击运行观察实时的运行效果，但需要保持数据线跟电脑连接；上传模式：可以通过将程序上传到童芯派，此时可以拔掉数据线运行程序。**），本课程需要切换成“上传模式”。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672886060620-3d7bcf13-1e0a-4f9a-8dcd-2d854f43af65.gif)

## Part 3 开始编程
1. <font style="color:#3370ff;"></font>新建一个py文件。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672885224232-38419788-7a1e-4d84-b9c6-f3bdbabee5e4.gif)



2. 查看童芯派的Python API，找到对应功能的python语句。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672885225486-006543c0-146d-4862-8325-05b6a480cbb7.gif)

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672885226432-f4abc96f-27e0-4df1-af0e-9b0c5f4819d4.gif)

3. <font style="color:#3370ff;"></font>编写程序，当童芯派启动后，一直亮起彩虹的灯效，中间间隔一秒。

```python
Pythonimport event, time, cyberpi
@event.start
def on_start():    
    while True:        
        cyberpi.led.play('rainbow')        
        time.sleep(1)
```

4. 将程序上传到童芯派设备里。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672885226903-8e61c651-15cc-4d69-a2b2-e58a5cce0953.gif)

## Part 4 练习
1. <font style="color:#3370ff;"></font>修改LED动画，呈现不同的灯效。
2. <font style="color:#3370ff;"></font>在等待时间后增加熄灭全部LED灯的语句，让灯效变化更明显。

# 课程2-小星星
## Part 1 学习目标
编写程序并上传，让童芯派播放《小星星》的旋律。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672886395242-704b02ff-7fee-4eed-96f6-59759807a9e9.gif)

## Part 2 课前准备
+ <font style="color:#3370ff;"> </font>童芯派*1
+ USB数据线（Type-C）*1
+ <font style="color:#3370ff;"></font>一台可以上网的电脑
1. 使用数据线连接童芯派和电脑。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672886426332-e42c5c68-8863-43e2-9b14-165e93f21519.gif)

2. 打开慧编程python工具（桌面端、网页端）,在左上方设备区点击“连接”，（**在线模式：可以通过点击运行观察实时的运行效果，但需要保持数据线跟电脑连接；上传模式：可以通过将程序上传到童芯派，此时可以拔掉数据线运行程序。**），本课程需要切换成“上传模式”。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672886472733-93faa279-d5d0-49fa-ab6d-240d63847511.gif)

## Part 3 开始编程
编写程序，当按下童芯派上的B键后，童芯派播放《小星星》的旋律。

```python
import event, time, cyberpi

@event.start
def on_start():
    """介绍使用方法"""
    cyberpi.console.println('按 B 播放乐曲')

@event.is_press('b')
def is_btn_press():
    # 查看音符序号使用了 MIDI 标准，此示例涉及的几个音符的对应关系如下：
    #
    # 简谱/音符/MIDI序号
    # 1 C4 60
    # 2 D4 62
    # 3 E4 64
    # 4 F4 65
    # 5 G4 67
    # 6 A4 69
    # 7 B4 71
    cyberpi.audio.play_music(60, 0.25)
    cyberpi.audio.play_music(60, 0.25)
    cyberpi.audio.play_music(67, 0.25)
    cyberpi.audio.play_music(67, 0.25)
    cyberpi.audio.play_music(69, 0.25)
    cyberpi.audio.play_music(69, 0.25)
    cyberpi.audio.play_music(67, 0.25)
    time.sleep(1)
    cyberpi.audio.play_music(65, 0.25)
    cyberpi.audio.play_music(65, 0.25)
    cyberpi.audio.play_music(64, 0.25)
    cyberpi.audio.play_music(64, 0.25)
    cyberpi.audio.play_music(62, 0.25)
    cyberpi.audio.play_music(62, 0.25)
    cyberpi.audio.play_music(60, 0.25)
```

## Part 4 练习
1. 请找到《两只老虎》的简谱，编写python程序并上传，让童芯派播放《两只老虎》的旋律。
2. 添加LED动画，实现边播放音乐边亮灯的效果。

# 课程3-神奇录音机
## Part 1 学习目标
编写程序并上传，让童芯派实现录音和播放录音的功能。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672887066021-fc710878-0701-46ea-b21c-e6a111a02a3b.gif)

## Part 2 课前准备
+ <font style="color:#3370ff;"> </font>童芯派*1
+ <font style="color:#3370ff;"> </font>USB数据线（Type-C）*1
+ <font style="color:#3370ff;"></font>一台可以上网的电脑
1. 使用数据线连接童芯派和电脑。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672886426332-e42c5c68-8863-43e2-9b14-165e93f21519.gif)

2. 打开慧编程python工具（桌面端、网页端）,在左上方设备区点击“连接”，（**在线模式：可以通过点击运行观察实时的运行效果，但需要保持数据线跟电脑连接；上传模式：可以通过将程序上传到童芯派，此时可以拔掉数据线运行程序。**），本课程需要切换成“上传模式”。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672886472733-93faa279-d5d0-49fa-ab6d-240d63847511.gif)

## Part 3 开始编程
编写程序，当按下童芯派上的A键后，童芯派开始录音；按下B键后，结束录音；按下摇杆中间时，播放录音。

```python
  import event, time, cyberpi

@event.is_press('a')
def is_btn_press():
    #开始录音
    cyberpi.led.show('red orange yellow green cyan')
    cyberpi.audio.record()

@event.is_press('b')
def is_btn_press1():
    #结束录音
    cyberpi.audio.stop_record()
    cyberpi.led.off("all")

@event.is_press('middle')
def is_joy_press():
    #播放录音
    cyberpi.audio.play_record()
    cyberpi.led.play('rainbow')
```

## Part 4 练习
1. 实现向左拨动摇杆时减小播放的音量，向右拨动摇杆时增加播放音量的效果。
2. 实现向上拨动摇杆时加快播放速度，向下拨动摇杆时降低播放速度的效果。

# 课程4-简易计时器
## Part 1 学习目标
编写程序并上传，让童芯派具备计时的功能。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672887335188-fda8f2b4-a14f-4fdd-82cd-2db058e46a46.gif)

## Part 2 课前准备
+ 童芯派*1
+ USB数据线（Type-C）*1
+ 一台可以上网的电脑
1. 使用数据线连接童芯派和电脑。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672886426332-e42c5c68-8863-43e2-9b14-165e93f21519.gif)

2. 打开慧编程python工具（桌面端、网页端）,在左上方设备区点击“连接”，（**在线模式：可以通过点击运行观察实时的运行效果，但需要保持数据线跟电脑连接；上传模式：可以通过将程序上传到童芯派，此时可以拔掉数据线运行程序。**），本课程需要切换成“上传模式”。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672887273213-998b3577-bde0-4a72-aba4-978fcdf67a0a.gif)



## Part 3 开始编程
编写程序，当按下童芯派上的B键后，重置计时器并在屏幕上开始计时；当按下A键后，结束计时。

```python
import event, time, cyberpi
# 初始化计时器
time2 = 0

@event.start
def on_start():
    global time2
    cyberpi.console.clear()
    cyberpi.console.println('按B开始计时')
    cyberpi.console.println('按A结束计时')

@event.is_press('b')
def is_btn_press():
    global time2
    cyberpi.timer.reset()
    while not cyberpi.controller.is_press('a'):
        cyberpi.display.show_label(str(cyberpi.timer.get()) + str('s'), 24, "center")
```

## Part 4 练习
1. 修改程序，实现计时到10秒时自动停止并发出警报声的功能。

# 课程5-计步器
## Part 1 学习目标
编写程序并上传，让童芯派能够检测运动并将运动步数显示在屏幕上。（下图为模拟效果）

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672887576956-212bffee-a669-438d-96b7-822c7f93be44.gif)

## Part 2 课前准备
+ 童芯派*1
+ USB数据线（Type-C）*1
+ 一台可以上网的电脑
1. 使用数据线连接童芯派和电脑。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672886426332-e42c5c68-8863-43e2-9b14-165e93f21519.gif)

2. 打开慧编程python工具（桌面端、网页端）,在左上方设备区点击“连接”，（**在线模式：可以通过点击运行观察实时的运行效果，但需要保持数据线跟电脑连接；上传模式：可以通过将程序上传到童芯派，此时可以拔掉数据线运行程序。**），本课程需要切换成“上传模式”。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672887472471-55be38be-1602-4672-b3c5-512dc63213b1.gif)

## Part 3 开始编程
编写程序，当童芯派启动后，开始检测运动并将步数实时显示在屏幕上，当按下A键后清空计步。

```python
import event, time, cyberpi
# 初始化步数的变量
step = 0

@event.start
def on_start():
    global step
    """该项目需要将童芯派绑在大腿上（摇杆一头指向地面）"""
    cyberpi.console.clear()
    cyberpi.display.rotate_to(0)
    step = 0
    while True:
        # 该线程用于刷新计步器的步数显示
        # 因为童芯派只检测一边大腿的运动情况，因此实际的步数还需要乘 2
        cyberpi.display.show_label(str('step:') + str(step * 2), 24, "center")

@event.start
def on_start1():
    global step
    while True:
        # 这里通过实际测试确定了一个经验边界，用来判断大腿的状态来实现计数。
        #
        # 对于不同的人，可能会存在差异
        if 30 < -cyberpi.get_roll() and -cyberpi.get_roll() < 70:
            step = step + 1
            time.sleep(0.2)

@event.is_press('a')
def is_btn_press():
    global step
    """按下A键可以清空计步重新开始"""
    step = 0
```

## Part 4 练习
1. 每走一百步的时候让童芯派发出提示声。

# 课程6-体感数据表格
## Part 1 学习目标
编写程序并上传，让童芯派能够在屏幕上以表格的形式实时显示各种体感数据。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672887747415-f5314366-cb95-407c-9292-a9e08933b2f7.gif)

## Part 2 课前准备
+ 童芯派*1
+ USB数据线（Type-C）*1
+ 一台可以上网的电脑
1. 使用数据线连接童芯派和电脑。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672886426332-e42c5c68-8863-43e2-9b14-165e93f21519.gif)

2. 打开慧编程python工具（桌面端、网页端）,在左上方设备区点击“连接”，（**在线模式：可以通过点击运行观察实时的运行效果，但需要保持数据线跟电脑连接；上传模式：可以通过将程序上传到童芯派，此时可以拔掉数据线运行程序。**），本课程需要切换成“上传模式”。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672887674765-efacafe3-6539-41d6-b22e-f48cbd442d7e.gif)

## Part3 开始编程
编写程序，当童芯派启动后，在屏幕上以表格形式显示俯仰角、翻滚角和摇晃强度的数据，并实时更新检测到的数据。

```python
import event, time, cyberpi

@event.start
def on_start():
    cyberpi.display.show_label('体感数据', 16, "top_mid")
    cyberpi.table.add(1, 1, '俯仰角')
    cyberpi.table.add(2, 1, '翻滚角')
    cyberpi.table.add(3, 1, '摇晃度')
    while True:
        cyberpi.table.add(1, 2, cyberpi.get_pitch())
        cyberpi.table.add(2, 2, cyberpi.get_roll())
        cyberpi.table.add(3, 2, cyberpi.get_shakeval())
```

## Part 4 练习
1. 在童芯派屏幕上以表格形式实时显示绕x、y、z轴转动的角度。

# 课程7-光影变幻（在线）
## Part 1 学习目标
编写程序，让童芯派的灯带灯效一边流动一边发生亮度变化。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672888031080-bf9d5a7c-ee9d-4fe6-8cb6-ff3d7e42e133.gif)

## Part 2 课前准备
+ 童芯派*1
+ USB数据线（Type-C）*1
+ 一台可以上网的电脑
1. 使用数据线连接童芯派和电脑。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672886426332-e42c5c68-8863-43e2-9b14-165e93f21519.gif)

2. 打开慧编程python工具（桌面端、网页端）,在左上方设备区点击“连接”，（**在线模式：可以通过点击运行观察实时的运行效果，但需要保持数据线跟电脑连接；上传模式：可以通过将程序上传到童芯派，此时可以拔掉数据线运行程序。**），本课程需要切换成“在线模式”。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672887985644-86b388a7-de25-4fe4-981f-45b10596f3c0.gif)

## Part 3 开始编程
+ 在线模式时，程序中可以使用Python3的库，此程序就用到了math库
+ 编写程序，使用math库的三角函数功能使童芯派灯带的亮度周期性变化。

```python
import math 
import random
import cyberpi
from time import sleep

cyberpi.led.show("r g b y c")
# 给童芯派上灯带一个初始灯效
count = 0
while True:
    cyberpi.led.set_bri(math.sin(count / 4) * 50 + 52) 
    # 利用 math 库的三角函数功能使得灯带的亮度周期性变化。
    cyberpi.led.move(1) 
    # 使用童芯派的灯带滚动功能实现跑马灯效果。
    count += 1
    sleep(0.1)
```

## Part 4 练习
1. 修改三角函数里的数值，观察下灯效发生了什么变化。

# 课程8-语音识别（在线）
## Part 1 学习目标
编写程序，让童芯派能识别输入的语音并将识别结果显示在屏幕上。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672888257920-6cf155d8-6d7b-4967-8952-60ec0b14a2bf.gif)

## Part 2 课前准备
+ 童芯派*1
+ USB数据线（Type-C）*1
+ 一台可以上网的电脑
1. 使用数据线连接童芯派和电脑。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672886426332-e42c5c68-8863-43e2-9b14-165e93f21519.gif)

2.  打开慧编程python工具（桌面端、网页端）,在左上方设备区点击“连接”，（**在线模式：可以通过点击运行观察实时的运行效果，但需要保持数据线跟电脑连接；上传模式：可以通过将程序上传到童芯派，此时可以拔掉数据线运行程序。**），本课程需要切换成“在线模式”。

![](https://cdn.nlark.com/yuque/0/2023/gif/757912/1672888207865-fefbe37e-6f95-4f76-b5e0-08bc2dc29dbc.gif)

## Part 3 开始编程
+ 在线模式时，程序中可以使用Python3的库，此程序就用到了math、random、sys、os等库
+ 编写程序，按下A键后对着童芯派输入语音，一段时间后童芯派在屏幕上会显示识别的结果。

```python
import os
import sys
from time import sleep
import random
import math
from time import sleep
import cyberpi

# 注意：该 接口在上传模式不存在，仅在在线模式起作用
cyberpi.set_recognition_url()

cyberpi.cloud.setkey("34d54aef8ede48379c5bf22c19aea159")
# 后续该部分会自动配置

cyberpi.wifi.connect("Maker-guest", "makeblock")
# 将此处的WiFi的账号密码改成你能访问到的

while not cyberpi.wifi.is_connect():
    pass
cyberpi.console.clear()
cyberpi.led.on(100, 0, 0)
#按下A键开始识别语音
@cyberpi.event.is_press("a")
def speech_recognition():
    cyberpi.console.clear()
    cyberpi.cloud.listen("chinese", 2)
    cyberpi.console.print(cyberpi.cloud.listen_result())
    cyberpi.led.on(0, 0, 0)
```

## Part 4 练习
1. 修改程序中的语言，试试看其它语言的语音能不能正确识别吧。

若有收获，就点个赞吧

  
 

