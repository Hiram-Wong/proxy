# -*- encoding: utf-8 -*-

from flask import Flask,Response,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import random
import json

#建立对象
app = Flask(__name__)

#载入配置文件

# 指定数据库连接还有库名
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://proxy:123456@127.0.0.1:3306/proxy?charset=utf8'

# #指定配置用来省略提交操作
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#建立数据库对象
db = SQLAlchemy(app)


#建立数据库类，用来映射数据库表,将数据库的模型作为参数传入
class User(db.Model):
    #声明表名
    __tablename__ = 'proxy'
    #建立字段函数
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    ip = db.Column(db.String(255))
    port = db.Column(db.String(255))
    protocol = db.Column(db.String(255))
    anonymity = db.Column(db.String(255))
    area = db.Column(db.String(255))


@app.route('/')
def index():
    #增，入库逻辑
    #生命对象
    # user = User(name='你好你好',password='456456')
    #调用添加方法
    # db.session.add(user)
    #提交入库，上面已经导入了提交配置，所以不需要在提交了
    # db.session.commit()
    proxy_count_all = User.query.count()
    proxy_count_rand = random.randint(1,proxy_count_all)
    proxy_datas = User.query.filter_by(id = proxy_count_rand).first()
    proxy_data_id = proxy_datas.id
    proxy_data_name = proxy_datas.name
    proxy_data_ip = proxy_datas.ip
    proxy_data_port = proxy_datas.port
    proxy_data_protocol = proxy_datas.protocol
    proxy_data_anonymity = proxy_datas.anonymity
    proxy_data_area = proxy_datas.area
    print(proxy_data_id,proxy_data_name,proxy_data_ip,proxy_data_port,proxy_data_protocol,proxy_data_anonymity,proxy_data_area)

    res = {
        'code' :200,
        'msg' : 'success',
        'data' : {
            'id' : proxy_data_id,
            'name' : proxy_data_name,
            'ip' : proxy_data_ip,
            'port': proxy_data_port,
            'protocol': proxy_data_protocol,
            'anonymity' : proxy_data_anonymity,
            'area' : proxy_data_area
        }
    }
    print(res)
    return Response(json.dumps(res,ensure_ascii=False), mimetype='application/json')

# http://127.0.0.1:5000?ip=192.168.0.1
@app.route('/delete', methods=['GET'])
def delete():
    id = request.args.get('id')
    ip = request.args.get('ip')
    if not ip:
        return Response(json.dumps({'error' : '缺少参数'}, ensure_ascii=False), mimetype='application/json')
        # return jsonify(dict(error='缺少参数'))
    else:
        proxy_datas = User.query.filter_by(ip=ip).first()
        db.session.delete(proxy_datas)
        db.session.commit()
        db.close()
        return Response(json.dumps({'msg' : '删除成功', '当前删除的ip' : ip}, ensure_ascii=False), mimetype='application/json')

if __name__ == "__main__":
    app.run()