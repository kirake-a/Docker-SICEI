from typing import List
from fastapi import FastAPI, HTTPException
from os import environ as env
from model.Student import Student

app = FastAPI()

students = []

@app.get("/")
def root():
    return {"details": f"Hello, World with {env['MY_VARIABLE_1']} and {env['MY_VARIABLE_2']}"}

@app.get("/students/", response_model=List[Student])
async def get_students():
    return students;

@app.post("/students/", response_model=Student)
async def new_student(student: Student):
    students.append(student)
    return student

@app.put("/students/{id_student}", response_model=Student)
async def edit_student(id_student: int, student: Student):
    for index in range(len(students)):
        if id_student == students[index].id:
            students[index] = student
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{id_student}", response_model=Student)
async def delete_student(id_student: int):
    for index, student in enumerate(students):
        if student.id == id_student:
            del students[index]
            return student
    raise HTTPException(status_code=404, detail="Student not found")