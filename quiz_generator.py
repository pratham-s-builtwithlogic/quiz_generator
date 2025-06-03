import mysql.connector
import random
from docx import Document

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="quiz_generator"
    )

