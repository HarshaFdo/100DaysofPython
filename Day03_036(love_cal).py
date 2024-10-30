print("Welcom to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("what is their name? \n")

combined_string = name1 + name2
lower_case_name = combined_string.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e
print(f"Total = {true}" )

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e
print(f"Total = {love}" )

love_score = int(str(true) + str(love))
print(f"Your score is {love_score}")

if 10 > love_score or love_score > 90 :
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score and love_score < 50 :
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
