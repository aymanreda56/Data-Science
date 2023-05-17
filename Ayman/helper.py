import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder




def CleanseData(df):
    df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df['body_level']=[1]*df.shape[0]
    df.loc[df[df['Were_underweight']=='Yes'].index,'body_level'] = 0
    df.loc[df[df['Were_overweight']=='Yes'].index,'body_level'] = 2
    df.loc[df[df['Were_obese']=='Yes'].index,'body_level'] = 3
    df.loc[df[df['Were_obese'].isnull()].index,'body_level'] = np.nan
    df['body_level'] = df['body_level'].fillna(df['body_level'].mode()[0])



    df['Bullied_on_school_property_in_past_12_months'] = df['Bullied_on_school_property_in_past_12_months'].fillna("No")
    df['Bullied_not_on_school_property_in_past_12_months'] = df['Bullied_not_on_school_property_in_past_12_months'].fillna("No")
    df['Cyber_bullied_in_past_12_months'] = df['Cyber_bullied_in_past_12_months'].fillna("No")


    df = df.drop(columns=[df.columns[0], 'Were_underweight', 'Were_overweight', 'Were_obese'])


    df['Custom_Age'] = df['Custom_Age'].replace('[a-zA-Z ]+', '', regex=True)
    df['Custom_Age'] = pd.to_numeric(df['Custom_Age'], errors='coerce')
    df.loc[df['Custom_Age'].isnull(),'Custom_Age'] = df.Custom_Age.mean()


    df['Physically_attacked'] = df['Physically_attacked'].replace('or', ',', regex=True)
    df['Physically_attacked'] = df['Physically_attacked'].replace('[a-zA-Z ]+', '', regex=True)
    df['Physically_attacked'] = df['Physically_attacked'].replace(',[0-9]*', '', regex=True)
    df['Physically_attacked'] = pd.to_numeric(df['Physically_attacked'], errors='coerce')
    df.loc[df['Physically_attacked'].isnull(),'Physically_attacked'] = df.Physically_attacked.mean()



    df['Physical_fighting'] = df['Physical_fighting'].replace('or', ',', regex=True)
    df['Physical_fighting'] = df['Physical_fighting'].replace('[a-zA-Z ]+', '', regex=True)
    df['Physical_fighting'] = df['Physical_fighting'].replace(',[0-9]*', '', regex=True)
    df['Physical_fighting'] = pd.to_numeric(df['Physical_fighting'], errors='coerce')
    df.loc[df['Physical_fighting'].isnull(),'Physical_fighting'] = df.Physical_fighting.mean()



    df['Miss_school_no_permission'] = df['Miss_school_no_permission'].replace('or', ',', regex=True)
    df['Miss_school_no_permission'] = df['Miss_school_no_permission'].replace('to', ',', regex=True)
    df['Miss_school_no_permission'] = df['Miss_school_no_permission'].replace('[a-zA-Z ]+', '', regex=True)
    df['Miss_school_no_permission'] = df['Miss_school_no_permission'].replace(',[0-9]*', '', regex=True)
    df['Miss_school_no_permission'] = pd.to_numeric(df['Miss_school_no_permission'], errors='coerce')
    df.loc[df['Miss_school_no_permission'].isnull(),'Miss_school_no_permission'] = df.Miss_school_no_permission.mean()




    df.loc[df['Missed_classes_or_school_without_permission'] == 'Yes', ['Missed_classes_or_school_without_permission']] = True
    df.loc[df['Missed_classes_or_school_without_permission'] == 'No', ['Missed_classes_or_school_without_permission']] = False
    df['Missed_classes_or_school_without_permission'] = df['Missed_classes_or_school_without_permission'].astype('bool')


    df['engaged_in_a_fight'] = False*len(df)
    df.loc[(df['Physical_fighting'] >0)|(df['Physically_attacked']>0), 'engaged_in_a_fight'] = True
    df['engaged_in_a_fight'] = df['engaged_in_a_fight'].astype('bool')





    Loneliness_list = ['Never', 'Rarely', 'Sometimes', 'Most of the time', 'Always']
    df.loc[df['Felt_lonely'].isna(), 'Felt_lonely'] = 'Never'
    df['Felt_lonely']=df['Felt_lonely'].apply(lambda x: Loneliness_list.index(str(x)))


    Close_friends_list = ['0', '1', '2', '3 or more']
    df.loc[df['Close_friends'].isna(), 'Close_friends'] = '0'
    df['Close_friends']=df['Close_friends'].apply(lambda x: Close_friends_list.index(str(x)))



    Other_students_kind_and_helpful_list = ['Never','Rarely', 'Sometimes', 'Most of the time' , 'Always' ]
    df['Other_students_kind_and_helpful'] = df['Other_students_kind_and_helpful'].fillna(df['Other_students_kind_and_helpful'].mode()[0])
    df['Other_students_kind_and_helpful']=df['Other_students_kind_and_helpful'].apply(lambda x: Other_students_kind_and_helpful_list.index(str(x)))


    Parents_understand_problems_list = ['Never','Rarely', 'Sometimes', 'Most of the time' , 'Always' ]
    df['Parents_understand_problems'] = df['Parents_understand_problems'].fillna(df['Parents_understand_problems'].mode()[0])
    df['Parents_understand_problems']=df['Parents_understand_problems'].apply(lambda x: Parents_understand_problems_list.index(str(x)))


    df.loc[df['Most_of_the_time_or_always_felt_lonely'] == 'Yes', 'Most_of_the_time_or_always_felt_lonely'] = True
    df.loc[df['Most_of_the_time_or_always_felt_lonely'] == 'No', 'Most_of_the_time_or_always_felt_lonely'] = False
    df['Most_of_the_time_or_always_felt_lonely'] = df['Most_of_the_time_or_always_felt_lonely'].fillna(df['Most_of_the_time_or_always_felt_lonely'].mode()[0])
    df['Most_of_the_time_or_always_felt_lonely'] = df['Most_of_the_time_or_always_felt_lonely'].astype('bool')


    df['Gender'] = False*len(df)
    df.loc[df['Sex']=="Male",'Gender'] = True
    df['Sex'] = df['Gender']
    df['Sex'] = df['Sex'].astype(int)
    df = df.drop(columns=['Gender'])


    new_df = df.copy()
    new_df['Age'] = new_df['Custom_Age']
    new_df.drop(columns=['Custom_Age'])
    new_df['Bullied_Outside_School'] = False*len(new_df)
    new_df.loc[(new_df['Bullied_not_on_school_property_in_past_12_months']=='Yes') | (new_df['Cyber_bullied_in_past_12_months']=='Yes'), 'Bullied_Outside_School'] = True
    new_df['Bullied_Outside_School'] = new_df['Bullied_Outside_School'].astype('bool')


    new_df['Bullied_in_school'] = False*len(new_df)
    new_df.loc[new_df['Bullied_on_school_property_in_past_12_months']=='Yes', 'Bullied_in_school'] = True
    new_df['Bullied_in_school'] = new_df['Bullied_in_school'].astype('bool')



    #new_df.drop(columns=['Bullied_not_on_school_property_in_past_12_months', 'Cyber_bullied_in_past_12_months', 'Bullied_on_school_property_in_past_12_months'], inplace=True)
    new_df['Bullied'] = False*len(new_df)
    new_df.loc[ (new_df['Bullied_in_school'] == True) | (new_df['Bullied_Outside_School']) == True,'Bullied'] = True

    return new_df

    
