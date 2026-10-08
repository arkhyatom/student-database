import sqlite3

conn = sqlite3.connect('school.db')  # connect to database

cursor=conn.cursor() # create cursor 

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        grade INTEGER        
    )                             
''')
# Insert students

students = [
    ('Alice', 18, 85),
    ('Bob', 17, 72),
    ('Charlie', 18, 91),
    ('David', 19, 64),
    ('Emma', 17, 88)
]
cursor.execute("SELECT COUNT(*) FROM students ")
count=cursor.fetchone()[0]

if count == 0:
    cursor.executemany(
        'INSERT INTO students (name, age, grade) VALUES (?, ?, ?)',
        students
    )
    conn.commit()
    print("5 students inserted")
else:
    print(f" Data already exists ({count} students). Skipping insert")
    
    
# view all students 
def view_all_students():
    cursor.execute('SELECT * FROM students')
    rows=cursor.fetchall()

    print("\n---All students--")
    for row in rows:
        print(f"{row[0]} - {row[1]} - Age:{row[2]} - grade:{row[3]}")
    
    
# finding passing students 
def view_passing_students():
    print("\n--Passing Students--")
    cursor.execute('SELECT name, grade FROM students WHERE grade >= 70')
    passed=cursor.fetchall()

    for student in passed:
        print(f"{student[0]} - {student[1]}")



# Calculate average grade
def show_average_grade():
    print(f"\n--Average Grade--")
    cursor.execute('SELECT AVG(grade) FROM students')

    average=cursor.fetchone()[0]
    print(f"Average grade: {average}")
    
    
    
# Add srudent
def add_student():
    name=input("Enter your name: ")
    age=int(input("Enter your Age: "))
    grade=int(input("Enter your grade: "))
    
    cursor.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)',
    (name, age, grade))
    
    conn.commit()
    print(" Successfully Inserted")
    
    
# search student
def search_student():
    text=input("Enter name : ")
    cursor.execute('SELECT * FROM students WHERE name = ?', (text,))
    searchedstudent=cursor.fetchone()
    if searchedstudent is None:
        print("Student is not found")
    else:
        print(f"ID : {searchedstudent[0]} - Name : {searchedstudent[1]} - Age: {searchedstudent[2]} - Grade: {searchedstudent[3]}")
    
    conn.commit()

# delete student
def delete_student():
    student_id=int(input("Enter  student ID : "))
    cursor.execute('DELETE  FROM students WHERE ID = ?', (student_id,))
    conn.commit()    
    
    if cursor.rowcount == 0:
        print("No students found")
    else:
        print("Student Delted successfully")
    
    
# Main loop


while True:
    print(f"\n--- Student Management System ---")
    choice = input("enter your choice : ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_all_students()
    elif choice == '3':
        view_passing_students()
    elif choice == '4':
        show_average_grade()
    elif choice == '5':
        search_student()
    elif choice == '6':
        delete_student()
    elif choice == '7':
        print("Good bye")
        break
        



    
conn.close() # close connection
