class Person:
    """Represents a human being with a name and age."""

    species = "Human"

    def __init__(self, name: str, age: int):
        """
        Initialize a Person.

        Args:
            name (str): The person's name.
            age (int): The person's age in years.
        """
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age!r})"

    def __str__(self) -> str:
        return f"{self.name}, age {self.age}"

    def greet(self) -> str:
        """Return a greeting message."""
        return f"Hello, I'm {self.name} and I'm {self.age}."


class Employee(Person):
    """Represents an employee, extending Person with position and ID."""

    num_employees: int = 0

    def __init__(
        self, name: str, age: int, position: str, employee_id: str, salary: float = 0.0
    ):
        """
        Initialize an Employee.

        Args:
            name (str): The person's name.
            age (int): The person's age in years.
            position (str): The person's role in the company.
            employee_id (str): Unique identifier for the employee.
            salary (float): Month income for employee
        """
        super().__init__(name, age)
        self.position = position
        self.employee_id = employee_id
        self._salary = 0.0
        self.salary = salary
        type(self).num_employees += 1

    @property
    def salary(self):
        """
        Get the employee's salary.
        """
        return self._salary

    @salary.setter
    def salary(self, value: float):
        """
        Set the employee's salary, enforcing non-negative
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = float(value)

    def greet(self) -> str:
        """Return a greeting message."""
        return (
            f"{super().greet()} I work as a {self.position}"
            f" (ID: {self.employee_id})."
        )

    @classmethod
    def get_headcount(cls) -> int:
        """
        Returns the number of employees
        """
        return cls.num_employees

    def annual_raise(self, pct: float):
        """Increase salary by a percentage (e.g., 0.05 for 5%)."""
        if pct < 0:
            raise ValueError("Raise percentage must be non-negative")
        self._salary *= 1 + pct


class Manager(Employee):
    """
    Represents a manager who gets an additional raise bonus
    """

    def __init__(
        self,
        name: str,
        age: int,
        position: str,
        employee_id: str,
        salary: float = 0.0,
        bonus_pct: float = 0.0,
    ):
        """
        Initialize Manager with salary and bonus percentage.
        Args:
            bonus_pct (float): Additional raise bonus(e.g. 0.02 for +2%)
        """
        super().__init__(name, age, position, employee_id, salary)

        if bonus_pct < 0:
            raise ValueError("Bonus percentage must be non-negative")
        self.bonus_pct = bonus_pct

    def annual_raise(self, pct: float):
        """
        Increase salary by base pct + bonus_pct.
        Overrides Employee to add manager bonus.
        """
        total_pct = pct + self.bonus_pct
        super().annual_raise(total_pct)


def test_manager_raise():
    mgr = Manager("Lucía", 40, "lead", "M1001", salary=6000, bonus_pct=0.02)
    mgr.annual_raise(0.05)  # should apply 5% + 2% = 7%
    expected_salary = 6000 * 1.07
    assert abs(mgr.salary - expected_salary) < 1e-6

    try:
        Manager("Bad", 50, "lead", "M1002", salary=5000, bonus_pct=-0.01)
    except ValueError as e:
        assert str(e) == "Bonus percentage must be non-negative"
    else:
        raise AssertionError("Negative bonus_pct should fail")


def main():
    try:
        test_manager_raise()
    except TypeError as e:
        print(f"Error in some property: {e}")
    except ValueError as e:
        print(f"Salary cannot be negative: {e}")
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
