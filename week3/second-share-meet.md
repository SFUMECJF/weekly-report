@[toc]
## 分享会链接

5月28日分享会长期链接：https://meeting.tencent.com/dm/Qet4sVXmOccd

---
Linux系统配环境很方便，大多数人有配Linux环境的需求。所以该主题足够普适。但对于每个人来说，到底使用哪种方式呢，都有什么优劣？
主要介绍以下方式Linux环境中的代理网络配置以及文件传输，编代码。

## 一台主机双系统❌



同一台电脑，每次启动时选择哪一个系统。
![如何实现Linux + Windows 双系统启动- 知乎](https://sfigure.oss-cn-beijing.aliyuncs.com/v2-f5bb6e10eac6816657af231169672798_1440w.jpg)



缺点：

- 文件不互通，需要专门的软件
- 需要划分电脑的硬盘等资源给双系统
- 只能有一个系统版本

## 两台主机❌

额外买一个硬件。

- NUC(2000 rmb)
- 二手笔记本
- 树莓派（400 rmb）,专门的树莓派系统
- 荔枝派，嵌入式用



<img src="https://sfigure.oss-cn-beijing.aliyuncs.com/image-20220528094152823.png" alt="image-20220528094152823" style="zoom: 50%;" />

<img src="https://sfigure.oss-cn-beijing.aliyuncs.com/image-20220528094312480.png" style="zoom:50%;" />

缺点：

- 花钱
- 只能有一个系统版本

优点✔️：搞嵌入式的同学推荐玩玩





## 虚拟机✔️

虚拟机是电脑上的一个软件，打开这个软件里的某个操作系统镜像，就可以使用这个操作系统。主流的虚拟机有vmware workstation和virtual box。个人在使用过程中，发现很多课程的教程都教virtual box, 所以本文也使用virtual box。



### 安装流程

看bilibili的安装教程就行。

大概来说：

1. 安装virtual box
2. 在virtual box中导入想要的某个系统的镜像，如果笔记本资源有限，可以选择`kubuntu`, `xubuntu`是真正ubuntu的精简版本，占用资源更小。还可以选择没有`GUI`的服务器版本，单纯通过命令行做控制。

### 文件互传

打开**VirtualBox**,选中虚拟机，依次点击设置->**共享文件夹**->最右边带+的**文件夹**按钮，在弹出的窗口如下图选择你的Windows下的某个**文件夹**（任意），然后只选择固定分配，点击OK。

### 网络代理

虚拟机可以使用允许本地局域网的连接，在虚拟机内再将终端的`http_proxy` 和`https_proxy`设置成127.0.0.1:7890

```
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

### 快照

<img src="https://sfigure.oss-cn-beijing.aliyuncs.com/image-20220528101555053.png" alt="image-20220528101555053" style="zoom:33%;" />

特点：

- 可以快照，保存系统的环境，但快照的文件体积相当相当大。
- 非常方便地添加各种系统版本
- 占用电脑资源多
- 速度更快
- 只能在一个电脑上用，受限于本地

### 编程-vsocde

vscode + remote-ssh (ssh-fs)插件。



### *vargrant

[COMS10012软件工具课](https://cs-uob.github.io/COMS10012/exercises/part1/overview.html)

## wsl2(不是wsl)✔️

文件互传



网络代理



常用技能



## 云主机✔️

特点：

- 可以快照，非常方便，到期了，新账号买主机，重新导入快照
- 一个系统版本
- 不占用电脑资源
- 速度相对更快
- 任何电脑上都能用

手头紧选最便宜的轻量应用服务器，

[腾讯云1c2g, 45元一年](https://curl.qcloud.com/eM5fxyMn)

[阿里云，1c1g有19元的](https://www.aliyun.com/activity/new?userCode=pqarxc0f)

### 代理
[使用sccreen设置为后台进程](https://www.cnblogs.com/Vicky1361/p/14490007.html)
```
screen -S clash
./clash-linux-amd64-v3-v1.10.6 -f onermb.yml 2>&1
Ctrl+A+D
screen -r clash
```



sudo vim ~/.zshrc
```
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```
输入export查看当前终端下的所有环境变量



一定要用curl，ping是不行的。最后实际上是将http和socket做了转发，ping是在更下一层的。

```
curl www.google.com
```
记得一定加www

关掉vscode之后，clash会运行在后台，它发送的终端信息也看不到了。
![在这里插入图片描述](https://img-blog.csdnimg.cn/912638769ff7493f8a7fe6ffd4420409.png)
左数第2个是进程号

```
ps -ef | grep clash
kill 进程号
unset http_proxy
unset https_proxy
unset no_proxy

```



## docker

有一些课程是提供配好环境的docker镜像的。可以尝试

![image-20220528102629844](https://sfigure.oss-cn-beijing.aliyuncs.com/image-20220528102629844.png)



## 演示代码

https://github.com/SFUMECJF/weekly-report/tree/main/week2/codes

## 找到组织

Telegram : https://t.me/+-FOA9RSORNJlNzJl

cs61abc基础课qq群： 482582963

嵌入式交流群qq： 1057158348

CMake交流群qq：433323162

CS 106B C++数据结构群qq：1023037623

CMake 在线电子书：https://sfumecjf.github.io/cmake-examples-Chinese/


## 问卷

希望大家能对本次分享会给个反馈，链接或者扫码~

https://jinshuju.net/f/Fj4Crr

<img src="https://sfigure.oss-cn-beijing.aliyuncs.com/%E7%AC%AC%E4%BA%8C%E6%AC%A1%E5%88%86%E4%BA%AB%E4%BC%9A%E5%8F%8D%E9%A6%88_256.png" alt="第二次分享会反馈_256" style="zoom:33%;" />

## 视频录播
更新在bilibili：

## 致谢