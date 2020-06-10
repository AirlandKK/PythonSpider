#### 环境
- django==2.1.1
- python==3.6.5

#### 安装依赖模块
``
pip install -r requirements.txt
``

#### 运行步骤
```python
1. 提前安装好依赖模块
2. 到utils目录下，运行两个文件，一个是爬虫的数据，一个是词云生成
    get_pyjobs.py (先运行这个)
    make_wordcloud.py (后运行这个)
3. Pycharm直接运行，或者命令运行
python manager runserver 127.0.0.1:8888
```

#### 注意
```python
mysql_conf.py 这个是用来连接mysql用的  这里没用到 如果需要 可以自己改 方法都写好了

```