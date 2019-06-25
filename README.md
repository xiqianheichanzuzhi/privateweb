# privateweb
个人开源网站
# flask 开发的个人web

### [BUG反馈](提交至bugdiff)

### 内容
1. 网页包括注册登录，个人博客，python，互联网新闻，福利，关于我等模块。
2.后台内容根据blueprint分成不同模块，每个模块无需与其他模块自关联
3. 服务端（debine/ubuntu）选型: 最前端是nginx, 其后是gunicorn。
4. python版本3.5以上
5. 集成支付宝，微信的支付。
6. 将遇到并解决web开发中常见的大部分场景。  
   登录/注册, (ok)  
   邮件,  
   验证,(restful is ok, admin is ok), 自搭脚手架  
   事件监听,  
   异常处理,  
   orm,(ok)  
   session管理,(ok)  
   cache,  
   文件上传下载,(ok)  
   安全保证,(deving)  
   在线支付,  
   日志管理,  
   性能提升,  
   预留分布式架构  
   ...

### 构建步骤
1. pip3 install -r requirements.txt
2. 配置nginx_flask_online_store.config文件, 设置hosts解析到本地 127.0.0.1 fos.dev api.fos.dev admin.fos.dev （未实现）
3. 配置redis 用于session状态保存及防自动化注册账户
4. APP.config 文件用于配置数据库及app默认设置
5. python(3) manage.py -p8000 -d  开启debug模式
...

### roadmap
1. 基本目录结构 --ok
2. 基本views(路径) --ok
3. 数据库与表的设计 --debug
4. 登陆及注册处理 --OK
5. 个人博客 --dev（amdin添加分类需关联个人博客,category_id=8）  
6. Python   -dev(admin添加分类需关联python,category_id in [1,2,3])
7. 福利   --waiting(部分内容需注册开放)
8. 互联网新闻 --waiting
9. ...

### 使用到的包
详见txt
...

```

### command line 命令行的使用
最外层的manager.py文件, 默认是python3的输出样式， 2版本需要手动修改一下print  
例如 python3 manager.py db_create 对应的是其中的 db_create函数

#### 急速添加中...
