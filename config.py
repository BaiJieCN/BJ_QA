#encoding: utf-8

DEBUG = True

import os

SECRET_KEY = os.urandom(24)

DIAlECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'admin'
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'anz_qa'
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIAlECT,DRIVER,USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False