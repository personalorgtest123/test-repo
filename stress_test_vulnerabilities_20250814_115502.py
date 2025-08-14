#!/usr/bin/env python3
"""
Stress test file with intentional security vulnerabilities for testing.
"""
import os
import yaml
import subprocess
import pickle
import sqlite3
import hashlib

# Vulnerability 1: Hardcoded secrets
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz123"
API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz"
DATABASE_PASSWORD = "super_secret_password_123!"

# Vulnerability 2: SQL Injection
def unsafe_db_query(user_input):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

# Vulnerability 3: Command Injection
def unsafe_system_call(filename):
    os.system(f"cat {filename}")
    subprocess.call(f"ls -la {filename}", shell=True)

# Vulnerability 4: Unsafe YAML loading
def load_config(config_data):
    return yaml.load(config_data)  # Uses unsafe loader

# Vulnerability 5: Pickle deserialization
def load_user_data(data):
    return pickle.loads(data)

# Vulnerability 6: Path traversal
def read_file(filename):
    with open(f"/app/data/{filename}", 'r') as f:
        return f.read()

# Vulnerability 7: Weak cryptography
def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

# Vulnerability 8: More hardcoded secrets
STRIPE_SECRET = "sk_test_abcdefghijklmnopqrstuvwxyz123456"
JWT_SECRET = "my_super_secret_jwt_key_12345"
ENCRYPTION_KEY = "0123456789abcdef"

# Vulnerability 9: Unsafe eval
def calculate(expression):
    return eval(expression)

# Vulnerability 10: XXE vulnerability potential
def parse_xml(xml_data):
    import xml.etree.ElementTree as ET
    return ET.fromstring(xml_data)

if __name__ == "__main__":
    print("Stress test vulnerabilities loaded")
