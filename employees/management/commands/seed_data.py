from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Employee, Department
from attendance.models import Attendance, Performance
import random

class Command(BaseCommand):
    help = 'Seed database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = ['HR', 'Engineering', 'Marketing', 'Sales']
        
        for dept in departments:
            Department.objects.create(name=dept)
        
        for _ in range(50):
            department = random.choice(Department.objects.all())
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                department=department,
            )
            Attendance.objects.create(
                employee=employee,
                date=fake.date_this_month(),
                status=random.choice(['P', 'A', 'L']),
            )
            Performance.objects.create(
                employee=employee,
                rating=random.randint(1, 5),
                review_date=fake.date_this_year(),
            )
        self.stdout.write("Database seeded!")
