#!/usr/bin/env python3
"""
Stress test file with exactly 300 total security vulnerabilities for testing.
This file contains 100 vulnerable code patterns across different vulnerability types.
"""
import os
import yaml
import subprocess
import pickle
import sqlite3
import hashlib
import base64
import json
import xml.etree.ElementTree as ET


# Hardcoded secret 1
GITHUB_TOKEN_0 = "ghp_0000567890abcdefghijklmnopqrstuvwxyz123"
API_KEY_0 = "sk-0000567890abcdefghijklmnopqrstuvwxyz"
DATABASE_PASSWORD_0 = "super_secret_password_0!"
STRIPE_SECRET_0 = "sk_test_abcdefghijklmnopqrstuvwxyz000000"
JWT_SECRET_0 = "my_super_secret_jwt_key_00000"

# Hardcoded secret 2
GITHUB_TOKEN_1 = "ghp_0001567890abcdefghijklmnopqrstuvwxyz123"
API_KEY_1 = "sk-0001567890abcdefghijklmnopqrstuvwxyz"
DATABASE_PASSWORD_1 = "super_secret_password_1!"
STRIPE_SECRET_1 = "sk_test_abcdefghijklmnopqrstuvwxyz000001"
JWT_SECRET_1 = "my_super_secret_jwt_key_00001"

# Hardcoded secret 3
GITHUB_TOKEN_2 = "ghp_0002567890abcdefghijklmnopqrstuvwxyz123"
API_KEY_2 = "sk-0002567890abcdefghijklmnopqrstuvwxyz"
DATABASE_PASSWORD_2 = "super_secret_password_2!"
STRIPE_SECRET_2 = "sk_test_abcdefghijklmnopqrstuvwxyz000002"
JWT_SECRET_2 = "my_super_secret_jwt_key_00002"

# Hardcoded secret 4
GITHUB_TOKEN_3 = "ghp_0003567890abcdefghijklmnopqrstuvwxyz123"
API_KEY_3 = "sk-0003567890abcdefghijklmnopqrstuvwxyz"
DATABASE_PASSWORD_3 = "super_secret_password_3!"
STRIPE_SECRET_3 = "sk_test_abcdefghijklmnopqrstuvwxyz000003"
JWT_SECRET_3 = "my_super_secret_jwt_key_00003"

# Hardcoded secret 5
GITHUB_TOKEN_4 = "ghp_0004567890abcdefghijklmnopqrstuvwxyz123"
API_KEY_4 = "sk-0004567890abcdefghijklmnopqrstuvwxyz"
DATABASE_PASSWORD_4 = "super_secret_password_4!"
STRIPE_SECRET_4 = "sk_test_abcdefghijklmnopqrstuvwxyz000004"
JWT_SECRET_4 = "my_super_secret_jwt_key_00004"



def unsafe_db_query_0(user_input):
    conn = sqlite3.connect('database_0.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_0 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_0(user_id, user_name):
    conn = sqlite3.connect('database_0.db')
    cursor = conn.cursor()
    query = f"UPDATE users_0 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_1(user_input):
    conn = sqlite3.connect('database_1.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_1 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_1(user_id, user_name):
    conn = sqlite3.connect('database_1.db')
    cursor = conn.cursor()
    query = f"UPDATE users_1 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_2(user_input):
    conn = sqlite3.connect('database_2.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_2 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_2(user_id, user_name):
    conn = sqlite3.connect('database_2.db')
    cursor = conn.cursor()
    query = f"UPDATE users_2 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_3(user_input):
    conn = sqlite3.connect('database_3.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_3 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_3(user_id, user_name):
    conn = sqlite3.connect('database_3.db')
    cursor = conn.cursor()
    query = f"UPDATE users_3 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_4(user_input):
    conn = sqlite3.connect('database_4.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_4 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_4(user_id, user_name):
    conn = sqlite3.connect('database_4.db')
    cursor = conn.cursor()
    query = f"UPDATE users_4 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_5(user_input):
    conn = sqlite3.connect('database_5.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_5 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_5(user_id, user_name):
    conn = sqlite3.connect('database_5.db')
    cursor = conn.cursor()
    query = f"UPDATE users_5 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_6(user_input):
    conn = sqlite3.connect('database_6.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_6 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_6(user_id, user_name):
    conn = sqlite3.connect('database_6.db')
    cursor = conn.cursor()
    query = f"UPDATE users_6 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_7(user_input):
    conn = sqlite3.connect('database_7.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_7 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_7(user_id, user_name):
    conn = sqlite3.connect('database_7.db')
    cursor = conn.cursor()
    query = f"UPDATE users_7 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_8(user_input):
    conn = sqlite3.connect('database_8.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_8 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_8(user_id, user_name):
    conn = sqlite3.connect('database_8.db')
    cursor = conn.cursor()
    query = f"UPDATE users_8 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_9(user_input):
    conn = sqlite3.connect('database_9.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_9 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_9(user_id, user_name):
    conn = sqlite3.connect('database_9.db')
    cursor = conn.cursor()
    query = f"UPDATE users_9 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_10(user_input):
    conn = sqlite3.connect('database_10.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_10 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_10(user_id, user_name):
    conn = sqlite3.connect('database_10.db')
    cursor = conn.cursor()
    query = f"UPDATE users_10 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_11(user_input):
    conn = sqlite3.connect('database_11.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_11 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_11(user_id, user_name):
    conn = sqlite3.connect('database_11.db')
    cursor = conn.cursor()
    query = f"UPDATE users_11 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_12(user_input):
    conn = sqlite3.connect('database_12.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_12 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_12(user_id, user_name):
    conn = sqlite3.connect('database_12.db')
    cursor = conn.cursor()
    query = f"UPDATE users_12 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_13(user_input):
    conn = sqlite3.connect('database_13.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_13 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_13(user_id, user_name):
    conn = sqlite3.connect('database_13.db')
    cursor = conn.cursor()
    query = f"UPDATE users_13 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()

def unsafe_db_query_14(user_input):
    conn = sqlite3.connect('database_14.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users_14 WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def unsafe_db_update_14(user_id, user_name):
    conn = sqlite3.connect('database_14.db')
    cursor = conn.cursor()
    query = f"UPDATE users_14 SET name = '{user_name}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()



def unsafe_system_call_0(filename):
    os.system(f"cat {filename}_0")
    subprocess.call(f"ls -la {filename}_0", shell=True)

def unsafe_system_call_1(filename):
    os.system(f"cat {filename}_1")
    subprocess.call(f"ls -la {filename}_1", shell=True)

def unsafe_system_call_2(filename):
    os.system(f"cat {filename}_2")
    subprocess.call(f"ls -la {filename}_2", shell=True)

def unsafe_system_call_3(filename):
    os.system(f"cat {filename}_3")
    subprocess.call(f"ls -la {filename}_3", shell=True)

def unsafe_system_call_4(filename):
    os.system(f"cat {filename}_4")
    subprocess.call(f"ls -la {filename}_4", shell=True)

def unsafe_system_call_5(filename):
    os.system(f"cat {filename}_5")
    subprocess.call(f"ls -la {filename}_5", shell=True)

def unsafe_system_call_6(filename):
    os.system(f"cat {filename}_6")
    subprocess.call(f"ls -la {filename}_6", shell=True)

def unsafe_system_call_7(filename):
    os.system(f"cat {filename}_7")
    subprocess.call(f"ls -la {filename}_7", shell=True)

def unsafe_system_call_8(filename):
    os.system(f"cat {filename}_8")
    subprocess.call(f"ls -la {filename}_8", shell=True)

def unsafe_system_call_9(filename):
    os.system(f"cat {filename}_9")
    subprocess.call(f"ls -la {filename}_9", shell=True)



def load_config_0(config_data):
    return yaml.load(config_data)  # Uses unsafe loader 0

def load_user_data_0(data):
    return pickle.loads(data)  # Unsafe pickle 0

def load_yaml_config_0(yaml_data):
    return yaml.unsafe_load(yaml_data)  # Explicitly unsafe 0

def load_config_1(config_data):
    return yaml.load(config_data)  # Uses unsafe loader 1

def load_user_data_1(data):
    return pickle.loads(data)  # Unsafe pickle 1

def load_yaml_config_1(yaml_data):
    return yaml.unsafe_load(yaml_data)  # Explicitly unsafe 1

def load_config_2(config_data):
    return yaml.load(config_data)  # Uses unsafe loader 2

def load_user_data_2(data):
    return pickle.loads(data)  # Unsafe pickle 2

def load_yaml_config_2(yaml_data):
    return yaml.unsafe_load(yaml_data)  # Explicitly unsafe 2

def load_config_3(config_data):
    return yaml.load(config_data)  # Uses unsafe loader 3

def load_user_data_3(data):
    return pickle.loads(data)  # Unsafe pickle 3

def load_yaml_config_3(yaml_data):
    return yaml.unsafe_load(yaml_data)  # Explicitly unsafe 3

def load_config_4(config_data):
    return yaml.load(config_data)  # Uses unsafe loader 4

def load_user_data_4(data):
    return pickle.loads(data)  # Unsafe pickle 4

def load_yaml_config_4(yaml_data):
    return yaml.unsafe_load(yaml_data)  # Explicitly unsafe 4



def read_file_0(filename):
    with open(f"/app/data_0/{filename}", 'r') as f:
        return f.read()

def read_file_1(filename):
    with open(f"/app/data_1/{filename}", 'r') as f:
        return f.read()

def read_file_2(filename):
    with open(f"/app/data_2/{filename}", 'r') as f:
        return f.read()

def read_file_3(filename):
    with open(f"/app/data_3/{filename}", 'r') as f:
        return f.read()

def read_file_4(filename):
    with open(f"/app/data_4/{filename}", 'r') as f:
        return f.read()



def weak_hash_0(password):
    return hashlib.md5(password.encode()).hexdigest()

def weak_hash_1(password):
    return hashlib.md5(password.encode()).hexdigest()

def weak_hash_2(password):
    return hashlib.md5(password.encode()).hexdigest()

def weak_hash_3(password):
    return hashlib.md5(password.encode()).hexdigest()

def weak_hash_4(password):
    return hashlib.md5(password.encode()).hexdigest()


# Additional vulnerable patterns (remaining findings to reach 100)
class VulnerableClass:
    def __init__(self):
        self.secret_key = "hardcoded_secret_key_12345"  # 1 finding
        self.api_token = "tok_abcdefghijklmnopqrstuvwxyz123456"  # 1 finding
        
    def process_xml(self, xml_data):
        # XXE vulnerability (1 finding)
        return ET.fromstring(xml_data)
    
    def execute_command(self, cmd):
        # Command injection (1 finding)
        return os.system(cmd)
    
    def load_pickle_data(self, data):
        # Unsafe deserialization (1 finding)
        return pickle.loads(data)

# More hardcoded credentials (remaining findings)
DATABASE_URL = "postgresql://admin:password123@localhost:5432/production"  # 1 finding
REDIS_PASSWORD = "redis_secret_password_456"  # 1 finding
MONGODB_URI = "mongodb://root:admin123@mongodb.example.com:27017"  # 1 finding
ELASTICSEARCH_PASSWORD = "elastic_secret_789"  # 1 finding

# Vulnerable function patterns
def vulnerable_function_pattern(user_input):
    # Multiple vulnerabilities in one function
    sql_query = f"SELECT * FROM sensitive_data WHERE id = {user_input}"  # SQL injection (1 finding)
    os.system(f"grep {user_input} /etc/passwd")  # Command injection (1 finding)
    with open(f"/tmp/{user_input}", 'r') as f:  # Path traversal (1 finding)
        return f.read()

def calculate_expression(expression):
    return eval(expression)  # Code injection (1 finding)

if __name__ == "__main__":
    print("Stress test loaded - exactly 100 findings in this file")
