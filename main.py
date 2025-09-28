from tabulate import tabulate   # pip install tabulate

class SkillMatrix:
    def _init_(self):
        # Employee data: { "name": {"department": dept, "age": age, "skills": {skill: rating}} }
        self.employees = {}

    # ---------------- CRUD ----------------
    def add_employee(self):
        name = input("Enter employee name: ").strip()
        if name in self.employees:
            print(f"{name} already exists!")
            return
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Invalid age! Defaulting to 0.")
            age = 0
        dept = input("Enter department: ").strip()
        self.employees[name] = {"department": dept, "age": age, "skills": {}}
        print(f"Employee '{name}' added successfully.")

    def edit_employee(self):
        name = input("Enter employee name to edit: ").strip()
        if name not in self.employees:
            print("Employee not found!")
            return

        emp_data = self.employees[name]
        print("\nPress Enter to keep current value.")

        new_name = input(f"New name [{name}]: ").strip()
        if new_name:
            self.employees[new_name] = self.employees.pop(name)
            name = new_name

        new_age = input(f"New age [{emp_data.get('age', '-')}] : ").strip()
        if new_age.isdigit():
            self.employees[name]["age"] = int(new_age)

        new_dept = input(f"New department [{emp_data['department']}] : ").strip()
        if new_dept:
            self.employees[name]["department"] = new_dept

        print("Employee details updated successfully.")

    def delete_employee(self):
        name = input("Enter employee name to delete: ").strip()
        if name in self.employees:
            del self.employees[name]
            print(f"Employee '{name}' deleted successfully.")
        else:
            print("Employee not found!")

    def add_or_update_skill(self):
        name = input("Enter employee name: ").strip()
        if name not in self.employees:
            print("Employee not found!")
            return
        skill = input("Enter skill: ").strip()
        try:
            rating = int(input("Enter rating (1-5): "))
            if 1 <= rating <= 5:
                self.employees[name]["skills"][skill] = rating
                print(f"Skill '{skill}' updated for {name}.")
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Invalid rating! Enter a number (1-5).")

    def delete_skill(self):
        name = input("Enter employee name: ").strip()
        if name not in self.employees:
            print("Employee not found!")
            return
        skill = input("Enter skill to delete: ").strip()
        if skill in self.employees[name]["skills"]:
            del self.employees[name]["skills"][skill]
            print(f"Skill '{skill}' deleted for {name}.")
        else:
            print(f"{name} does not have the skill '{skill}'.")

    # ---------------- View Matrix ----------------
    def view_matrix(self):
        if not self.employees:
            print("No employees added yet.")
            return

        headers = ["Employee", "Age", "Department", "Skill", "Rating"]
        table = []

        for emp, data in self.employees.items():
            if data["skills"]:
                for skill, rating in data["skills"].items():
                    row = [emp, data.get("age", "-"), data["department"], skill, rating]
                    table.append(row)
            else:
                row = [emp, data.get("age", "-"), data["department"], "No skills", "-"]
                table.append(row)

        print("\nEmployee Skill Matrix:\n")
        print(tabulate(table, headers=headers, tablefmt="grid"))

    # ---------------- Analysis ----------------
    def find_expert_skills(self):
        experts = {}
        for emp, data in self.employees.items():
            for skill, rating in data["skills"].items():
                if rating == 5:
                    experts.setdefault(skill, []).append(emp)
        if not experts:
            print("No experts found yet.")
        else:
            print("\nExpert Skills:")
            for skill, emps in experts.items():
                print(f"Skill: {skill} → Experts: {', '.join(emps)}")

    def find_experts_in_skill(self):
        skill = input("Enter skill to search experts for: ").strip()
        experts = [emp for emp, data in self.employees.items() if data["skills"].get(skill, 0) >= 4]
        if experts:
            print(f"Employees expert in {skill}: {', '.join(experts)}")
        else:
            print(f"No employees found with expertise in {skill}.")

    def generate_skill_gap(self):
        name = input("Enter employee name: ").strip()
        if name not in self.employees:
            print("Employee not found!")
            return
        # Example required skills
        required = {"Python": 4, "Java": 4, "Communication": 4}
        emp_skills = self.employees[name]["skills"]
        table = []
        for skill, req_level in required.items():
            emp_level = emp_skills.get(skill, 0)
            if emp_level < req_level:
                table.append([skill, req_level, emp_level])
        if table:
            print(f"\nSkill Gap for {name}:")
            print(tabulate(table, headers=["Skill", "Required", "Has"], tablefmt="grid"))
        else:
            print(f"{name} meets all required skills.")

    def identify_department_gaps(self):
        dept = input("Enter department: ").strip()
        dept_emps = {emp: data for emp, data in self.employees.items() if data["department"] == dept}
        if not dept_emps:
            print("No employees in this department.")
            return
        required = {"Python": 4, "Java": 4, "Communication": 4}
        table = []
        for emp, data in dept_emps.items():
            for skill, req_level in required.items():
                emp_level = data["skills"].get(skill, 0)
                if emp_level < req_level:
                    table.append([emp, skill, req_level, emp_level])
        if table:
            print(f"\nSkill Gaps in {dept} Department:")
            print(tabulate(table, headers=["Employee", "Skill", "Required", "Has"], tablefmt="grid"))
        else:
            print(f"All employees in {dept} department meet the required skills.")

    # ---------------- Main Loop ----------------
    def run(self):
        while True:
            print("\n=== Employee Skill Matrix ===")
            print("1. Add Employee")
            print("2. Edit Employee Details")
            print("3. Add/Update Skill")
            print("4. Delete Employee")
            print("5. Delete Skill")
            print("6. View Matrix")
            print("7. Find Expert Skills")
            print("8. Find Employees Expert in a Particular Skill")
            print("9. Generate Skill Gap for an Employee")
            print("10. Identify Skill Gaps in a Department")
            print("11. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.edit_employee()
            elif choice == "3":
                self.add_or_update_skill()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                self.delete_skill()
            elif choice == "6":
                self.view_matrix()
            elif choice == "7":
                self.find_expert_skills()
            elif choice == "8":
                self.find_experts_in_skill()
            elif choice == "9":
                self.generate_skill_gap()
            elif choice == "10":
                self.identify_department_gaps()
            elif choice == "11":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice! Try again.")


# ----------------- MAIN -----------------
if _name_ == "_main_":
    sm = SkillMatrix()
    sm.run()
