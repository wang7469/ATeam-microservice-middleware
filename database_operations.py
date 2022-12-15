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
        pw = "84443295412lx."
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
    def get_ownwer_id_and_blog_title(blog_id):
        sql = "SELECT OWNER_ID, blog_title FROM blogs.blog_info WHERE unique_blog_id = %s"
        conn = DatabaseOperations._get_connection()

        cur = conn.cursor()
        res = cur.execute(sql, args=(blog_id))
        blog_data = cur.fetchone()
        owner_id = blog_data['OWNER_ID']
        blog_title = blog_data['blog_title']
        return owner_id, blog_title

    @staticmethod
    def new_notification(blog_owner, comment_poster, blog_title):
        sql = "INSERT INTO cs6156_middleware.notification VALUES (%s, %s, %s)"
        conn = DatabaseOperations._get_connection()

        cur = conn.cursor()
        res = cur.execute(sql, args=(blog_owner, comment_poster, blog_title))
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
        sql = "DELETE FROM cs6156_middleware.notification WHERE blog_owner = (%s)"
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
        sql = "SELECT COUNT(*) FROM cs6156_middleware.notification WHERE blog_owner = (%s)"
        conn = DatabaseOperations._get_connection()

        cur = conn.cursor()
        res = cur.execute(sql, args=(blog_owner))
        result = cur.fetchone()["COUNT(*)"]
        return result

    @staticmethod
    def comment_poster_and_blog_title_info(blog_owner):
        sql = "SELECT comment_poster, blog_title FROM cs6156_middleware.notification WHERE blog_owner = (%s)"
        conn = DatabaseOperations._get_connection()

        cur = conn.cursor()
        res = cur.execute(sql, args=(blog_owner))
        result = cur.fetchall()
        print(result)
        if result:
            success_response = Response(json.dumps(result), status=200, content_type="application.json")
            return success_response
        else:
            count_failed = {'status': 'fail', 'message': 'Failed to get notifications'}
            fail_response = Response(json.dumps(count_failed), status=200, content_type="application.json")
            return fail_response


    
