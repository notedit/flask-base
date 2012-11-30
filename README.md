# flask-base

a skeleton for flask

author: notedit

### virtualenv+flask+gunicorn+supervisor环境搭建与部署


这个代码库包含了一个flask web站的基本框架,可以通过如下的步骤把一个生产环境搭建起来

#### 新建一个用户

新建一个用户名wwwuser 所属wwwuser组的用户,具体的步骤可自行搜索 

#### 安装virtualenv和依赖

```
sudo pip install virtualenv
sudo pip install virtualenvwrapper
```

这样就安装好virtualenv 和 virtualenvwrapper,然后建立一个虚拟环境,

```
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv --no-site-packages online
```
这样就建立了一个online的虚拟环境,为了以后不用每次都执行source /usr/local/bin/virtualenvwrapper.sh,可以把这行语句放到 ~/.bashrc 中去.

进入flask-base中,安装需要的依赖

```
pip install -r requirement.txt
```

#### 查看目录和运行单元测试

装完依赖之后就可以查看代码布局了,代码很简单,你可以在此基础上添加一些自己的东西.

在代码的根目录你可以看到一个manage.py,这个是整个代码的入口,你可以运行

```
python  manage.py  
```
你可以添加自己想要的命令,比如新建用户,迁移一些数据等等.

还包含了一些测试代码,你可以在代码的根目录运行单元测试:

```
nosetest  tests
```

#### supervisor

在正常的网站运行中,你需要一些进程管理工具,这里使用supervisor,代码库中已经包含一个 supervisord 的配置文件,你可以添加自己的服务.





