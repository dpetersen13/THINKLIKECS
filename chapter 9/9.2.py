# julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")


# (name, surname, b_year, movie, m_year, profession, b_place) = julia
# print(profession)
'''
this was about unpacking tuples and asssigning values
tuples can be return as function output
'''
students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]


# for (name, subjects) in students:
#     print(name ," : ",end="")
#     for subject in subjects:
#         print(subject,",",end="") 
#     print()

for (name, subjects) in students:
    print(name, subjects)
    



