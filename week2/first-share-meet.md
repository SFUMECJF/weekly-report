## 使用IDEA系列软件debug的全面技巧
分享会长期链接：https://meeting.tencent.com/dm/Qet4sVXmOccd
每个人都会debug，所以该主题足够**普适。**但大家对各种语言的ide的熟悉程度也不一样, 也不一定能够使用好所有的功能，不同语言的ide提供的debug功能也不尽相同。

笔者最熟悉python，所以以pycharm为例，不管在什么地方，jet brains的ide都不会让你失望。

- python: pycharm
- go: goland
- c/c++: clion
- java:intellij

**调试，将自己想象的过程与实际的过程做对比**

## 基本单步调试技巧

- 打断点。断点当前行不执行
- step over。逐行执行代码
- step into。跳转进入当前行调用的函数，<不论函数是否在当前脚本文件内，都跳转>
- step into my code。只跳转当前脚本文件内的函数内部。（经测试也是可以进去其他脚本的。）
- step out。从里面一层的函数跳转到外边一层
- run to cursor。运行到光标选定的代码处

## evaluate expressions

1. 查看变量。经常看的变量添加到watch区
2. 使if分支按照意愿执行
3. 类似drop frame，重复执行一次某函数。



## 条件断点

满足条件时停止的断点。

## 异常断点

闪电标志：debug时，如果某行语句没打断点，但执行过程中产生异常，会在该行产生闪电标志的断点，同时停顿。

可以在左侧选择是否添加该类型的断点。

<img src="https://sfigure.oss-cn-beijing.aliyuncs.com/image-20220521101651723.png" alt="image-20220521101651723" style="zoom: 25%;" />



## 添加命令行参数

按照在命令行中添加参数的方式，在edit config的parameters栏添加参数。

## jupyter notebook

基本一致，注意每一个块的代码执行后，相应的变量都会在全局生效。所以命名时，要谨慎一点。另外，一个好的noteboke可以保证从头到尾执行后，不出问题。

## 类的调试

可以实现`__str__`函数令类更直观。

## 多线程调试

1. print大法好。
2. 一个线程调试，使用thread模式，只会阻塞该线程，其他线程会一直执行。使用all模式会在到达断点时阻塞所有线程（到达断点前，其他进程可能已经执行了），并且单步时其他线程也不会再执行。
3. 想在多个线程分别调试，要全部使用thread模式，手动来条件各个进程的执行过程。







## vscode远程调试

注意，vscode是以文件夹的形式来作为工程的。所以，一定要在调试的时候，在工程目录中大概vscode。不管是Linux还是Windows都一样。

c/c++安装好插件，以及gdb。如果工程目录对了，但是还是无法调试，就是插件或者其他东西没安装好。

[vscode 远程debug 调试linux上的makefile工程步骤](https://sanfengcs.blog.csdn.net/article/details/122807706)

Python会非常简单

## 其他（intellij调试技巧）

搞Java的同学再补充一下[这个视频](https://www.bilibili.com/video/BV1xa411Y72S?spm_id_from=333.880.my_history.page.click)

### 方法断点

帮助判断具体是接口的哪个实现在运行。

### drop frame

Java中可以重新执行函数。

python中可以使用evaluation实现大体相同的功能。





pycharm快捷键：

1. Alt+Shift+E，将代码放到console中执行。



## 演示代码

https://github.com/SFUMECJF/weekly-report/tree/main/week2/codes

## 找到组织

在论坛页面。



## 问卷

希望大家能对本次分享会给个建议，链接或者扫码~

https://jinshuju.net/f/kok6NH

<img src="https://sfigure.oss-cn-beijing.aliyuncs.com/%E7%AC%AC%E4%B8%80%E6%AC%A1%E5%88%86%E4%BA%AB%E4%BC%9A%E5%8F%8D%E9%A6%88_256.png" alt="第一次分享会反馈_256" style="zoom: 33%;" />



## 视频录播

bilibili : https://www.bilibili.com/video/BV1ct4y1s72a/







## 致谢

- cs61b某节课的lab
- bilibili的很多debug教程

