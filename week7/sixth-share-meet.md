# cs61abc分享会（六）程序的输入输出详解 - 标准输入输出，文件，设备，EOF，命令行参数
## 分享会链接

2022年7月23日分享会长期链接：https://meeting.tencent.com/dm/Qet4sVXmOccd

分享时间：9点20到9点50
视频录播在最下方

---

@[TOC](文章目录)
## 标准输出 /dev/stdout
就是键盘
在终端上显示。

## 标准错误 /dev/stderr
错误信息
也在终端上显示。
虽然在同一个地方显示，但可以和stdin区别开。通过重定向符号 > 

## 交互式标准输入 /dev/stdin
换行和空格区分每一次的输入。
```shell
3
a 1 bccc
```
python为例：
```python
try :
	while True:
	    line = input()
	    # process line
except EOFError:
     pass
```
如何处理EOF呢？

## EOF结尾式标准输入 /dev/stdin
End Of File的缩写，通常在文件的最后存在此字符表示文件结束。
### EOF表示
终端中：CTRL + D
C语言中：-1，头文件有定义stdio.h
python: 空字符串
在Linux系统之中，EOF根本不是一个字符，而是当系统读取到文件结尾，所返回的一个信号值（也就是-1）。至于系统怎么知道文件的结尾，资料上说是通过比较文件的长度。
### EOF处理
没有用户输入的情况下, 那就使用标准输出。
使用input的方式：
```python
try :
	while True:
	    line = input()
	    # process line
except EOFError:
     pass
```
使用stdin的方式，遇到EOF为空：
```python
while True:
    line = sys.stdin.readline()
    if line = '':
        break
    else:
        # Do what
        pass
```
C++方式 ,遇到EOF，返回值为0：
```c++
while (cin >> a) {
// process
}
```
## 文件的输入和输出
输入直接全读。
输出不用在乎EOF。
但是是有EOF的。

## Linux 设备的输出和重定向
/dev/null
/dev/zero
1 标准输入
2 标准输出
默认是对标准输入做处理：`./p.py > a.txt`
如果想改的话，把改的地方说清楚。是1的文件，还是1这个stdin
1 >&2
1 > /dev/null      2 >/dev/null

### 在shell中的应用
```shell
if cat a ;then
:
fi
```

```shell
if cat a 1 > /dev/null 2 >/dev/null;then
:
fi
```
## 命令行参数的输入




## debug
所有的输入输出都可以debug，但不知道pycharm的话，可能有坑点。
[pycharmdebug时，输入标准输入没反应的处理方式](https://youtrack.jetbrains.com/issue/PY-42488)
在pycharm中debug注意取消选择。


## 补充
关于术语，有没有什么需要修改的？
补充的地方
问题

## 演示代码

https://github.com/SFUMECJF/weekly-report/

## 找到组织

Telegram : https://t.me/+-FOA9RSORNJlNzJl

cs61abc基础课qq群： 482582963

嵌入式交流群qq： 1057158348

CMake交流群qq：433323162

CS 106B C++数据结构群qq：1023037623

CMake 在线电子书：https://sfumecjf.github.io/cmake-examples-Chinese/

公众号：三丰杂货铺


## 问卷

希望大家能对本次分享会给个建议，链接或者扫码~

https://jinshuju.net/f/Fj4Crr

![问卷反馈](https://img-blog.csdnimg.cn/img_convert/985bc80ede1c053d078ee0451aa8f563.png)

## 视频录播

更新在bilibili：https://space.bilibili.com/39544331/channel/seriesdetail?sid=2315808

## 公众号
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200529103009878.gif#pic_center)

## 致谢