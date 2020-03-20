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


def proxy():
    proxy_count_all = User.query.count()
    proxy_count_rand = random.randint(1, proxy_count_all)
    proxy_datas = User.query.filter_by(id=proxy_count_rand).first()
    proxy_data_id = proxy_datas.id
    proxy_data_name = proxy_datas.name
    proxy_data_ip = proxy_datas.ip
    proxy_data_port = proxy_datas.port
    proxy_data_protocol = proxy_datas.protocol
    proxy_data_anonymity = proxy_datas.anonymity
    proxy_data_area = proxy_datas.area
    print(proxy_data_id, proxy_data_name, proxy_data_ip, proxy_data_port, proxy_data_protocol, proxy_data_anonymity,proxy_data_area)
    return proxy_data_id, proxy_data_name, proxy_data_ip, proxy_data_port, proxy_data_protocol, proxy_data_anonymity,proxy_data_area

# http://127.0.0.1:5000
@app.route('/')
def index():
    res = {
        'code' :200,
        'msg' : 'success',
        'data' : {
            'id' : proxy()[0],
            'name' : proxy()[1],
            'ip' : proxy()[2],
            'port': proxy()[3],
            'protocol': proxy()[4],
            'anonymity' : proxy()[5],
            'area' : proxy()[6]
        }
    }
    print(res)
    return Response(json.dumps(res,ensure_ascii=False), mimetype='application/json')

# http://127.0.0.1:5000?ip=192.168.0.1
@app.route('/delete', methods=['GET'])
def delete():
    ip = request.args.get('ip')
    if not ip:
        return Response(json.dumps({'error' : '缺少参数'}, ensure_ascii=False), mimetype='application/json')
    else:
        proxy_datas = User.query.filter_by(ip=ip).first()
        db.session.delete(proxy_datas)
        db.session.commit()
        db.close()
        return Response(json.dumps({'msg' : '删除成功', '当前删除的ip' : ip}, ensure_ascii=False), mimetype='application/json')


# http://127.0.0.1:5000/add?name=xx代理&ip=192.168.0.1&port=8888&protocol=http&anonymity=匿名&area=浙江
@app.route('/add', methods=['GET'])
def add():
    name = request.args.get('name')
    ip = request.args.get('ip')
    port = request.args.get('port')
    protocol = request.args.get('protocol')
    anonymity = request.args.get('anonymity')
    area = request.args.get('area')
    print(name,ip,port,protocol,anonymity,area)
    if not (name and ip and port and protocol and anonymity and area):
        return Response(json.dumps({'error' : '缺少参数'}, ensure_ascii=False), mimetype='application/json')
    else:
        proxy_add_data = User(name=name,ip=ip,port=port,protocol=protocol,anonymity=anonymity,area=area)
        db.session.add(proxy_add_data)
        db.session.commit()
        return Response(json.dumps({'msg' : '插入成功', '当前添加的ip' : ip}, ensure_ascii=False), mimetype='application/json')

if __name__ == "__main__":
    app.run()