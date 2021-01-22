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
        print("获得技能%s"%t.name)
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
        ran_int = random.randint(0,len(obj1.wea) - 1)
        obj1.wea[ran_int].attack(obj2)
        print(wea3.ad)
    else:
        obj1.attack(obj2)
def skill(obj):
    while()
if __name__ == '__main__':
    input("--->"
          "输入回车开始游戏！")
    zhao = Role("斌子", 200, 20)
    li = Role("卉子", 200, 10)
    wea1 = Weapon("喵喵拳", 30)
    wea2 = Weapon("拍了拍", 20)
    wea3 = Weapon("买了个萌", 25)
    flag1 = True
    flag2 = True
    flag3 = True
    while True:
        attack(zhao,li)
        time.sleep(0.5)
        attack(li,zhao)
        skill = input("请输入技能，问号查询")

        time.sleep(0.5)
        if zhao.hp <= 0:
            print("斌子被卉子萌翻了！！！")
            break
        if li.hp <= 0:
            print("卉子被斌子征服了！！！")
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





