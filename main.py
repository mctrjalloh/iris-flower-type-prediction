from model.api import use_model
import numpy as np

iris_model = use_model()

print("Give the four measurements of the flower: ")

m1 = input("Measure 1: ")
m2 = input("Measure 2: ")
m3 = input("Measure 3: ")
m4 = input("Measure 4: ")

output = iris_model(m1, m2, m3, m4)

print("This is an " + output + " flower!")
