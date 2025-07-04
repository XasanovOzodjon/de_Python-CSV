import csv

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    students = list(reader)

students.sort(key=lambda x: int(x['score']), reverse=True)

with open('rating.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'score'])
    writer.writeheader()
    writer.writerows(students)
