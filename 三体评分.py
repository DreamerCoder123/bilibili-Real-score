import requests  # 导入request库
import os
from win10toast import ToastNotifier
count = 20  # 尝试获取count人的评分
pos = ""
toaster=ToastNotifier()
commentScore = []  # 先行定义comments，也就是评论的内容
commentDetails=[0,0,0,0,0,0,0,0,0,0]  # 定义细节
totalComment=0
###########################################
id=input("请输入要爬取的电影or番剧的ID")
if id=='':
    print("请输入！！！")
    exit()
comm=input("请输入要爬取的评论数")
if comm=='':
    print("请输入！！！")
    exit()
print("时间或许需要30s及以上，请坐和放宽\n请不要断网，否则可能导致爬取失败！\n占用内存可能较多，请保证你的设备剩余内存在1G以上！")
requestCount = int(int(comm)/30)  # 请求requestCount次
###########################################

def getAVG(requestArray):
    total = 0
    for a in range(0, len(requestArray)):
        total += requestArray[a]
    return total/(len(requestArray))*1.0
###########################################
def getCom(mode):
    global pos,commentScore,commentDetails,totalComment
    url = "https://api.bilibili.com/pgc/review/"+mode+"/list?media_id="+id+"&ps=30&sort=0"  # 从最新的开始排序
    for com in range(0, requestCount):  # 此程序将运行requestCount次
        data = requests.get(url+pos).json()
        if data['message'] != "success":
            print("获取失败QWQ,请检查输入ID是否正确")
            exit()
        if data['data']['next'] == 0 and mode=="short":
            print("所有可用短评论已经获取完毕，正在尝试获取长评论")
            getCom("long")
            return 
        if data['data']['next'] == 0 and mode=="long":
            print("计算分数中")
            return
        if com+1==int(requestCount/2) and mode=="short":
            print("短评论收集终了")
            getCom("long")
            return
        if com+1==int(requestCount/2) and mode=="long":
            print("长评论收集终了")
            return
        os.system("cls")
        print("第", com+1, "次获取，虚拟鼠标信息", data['data']['next'],mode,"comment mode")
        pos = "&cursor="+str(data['data']['next'])
        for comments in range(0, len(data['data']['list'])):
            score=data['data']['list'][comments]['score']
            commentScore.append(score)
            commentDetails[score-1]+=1
getCom("short")
toaster.show_toast("进行的分析已经完成，真实评分为"+str(getAVG(commentScore)),
                   "本次获取到了"+str(len(commentScore))+"个人的评分\n详细数据为\n"+str(commentDetails),
                   duration=10,icon_path='')
os.system("pause")