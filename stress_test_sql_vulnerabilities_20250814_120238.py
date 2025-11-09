#!/usr/bin/env python3
"""
SQL Injection vulnerability patterns for security testing.
"""
import sqlite3
import psycopg2
import mysql.connector


def vulnerable_select_0(user_input):
    conn = sqlite3.connect('app_0.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_0 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_0(name, email):
    conn = sqlite3.connect('app_0.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_0 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_0(user_id, field, value):
    conn = sqlite3.connect('app_0.db')
    cursor = conn.cursor()
    query = f"UPDATE users_0 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_0(condition):
    conn = sqlite3.connect('app_0.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_0 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_1(user_input):
    conn = sqlite3.connect('app_1.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_1 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_1(name, email):
    conn = sqlite3.connect('app_1.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_1 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_1(user_id, field, value):
    conn = sqlite3.connect('app_1.db')
    cursor = conn.cursor()
    query = f"UPDATE users_1 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_1(condition):
    conn = sqlite3.connect('app_1.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_1 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_2(user_input):
    conn = sqlite3.connect('app_2.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_2 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_2(name, email):
    conn = sqlite3.connect('app_2.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_2 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_2(user_id, field, value):
    conn = sqlite3.connect('app_2.db')
    cursor = conn.cursor()
    query = f"UPDATE users_2 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_2(condition):
    conn = sqlite3.connect('app_2.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_2 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_3(user_input):
    conn = sqlite3.connect('app_3.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_3 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_3(name, email):
    conn = sqlite3.connect('app_3.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_3 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_3(user_id, field, value):
    conn = sqlite3.connect('app_3.db')
    cursor = conn.cursor()
    query = f"UPDATE users_3 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_3(condition):
    conn = sqlite3.connect('app_3.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_3 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_4(user_input):
    conn = sqlite3.connect('app_4.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_4 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_4(name, email):
    conn = sqlite3.connect('app_4.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_4 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_4(user_id, field, value):
    conn = sqlite3.connect('app_4.db')
    cursor = conn.cursor()
    query = f"UPDATE users_4 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_4(condition):
    conn = sqlite3.connect('app_4.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_4 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_5(user_input):
    conn = sqlite3.connect('app_5.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_5 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_5(name, email):
    conn = sqlite3.connect('app_5.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_5 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_5(user_id, field, value):
    conn = sqlite3.connect('app_5.db')
    cursor = conn.cursor()
    query = f"UPDATE users_5 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_5(condition):
    conn = sqlite3.connect('app_5.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_5 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_6(user_input):
    conn = sqlite3.connect('app_6.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_6 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_6(name, email):
    conn = sqlite3.connect('app_6.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_6 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_6(user_id, field, value):
    conn = sqlite3.connect('app_6.db')
    cursor = conn.cursor()
    query = f"UPDATE users_6 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_6(condition):
    conn = sqlite3.connect('app_6.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_6 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_7(user_input):
    conn = sqlite3.connect('app_7.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_7 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_7(name, email):
    conn = sqlite3.connect('app_7.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_7 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_7(user_id, field, value):
    conn = sqlite3.connect('app_7.db')
    cursor = conn.cursor()
    query = f"UPDATE users_7 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_7(condition):
    conn = sqlite3.connect('app_7.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_7 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_8(user_input):
    conn = sqlite3.connect('app_8.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_8 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_8(name, email):
    conn = sqlite3.connect('app_8.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_8 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_8(user_id, field, value):
    conn = sqlite3.connect('app_8.db')
    cursor = conn.cursor()
    query = f"UPDATE users_8 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_8(condition):
    conn = sqlite3.connect('app_8.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_8 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_9(user_input):
    conn = sqlite3.connect('app_9.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_9 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_9(name, email):
    conn = sqlite3.connect('app_9.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_9 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_9(user_id, field, value):
    conn = sqlite3.connect('app_9.db')
    cursor = conn.cursor()
    query = f"UPDATE users_9 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_9(condition):
    conn = sqlite3.connect('app_9.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_9 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_10(user_input):
    conn = sqlite3.connect('app_10.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_10 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_10(name, email):
    conn = sqlite3.connect('app_10.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_10 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_10(user_id, field, value):
    conn = sqlite3.connect('app_10.db')
    cursor = conn.cursor()
    query = f"UPDATE users_10 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_10(condition):
    conn = sqlite3.connect('app_10.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_10 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_11(user_input):
    conn = sqlite3.connect('app_11.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_11 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_11(name, email):
    conn = sqlite3.connect('app_11.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_11 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_11(user_id, field, value):
    conn = sqlite3.connect('app_11.db')
    cursor = conn.cursor()
    query = f"UPDATE users_11 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_11(condition):
    conn = sqlite3.connect('app_11.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_11 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_12(user_input):
    conn = sqlite3.connect('app_12.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_12 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_12(name, email):
    conn = sqlite3.connect('app_12.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_12 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_12(user_id, field, value):
    conn = sqlite3.connect('app_12.db')
    cursor = conn.cursor()
    query = f"UPDATE users_12 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_12(condition):
    conn = sqlite3.connect('app_12.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_12 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_13(user_input):
    conn = sqlite3.connect('app_13.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_13 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_13(name, email):
    conn = sqlite3.connect('app_13.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_13 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_13(user_id, field, value):
    conn = sqlite3.connect('app_13.db')
    cursor = conn.cursor()
    query = f"UPDATE users_13 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_13(condition):
    conn = sqlite3.connect('app_13.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_13 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_14(user_input):
    conn = sqlite3.connect('app_14.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_14 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_14(name, email):
    conn = sqlite3.connect('app_14.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_14 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_14(user_id, field, value):
    conn = sqlite3.connect('app_14.db')
    cursor = conn.cursor()
    query = f"UPDATE users_14 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_14(condition):
    conn = sqlite3.connect('app_14.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_14 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_15(user_input):
    conn = sqlite3.connect('app_15.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_15 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_15(name, email):
    conn = sqlite3.connect('app_15.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_15 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_15(user_id, field, value):
    conn = sqlite3.connect('app_15.db')
    cursor = conn.cursor()
    query = f"UPDATE users_15 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_15(condition):
    conn = sqlite3.connect('app_15.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_15 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_16(user_input):
    conn = sqlite3.connect('app_16.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_16 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_16(name, email):
    conn = sqlite3.connect('app_16.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_16 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_16(user_id, field, value):
    conn = sqlite3.connect('app_16.db')
    cursor = conn.cursor()
    query = f"UPDATE users_16 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_16(condition):
    conn = sqlite3.connect('app_16.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_16 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_17(user_input):
    conn = sqlite3.connect('app_17.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_17 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_17(name, email):
    conn = sqlite3.connect('app_17.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_17 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_17(user_id, field, value):
    conn = sqlite3.connect('app_17.db')
    cursor = conn.cursor()
    query = f"UPDATE users_17 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_17(condition):
    conn = sqlite3.connect('app_17.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_17 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_18(user_input):
    conn = sqlite3.connect('app_18.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_18 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_18(name, email):
    conn = sqlite3.connect('app_18.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_18 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_18(user_id, field, value):
    conn = sqlite3.connect('app_18.db')
    cursor = conn.cursor()
    query = f"UPDATE users_18 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_18(condition):
    conn = sqlite3.connect('app_18.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_18 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_19(user_input):
    conn = sqlite3.connect('app_19.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_19 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_19(name, email):
    conn = sqlite3.connect('app_19.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_19 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_19(user_id, field, value):
    conn = sqlite3.connect('app_19.db')
    cursor = conn.cursor()
    query = f"UPDATE users_19 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_19(condition):
    conn = sqlite3.connect('app_19.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_19 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_20(user_input):
    conn = sqlite3.connect('app_20.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_20 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_20(name, email):
    conn = sqlite3.connect('app_20.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_20 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_20(user_id, field, value):
    conn = sqlite3.connect('app_20.db')
    cursor = conn.cursor()
    query = f"UPDATE users_20 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_20(condition):
    conn = sqlite3.connect('app_20.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_20 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_21(user_input):
    conn = sqlite3.connect('app_21.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_21 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_21(name, email):
    conn = sqlite3.connect('app_21.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_21 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_21(user_id, field, value):
    conn = sqlite3.connect('app_21.db')
    cursor = conn.cursor()
    query = f"UPDATE users_21 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_21(condition):
    conn = sqlite3.connect('app_21.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_21 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_22(user_input):
    conn = sqlite3.connect('app_22.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_22 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_22(name, email):
    conn = sqlite3.connect('app_22.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_22 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_22(user_id, field, value):
    conn = sqlite3.connect('app_22.db')
    cursor = conn.cursor()
    query = f"UPDATE users_22 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_22(condition):
    conn = sqlite3.connect('app_22.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_22 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_23(user_input):
    conn = sqlite3.connect('app_23.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_23 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_23(name, email):
    conn = sqlite3.connect('app_23.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_23 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_23(user_id, field, value):
    conn = sqlite3.connect('app_23.db')
    cursor = conn.cursor()
    query = f"UPDATE users_23 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_23(condition):
    conn = sqlite3.connect('app_23.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_23 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_24(user_input):
    conn = sqlite3.connect('app_24.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_24 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_24(name, email):
    conn = sqlite3.connect('app_24.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_24 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_24(user_id, field, value):
    conn = sqlite3.connect('app_24.db')
    cursor = conn.cursor()
    query = f"UPDATE users_24 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_24(condition):
    conn = sqlite3.connect('app_24.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_24 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_25(user_input):
    conn = sqlite3.connect('app_25.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_25 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_25(name, email):
    conn = sqlite3.connect('app_25.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_25 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_25(user_id, field, value):
    conn = sqlite3.connect('app_25.db')
    cursor = conn.cursor()
    query = f"UPDATE users_25 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_25(condition):
    conn = sqlite3.connect('app_25.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_25 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_26(user_input):
    conn = sqlite3.connect('app_26.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_26 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_26(name, email):
    conn = sqlite3.connect('app_26.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_26 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_26(user_id, field, value):
    conn = sqlite3.connect('app_26.db')
    cursor = conn.cursor()
    query = f"UPDATE users_26 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_26(condition):
    conn = sqlite3.connect('app_26.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_26 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_27(user_input):
    conn = sqlite3.connect('app_27.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_27 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_27(name, email):
    conn = sqlite3.connect('app_27.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_27 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_27(user_id, field, value):
    conn = sqlite3.connect('app_27.db')
    cursor = conn.cursor()
    query = f"UPDATE users_27 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_27(condition):
    conn = sqlite3.connect('app_27.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_27 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_28(user_input):
    conn = sqlite3.connect('app_28.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_28 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_28(name, email):
    conn = sqlite3.connect('app_28.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_28 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_28(user_id, field, value):
    conn = sqlite3.connect('app_28.db')
    cursor = conn.cursor()
    query = f"UPDATE users_28 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_28(condition):
    conn = sqlite3.connect('app_28.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_28 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_29(user_input):
    conn = sqlite3.connect('app_29.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_29 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_29(name, email):
    conn = sqlite3.connect('app_29.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_29 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_29(user_id, field, value):
    conn = sqlite3.connect('app_29.db')
    cursor = conn.cursor()
    query = f"UPDATE users_29 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_29(condition):
    conn = sqlite3.connect('app_29.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_29 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_30(user_input):
    conn = sqlite3.connect('app_30.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_30 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_30(name, email):
    conn = sqlite3.connect('app_30.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_30 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_30(user_id, field, value):
    conn = sqlite3.connect('app_30.db')
    cursor = conn.cursor()
    query = f"UPDATE users_30 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_30(condition):
    conn = sqlite3.connect('app_30.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_30 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_31(user_input):
    conn = sqlite3.connect('app_31.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_31 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_31(name, email):
    conn = sqlite3.connect('app_31.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_31 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_31(user_id, field, value):
    conn = sqlite3.connect('app_31.db')
    cursor = conn.cursor()
    query = f"UPDATE users_31 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_31(condition):
    conn = sqlite3.connect('app_31.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_31 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_32(user_input):
    conn = sqlite3.connect('app_32.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_32 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_32(name, email):
    conn = sqlite3.connect('app_32.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_32 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_32(user_id, field, value):
    conn = sqlite3.connect('app_32.db')
    cursor = conn.cursor()
    query = f"UPDATE users_32 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_32(condition):
    conn = sqlite3.connect('app_32.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_32 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_33(user_input):
    conn = sqlite3.connect('app_33.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_33 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_33(name, email):
    conn = sqlite3.connect('app_33.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_33 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_33(user_id, field, value):
    conn = sqlite3.connect('app_33.db')
    cursor = conn.cursor()
    query = f"UPDATE users_33 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_33(condition):
    conn = sqlite3.connect('app_33.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_33 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_34(user_input):
    conn = sqlite3.connect('app_34.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_34 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_34(name, email):
    conn = sqlite3.connect('app_34.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_34 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_34(user_id, field, value):
    conn = sqlite3.connect('app_34.db')
    cursor = conn.cursor()
    query = f"UPDATE users_34 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_34(condition):
    conn = sqlite3.connect('app_34.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_34 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_35(user_input):
    conn = sqlite3.connect('app_35.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_35 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_35(name, email):
    conn = sqlite3.connect('app_35.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_35 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_35(user_id, field, value):
    conn = sqlite3.connect('app_35.db')
    cursor = conn.cursor()
    query = f"UPDATE users_35 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_35(condition):
    conn = sqlite3.connect('app_35.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_35 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_36(user_input):
    conn = sqlite3.connect('app_36.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_36 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_36(name, email):
    conn = sqlite3.connect('app_36.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_36 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_36(user_id, field, value):
    conn = sqlite3.connect('app_36.db')
    cursor = conn.cursor()
    query = f"UPDATE users_36 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_36(condition):
    conn = sqlite3.connect('app_36.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_36 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_37(user_input):
    conn = sqlite3.connect('app_37.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_37 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_37(name, email):
    conn = sqlite3.connect('app_37.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_37 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_37(user_id, field, value):
    conn = sqlite3.connect('app_37.db')
    cursor = conn.cursor()
    query = f"UPDATE users_37 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_37(condition):
    conn = sqlite3.connect('app_37.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_37 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_38(user_input):
    conn = sqlite3.connect('app_38.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_38 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_38(name, email):
    conn = sqlite3.connect('app_38.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_38 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_38(user_id, field, value):
    conn = sqlite3.connect('app_38.db')
    cursor = conn.cursor()
    query = f"UPDATE users_38 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_38(condition):
    conn = sqlite3.connect('app_38.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_38 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_39(user_input):
    conn = sqlite3.connect('app_39.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_39 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_39(name, email):
    conn = sqlite3.connect('app_39.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_39 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_39(user_id, field, value):
    conn = sqlite3.connect('app_39.db')
    cursor = conn.cursor()
    query = f"UPDATE users_39 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_39(condition):
    conn = sqlite3.connect('app_39.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_39 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_40(user_input):
    conn = sqlite3.connect('app_40.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_40 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_40(name, email):
    conn = sqlite3.connect('app_40.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_40 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_40(user_id, field, value):
    conn = sqlite3.connect('app_40.db')
    cursor = conn.cursor()
    query = f"UPDATE users_40 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_40(condition):
    conn = sqlite3.connect('app_40.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_40 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_41(user_input):
    conn = sqlite3.connect('app_41.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_41 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_41(name, email):
    conn = sqlite3.connect('app_41.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_41 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_41(user_id, field, value):
    conn = sqlite3.connect('app_41.db')
    cursor = conn.cursor()
    query = f"UPDATE users_41 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_41(condition):
    conn = sqlite3.connect('app_41.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_41 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_42(user_input):
    conn = sqlite3.connect('app_42.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_42 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_42(name, email):
    conn = sqlite3.connect('app_42.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_42 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_42(user_id, field, value):
    conn = sqlite3.connect('app_42.db')
    cursor = conn.cursor()
    query = f"UPDATE users_42 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_42(condition):
    conn = sqlite3.connect('app_42.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_42 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_43(user_input):
    conn = sqlite3.connect('app_43.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_43 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_43(name, email):
    conn = sqlite3.connect('app_43.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_43 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_43(user_id, field, value):
    conn = sqlite3.connect('app_43.db')
    cursor = conn.cursor()
    query = f"UPDATE users_43 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_43(condition):
    conn = sqlite3.connect('app_43.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_43 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_44(user_input):
    conn = sqlite3.connect('app_44.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_44 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_44(name, email):
    conn = sqlite3.connect('app_44.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_44 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_44(user_id, field, value):
    conn = sqlite3.connect('app_44.db')
    cursor = conn.cursor()
    query = f"UPDATE users_44 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_44(condition):
    conn = sqlite3.connect('app_44.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_44 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_45(user_input):
    conn = sqlite3.connect('app_45.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_45 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_45(name, email):
    conn = sqlite3.connect('app_45.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_45 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_45(user_id, field, value):
    conn = sqlite3.connect('app_45.db')
    cursor = conn.cursor()
    query = f"UPDATE users_45 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_45(condition):
    conn = sqlite3.connect('app_45.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_45 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_46(user_input):
    conn = sqlite3.connect('app_46.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_46 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_46(name, email):
    conn = sqlite3.connect('app_46.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_46 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_46(user_id, field, value):
    conn = sqlite3.connect('app_46.db')
    cursor = conn.cursor()
    query = f"UPDATE users_46 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_46(condition):
    conn = sqlite3.connect('app_46.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_46 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_47(user_input):
    conn = sqlite3.connect('app_47.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_47 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_47(name, email):
    conn = sqlite3.connect('app_47.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_47 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_47(user_id, field, value):
    conn = sqlite3.connect('app_47.db')
    cursor = conn.cursor()
    query = f"UPDATE users_47 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_47(condition):
    conn = sqlite3.connect('app_47.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_47 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_48(user_input):
    conn = sqlite3.connect('app_48.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_48 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_48(name, email):
    conn = sqlite3.connect('app_48.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_48 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_48(user_id, field, value):
    conn = sqlite3.connect('app_48.db')
    cursor = conn.cursor()
    query = f"UPDATE users_48 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_48(condition):
    conn = sqlite3.connect('app_48.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_48 WHERE {condition}"
    cursor.execute(query)
    conn.commit()

def vulnerable_select_49(user_input):
    conn = sqlite3.connect('app_49.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM table_49 WHERE column = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_insert_49(name, email):
    conn = sqlite3.connect('app_49.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users_49 (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(query)
    conn.commit()

def vulnerable_update_49(user_id, field, value):
    conn = sqlite3.connect('app_49.db')
    cursor = conn.cursor()
    query = f"UPDATE users_49 SET {field} = '{value}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def vulnerable_delete_49(condition):
    conn = sqlite3.connect('app_49.db')
    cursor = conn.cursor()
    query = f"DELETE FROM users_49 WHERE {condition}"
    cursor.execute(query)
    conn.commit()
