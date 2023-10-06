class PythonDev:
    ''' This is the docstrings for the PythonDev class  '''''

    def __init__(self, age=18, nationality="Nicaraguense"):
        self.age = age
        self.nationality = nationality

    def greet(self):
        print(f"Nationality: {self.nationality}.")
        print(f"Current age: {self.age} years old.")

# First, we create the instance of this class
pythonDev01 = PythonDev(39)

# Let's use the methods of this object
pythonDev01.greet()

# Create another instance passing both parameters now
pythonDev02 = PythonDev(20, "Costarricense")
pythonDev02.greet()

# We can also access your methods individually
print(f"Nationality: {pythonDev01.nationality}")
print(f"Current Age: {pythonDev01.age}")
