# Dont-Bully 😭
### A Data-Science project aiming to analyze bullying problems in schools and perhaps find a solution that minimizes those bullying incidents and to avoid scarring those poor kids for life

This project is an implementation of our Data-Science course project, it involves choosing questions, doing the famous DS epicycle to solve each question as is. then documenting the results after each step.

### The Famous DS epicycle  🔩
![image](https://github.com/aymanreda56/Data-Science/assets/58632281/a38a69f4-2ba5-4871-933e-9bf8ae6682e8)

## Problem Definition 😟
Bullying was present for a long period of time but left unnoticed, bullying is tightly correlated with PTSD among children. 95% of patients in psych wards reported being bullied during their childhood.
Bullying is a natural societal conduct due to the different lifestyle of some minorities.
Bullying is claimed to be decreased when the patient himself understands how to deal with his different lifestyle, through therapies and life changing acts.
Bullying makes it hard for children to have healthy friendships, makes it hard for them to study and attend school or engage in social activities, raising their probability of becoming introverts or having mental disorders in their adulthood.

## Dataset Source 🐬
This dataset was collected via a Questionnaire conducted on students of different ages in Argentina in 2018.
56,981 students participated in this Questionnaire.
Questionnaire consisting of 18 direct questions, example: How many times have you been physically attacked? Do your parents understand your problems? etc.


as you know, Data-Science cycle requires stating questions...
## Questions ❓
1. How many close friends does a student have on average?
2. What's the percentage of people being cyberbullied?
3. On average, How many days does the bullied kid skip school?
4. What’s the relationship between body morph and being bullied for both genders?
5. What is  the correlation between having close friends and feeling lonely?
6. What is the relationship between physically attacked and missing class or school without permission?
7. Is being (overweight) related to cyberbullying, does it generalize to bullying at school?
8. Does bullying differ based on gender?
9. can we generalize being bullied in school, to being bullied outside school and cyberbullied?
10. Can we predict probability of bullying inside&outside of school given parent’s understanding and having certain number of friends?
11. Is a student suffering from bullying increasing the times of missing school with no permission in the future?

no one likes the boring details, let's skip to the results of our study...
# Results 👀
### In order to reduce bullying incidents, your school should:
* **Encourage students** to make friends
* **Do more sports events**; Dont let the students go overweight
* **Give Enlighting lectures**, Specifically for the parents. On how to understand children
* **DONT LET FIGHTS EVER HAPPEN**
* **Teach children how** to defend themselves

now to the boring Details 😆
which you can also find them in this [report](https://docs.google.com/document/d/1O5drmZ-L4TCDsvxNBjqH4opfhx08Oo9neyHvOxFxGi0/edit) and this [presentation](https://docs.google.com/presentation/d/1gvgdro78xpnMGE7PGveBQxFM2IuKEdKcpY4GZgWKSTY/edit#slide=id.g127f379f983_0_31)

## Preprocessing and Cleaning ⭐
* We turned a lot of categorical data into numeric
* Added new features which are a combination of others or binarized ones
* Dealt with null values by imputing mean or mode
* Resampled some unbalanced classes using SMOTE

## Questions and their answers 
## What is the Percentage of people in the population getting bullied? ⭐
![image](https://github.com/aymanreda56/Data-Science/assets/58632281/1a3de8b8-0dec-4e52-a13d-46dea3c17a2d)

From this cross-table we can see that 59.3% didn’t report any form of bullying.
Meaning that the remaining 40.7% suffer from at least one form of bullying which is a large percentage.

Students bullied inside school AND outside school = 10.7717
Meaning that HALF of the students bullied inside school, experience bullying outside school.
Bullied both is school & outside school is a large percentage of all students.

Very small number of students who don’t get bullied in school experience bullying outside school, this concludes that a student is more likely to experience different forms of bullying if he was bullied in school.

This also means that the psychological reasons for bullying a kid is in the kid himself (his personality/appearance/talking skills) not due to the school’s other students.


## How many close friends does a student have on average? ⭐
![image](https://github.com/aymanreda56/Data-Science/assets/58632281/9f1a8095-4b8b-42e0-be6d-0564c4ae72d2)

average close friends reported from bullied kids <= 1

#### Having less friends leads to feeling lonely, Leading to increased internet session time. More CyberBullying!



## What is the relationship between being physically attacked and missing school? ⭐
![image](https://github.com/aymanreda56/Data-Science/assets/58632281/d3445d1b-7443-4070-80be-9e24dde11911)

We should try to minimize fights as little as possible, so kids don’t miss school and other important days.
The variable “engaged_in_a_fight” is a binary variable if the student undergoes any form of fighting or attacking,


There is a weak correlation between engaging in a fight and missing school which was against our expectations.

Notice that physical fights correlate more to missing school than attacks. Because fights are more violent than just plain attacks.

## How many days does a student being bullied usually skip on average? ⭐

We combined between all variables of being bullied (bullied in school on past 12 months, bullied not in school in past 12 months, cyber bullied) if anyone is yes so the student suffer from bullied
And the result that there are a few student suffer from any sort of bullying


![image](https://github.com/aymanreda56/Data-Science/assets/58632281/b0e5ded9-c364-4049-8e46-da9ba221b2bb)

![image](https://github.com/aymanreda56/Data-Science/assets/58632281/8912bef4-b868-4b36-8309-643f7bdc0368)

**The average day to miss school without permission:**

![image](https://github.com/aymanreda56/Data-Science/assets/58632281/456dcb6d-5c80-4bed-9146-e7812cfc6356)

### Expectations: bullied kids miss more than one day
### Reality: only a day!
### Conclusion: there must be another hidden Variable we didn't make use of!

## What’s the relationship between body level and being bullied? ⭐
![image](https://github.com/aymanreda56/Data-Science/assets/58632281/c8c82c53-fde3-4772-9ff6-5916c7aea3c3)

unlike our expectations, body level does not contribute to more bullying, some people are just funny and loveable regardless of their physique 💝

## Can we predict that a student misses school with no permission given the number of close friends, parents understanding problems, feeling lonely and other students kind and helpful? ⭐

## Is body level related to the number of close friends? ⭐
![image](https://github.com/aymanreda56/Data-Science/assets/58632281/65b176b3-cfe1-4ca1-ab04-13084ce064ef)


## Are bullying and missing school going to increase in the future? ⭐
![image](https://github.com/aymanreda56/Data-Science/assets/58632281/4903e9f9-54b8-459e-8456-d1aaf5511b85)

from this infograph we conclude that as kids age, their probability of experiencing bullying decreases, as they become more mature and responsible.
but this does not indicate anything about bullying in the future!

## Why does bullying happen? ⭐

this question is supposed to be answered by research and field knowledge, but we conducted our usual studies whatsoever, trying to find a variable having more correlation with bullying.

![image](https://github.com/aymanreda56/Data-Science/assets/58632281/2af25797-6b35-447d-bc55-af436b9b0144)


## Does bullying differ based on gender? ⭐

![image](https://github.com/aymanreda56/Data-Science/assets/58632281/bc28a2d7-107d-410d-987e-aed3e640121c)


Females experience more bullying than males, Perhaps because males are not likely to report being bullied and bottling everything unlike girls which can talk openly about their feelings.

## Does increasing close friends Decrease being lonely? ⭐

this question was answered using a Persona hypothesis test

stat = 0.061, p-0.0001, therefore the variable "close_friends" is dependent on the variable "feeling_lonely"

#### **Yes increasing number of close friends make student doesn’t feel lonely.**





