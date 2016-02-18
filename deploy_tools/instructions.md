#Instructions#
1.$ django-admin.py startproject superlists //新建项目
2.$ python manage.py runserver //啟動Django的開發服務器
3.$ python manage.py startapp lists //Django鼓励以"应用"的方式组织代码.新建一个app
$ python functional_test.py //運行功能測試
$ python manage.py test //運行單元測試

-'單元測試/編寫代碼' 循環
1,在終端裏運行單元側室;
2,在編輯器中改動最少量的代碼;
3,重複上兩步.

##总结一下配置和部署的过程.##
-配置
1. 假设有用户账户和home目录;
2. apt-get nginx git python-pip;
3. pip install virtualenv;
4. 添加Nginx虚拟主机配置;
5. 添加Upstart任务, 自动启动Gunicorn.

-部署
1. 在~/sites中创建目录结构;
2. 拉取源码, 保存在source文件夹中;
3. 启动../virtualenv 中的虚拟环境;
4. pip install -r requirements.txt;
5. 执行manage.py migrate, 创建数据库;
6. 执行collectstatic 命令, 收集静态文件;
7. 在setting.py中设置DEBUG = False和ALLOWED_HOSTS;
8. 重启Gunicorn;
9. 运行功能测试, 确保一切正常.


