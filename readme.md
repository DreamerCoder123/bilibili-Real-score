# 自动获取b站番剧真实评分
# 警告：此项目还在测试
## 创作初衷
这个世界上好的作品不多，有些作品也是烂的跟依托答辩一样，但是还是登顶了国创排行榜 **（点名异化三体）*(doge)*** 我们要做的就是揭开资本的伪装，了解他的真实

## 代码实现
1. 使用浏览器的开发者模式爬取Bilibili评论接口
```
api.bilibili.com/pgc/review/short/list?media_id=(当前想要查询的id)&ps=30&sort=0
```
2. 编写代码
## 使用
1. ### 不使用python
    1. 下载Release中的get.exe
    2. 输入电影的 id
    3. 耐心等待，当获取完成后会通知
## 当前BUG
- 使用exe版本时无法正常调用win10toast库，可能是python打包的问题
- 无法获取数目较小的评论数据

## 愿想
- 多修点bug
- 多来点假期
_______
$markdown$ $was$ $written$ $by$ $homo$