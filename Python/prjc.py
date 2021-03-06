#!/usr/bin/env python3
from flask import Flask, request, jsonify, abort, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime
import jwt
from passlib.hash import sha256_crypt
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/data.db'
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY']="secretkey"
db = SQLAlchemy(app)
ma = Marshmallow(app)


class post_office(db.Model):
    __tablename__ = 'post_office'
    id = db.Column(db.Integer, primary_key=True)
    Officename = db.Column(db.String(20))
    Pincode = db.Column(db.String(6))
    Officetype = db.Column(db.String(5))
    Dstats = db.Column(db.String(15))
    Divname = db.Column(db.String(50))
    Regname = db.Column(db.String(50))
    Circlename = db.Column(db.String(50))
    Taluk = db.Column(db.String(50))
    Distname = db.Column(db.String(50))
    Statename = db.Column(db.String(50))
    Phnum = db.Column(db.String(50))
    RHO = db.Column(db.String(50))
    RSO = db.Column(db.String(50))

    def __init__(self, **kwargs):
        self.Officename = kwargs['Officename']
        self.Pincode = kwargs['Pincode']
        self.Officetype = kwargs['Officetype']
        self.Dstats = kwargs['Dstats']
        self.Divname = kwargs['Divname']
        self.Regname = kwargs['Regname']
        self.Circlename = kwargs['Circlename']
        self.Taluk = kwargs['Taluk']
        self.Distname = kwargs['Distname']
        self.Statename = kwargs['Statename']
        self.Phnum = kwargs['Phnum']
        self.RHO = kwargs['RHO']
        self.RSO = kwargs['RSO']


class users(db.Model):
    ___tasblename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    passwd = db.Column(db.String(100))
    time = db.Column(
        db.DateTime, default=datetime.datetime.utcnow() + datetime.timedelta(minutes=1))

    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd


def token_req(f):
    def check(*args,**kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({'message': 'Token is missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid'})
        return f(*args,**kwargs)
    check.__name__=f.__name__
    return check



class post_office_schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = post_office


post = post_office_schema()
posts = post_office_schema(many=True)


@app.route('/api/post_office/all', methods=['GET'])
def api_all():
    qry = post_office.query.all()
    output = posts.dump(qry)
    return jsonify(output)


@app.route('/api/post_office', methods=['POST'])
@token_req
def new_office():
    r = {
        'Officename': " ",
        'Pincode': " ",
        'Officetype': " ",
        'Dstats': " ",
        'Divname': " ",
        'Regname': " ",
        'Circlename': " ",
        'Taluk': " ",
        'Distname': " ",
        'Statename': " ",
        'Phnum': " ",
        'RHO': " ",
        'RSO': " "

    }
    if request.is_json:
        for key in r:
            if not(request.json[key].strip() and type(request.json[key]) is str):
                abort(400)
            r[key] = request.json[key].upper()
        else:
            new_office = post_office(**r)
            db.session.add(new_office)
            db.session.commit()
            r['id'] = new_office.id
            return jsonify(r)
    else:
        abort(400)


@app.route('/api/post_office/<int:id>', methods=['DELETE'])
@token_req
def delete_office(id):
    office = post_office.query.get(id)
    try:
        db.session.delete(office)
        db.session.commit()
        result = post.dump(office)
        return jsonify(result)
    except:
        return jsonify({'data': "not_existing"})


@app.route('/api/post_office/<int:id>', methods=['PUT'])
@token_req
def modify_office(id):

    office = post_office.query.get(id)
    if office:
        office.Officename = request.get_json().get('Officename', office.Officename).upper()
        office.Pincode = request.get_json().get('Pincode', office.Pincode).upper()
        office.Officetype = request.get_json().get('Officetype', office.Officetype).upper()
        office.Dstats = request.get_json().get('Dstats', office.Dstats).upper()
        office.Divname = request.get_json().get('Divname', office.Divname).upper()
        office.Regname = request.get_json().get('Regname', office.Regname).upper()
        office.Circlename = request.get_json().get('Circlename', office.Circlename).upper()
        office.Taluk = request.get_json().get('Taluk', office.Taluk).upper()
        office.Distname = request.get_json().get('Distname', office.Distname).upper()
        office.Statename = request.get_json().get('Statename', office.Statename).upper()
        office.Phnum = request.get_json().get('Phnum', office.Phnum).upper()
        office.RHO = request.get_json().get('RHO', office.RHO).upper()
        office.RSO = request.get_json().get('RSO', office.RSO).upper()
        db.session.commit()
        return post.jsonify(office)
    else:
        return jsonify({'data': "not_existing"})


@app.route('/api/post_office', methods=['GET'])
def qry_select():
    ref = {}
    for key in request.args:
        ref[key] = request.args[key].upper()
    offices = post_office.query.filter_by(**ref)
    results = posts.dump(offices)
    return jsonify(results)


@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password and auth.username:
        a = users.query.filter_by(name=auth.username).first()
        # print(a.time)
        # print(datetime.datetime.utcnow())
        if a:
            # a.time = datetime.datetime.utcnow()
            if  sha256_crypt.verify(auth.password,a.passwd):
                if a.time <= datetime.datetime.utcnow():
                    a.time = datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
                    db.session.commit()
                    token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)}, app.config['SECRET_KEY'])
                    return jsonify({'token': token.decode('utf-8')})
                return jsonify({'token': 'Not expired'})
            else:
                return ("username/password not matching")
        passwd=sha256_crypt.encrypt(auth.password)
        info = users(auth.username, passwd)
        db.session.add(info)
        db.session.commit()
        token= jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=1)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('utf-8')})
    return make_response('could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required'})



app.run(host='0.0.0.0', port=5000)
