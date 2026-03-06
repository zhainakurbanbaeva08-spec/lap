import csv
data=[
    ['name','department','salary'],
    ['Ali','IT',500000],
    ['Dana','HR',300000],
    ['Arman','IT',600000],
    ['Aruzhan','Marketing',400000],
    ['Dias','IT',450000]


]
employees=[]
with open("employees.csv", "w", encoding="utf-8", newline="") as f:
    writer=csv.writer(f)
    writer.writerows(data)



with open("employees.csv", "r", encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        employees.append({
            "name":row["name"],
            "department":row["department"],
            "salary":int(row["salary"])
        })

average_salary=sum(emp["salary"] for emp in employees)/len(employees)
top_employee=max(employees, key=lambda x: x["salary"])
high_salary_employees=[emp for emp in employees if emp["salary"]>average_salary]


print("Средняя зарплата:", average_salary)
print("Самый высокооплачиваемый:", top_employee["name"])
print("Сотрудники выше средней:", [emp["name"] for emp in high_salary_employees])