#POSITIONAL ARGUMENTS
def greet(name,dept):
    print(f"Hi {name}")
    print(f"Are u from {dept} Dept?")

greet("RAM","CS")
greet("CS","RAM")

#KEYWORD ARGUMENTS
def greet(name,dept):
    print(f"Hi {name}")
    print(f"Are u from {dept} Dept?")

greet(name="RAM",dept="CS") #or change position
greet(dept="CS",name="RAM")

#default arguments
def greet(name,dept="ME"):
    print(f"Hi {name}")
    print(f"Are u from {dept} Dept?")

greet("RAM") #or
greet("RAM",dept="CS")
