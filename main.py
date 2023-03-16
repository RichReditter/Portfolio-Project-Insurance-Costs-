import csv  # import csv module we're going to work with

# main goal is to check who smoke more : men or women
# additionally to see the average age of smokers

male = "male"
female = "female"
insurance_info = []


def human_smokers_count(list, sex):          # count how many smokers are in the list depending on each sex
    sex_smokers = []
    total_human_smokers = 0
    for human in list:
        if human["sex"] == sex and human["smoker"] == "yes":
            total_human_smokers += 1
            sex_smokers.append(human)
    return {"total {sex} smokers".format(sex=sex): total_human_smokers, "list of {sex} smokers".format(sex=sex): sex_smokers}         # function return the dictionary
                                                                                                                                      # because i want to return two values

def define_avg_smokers_age(list):            # I'm counting the average age of smokers here
    smokers = []
    total_age = 0
    for person in list:
        if person["smoker"] == "yes":
            total_age += int(person["age"])           # sum of all the persons' ages
            smokers.append(person)                    # list of smokers overall (not depending on sex)
    avg_smokers_age = total_age / len(smokers)
    return avg_smokers_age


with open("insurance.csv") as insurance_csv:          # open the file where all the insurance information is
    insurance = csv.DictReader(insurance_csv)         # i read it with the help of csv.DictReader
    for row in insurance:                             # and store it in the global variable - insurance_info
        insurance_info.append(row)

    women_smokers = human_smokers_count(insurance_info, female)[                    # here is the output and function calls for the totals
        "total {female} smokers".format(female=female)]
    men_smokers = human_smokers_count(insurance_info, male)[
        "total {male} smokers".format(male=male)]
    avg_age = round(define_avg_smokers_age(insurance_info),2)
    avg_age_men = round(define_avg_smokers_age(human_smokers_count(insurance_info, male)[
                                         "list of {male} smokers".format(male=male)]),2)
    avg_age_women = round(define_avg_smokers_age(human_smokers_count(
        insurance_info, female)["list of {female} smokers".format(female=female)]),2)

print("The number of smoking men is {men_smokers} and of smoking women is {women_smokers}".format(
    men_smokers=men_smokers, women_smokers=women_smokers))
if men_smokers > women_smokers:
    print("There are more men who smoke than a women.")
else:
    print("There are more women who smoke than a men.")

print("The average age of all the smokers is {avg_age}".format(
    avg_age=avg_age))

print("The average age of men who smoke is {avg_age_men}. Moreover as far as women are concerned - {avg_age_women}".format(
    avg_age_men=avg_age_men, avg_age_women=avg_age_women))


