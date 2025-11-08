class BDUniversityCGPACalculator:
    def __init__(self):
        self.grade_scale = {
            'A+': 4.00, 'A': 3.75, 'A-': 3.50,
            'B+': 3.25, 'B': 3.00, 'B-': 2.75,
            'C+': 2.50, 'C': 2.25, 'D': 2.00, 'F': 0.00
        }
        self.semesters = {}

    def add_course(self, semester, course, grade, credit):
        if grade not in self.grade_scale:
            print(f"Invalid grade '{grade}'. Use valid letter grades.")
            return
        if credit <= 0:
            print("Credit hours must be positive number")
            return

        if semester not in self.semesters:
            self.semesters[semester] = []
        self.semesters[semester].append({'course': course, 'grade': grade, 'credit': credit})

    def calculate_semester_gpa(self, semester):
        if semester not in self.semesters:
            return None
        total_points = 0
        total_credits = 0
        for c in self.semesters[semester]:
            gp = self.grade_scale[c['grade']]
            total_points += gp * c['credit']
            total_credits += c['credit']
        if total_credits == 0:
            return 0
        return round(total_points / total_credits, 2)

    def calculate_cgpa(self):
        total_points = 0
        total_credits = 0
        for sem in self.semesters:
            for c in self.semesters[sem]:
                gp = self.grade_scale[c['grade']]
                total_points += gp * c['credit']
                total_credits += c['credit']
        if total_credits == 0:
            return 0
        return round(total_points / total_credits, 2)

    def print_summary(self):
        print("Semester Summaries:")
        for semester in self.semesters:
            gpa = self.calculate_semester_gpa(semester)
            print(f"{semester}: GPA = {gpa}")
            for c in self.semesters[semester]:
                print(f" - {c['course']} | Grade: {c['grade']} | Credits: {c['credit']}")
        print(f"\nCumulative CGPA: {self.calculate_cgpa()}")

# Example usage for Biochemistry-related courses:
calculator = BDUniversityCGPACalculator()

calculator.add_course('Semester 1', 'General Biochemistry', 'A', 3)
calculator.add_course('Semester 1', 'Organic Chemistry', 'B+', 4)
calculator.add_course('Semester 1', 'Molecular Biology', 'A-', 3)
calculator.add_course('Semester 1', 'Cell Biology', 'B', 3)

calculator.add_course('Semester 2', 'Analytical Biochemistry', 'A+', 3)
calculator.add_course('Semester 2', 'Enzymology', 'A-', 3)
calculator.add_course('Semester 2', 'Genetics', 'B+', 4)
calculator.add_course('Semester 2', 'Physical Chemistry', 'B', 2)

calculator.add_course('Semester 3', 'Immunology', 'A', 3)
calculator.add_course('Semester 3', 'Plant Biochemistry', 'A-', 3)

calculator.print_summary()

