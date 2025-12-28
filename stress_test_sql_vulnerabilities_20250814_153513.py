#!/usr/bin/env python3
"""
SQL Injection vulnerability patterns for security testing - 50 findings.
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

def vulnerable_search_0(search_term):
    conn = sqlite3.connect('app_0.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM products_0 WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    return cursor.fetchall()

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

def vulnerable_search_1(search_term):
    conn = sqlite3.connect('app_1.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM products_1 WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    return cursor.fetchall()

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

def vulnerable_search_2(search_term):
    conn = sqlite3.connect('app_2.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM products_2 WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    return cursor.fetchall()

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

def vulnerable_search_3(search_term):
    conn = sqlite3.connect('app_3.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM products_3 WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    return cursor.fetchall()

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

def vulnerable_search_4(search_term):
    conn = sqlite3.connect('app_4.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM products_4 WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    return cursor.fetchall()

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

def vulnerable_search_5(search_term):
    conn = sqlite3.connect('app_5.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM products_5 WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    return cursor.fetchall()

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

def vulnerable_search_6(search_term):
    conn = sqlite3.connect('app_6.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM products_6 WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    return cursor.fetchall()

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

def vulnerable_search_7(search_term):
    conn = sqlite3.connect('app_7.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM products_7 WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    return cursor.fetchall()

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

def vulnerable_search_8(search_term):
    conn = sqlite3.connect('app_8.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM products_8 WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    return cursor.fetchall()

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

def vulnerable_search_9(search_term):
    conn = sqlite3.connect('app_9.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM products_9 WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    return cursor.fetchall()
