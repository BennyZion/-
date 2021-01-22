import random
import time
import copy
import sys
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
        print("在战斗中，您觉醒了技能 %s！"%t.name)
        self.wea.append(t)
        self.wea[-1].ad = t.ad + self.ad
        self.wea[-1].ownnwer = self.name
class Weapon:
    def __init__(self, name, ad, ownner=None):
        self.name = name
        self.ad = ad
        self.ownnwer = ownner
    def attack(self,obj):
        rand_ad = random.randint(self.ad - 15, self.ad)
        obj.hp = obj.hp - rand_ad
        print("%s 使用 %s 攻击了 %s 造成了 %d 点伤害，%s 还剩 %d 点血"%(self.ownnwer, self.name, obj.name, rand_ad, obj.name, obj.hp))
def attack(obj1, obj2):
    if len(obj1.wea) > 0:
        skill(obj1,obj2)
    else:
        obj1.attack(obj2)
def skill(obj1,obj2):
    while True:
        skill = input("请输入技能序号，问号查询:").strip()
        if skill == "?":
            print("技能列表".center(50,"="))
            for i, element in enumerate(obj1.wea):
                print(i, element.name)
            continue
        try:
            skill = int(skill)
            obj1.wea[skill].attack(obj2)
        except:
            print("请输入正确的索引!")
        else:
            break
if __name__ == '__main__':
    zhao = Role("大魔王BIN", 200, 20)
    wea1 = Weapon("喵喵拳", 30)
    wea2 = Weapon("拍一拍", 20)
    wea3 = Weapon("买了个萌", 25)
    flag1 = True
    flag2 = True
    flag3 = True
    print("---游戏加载中 ： LOADING---")
    print("Loading", end="")
    for i in range(10):
        print(".", end='', flush=True)
        time.sleep(0.5)
    print(">", end='', flush=True)
    print("SUCCESS！")
    input("--->"
          "输入回车开始游戏！")
    input("很久很久以前，魔王BIN突然出现，带来灾难带走了公主！（回车键继续）")
    input("王国危在旦夕，这时，您站了出来！")
    name = input("少年，您叫？").strip()
    li = Role(name, 200, 10)
    input("%s 骑上最快的马,带着大家的希望从城堡里出发" % name)
    input("一路风霜,最后来到了魔王的宫殿！")
    input("您遇到了大魔王！！(回车开始战斗)")
    while True:
        attack(zhao,li)
        time.sleep(0.5)
        attack(li,zhao)
        time.sleep(0.5)
        if zhao.hp <= 0:
            print("大魔王BIN被您萌翻了，但是你不计前嫌，和魔王BIN幸福的生活在了一起！！！")
            break
        if li.hp <= 0:
            print("您被大魔王打败了，三十年河西，三十年河东,莫欺少年穷！！！")
            break
        if li.hp <= 180 and flag1:
            li.setWea(wea2)
            flag1 = False
        if li.hp <= 120 and flag2:
            li.setWea(wea3)
            flag2 = False
        if li.hp <= 80 and flag3:
            li.setWea(wea1)
            flag3 = False
    input("按回车键退出！")





