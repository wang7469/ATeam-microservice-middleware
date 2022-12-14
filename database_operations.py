from optparse import TitledHelpFormatter
#from turtle import title
import pymysql
from flask import Flask, Response, request
import json
# from flask_mysqldb import MySQL
import os


class DatabaseOperations:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = "root"
        pw = "Wd311714@"
        h = "localhost"

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn
