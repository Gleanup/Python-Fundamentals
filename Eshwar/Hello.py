#HW Assignment

weightlol = int(input("Enter your weight in kg: "))
heightunitlol = str(input("What is your preferred unit of height? Type F for feet and M for meters: "))

if heightunitlol == "F":
  print ("Please enter your height in feet and inches down below")
  heightinfeet = int(input("Feet: "))
  heightininches = int(input("Inches: "))

if heightunitlol == "M":
  print ("Please enter your height in meters down below")
  heightinmeters = int(input("Meters: "))

feetintometers = (heightinfeet*0.3048)
inchesintometers = (heightininches*0.0254)
america_unit_bad = (feetintometers+inchesintometers)

if heightunitlol == "F":
  bmihuh = (weightlol/america_unit_bad)

if heightunitlol == "M":
  bmihuh = (weightlol/heightinmeters)

if bmihuh < 18.5:
  print ("BMI:",bmihuh," You are underweight.")

if 18.5 <= bmihuh < 25:
  print ("BMI:",bmihuh," Your weight is average.")

if 25 <= bmihuh < 30:
  print ("BMI:",bmihuh," You are overweight.")

if 30 <= bmihuh:
  print ("BMI:",bmihuh," You are extremely overweight.")
