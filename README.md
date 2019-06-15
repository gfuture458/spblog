#spblog

#markdown
https://blog.csdn.net/duke10/article/details/81033686

#解决安装mysqlclient的冲突
apt-get install libmysqlclient-dev python3-dev

#解决ajax post出现“CSRF token missing or incorrect.”的问题（非表单提交）
data: {csrfmiddlewaretoken: '{{ csrf_token }}'}