from atexit import register
from multiprocessing.sharedctypes import Value
from shutil import register_unpack_format

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
    else:
        print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
    else:
        print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

for county in counties:
    print(county)    

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for county in counties_dict.values():
    print(county)

for county in counties_dict:
    print(counties_dict[county])

for key, Value in counties_dict.items():
    print(key, Value)

for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registeted voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)  

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registeted voters.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

condidate_votes = int(input("How many votes did the condidate get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
message_to_condidate = (
    f"You received {condidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}"
    f" You received {condidate_votes / total_votes * 100:.2f}% of the total votes. ")

print(message_to_condidate)  

