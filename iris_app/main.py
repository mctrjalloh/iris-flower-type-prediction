from model.api import use_model

iris_model = use_model()

print("\nGive the four measurements of the flower: \n")

m1 = input("Measure 1: ")
m2 = input("Measure 2: ")
m3 = input("Measure 3: ")
m4 = input("Measure 4: ")

print('\n')

output = iris_model(m1, m2, m3, m4)

print("\nThis is an " + output + '\n')
