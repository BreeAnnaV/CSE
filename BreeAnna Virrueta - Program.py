class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, job):
        super(Employee, self).__init__(name, job)
        self.job = job

    def do_job(self):
        print("%s starts working." % self.name)


test_employee = Employee('bob', 'programmer')
test_employee.work()
test_employee.do_job()


class Programmer(Employee):
    def __init__(self, name, computer):
        super(Programmer, self).__init__(name, computer)
        self.computer = computer

    def program_website(self):
        print("%s codes a website." % self.name)


test_programmer = Programmer('bob', 'programmer')
test_programmer.program_website()
