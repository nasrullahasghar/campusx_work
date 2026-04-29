from sqlalchemy.orm import Session
import models,schemas

# ================ READ ================

# Read all the data of employees
def get_employees(db:Session):
    return db.query(models.Employee).all()

# Read Specific employee's data
def get_employee(db:Session , emp_id:int):
    return(
        db.query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )

# ================ CREAT ================

def create_employee(db: Session , employee: schemas.EmployeeCreate):
    # create the new employee
    db_employee = models.Employee(
        name = employee.name,
        email = employee.email
    )
    db.add(db_employee) # add the new employee to the databse
    db.commit() # Commit the new changes for confirmation
    db.refresh(db_employee) # Refresh the data to update the record

    # return the employee for output
    return db_employee

# ================ UPDATE ================

def update_employees(db: Session , emp_id: int , employee: schemas.EmployeeUpdate):
    # Filter the employee
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    # update the employee
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db.commit() # Commit the new changes for confirmation
        db.refresh(db_employee) # Refresh the data to update the record
    # return the employee for output
    return db_employee

# ================ DELETE ================

def delete_employee(db: Session, emp_id: int):
    # Filter the employee
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit() # Commit the new changes for confirmation
    # return the employee for output
    return db_employee