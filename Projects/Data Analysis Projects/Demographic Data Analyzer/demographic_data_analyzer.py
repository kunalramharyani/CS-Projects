import pandas as pd
def calculate_demographic_data(print_data=True):

    # Reading data from file
    df = pd.read_csv('adult.data.csv')  

    # Different races
    race_count = df.groupby("race")["race"].count().sort_values(ascending = False)

    # Average age of men
    average_age_men = df[df["sex"] == "Male"]["age"].mean().round(1)

    # The percentage of people who have a Bachelor's degree
    percentage_bachelors_degree = (df[df["education"] == "Bachelors"]["education"].count() / df["education"].count() * 100).round(1)

    # Percentage of people with advanced degree make salary >50K
    df2 = df[(df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")]
    higher_education_rich = (df2[df2["salary"] == ">50K"].count() / df2.count() * 100)["age"].round(1)
    
    # Percentage of people without advanced education make salary >50k
    df3 = df[(df["education"] != "Bachelors") & (df["education"] != "Masters") & (df["education"] != "Doctorate")]
    lower_education_rich = (df3[df3["salary"] == ">50K"].count() / df3.count() * 100)["age"].round(1)

    # The minimum number of hours a person works per week (hours-per-week feature)
    min_work_hours = df.min()["hours-per-week"]

    # Percentage of the people who work the minimum number of hours per week have a salary of >50K
    df4 = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = (df4[df4["salary"] == ">50K"].count() / df4.count() * 100)["age"].round(0)

    # The country has the highest percentage of people that earn >50K
    grouped_by_country_rich = df[df["salary"] == ">50K"].groupby("native-country")["native-country"].count().rename("# salary >50K by country")
    grouped_by_country = df.groupby("native-country")["native-country"].count().rename("# by country")
    grouped = pd.merge(grouped_by_country, grouped_by_country_rich, on="native-country")
    grouped["% salary >50K by country"] = (grouped["# salary >50K by country"] / grouped["# by country"] * 100).round(1) 
    grouped_sorted = grouped.sort_values(by=["% salary >50K by country"], ascending=False)

    # Country with highest percentage of rich
    highest_earning_country = grouped_sorted.iloc[0].name
    
    # Highest percentage of rich people in the country
    highest_earning_country_percentage = grouped_sorted.iloc[0]["% salary >50K by country"]

    # The most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[df["native-country"] == "India"].groupby("occupation", as_index=False).count().sort_values(by = "age", ascending = False).iloc[0]["occupation"]

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors_degree}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors_degree,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
