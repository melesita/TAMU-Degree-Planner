import os
from unicodedata import normalize
from urllib.request import urlopen
import random

from bs4 import BeautifulSoup

# The links to every engineering program requirements
links = "https://catalog.tamu.edu/undergraduate/engineering/aerospace/bs/@https://catalog.tamu.edu/undergraduate/engineering/biomedical/bs/@https://catalog.tamu.edu/undergraduate/engineering/chemical/bs/@https://catalog.tamu.edu/undergraduate/engineering/civil-environmental/bs-coastal-engineering-track/@https://catalog.tamu.edu/undergraduate/engineering/civil-environmental/bs-construction-engineering-management-track/@https://catalog.tamu.edu/undergraduate/engineering/civil-environmental/bs-environmental-engineering-track/@https://catalog.tamu.edu/undergraduate/engineering/civil-environmental/bs-general-civil-engineering-track/@https://catalog.tamu.edu/undergraduate/engineering/civil-environmental/bs-geotechnical-engineering-track/@https://catalog.tamu.edu/undergraduate/engineering/civil-environmental/bs-structural-engineering-track/@https://catalog.tamu.edu/undergraduate/engineering/civil-environmental/bs-transportation-infrastructure-materials-engineering-track/@https://catalog.tamu.edu/undergraduate/engineering/civil-environmental/bs-water-resources-engineering-track/@https://catalog.tamu.edu/undergraduate/engineering/civil-environmental/environmental-engineering-bs/@https://catalog.tamu.edu/undergraduate/engineering/computer-science/computer-engineering-bs/@https://catalog.tamu.edu/undergraduate/engineering/computer-science/bs/@https://catalog.tamu.edu/undergraduate/engineering/computer-science/computing-ba/@https://catalog.tamu.edu/undergraduate/engineering/electrical-computer/computer-engineering-bs/@https://catalog.tamu.edu/undergraduate/engineering/electrical-computer/electrical-bs/@https://catalog.tamu.edu/undergraduate/engineering/technology-industrial-distribution/technology-electronic-systems-bs/@https://catalog.tamu.edu/undergraduate/engineering/technology-industrial-distribution/industrial-distribution-bs/@https://catalog.tamu.edu/undergraduate/engineering/technology-industrial-distribution/information-technology-service-management-ba/@https://catalog.tamu.edu/undergraduate/engineering/technology-industrial-distribution/technology-manufacturing-mechanical-bs/@https://catalog.tamu.edu/undergraduate/engineering/technology-industrial-distribution/multidisciplinary-engineering-technology-bs-electro-marine-engineering-technology-track/   @https://catalog.tamu.edu/undergraduate/engineering/technology-industrial-distribution/multidisciplinary-engineering-technology-bs-mechatronics-track/@https://catalog.tamu.edu/undergraduate/engineering/technology-industrial-distribution/multidisciplinary-engineering-technology-bs-stem-education-track/@https://catalog.tamu.edu/undergraduate/engineering/technology-industrial-distribution/technology-management-bs/@https://catalog.tamu.edu/undergraduate/engineering/industrial-systems/data-engineering-bs/@https://catalog.tamu.edu/undergraduate/engineering/industrial-systems/industrial-bs/@https://catalog.tamu.edu/undergraduate/engineering/industrial-systems/industrial-bs-occupational-safety-and-health-mph/@https://catalog.tamu.edu/undergraduate/engineering/industrial-systems/industrial-bs-finance-ms/@https://catalog.tamu.edu/undergraduate/engineering/materials-science/bs/@https://catalog.tamu.edu/undergraduate/engineering/mechanical/bs/@https://catalog.tamu.edu/undergraduate/engineering/multidisciplinary/architectural-engineering-bs-mechanical-systems-buildings-track/@https://catalog.tamu.edu/undergraduate/engineering/multidisciplinary/architectural-engineering-bs-structural-systems-buildings-track/@https://catalog.tamu.edu/undergraduate/engineering/multidisciplinary/interdisciplinary-engineering-bs/@https://catalog.tamu.edu/undergraduate/engineering/multidisciplinary/interdisciplinary-engineering-bs-occupational-safety-and-health-mph/@https://catalog.tamu.edu/undergraduate/engineering/multidisciplinary/interdisciplinary-engineering-bs-juris-doctor/@https://catalog.tamu.edu/undergraduate/engineering/nuclear/bs/@https://catalog.tamu.edu/undergraduate/engineering/ocean/ocean-engineering-bs/@https://catalog.tamu.edu/undergraduate/engineering/petroleum/bs/@https://catalog.tamu.edu/undergraduate/engineering/industrial-systems/industrial-bs-finance-ms@https://catalog.tamu.edu/undergraduate/engineering/industrial-systems/industrial-bs-occupational-safety-and-health-mph@https://catalog.tamu.edu/undergraduate/engineering/multidisciplinary/interdisciplinary-engineering-bs-occupational-safety-and-health-mph@https://catalog.tamu.edu/undergraduate/engineering/multidisciplinary/interdisciplinary-engineering-bs-juris-doctor"

print("Welcome to the Better Degree Planner!")

list = links.split("@")
num = 1

majorDict = {}

# Formats the list of majors for user output convenience
for major in list:
  slashes = major[51:].split("/")
  print(str(num) + ":", slashes[0].replace("-", " ").title(), "-", slashes[1].replace("-", " ").title().replace("Bs", "BS").replace("Ba", "BA").replace("Ms", "MS"))
  majorDict[num] = slashes[0].replace("-", " ").title() + " - " + slashes[1].replace("-", " ").title().replace("Bs", "BS").replace("Ba", "BA").replace("Ms", "MS")
  num +=1

# Gets input of user's major
print("-------------------------------------------------------------")
major = 0
while(major == 0):
  try:
    major = int(input("Please enter the number that corresponds with your major: "))
    os.system('clear')
  except:
    print()
    print("You did something wrong, please try again.")
    print("Enter a numberical input (1-43) that corresponds with your desired major: ")
    print()

print(f"You selected #{major} which is {majorDict[major]}\n")

majorword = majorDict[major]

# Getting major specific requirements
# Getting html from website 
majorlink = links.split("@")[major-1] + "#programrequirementstext"
page = urlopen(majorlink)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')

text_content = soup.get_text(separator='\n')

index = text_content.find("Semester Credit Hours")
last_index = text_content.find("Total Program Hours")

text_content = text_content[index:last_index+25]

with open("new.txt", 'w') as n:
  n.write(text_content)

# first attempt! We then realized that we did not need to webscrap
# degree = []
# while html.find('<table pdfnorepeatheader="true" class="sc_plangrid">') != -1:
#   year_idx = html.find('<table pdfnorepeatheader="true" class="sc_plangrid">')
#   start_idx = year_idx + len('<table pdfnorepeatheader="true" class="sc_plangrid">')
#   end_idx = html.find("</table>")
#   year1 = html[start_idx:end_idx]
#   yearsplit = year1.split('\"')
#   ans = []
#   for i in range(len(yearsplit)):
#     section = yearsplit[i]
#     if section[-6:] == "title=":
#       ans.append(normalize('NFKD', yearsplit[i+1]).encode('ascii','ignore').decode())
#   degree.append(ans)
#   html = html[end_idx+len("</table>"):]
# print(degree)

# print("Test: " + str(start_idx) + " " + str(end_idx) + " \n\n")
# print(year1)

AP = ""
aplist = []
apkey = "Art History | 3 | ARTS 149 | 4 | ARTS 149, ARTS 150@Biology | 3 | BIOL 113@Calculus AB | 4 | MATH 151@Calculus BC | 3 | MATH 151 | 4 | MATH 151, MATH 152@Chemistry | 3 | CHEM 119 | 4 | CHEM 107, CHEM 117, CHEM 119, CHEM 120@Chinese Language and Culture | 4 | CHIN 201, CHIN 202@Comparative Government and Politics | 3 | POLS 229@Macroeconomics | 3 | ECON 202@Microeconomics | 3 | ECON 202@English Language and Composition | 3 | ENGL 104@English Literature and Composition | 3 | ENGL 104 |4 | ENGL 104, ENGL 203@French Language | 4 | FREN 201, FREN 202@German Language | 4 | GERM 201, GERM 202@Human Geography | 3 | GEOG 201@Italian Language | 4 | ITAL 201, ITAL 202@Japanese Language | 4 | JAPN 201, JAPN 202@Physics C — Mechanics | 3 | PHYS 206@Physics C — Electricity | 3 | PHYS 207@Psychology | 3 | PSYC 107@Spanish Language | 5 | SPAN 201, SPAN 202@Spanish Literature | 3 | SPAN 202 | 5 | SPAN 202, SPAN 320@Statistics | 3 | STAT 201@US Government and Politics | 3 | POLS 206@US History | 3 | HIST 105, HIST 106"

aps = apkey.split("@")
num = 1
for ap in aps:
  temp = ap.split("|")
  print(f"{str(num).rjust(2)}: {temp[0]}")
  num +=1

print("-----------------------------------------------------------------\nYou are now entering AP scores, enter 'quit' at any time to finish entering AP scores\n")
while True:
  try:
    AP = input("Please enter the number that corresponds with the AP exams you took: ")
    if AP == 'quit':
      break
    AP = int(AP)
    score = input("Please enter the score you recieved for that exam (1-5): ")
    if score == 'quit':
      break
    score = int(score)
    if not (1<=score<=5):
      raise ValueError

    temp = aps[AP-1].split("|")
    if len(temp) == 3:
      for item in temp[2].split(", "):
        if score >= int(temp[1].strip()):
          aplist.append(item.strip()) #haha item is a slut
    elif len(temp) == 5:
      if score >= int(temp[3].strip()):
        for item in temp[4].split(", "):
          aplist.append(item.strip())
      elif score >= int(temp[1].strip()):
        for item in temp[2].split(", "):
          aplist.append(item.strip()) 
    print()
  except:
    print()
    print("You did something wrong, please try again.")
    print("Enter a numberical input (1-24) that corresponds with an AP course and a valid score (1-5): ")
    print()

os.system("clear")
print("\nThank you for entering your AP tests. You have credit for:")
stringaps = " | ".join(aplist)
print(stringaps)
#   As of this point in the code there is a variable called 'aplists'
# that is a list containing every course a person has credit for
# formatted like 'ARTS 149'

ucc = {}
uccA = {}
# process UCC and ap credits together
# make a dict w each ucc category associated w a number of credits
with open("UCC.txt", "r") as file:
  categories = file.read().split("\n\n")
  for cat in categories:
    lines = cat.split("\n")
    firstlines = lines[0].split(" - ")
    catName = firstlines[0]
    ucc[catName] = firstlines[1][0]
    uccA[catName] = []

    for i in range(1, len(lines)):
      line = lines[i].split(" ")
      if (line[0] + " " + line[1]) in aplist:
        credleftold = int(ucc[catName][0])
        credsub = int(lines[i][-1])
        credleft = credleftold - credsub
        ucc[catName] = str(credleft)
      else:
        uccA[catName].append(line[0] + " " + line[1] + ", " + line[-1] + " credit hours")

uccForGPT = []
for keys,values in ucc.items():
  value = values
  if int(values) < 0:
    value = 0
  uccForGPT.append(f"{value} more credit hours for {keys}")

uccForGPT = "You need:\n" + ",\n".join(uccForGPT)
print()
print(uccForGPT)
print("\nFor your degree plan, we recommend you take the following courses:")

#This is where we would use the anex.us data if we had more time, so instead we'll use random numbers

for keys,values in ucc.items():
  value = int(values)
  while value > 0:
    rand = random.randint(0,len(uccA[keys]))
    print(f"For the {keys} category we reccomend {uccA[keys][rand]}")
    value -= 3
    del uccA[keys][rand]