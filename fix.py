import pymysql
from werkzeug.security import generate_password_hash
conn = pymysql.connect(
    host="localhost",
    user="labuser",
    password="labpass123",
    database="student_portal_lab_secure",
    autocommit=True
)
users = {
    "student1": "password123",
    "student2": "password123",
    "lecturer1": "password123",
    "admin1": "admin123"
}
with conn.cursor() as cur:
    for username, password in users.items():
        cur.execute(
            "UPDATE users SET password_hash=%s WHERE username=%s",
            (generate_password_hash(password), username)
        )
print("Password hashes updated successfully.")

