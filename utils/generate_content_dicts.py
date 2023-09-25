#!/usr/bin/env python3
# Utility to take CSV input and make dictionaries to iterate through experiences

import pandas as pd
import os


# GENERATE DICT FOR KEY PROFESSIONAL EXPERIENCES
def make_experience_dict(dir_content):
    # import data
    df_summary = pd.read_csv(os.path.join(dir_content, 'ExperiencesEmployment.csv'), sep=",").fillna('')
    df_descriptions = pd.read_csv(os.path.join(dir_content, 'ExperiencesEmploymentDescriptions.csv'), sep=",")

    list_of_primary_experiences = []
    list_of_additional_experiences = []
    for index, row in df_summary.iterrows():
        dict_exp = {'position': row['Position'],
                    'dates': " - ".join([str(row['Start Date']), str(row['End Date'])]),
                    'location': row['Location'],
                    'address': row['Address']}
        
        idx = (df_descriptions['Position'] == row['Position']) & (df_descriptions['Location'] == row['Location']) 
        exp_details = [x.replace("$", "\\textdollar").replace("%", "\\%") for x in df_descriptions.loc[idx]['Description']] #
        dict_exp.update({'details': exp_details})

        if row['Primary_or_Additional_Experience'] == 'Primary':
            list_of_primary_experiences.append(dict_exp)
        if row['Primary_or_Additional_Experience'] == 'Additional':
            list_of_additional_experiences.append(dict_exp)

    return(list_of_primary_experiences, list_of_additional_experiences)


# GENERATE DICT FOR EDUCATION
def make_education_dict(dir_content):
    # import data
    df_education = pd.read_csv(os.path.join(dir_content, 'Education.csv'), sep=",").fillna(' ')
    df_awards = pd.read_csv(os.path.join(dir_content, 'AwardsAchievementsMemberships.csv'), sep=",").fillna(' ')

    list_of_edu = []

    for index, row in df_education.iterrows():
        date_span = " - ".join([str(row['Start Year']), str(row['End Year'])])
        dict_edu = {'institution': row['Institution'],
                    'dates': date_span,
                    'location': row['Location'],
                    'degree': row['Degree'],
                    'award_date': row['Award Date'],
                    'gpa': row['GPA'],
                    'degree_dates': row['Degree'] + ", " + date_span}
            
        idx = (df_awards['Institution'] == row['Institution']) & (df_awards['Degree'] == row['Degree']) 
        relevant_awards =  df_awards.loc[idx].copy()
        edu_details_list = []

        print(relevant_awards['Award'])
        print(relevant_awards['Description'])
        
        if sum(idx) > 0:
            relevant_awards['Compressed'] = relevant_awards.apply(lambda x: x.Award + ". " + x.Description, axis = 1)
            edu_details_list = [x.replace("$", "\\textdollar").replace("%", "\\%") for x in relevant_awards['Compressed']] #
        dict_edu.update({'details_list': edu_details_list})
        dict_edu.update({'details_string': ", ".join(edu_details_list)})

        list_of_edu.append(dict_edu)

    return(list_of_edu)


# GENERATE DICT FOR SKILLS
def make_skills_dict(dir_content):
    df = pd.read_csv(os.path.join(dir_content, 'Skills.csv'), sep=",").fillna('')

    dict_skills = {}
    for category in set(df['Category']):
        relevant_skills = df.loc[df['Category'] == category, 'Skill'].to_list()
        dict_skills.update({category: ", ".join(relevant_skills)})

    return(dict_skills)


# GENERATE DICT FOR PAPERS
def make_paper_dict(dir_content):
    # column renaming to turn human-readable into latex-readable
    dict_rename_cols = {'Authors':'author',
                       'Title': 'title',
                       'Journal': 'journal',
                       'When': 'year',
                       'Volume': 'volume',
                       'Issue(Number)': 'number',
                       'Pages': 'pages',
                       'Where': 'publisher'}

    # import data
    df = pd.read_csv(os.path.join(dir_content, 'PapersPresentations.csv'), sep=",")
    df = df[df['Type'] == 'Paper']
    df = df.rename(columns=dict_rename_cols)

    df.author = df.author.apply(lambda x: x.replace("…", "...").replace(",", " and "))
    df.index = df.index.astype(str)


    df['paper_id'] = df['title'].apply(lambda x: "".strip().join(x.replace('"', '').replace(".","").replace("-", "").split(" ")[0:3])) + df['year'].astype(str).apply(lambda x: x.strip().replace(" ", ""))
    df = df.set_index('paper_id')
    
    df = df[[x for x in dict_rename_cols.values() if x in df.columns]]
    
    # make dict
    dict_papers = df.to_dict(orient="index")

    return (dict_papers)


# IMPORT SUMMARY
def make_summary(dir_content):
    df = pd.read_csv(os.path.join(dir_content, 'Summary.csv'), header=None)
    return(df.iloc[0,0])
