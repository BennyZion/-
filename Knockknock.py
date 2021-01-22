import random
import time
import copy
import sys
from colorama import init,Fore,Back,Style
init(autoreset=True)
class Role:
    def __init__(self,name, hp, ad):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.wea = []
    def attack(self, obj):
        rand_ad = random.randint(self.ad-5, self.ad)
        obj.hp = obj.hp - rand_ad
        print("%s 攻击了 %s 造成了 %d 伤害，%s 还剩 %d 点血"%(self.name, obj.name, rand_ad, obj.name, obj.hp))
    def setWea(self, obj):
        t = copy.deepcopy(obj)
        print("\033[33m在战斗中，您觉醒了技能 %s！"%t.name)
        self.wea.append(t)
        self.wea[-1].ad = t.ad + self.ad
        self.wea[-1].ownnwer = self.name
class Weapon:
    def __init__(self, name, ad, cd, ownner=None):
        self.name = name
        self.ad = ad
        self.ownnwer = ownner
        self.cd = 0
        self.cd_plus = cd
    def attack(self,obj):
        rand_ad = random.randint(self.ad - 15, self.ad)
        rand_cp = random.randint(0,9)
        if rand_cp <= 2:
            obj.hp = obj.hp - 2*rand_ad
            print("%s 使用 %s 攻击 %s \033[31m命中要害\033[0m！造成了\033[31m %d \033[0m点伤害，%s 还剩 %d 点血"%(self.ownnwer, self.name, obj.name, 2*rand_ad, obj.name, obj.hp))
        else:
            obj.hp = obj.hp - rand_ad
            print("%s 使用 %s 攻击了 %s 造成了 %d 点伤害，%s 还剩 %d 点血" % (
            self.ownnwer, self.name, obj.name, rand_ad, obj.name, obj.hp))
        self.cd = self.cd_plus
    def cd_minus(self):
        if self.cd > 0:
            self.cd = self.cd - 1
def attack(obj1, obj2):
    if len(obj1.wea) > 0:
        skill(obj1,obj2)
    else:
        obj1.attack(obj2)
def skill(obj1,obj2):
    while True:
        skill = input("请选择您要释放的技能，输入序号，问号查询:").strip()
        if skill in ["?", "？"]:
            print("技能列表".center(50,"="))
            print("序号","技能名称", "冷却回合")
            for i, element in enumerate(obj1.wea):
                print(i, "  ", element.name, "  ",element.cd)
            continue
        try:
            skill = int(skill)
            if obj1.wea[skill].cd == 0:
                obj1.wea[skill].attack(obj2)
            else:
                print("由于技能在冷却，您使用了普通攻击！")
                obj1.attack(obj2)
        except:
            print("请输入正确的技能号!")
        else:
            break
def progress_bar():
    for i in range(1, 101):
        print("\r", end="")
        print("LOADING: {}%: ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    input("加载成功！输入回车开始游戏！")
if __name__ == '__main__':
    zhao = Role("大魔王BIN", 250, 20)
    wea0 = Weapon("眨眼睛", 8, 0)
    wea1 = Weapon("拍一拍", 15, 2)
    wea2 = Weapon("买个萌", 25, 4)
    wea3 = Weapon("喵喵拳", 35, 5)
    flag1 = True
    flag2 = True
    flag3 = True
    progress_bar()
    input("很久很久以前，魔王BIN突然出现，带来灾难带走了公主！（回车键继续）")
    input("王国危在旦夕，这时，您站了出来！")
    name = input("少年，您叫？（请输入您的角色名）").strip()
    if len(name) == 0:
        print("看您这么可爱，不如叫你卉子吧！")
        li = Role("卉子", 200, 10)
    else:
        li = Role(name, 200, 10)
    input("%s 骑上最快的马,带着大家的希望从城堡里出发!" % li.name)
    input("一路风霜,最后来到了魔王的宫殿！")
    input("您遇到了大魔王！！(回车开始战斗)")
    while True:
        for sk in li.wea:
            sk.cd_minus()
        attack(zhao,li)
        time.sleep(1)
        attack(li,zhao)
        time.sleep(1)
        if zhao.hp <= 0:
            print("大魔王BIN被您萌翻了，但是你不计前嫌，和魔王BIN幸福的生活在了一起！！！")
            break
        if li.hp <= 0:
            print("您被大魔王打败了，三十年河西，三十年河东,莫欺少年穷！！！")
            break
        if li.hp <= 180 and flag1:
            li.setWea(wea0)
            li.setWea(wea1)
            flag1 = False
        if li.hp <= 120 and flag2:
            li.setWea(wea2)
            flag2 = False
        if li.hp <= 80 and flag3:
            li.setWea(wea3)
            flag3 = False
    input("按回车键退出！")
