'''
060 - Function Packing, Unpacking Keyword Arguments 
link :  https://www.youtube.com/watch?v=pMeKs94OrxQ&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs
'''
# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

def show_skills(*skills):

  print(type(skills))

  for skill in skills:

    print(f"{skill}")

show_skills("Html", "CSS", "JS")

mySkills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "40%"
}

def show_skills(**skills):

  print(type(skills))

  for skill, value in skills.items():

    print(f"{skill} => {value}")

show_skills(**mySkills)