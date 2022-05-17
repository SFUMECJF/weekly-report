## 科学上网
首先认认真真去把上面这篇教程看明白了。搞懂整个过程的大概讲什么意思。
不同点：

1. 我直接在windows上，把测试可行的yml文件都复制到了Linux下自己的文件夹下，想使用哪个机场的配置文件的时候，直接用`-f`指定就好。

   也就是说，我并没有下面这一步，我直接把配置文件复制到clash可执行文件所在的目录。

   ```
   wget -O config.yaml 您的订阅链接
   ```

   

   另外也不需要设置开机自启，反正也不经常开关机(云服务器)。

2. 使用的时候，也不需要使用它的setsid命令。看我下面的使用方法

### 使用
[使用sccreen设置为后台进程](https://www.cnblogs.com/Vicky1361/p/14490007.html)

我想在执行一次clash之后，把它放在后台，同时还能够在想看clash信息的时候，随时去看。所以这里使用screen命令包装了一下clash。

```
screen -S clash
./clash-linux-amd64-v3-v1.10.6 -f onermb.yml 2>&1
Ctrl+A+D
screen -r clash
```

### 设置zsh每次打开都进行端口的转发
sudo vim ~/.zshrc
```
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```
输入export查看当前终端下的所有环境变量
### 测试 
一定要用curl，ping是不行的。最后实际上是将http和socket做了转发，ping是在更下一层的。

```
curl www.google.com
```
记得一定加www

### vscode
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