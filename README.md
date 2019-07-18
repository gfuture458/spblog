#spblog

个人博客

django + xadmin

模版  https://www.yangqq.com/  
部署 nginx + uwsgi

编辑器  ueditor



#解决安装mysqlclient的冲突
apt-get install libmysqlclient-dev python3-dev

#解决ajax post出现“CSRF token missing or incorrect.”的问题（非表单提交）
data: {csrfmiddlewaretoken: '{{ csrf_token }}'}

## todo
    不重要数据和session存入redis
    用celery实现每天数据的增量备份
    评论邮件通知
    seo
     