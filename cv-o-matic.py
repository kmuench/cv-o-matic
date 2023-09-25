#!/usr/bin/env python3
# CV-O-MATIC
# By: Kristin Muench
# Created: 25 09 2023
# Last Updated: 25 09 2023
#
# # # # # # # # # # # # #
#
# This is a Python script that takes a CSV database of professional attributes as input
# and generates a LaTeX document for further use.
#
# # # # # # # # # # # # #

import click
import os
from utils.latex_template import *
from utils.generate_content_dicts import make_paper_dict, make_experience_dict, make_education_dict, make_skills_dict, make_summary

@click.command()
@click.option(
    "-o",
    "--output_dir",
    type=str,
    help="Output directory where latex draft should be output"
)
@click.option(
    "-c",
    "--content_dir",
    type=str,
    help="Input directory containing csv files with content that should be used to populate CV"
)
@click.option(
    "-k",
    "--keyword",
    type=str,
    help="string to prepend CV file name to help keep track of versions"
)
def main(output_dir, content_dir, keyword):
    os.makedirs(output_dir, exist_ok=True)
    output_file=os.path.join(output_dir, keyword + '_cv.tex')

    # generate content
    papers_dict = make_paper_dict(content_dir)
    experiences_dict_list, addl_experiences_dict_list = make_experience_dict(content_dir)
    education_dict_list = make_education_dict(content_dir)
    skills_dict = make_skills_dict(content_dir)
    summary = make_summary(content_dir)


    # generate file
    with open(os.path.join(output_dir, 'papers.bib'),'w') as b:
        b.write(create_bib_file(papers_dict))

    with open(output_file, 'w') as f:
        f.write(generate_latex_template_text(FULL_NAME, MY_ADDRESS, MY_CITY, MY_COUNTRY, MY_LINKEDIN,
                                            MY_GITHUB, MY_EMAIL, MY_PHONE_NUMBER,
                                            summary,
                                            papers_dict, experiences_dict_list, addl_experiences_dict_list,
                                            education_dict_list, skills_dict))



    
if __name__ == "__main__":
    main()