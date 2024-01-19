import psycopg2
import logging
import datetime
import uuid
from typing import UUID

con: psycopg2.extensions.connection

def connectDatabase(database, user, password, host, port) -> psycopg2.extensions.connection:
    try:
        con = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )

        return con
    except psycopg2.Error as e:
        print(f"Error connecting with the database")
        return e
    
def checkUser(userId:int) -> bool:
    try:
        con = connectDatabase("auroradb", "aurora", "aurora123", "localhost", "5432")
        cursor = con.cursor()
        query = 'SELECT user_id FROM "auroraAI"."user" WHERE user_id = %s'
        cursor.execute(query, (userId,))
        result = cursor.fetchall()
        if len(result) == 0:
            return False
        else:
            return True
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return False

    finally:
        if con:
            cursor.close()
            con.close()


def createUser (userId:int, name:str, cellphone_number:str) :
    currentDate = datetime.datetime.now()
    try:
        con = connectDatabase("auroradb", "aurora", "aurora123", "localhost", "5432")
        cursor = con.cursor()
        insertQuery = '''
                                INSERT INTO "auroraAI"."user"
                                            (user_id, name, cellphone_number, created_at)
                                            VALUES(%s, %s, %s, %s)
                                '''
        values = (userId, name, cellphone_number, currentDate)
        cursor.execute(insertQuery, values)
        con.commit()
        count = cursor.rowcount()
        message = f"[DATABASE] {count} Row(s) updated, with these info: user_id: {userId}, name: {name}, cellphone_number: {cellphone_number} and created_at: {currentDate}"
        logging.info(message)
        return None
    except Exception as e:
        logging.error(f"[DATABASE] An error ocurred while inserting an user on database, user_id: {userId}, name: {name}, cellphone_number: {cellphone_number} and created_at: {currentDate}")


def addMessages(chat_id: UUID, message_id:  UUID, body_message: str, user_id: int):
    currentDate = datetime.datetime.now()
    try:
        con = connectDatabase("auroradb", "aurora", "aurora123", "localhost", "5432")
        cursor = con.cursor()
        insertQuery = '''
                                INSERT INTO "auroraAI"."user"
                                    (chat_id, message_id, body_message, user_id, message_date)
                                    VALUES(%s, %s, %s, %s, %s)
                                '''
        values = (chat_id, message_id, body_message, user_id, currentDate)
        cursor.execute(insertQuery, values)
        con.commit()
        message = f"[DATABASE] A successful message inserted on Database chat_id: {chat_id}, user_id: {user_id},message_id: {message_id}"
        logging.info(message)
        return None
    except Exception as e:
        logging.error(f"[DATABASE] An error occured while was inserting a message in the database. chat_id: {chat_id}, user_id: {user_id},message_id: {message_id} ")

