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
    
    @staticmethod
    def get_ownwer_id(blog_id):
        sql = "SELECT OWNER_ID FROM cs6156_login_microservice.blog_info WHERE unique_blog_id = %s"
        conn = DatabaseOperations._get_connection()

        cur = conn.cursor()
        res = cur.execute(sql, args=(blog_id))
        result = cur.fetchone()
        return result

    @staticmethod
    def new_notification(blog_owner, comment_poster):
        sql = "INSERT INTO cs6156_middleware.notification VALUES (%s, %s)";
        conn = DatabaseOperations._get_connection()

        cur = conn.cursor()
        res = cur.execute(sql, args=(blog_owner, comment_poster))
        if res:
            new_notification_created = {'status': 'success', 'message': 'Successfully inserted new notification into database'}
            success_response = Response(json.dumps(new_notification_created), status=200, content_type="application.json")
            return success_response
        else:
            new_notification_failed = {'status': 'fail', 'message': 'Failed to insert new notification'}
            fail_response = Response(json.dumps(new_notification_failed), status=200, content_type="application.json")
            return fail_response
    
    @staticmethod
    def remove_notification(blog_owner):
        sql = "DELETE FROM cs6156_middleware.notification WHERE blog_owner = (%s)";
        conn = DatabaseOperations._get_connection()

        cur = conn.cursor()
        res = cur.execute(sql, args=(blog_owner))
        if res:
            notification_deleted = {'status': 'success', 'message': 'Successfully deleted notifications'}
            success_response = Response(json.dumps(notification_deleted), status=200, content_type="application.json")
            return success_response
        else:
            delete_failed = {'status': 'fail', 'message': 'Failed to delete notifications'}
            fail_response = Response(json.dumps(delete_failed), status=200, content_type="application.json")
            return fail_response

    @staticmethod
    def count_notification(blog_owner):
        sql = "SELECT COUNT(*) FROM cs6156_middleware.notification WHERE blog_owner = (%s)";
        conn = DatabaseOperations._get_connection()

        cur = conn.cursor()
        res = cur.execute(sql, args=(blog_owner))
        result = cur.fetchone()
        if result:
            notification_counted = {'status': 'success', 'message': 'Successfully counted notifications'}
            success_response = Response(json.dumps(notification_counted), status=200, content_type="application.json")
            return success_response
        else:
            count_failed = {'status': 'fail', 'message': 'Failed to count notifications'}
            fail_response = Response(json.dumps(count_failed), status=200, content_type="application.json")
            return fail_response



    

