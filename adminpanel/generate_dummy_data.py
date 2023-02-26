import uuid
import hashlib
from faker import Faker
import mysql.connector


fake = Faker()

db = mysql.connector.connect(
    host="localhost",
    user="pranav"
)