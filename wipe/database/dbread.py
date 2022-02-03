# author - dot.PY
# version - 
# date -

import cx_Oracle
import pymongo
import psycopg2
import pandas as pd

class oracle(object):
    '''
        create connection to a oracle database
    '''

    def __init__(self,host,port,service_name,username,password):
        self.host = host
        self.port = port
        self.service_name = service_name
        self.username = username
        self.password = password

        self.error = False
        self.msg = ''

        self.__initial_validation()
        self.__create_connection()

    def __initial_validation(self):

        if type(self.port) != type(123):
            self.error = True
            self.msg = "Error : port should be number "

    def __create_connection(self):

        try:
            dsn = cx_Oracle.makedsn(self.host,self.port,self.service_name)
            self.conn = cx_Oracle.connect(self.username, self.password , dsn=dsn, encoding="UTF-8")
        except Exception as ex:
            self.error = True
            self.msg = self.msg+"Error : while connecting to database "+str(ex)+" "

    def run_query(self,query):
        df = ''
        try:
            df = pd.read_sql(query,self.conn)
        except Exception as ex:
            self.error = True
            self.msg = self.msg+"Error : while executing the query "+str(ex)

class mongo(object):
    '''
        create connection to a oracle database
    '''

    def __init__(self,**kwargs):
        self.host = kwargs[host
        self.port = port
        self.db_name = db_name
        self.username = username
        self.password = password

        self.error = False
        self.msg = ''

        self.__initial_validation()
        self.__create_connection()

    def __initial_validation(self):

        if type(self.port) != type(123):
            self.error = True
            self.msg = "Error : port should be number "

    def __create_connection(self):

        try:
            dsn = cx_Oracle.makedsn(self.host,self.port,self.service_name)
            self.conn = cx_Oracle.connect(self.username, self.password , dsn=dsn, encoding="UTF-8")
        except Exception as ex:
            self.error = True
            self.msg = self.msg+"Error : while connecting to database "+str(ex)+" "

    def run_query(self,query):
        df = ''
        try:
            df = pd.read_sql(query,self.conn)
        except Exception as ex:
            self.error = True
            self.msg = self.msg+"Error : while executing the query "+str(ex)