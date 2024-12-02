class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.team_members = []

    def add_team_member(self, employee):
        if isinstance(employee, Employee):
            self.team_members.append(employee)
            print(f"{employee.name} has been added to the team.")
        else:
            print("Only Employee instances can be added to the team.")

    def display_team(self):
        print(f"Manager: {self.name}'s Team Members:")
        if self.team_members:
            for member in self.team_members:
                member.display_info()
        else:
            print("No team members yet.")

# 예제 사용
employee1 = Employee("김대열", 50000)
employee2 = Employee("교수님", 60000)

manager = Manager("사랑해요", 80000)
manager.display_info()
manager.add_team_member(employee1)
manager.add_team_member(employee2)
manager.display_team()
