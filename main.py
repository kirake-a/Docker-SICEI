from typing import List
from fastapi import FastAPI, HTTPException
from os import environ as env
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    matricula: str

students = []


@app.get("/")
def root():
    return {"details": f"Hello, World! Secret {env['MY_VARIABLE']}"}

@app.get("/students/", response_model=List[Student])
def get_students():
    return students;

@app.post("/students/", response_model=Student)
def new_student(student: Student):
    students.append(student)
    return student

@app.put("/students/{id_student}", response_model=Student)
def edit_student(id_student: int, student: Student):
    for index in range(len(students)):
        if id_student == students[index]:
            students[index] = student
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{id_student}", response_model=Student)
def delete_student(id_student: int,):
    for index, student in enumerate(student):
        if student.id == id_student:
            del students[index]
            return student
    raise HTTPException(status_code=404, detail="Student not found")