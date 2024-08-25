"""
此信息需要保留！

作者:zzXiaoZhu
github主页:https://github.com/zzXiaoZhu
仓库地址:https://github.com/zzXiaoZhu/five-in-a-row_byJuniorXZ/
项目开发于2022年

"""



import tkinter.messagebox
import subprocess
import tkinter
import pygame
import random
import time
import sys

pygame.init()

# 版本信息
Version = "2.0"
Beta = False

# 主战场
if Beta:
    pygame.display.set_caption("Jerry eat shit V{} Beta".format(Version))
else:
    pygame.display.set_caption("Jerry eat shit V{}".format(Version))
pygame.display.set_icon(pygame.image.load("Files\\Jerry.png"))
sc = pygame.display.set_mode((500, 500))
tk = tkinter.Tk()
tk.iconbitmap(default="Files\\logo.ico")
tk.withdraw()

# 运动不息，生命止
# Jerry
JerryUp = False
JerryLeft = False
JerryRight = False
JerryDown = False
LastX = []
LastY = []

# Shit
ShitUp = False
ShitLeft = False
ShitRight = False
ShitDown = False
ShitFastSkill = False
ShitFastSkillStartTime = 0

# 别考个鸭蛋抱回家~~~
Score = 20
LastScore = 20

# 我说你输你就是输了
JerryLose = False

# 作弊开关
auto = False
if "auto=true" in sys.argv:
    auto = True

# 等待时间
WaitTime = 0

# 选择界面
if auto:
    HardModeChoiceUi = True
    PlayerNumChoiceUi = False
else:
    HardModeChoiceUi = False
    PlayerNumChoiceUi = True

# 玩法相关初始变量
TwoPlayerMode = False
Easy = False
Middle = False
Hard = False
Hell = False
Purgatory = False
PurgatoryMove = 0
PurgatoryTime = 0
LastPurgatoryTime = 0

# Jerry的绿帽子
GreenHat = False

# 初始化绿屎生成概率变量
GreenShit = 0
GreenShitBool = False

# 角色Jerry\绿帽子以及相关变量
Jerry = pygame.image.load("Files\\Jerry.png")
GreenHatImage = pygame.image.load("Files\\GreenCap.png")
JerryX = 240
JerryY = 240

# 分数字体
ScoreFont = pygame.font.Font("Files\\MiSans.ttf", 20)

# 角色Shit
Shit = pygame.image.load("Files\\Shit.png")
ShitX = random.randint(0, 24) * 20
ShitY = random.randint(1, 24) * 20


# 关闭游戏
def Exit():
    # 你**关我游戏是吧
    global Time1
    Time1 = time.time()
    sys.exit()
    Wait(1)
    exit()


# 获取、处理事件
def GetEvent():
    Get = pygame.event.get()
    for event in Get:
        if event.type == pygame.QUIT:
            Exit()
        elif event.type == pygame.KEYDOWN:
            global JerryUp
            global JerryDown
            global JerryLeft
            global JerryRight
            global ShitUp
            global ShitDown
            global ShitLeft
            global ShitRight
            global auto
            global ShitFastSkillStartTime
            global ShitFastSkill

            if not auto and not HardModeChoiceUi and not JerryLose:
                # Jerry 移动
                if event.key == pygame.K_UP or event.key == pygame.K_i:
                    JerryUp = True
                    JerryLeft = False
                    JerryRight = False
                    JerryDown = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_k:
                    JerryUp = False
                    JerryLeft = False
                    JerryRight = False
                    JerryDown = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_j:
                    JerryUp = False
                    JerryLeft = True
                    JerryRight = False
                    JerryDown = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                    JerryUp = False
                    JerryLeft = False
                    JerryRight = True
                    JerryDown = False

                # Shit移动
                if event.key == pygame.K_w:
                    ShitUp = True
                    ShitLeft = False
                    ShitRight = False
                    ShitDown = False
                elif event.key == pygame.K_s:
                    ShitUp = False
                    ShitLeft = False
                    ShitRight = False
                    ShitDown = True
                elif event.key == pygame.K_a:
                    ShitUp = False
                    ShitLeft = True
                    ShitRight = False
                    ShitDown = False
                elif event.key == pygame.K_d:
                    ShitUp = False
                    ShitLeft = False
                    ShitRight = True
                    ShitDown = False
                elif event.key == pygame.K_q:
                    if time.time() - ShitFastSkillStartTime > 60:
                        ShitFastSkill = True
                        ShitFastSkillStartTime = time.time()


# 定义移动Jerry变量
def MoveJerry():
    global JerryUp
    global JerryDown
    global JerryLeft
    global JerryRight
    global JerryLose
    global JerryX
    global JerryY
    global Score
    global LastX
    global LastY
    global auto
    BodyX = []
    BodyY = []
    Named = locals()

    if JerryUp and not JerryY == 0:
        JerryY -= 20
    elif JerryDown and not JerryY == 480:
        JerryY += 20
    elif JerryLeft and not JerryX == 0:
        JerryX -= 20
    elif JerryRight and not JerryX == 480:
        JerryX += 20
    elif not JerryRight and not JerryLeft and not JerryUp and not JerryDown:
        pass
    else:
        if not JerryLose:
            if not auto and not HardModeChoiceUi and not PlayerNumChoiceUi:
                tkinter.messagebox.showerror("你个傻逼", "你输了 死亡原因:撞了南墙不回头（皇家翻译:碰壁了）")
            JerryLose = True

    if not LastY:
        LastY.append(JerryY)
    if not LastX:
        LastX.append(JerryX)
    for i in range(int(Score // 1.0)):
        if i == 0:
            BodyX.append(JerryX)
            BodyY.append(JerryY)
        else:
            try:
                BodyX.append(LastX[i - 1])
                BodyY.append(LastY[i - 1])
            except:
                BodyX.append(JerryX)
                BodyY.append(JerryY)

    for i in range(int(Score // 1.0)):
        if not i == 0:
            try:
                sc.blit(Named["Body{}".format(i)], (BodyX[i], BodyY[i]))
            except:
                Named["Body{}".format(i)] = pygame.image.load("Files\\Body.png")
                sc.blit(Named["Body{}".format(i)], (BodyX[i], BodyY[i]))
    if not auto:
        for i in range(int(Score // 1.0)):
            if not i == 0:
                if JerryX == BodyX[i] and JerryY == BodyY[i]:
                    if not JerryLose and not HardModeChoiceUi and not Score - LastScore > 1 and not PlayerNumChoiceUi:
                        tkinter.messagebox.showerror("你个硫硼", "你输了 死亡原因:让我看看！  不要！（皇家翻译:吃到自己尾巴了）")
                        JerryLose = True
    LastX = BodyX
    LastY = BodyY
    sc.blit(Jerry, (JerryX, JerryY))
    if GreenHat:
        sc.blit(GreenHatImage, (JerryX, JerryY - 10))


# 等待函数
def Wait(Time):
    # 防未响应
    while True:
        GetEvent()
        if not time.time() - Time1 > Time:
            continue
        else:
            break


# 加分
def AddScore():
    global ShitY
    global ShitX
    global JerryX
    global JerryY
    global Score
    global Shit
    global GreenShitBool
    global PurgatoryMove
    global LastScore
    global PurgatoryTime
    global LastPurgatoryTime

    LastScore = Score

    if TwoPlayerMode:
        if ShitX + 18 >= JerryX >= ShitX - 2 and ShitY + 18 >= JerryY >= ShitY - 2 or ShitX + 22 >= JerryX + 20 >= ShitX + 2 and ShitY + 22 >= JerryY + 20 >= ShitY + 2:
            Score += 1
            ShitX = random.randint(0, 24) * 20
            ShitY = random.randint(1, 24) * 20
    else:
        if JerryX == ShitX and JerryY == ShitY:
            if GreenShitBool:
                Score += 2
            elif Hell:
                Score += 0.5
            elif Purgatory:
                if PurgatoryMove < 2:
                    PurgatoryMove += 1
                else:
                    Score += 0.3
                    PurgatoryTime = time.time()
                    PurgatoryMove = 0
            else:
                Score += 1

            ShitX = random.randint(0, 24) * 20
            ShitY = random.randint(1, 24) * 20

            if random.randint(0, 100) < GreenShit:
                Shit = pygame.image.load("Files\\GreenShit.png")
                GreenShitBool = True
            elif Hell or Purgatory:
                Shit = pygame.image.load("Files\\HalfShit.png")
            else:
                Shit = pygame.image.load("Files\\Shit.png")
                GreenShitBool = False
        else:
            if Purgatory:
                if time.time() - PurgatoryTime > 5 and Score >= 0.1 and time.time() - LastPurgatoryTime > 1:
                    Score -= 0.1
                    LastPurgatoryTime = time.time()
    Score = round(Score, 1)


# 移动Shit
def MoveShit():
    global ShitY
    global ShitX
    global ShitUp
    global ShitDown
    global ShitRight
    global ShitLeft
    global ShitFastSkillStartTime
    global ShitFastSkill

    if ShitFastSkill:
        if time.time() - ShitFastSkillStartTime > 10:
            ShitFastSkillStartTime = time.time()
            ShitFastSkill = False
            Temp = 15
        else:
            Temp = 30
    else:
        Temp = 15
    if ShitUp:
        ShitY -= Temp
    elif ShitDown:
        ShitY += Temp
    elif ShitLeft:
        ShitX -= Temp
    elif ShitRight:
        ShitX += Temp

    if ShitX > 480:
        ShitX = 480
    elif ShitX < 0:
        ShitX = 0
    elif ShitY > 480:
        ShitY = 480
    elif ShitY < 0:
        ShitY = 0


def ShowScore():
    # 显示分数
    global Score
    global auto
    if Beta:
        BetaText = ScoreFont.render("测试版本", True, (255, 25, 255))
        sc.blit(BetaText, (0, 480))
        sc.blit(BetaText, (420, 0))
        sc.blit(BetaText, (420, 480))
    elif auto:
        AutoText = ScoreFont.render("自动模式", True, (255, 25, 255))
        sc.blit(AutoText, (0, 480))
        sc.blit(AutoText, (420, 0))
        sc.blit(AutoText, (420, 480))
    ScoreText = ScoreFont.render("当前分数：{};屏幕完全变绿需要30分".format(Score), True, (255, 25, 255))
    sc.blit(ScoreText, (0, 0))


def UpdateDisplay():
    global Score
    global sc
    global JerryLose
    global GreenHat
    # Jerry绿了
    if not Score == 30:
        sc.fill((0, Score * 8, 0))
    else:
        if not JerryLose and not HardModeChoiceUi:
            if not auto:
                tkinter.messagebox.showinfo("是不是应该给你搬个奖啊", "你成功把Jerry绿了")
            GreenHat = True
            JerryLose = True
        sc.fill((0, 255, 0))
    sc.blit(Shit, (ShitX, ShitY))
    GetEvent()
    AddScore()
    MoveJerry()
    if TwoPlayerMode and not JerryLose:
        MoveShit()
    ShowScore()
    pygame.display.update()


# 按钮
ButtonImage = pygame.image.load("Files\\Button.png")


def Button(XY, Word, Event, TextColor):
    sc.blit(ButtonImage, (XY[0], XY[1]))
    WordLen = len(Word)
    Word = ScoreFont.render(Word, True, TextColor)
    sc.blit(Word, (XY[0] + 90 - (20 * WordLen) / 2, XY[1] + 30))
    MousePos = pygame.mouse.get_pos()

    for event in Event:
        if XY[0] < MousePos[0] < XY[0] + 180 and XY[1] < MousePos[1] < XY[1] + 80:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        elif event.type == pygame.QUIT:
            Exit()


# 隐藏鼠标
pygame.mouse.set_visible(False)

# 孤寡孤寡孤寡孤寡孤寡孤寡孤寡孤寡
if PlayerNumChoiceUi:
    # 位置
    PlayerNumButtonX = (150, 150)
    PlayerNumButtonY = (100, 300)

    # 文字内容
    PlayerNumButtonWord = ("单人模式", "双人模式")

    # 人数选择进入动画
    for i in range(130):
        if i > 115:
            i = i - 115
            i = 115 - i
        sc.fill("white")
        event = pygame.event.get()
        Button(XY=(PlayerNumButtonX[0], PlayerNumButtonY[0] * i / 100),
               Word=PlayerNumButtonWord[0][0:int(len(PlayerNumButtonWord[0]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        Button(XY=(PlayerNumButtonX[1], PlayerNumButtonY[1] * i / 100),
               Word=PlayerNumButtonWord[1][0:int(len(PlayerNumButtonWord[1]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        pygame.display.update()
        time.sleep(0.003)

    # 瞒天过海(正式进入人数选择界面)
    while PlayerNumChoiceUi:
        event = pygame.event.get()
        MouseXY = pygame.mouse.get_pos()
        sc.fill("white")
        # 人数按钮
        OnePlayer = Button(XY=(PlayerNumButtonX[0], PlayerNumButtonY[0]), Word=PlayerNumButtonWord[0], Event=event,
                           TextColor=(0, 255, 0))
        TwoPlayers = Button(XY=(PlayerNumButtonX[1], PlayerNumButtonY[1]), Word=PlayerNumButtonWord[1], Event=event,
                            TextColor=(0, 255, 0))
        if OnePlayer:
            PlayerNumChoiceUi = False
            HardModeChoiceUi = True
            break
        elif TwoPlayers:
            PlayerNumChoiceUi = False
            TwoPlayerMode = True
            WaitTime = 0.2
            GreenShit = 0
            break

        # “鼠”标
        MoveJerry()
        JerryX = MouseXY[0]
        JerryY = MouseXY[1]
        pygame.display.update()

    # 人数选择退出动画
    for i in range(100):
        i = 100 - i
        sc.fill("white")
        event = pygame.event.get()
        Button(XY=(PlayerNumButtonX[0], PlayerNumButtonY[0] * i / 100),
               Word=PlayerNumButtonWord[0][0:int(len(PlayerNumButtonWord[0]) * i / 100 // 1)],
               Event=event,
               TextColor=(0, 255, 0))
        Button(XY=(PlayerNumButtonX[1], PlayerNumButtonY[1] * i / 100),
               Word=PlayerNumButtonWord[1][0:int(len(PlayerNumButtonWord[1]) * i / 100 // 1)],
               Event=event,
               TextColor=(0, 255, 0))
        pygame.display.update()
        time.sleep(0.003)

# 难度选择界面
if HardModeChoiceUi:
    # 位置
    HardButtonX = (150, 150, 150, 150, 150)
    HardButtonY = (10, 110, 210, 310, 410)

    # 文字内容
    HardButtonWord = ("简单", "中等", "困难", "地狱", "炼狱")

    # 困难选择进入动画
    for i in range(130):
        if i > 115:
            i = i - 115
            i = 115 - i
        sc.fill("white")
        event = pygame.event.get()
        Button(XY=(HardButtonX[0], HardButtonY[0] * i / 100),
               Word=HardButtonWord[0][0:int(len(HardButtonWord[0]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        Button(XY=(HardButtonX[1], HardButtonY[1] * i / 100),
               Word=HardButtonWord[1][0:int(len(HardButtonWord[1]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        Button(XY=(HardButtonX[2], HardButtonY[2] * i / 100),
               Word=HardButtonWord[2][0:int(len(HardButtonWord[2]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        Button(XY=(HardButtonX[3], HardButtonY[3] * i / 100),
               Word=HardButtonWord[3][0:int(len(HardButtonWord[3]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        Button(XY=(HardButtonX[4], HardButtonY[4] * i / 100),
               Word=HardButtonWord[4][0:int(len(HardButtonWord[4]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        pygame.display.update()
        time.sleep(0.003)

    # 偷天换日（正式进入难度选择界面）
    while HardModeChoiceUi:
        event = pygame.event.get()
        MouseXY = pygame.mouse.get_pos()
        sc.fill("white")
        # 困难按钮
        Easy = Button(XY=(HardButtonX[0], HardButtonY[0]), Word=HardButtonWord[0], Event=event, TextColor=(0, 255, 0))
        Middle = Button(XY=(HardButtonX[1], HardButtonY[1]), Word=HardButtonWord[1], Event=event, TextColor=(0, 255, 0))
        Hard = Button(XY=(HardButtonX[2], HardButtonY[2]), Word=HardButtonWord[2], Event=event, TextColor=(0, 255, 0))
        Hell = Button(XY=(HardButtonX[3], HardButtonY[3]), Word=HardButtonWord[3], Event=event, TextColor=(0, 255, 0))
        Purgatory = Button(XY=(HardButtonX[4], HardButtonY[4]), Word=HardButtonWord[4], Event=event,
                           TextColor=(0, 255, 0))

        if Easy:
            Easy = True
            WaitTime = 0.3
            GreenShit = 50
            HardModeChoiceUi = False
            break
        elif Middle:
            Middle = True
            WaitTime = 0.2
            GreenShit = 8
            HardModeChoiceUi = False
            break
        elif Hard:
            Hard = True
            WaitTime = 0.1
            GreenShit = 0
            HardModeChoiceUi = False
            break
        elif Hell:
            Hell = True
            WaitTime = 0.05
            GreenShit = 0
            HardModeChoiceUi = False
            Shit = pygame.image.load("Files\\HalfShit.png")
            break
        elif Purgatory:
            Purgatory = True
            WaitTime = 0.03
            GreenShit = 0
            HardModeChoiceUi = False
            Shit = pygame.image.load("Files\\HalfShit.png")
            break
        MoveJerry()
        JerryX = MouseXY[0]
        JerryY = MouseXY[1]
        pygame.display.update()

    # 困难选择退出动画
    for i in range(100):
        i = 100 - i
        sc.fill("white")
        event = pygame.event.get()
        Button(XY=(HardButtonX[0], HardButtonY[0] * i / 100),
               Word=HardButtonWord[0][0:int(len(HardButtonWord[0]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        Button(XY=(HardButtonX[1], HardButtonY[1] * i / 100),
               Word=HardButtonWord[1][0:int(len(HardButtonWord[1]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        Button(XY=(HardButtonX[2], HardButtonY[2] * i / 100),
               Word=HardButtonWord[2][0:int(len(HardButtonWord[2]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        Button(XY=(HardButtonX[3], HardButtonY[3] * i / 100),
               Word=HardButtonWord[3][0:int(len(HardButtonWord[3]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        Button(XY=(HardButtonX[4], HardButtonY[4] * i / 100),
               Word=HardButtonWord[4][0:int(len(HardButtonWord[4]) * i / 100 // 1)], Event=event,
               TextColor=(0, 255, 0))
        pygame.display.update()
        time.sleep(0.003)

# 显示鼠标
pygame.mouse.set_visible(True)

# 回到(0,0)
# 防输
Score = 40
JerryLose = True
i = 255
while True:
    if not i == 0:
        i -= 1
    sc.fill((i, i, i))
    GetEvent()
    if JerryX > 240:
        JerryX -= 1
    elif JerryX < 240:
        JerryX += 1
    elif JerryY > 240:
        JerryY -= 1
    elif JerryY < 240:
        JerryY += 1
    elif JerryX == 240 and JerryY == 240:
        pass
    MoveJerry()
    if JerryX == 240 and JerryY == 240 and not i:
        JerryLose = False
        break
    time.sleep(0.001)
    pygame.display.update()

Score = 0
while True:
    Time1 = time.time()
    UpdateDisplay()

    # 诚信作弊，考试可耻
    if auto:
        if JerryX > ShitX:
            JerryX -= 20
        elif JerryX < ShitX:
            JerryX += 20
        elif JerryY > ShitY:
            JerryY -= 20
        elif JerryY < ShitY:
            JerryY += 20

    # 我好不容易玩一次游戏，你却让我输的这么彻底？ 哈哈哈哈哈哈哈 氧化钙！！！
    while JerryLose:
        UpdateDisplay()
        if JerryLose and not Score == 0:
            if Score < 1:
                Score = 0
            else:
                Score -= 1
        if JerryLose and not JerryX == 240:
            if JerryX > 240:
                JerryX -= 20
            else:
                JerryX += 20
        elif JerryLose and not JerryY == 240:
            if JerryY > 240:
                JerryY -= 20
            else:
                JerryY += 20
        if JerryLose:
            JerryUp = False
            JerryDown = False
            JerryLeft = False
            JerryRight = False
        if Score == 0 and JerryY == 240 and JerryX == 240:
            JerryLose = False
        time.sleep(0.1)
    Wait(WaitTime)
