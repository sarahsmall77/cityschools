
PyCitySchools Analysis
I have not had a chance to analyze the data yet, as I have been getting continuously stuck getting through the District Summary section. At this point, my only analysis is that I'm in over my head with this course. 
This section will be updated when I manage to work through the full analysis.

import pandas as pd
import numpy as np

#load csv files
school_data = "Resources/schools_complete.csv"
student_data = "Resources/students_complete.csv"
#read files
schools = pd.read_csv(school_data)
students = pd.read_csv(student_data)
schools.head()
students.head()


#combine data sets
school_data_complete = pd.merge(students, schools, how="left", on=["school_name", "school_name"])
school_data_complete.head()

#reference column names
school_data_complete.columns

#check for missing data
school_data_complete.count()

#calculate total schools
total_schools = len(school_data_complete["school_name"].unique())
print(total_schools)

#calculate total students
total_students = len(school_data_complete["Student ID"].unique())
print(total_students)

#before calculating total budget, need to isolate schools so getting only 1 budget per school
#create dataframe for school name and budget, eliminate duplicates

grouped_schools = school_data_complete.groupby(['school_name'])
grouped_schools.count()

total_budget = grouped_schools["budget"].sum()
total_budget.sum()

# calculate average reading score...need total divided by number of students
reading_total = grouped_schools["reading_score"].sum()
#reading_total.sum()
reading_avg = reading_total / 39170
reading_avg.sum()

# calculate average math score
math_total = grouped_schools["math_score"].sum()
#math_total.sum()
math_avg = math_total / 39170
math_avg.sum()

#calculate overall pass rate
pass_rate_total = math_avg + reading_avg
pass_rate_total.sum()
overall_pass = pass_rate_total / 2
overall_pass.sum()

# calculate percentage of students with passing math (> 70)
# number of passing students/total number of students(39170) 
total_passing_math = school_data_complete["math_score"].loc[(school_data_complete["math_score"] >= 70)].count()
total_passing_math
percent_passing_math = total_passing_math / total_students * 100
percent_passing_math

# calculate percent passing reading
total_passing_reading = school_data_complete["reading_score"].loc[(school_data_complete["reading_score"] >= 70)].count()
total_passing_reading
percent_passing_reading = total_passing_reading / total_students * 100
percent_passing_reading

# create district summary dataframe
district_summary = pd.DataFrame({"Total Schools": [total_schools], "Total Students": [total_students],
                                "Total Budget": [total_budget], "Average Math Score": [math_avg],
                                "Average Reading Score": [reading_avg], "% Passing Math": [percent_passing_math],
                                "% Passing Reading": [percent_passing_reading], 
                                "% Overall Passing Rate": [overall_pass]})
district_summary