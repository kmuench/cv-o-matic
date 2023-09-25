#!/usr/bin/env python3
# Helper functions to generate strings for LaTeX template.
# This template is based off Rezume by Nanu Panchamurthy (https://github.com/sb2nov/resume)

# Import needed vars
import os
from utils.variables import *

# # HEADER
LATEX_TEMPLATE_FORMATTING=f"""
    %-------------------------
    % Rezume, a latex resume template for developers
    % Author : Nanu Panchamurthy
    % Based off of: https://github.com/sb2nov/resume
    % License : MIT

    % Hope this resume template helps you land an awesome job. If you found this helpful, please consider starring the github repo here, .
    %-------------------------



    %------------PACKAGES----------------
    \\documentclass[a4paper,11pt]{{article}}

    \\usepackage{{verbatim}} % reimplements the "verbatim" and "verbatim*" environments

    \\usepackage{{titlesec}} % provides an interface to sectioning commands i.e. custom elements

    \\usepackage[usenames,dvipsnames]{{xcolor}} % provides both foreground and background color management. was color

    \\usepackage{{enumitem}} % provides control over enumerate, itemize and description

    \\usepackage{{fancyhdr}} % provides extensive facilities for constructing headers, footers and also controlling their use

    \\usepackage{{tabularx}} % defines an environment tabularx, extension of "tabular" with an extra designator x, paragraph like column whose width automatically expands to fill the width of the environment

    \\usepackage{{latexsym}} % provides mathematical symbols

    \\usepackage{{marvosym}} % provides martin vogel's symbol font which contains various symbols

    \\usepackage[empty]{{fullpage}} % sets margins to one inch and removes headers, footers etc..

    \\usepackage[hidelinks]{{hyperref}} % removes color and shadow of hyperlinks

    \\usepackage[normalem]{{ulem}} % provides "\\ul" (uline) command which will break at line breaks

    \\usepackage[english]{{babel}} % provides culturally determined typographical rules for wide range of languages

    \\usepackage{{bibentry}} % for the papers section
    %-----------------------------------------

    \\input glyphtounicode % converts glyph names to unicode
    \\pdfgentounicode=1 % ensures pdfs generated are ats readable

    %----------FONT OPTIONS-------------------
    \\usepackage[default]{{sourcesanspro}} % uses the font source sans pro
    \\urlstyle{{same}} % changes url font from default urlfont to font being used by the document
    %-----------------------------------------


    %----------MARGIN OPTIONS-----------------
    \\pagestyle{{fancy}} % set page style to one configured by fancyhdr
    \\fancyhf{{}} % clear all header and footer fields

    \\renewcommand{{\\headrulewidth}}{{0in}} % sets thickness of linerule under header to zero
    \\renewcommand{{\\footrulewidth}}{{0in}} % sets thickness of linerule over footer to zero

    \\setlength{{\\tabcolsep}}{{0in}} % sets thickness of column separator in tables to zero

    % origin of the document is one inch from the top and from and the left
    % oddsidemargin and evensidemargin both refer to the left margin
    % right margin is indirectly set using oddsidemargin
    \\addtolength{{\\oddsidemargin}}{{-0.5in}}
    \\addtolength{{\\topmargin}}{{-0.5in}}

    \\addtolength{{\\textwidth}}{{1.0in}} % sets width of text area in the page to one inch
    \\addtolength{{\\textheight}}{{1.0in}} % sets height of text area in the page to one inch

    \\raggedbottom{{}} % makes all pages the height of current page, no extra vertical space added
    \\raggedright{{}} % makes all pages the width of current page, no extra horizontal space added
    %------------------------------------------


    %--------SECTIONING COMMANDS---------
    % \\titleformat{{<command>}}
    %   [<shape>]{{<format>}}{{<label>}}{{<sep>}}
    %     {{<before-code>}}[<after-code>]

    % command is the sectioning command to be redefined
    % shape is the style of the font; scshape stands for small caps style
    % format is the format to be applied to whole title- label and text; absent here
    % label defines the label
    % sep is the horizontal separation between label and title body
    % before-code is the code to be executed before
    % after-code is the code to be executed after

    \\titleformat{{\\section}}
    {{\\scshape\\large}}{{}}
        {{0em}}{{\\color{{MidnightBlue}}}}[\\color{{black}}\\titlerule\\vspace{{0pt}}] % get inspo for color here: https://steeven9.github.io/USI-LaTeX/html/packages_hyperref_babel_xcolor3.html
    %-------------------------------------


    %--------REDEFINITIONS----------------
    % redefines the style of the bullet point
    \\renewcommand\\labelitemii{{$\\vcenter{{\\hbox{{\\tiny$\\bullet$}}}}$}}

    % redefines the underline depth to 2pt
    \\renewcommand{{\\ULdepth}}{{2pt}}
    %-------------------------------------


    %--------CUSTOM COMMANDS--------------
    %\\vspace{{}} defines a vertical space of given size, modifying this in custom commands can help stretch or shrink resume to remove or add content

    % resumeItem renders a bullet point
    \\newcommand{{\\resumeItem}}[1]{{
    \\item\\small{{#1}}
    }}

    % commands to start and end itemization of resumeItem, rightmargin set to 0.11in to avoid the overflow of resumetItem beyond whatever resumeItemHeading is being used
    \\newcommand{{\\resumeItemListStart}}{{\\begin{{itemize}}[rightmargin=0.11in]}}
    \\newcommand{{\\resumeItemListEnd}}{{\\end{{itemize}}}}

    % resumeSectionType renders a bolded type to be used under a section, used as skill type here, middle element is used to keep ":"s in the same vertical line
    \\newcommand{{\\resumeSectionType}}[3]{{
    \\item\\begin{{tabular*}}{{0.96\\textwidth}}[t]{{
        p{{0.15\\linewidth}}p{{0.02\\linewidth}}p{{0.81\\linewidth}}
    }}
        \\textbf{{#1}} & #2 & #3
    \\end{{tabular*}}\\vspace{{-2pt}}
    }}

    % resumeTrioHeading renders three elements in three columns with second element being italicized and first element bolded, can be used for projects with three elements
    \\newcommand{{\\resumeTrioHeading}}[3]{{
    \\item\\small{{
        \\begin{{tabular*}}{{0.96\\textwidth}}[t]{{
        l@{{\\extracolsep{{\\fill}}}}c@{{\\extracolsep{{\\fill}}}}r
        }}
        \\textbf{{#1}} & \\textit{{#2}} & #3
        \\end{{tabular*}}
    }}
    }}

    % resumeQuadHeading renders four elements in a two columns with the second row being italicized and first element of first row bolded, can be used for experience and projects with four elements
    \\newcommand{{\\resumeQuadHeading}}[4]{{
    \\item
    \\begin{{tabular*}}{{0.96\\textwidth}}[t]{{l@{{\\extracolsep{{\\fill}}}}r}}
        \\textbf{{#1}} & #2 \\\\
        \\textit{{\\small#3}} & \\textit{{\\small #4}} \\\\
    \\end{{tabular*}}
    }}

    % resumeQuadHeadingChild renders the second row of resumeQuadHeading, can be used for experience if different roles in the same company need to added
    \\newcommand{{\\resumeQuadHeadingChild}}[2]{{
    \\item
    \\begin{{tabular*}}{{0.96\\textwidth}}[t]{{l@{{\\extracolsep{{\\fill}}}}r}}
        \\textbf{{\\small#1}} & {{\\small#2}} \\\\
    \\end{{tabular*}}
    }}

    % commands to start and end itemization of resumeQuadHeading, lefmargin for left indent of 0.15in for resumeItems
    \\newcommand{{\\resumeHeadingListStart}}{{
    \\begin{{itemize}}[leftmargin=0.15in, label={{}}]
    }}
    \\newcommand{{\\resumeHeadingListEnd}}{{\\end{{itemize}}}}
    %-------------------------------------------

    """


# # TEXT-GENERATING FUNCTIONS
def generate_latex_contact(FULL_NAME, MY_ADDRESS, MY_CITY, MY_COUNTRY,
                           MY_LINKEDIN, MY_GITHUB, MY_EMAIL, MY_PHONE_NUMBER):
    # TODO add back in when ready:
    # \\href{{{MY_WEBSITE}}}{{\\uline{{ {MY_WEBSITE.replace("https://","").replace("/","")} }}}} $|$ % row = 2, col = 1

    LATEX_TEMPLATE_CONTACT=f"""
    %-----------CONTACT DETAILS------------------
    % Make sure all the details are correct, you can add more links in the first row of second column if needed

    \\begin{{tabular*}}{{\\textwidth}}{{l@{{\\extracolsep{{\\fill}}}}r}}
    \\textbf{{\\Huge {FULL_NAME} \\vspace{{2pt}}}} & % row = 1, col = 1
    {MY_ADDRESS}, {MY_CITY}, {MY_COUNTRY} \\\\ % row = 1, col = 2
    \\href{{{MY_LINKEDIN}}}{{\\uline{{LinkedIn}}}} $|$ % row = 2, col = 1
    \\href{{{MY_GITHUB}}}{{\\uline{{GitHub}}}} $|$ % row = 2, col = 1
    \\href{{mailto:{MY_EMAIL}}}{{\\uline{{ {MY_EMAIL} }}}} $|$ % row = 2, col = 2
    {MY_PHONE_NUMBER} \\\\ % row = 2, col = 2
    \\end{{tabular*}}
    %--------------------------------------------
    """

    return(LATEX_TEMPLATE_CONTACT)


def generate_latex_summary(summary):
    LATEX_TEMPLATE_SUMMARY=f"""
    %-----------SUMMARY--------------------------
    % Keep this short, simple and straigth to point

    \\section{{SUMMARY}}
    \\small{{
    {summary}
    }}
    %--------------------------------------------
    """

    return(LATEX_TEMPLATE_SUMMARY)


def generate_latex_skills(skills_dict):

    TEMPLATE_PREFIX="""
        %--------------SKILLS------------------------
        % Add or remove resumeSectionTypes according to your needs

        \\section{{Technical Skills}}
        \\resumeHeadingListStart{{}}
    """

    TEMPLATE_SUFFIX="""
    \\resumeHeadingListEnd{{}}
    %--------------------------------------------
    """

    SKILLS_LIST = []
    for category, skills in skills_dict.items():
        SKILLS_LIST.append(f"""\\resumeSectionType{{ {category} }}{{:}}{{ {skills} }}""")

    TEMPLATE_SKILLS = "\n".join(SKILLS_LIST)

    LATEX_TEMPLATE_SKILLS = TEMPLATE_PREFIX + TEMPLATE_SKILLS + TEMPLATE_SUFFIX

    return(LATEX_TEMPLATE_SKILLS)


def generate_latex_education(education_dict_list):

    LATEX_TEMPLATE_EDUCATION = generate_latex_experience_general(education_dict_list, 
                                                                 section_name = "Education", 
                                      upper_left='institution', upper_right='degree_dates',
                                      lower_left='details_string', lower_right='location',
                                      flag_add_details=False)
    

    return(LATEX_TEMPLATE_EDUCATION)


def generate_latex_experience(experiences_dict):
    LATEX_TEMPLATE_EXPERIENCE = generate_latex_experience_general(experiences_dict=experiences_dict, 
                                                                  section_name="Key Professional Experiences")
    
    return(LATEX_TEMPLATE_EXPERIENCE)


def generate_latex_addl_experience(addl_experiences_dict_list):
    # if there are no additional experiences, don't add to CV
    if len(addl_experiences_dict_list) == 0:
        return(" ")
    else:
        LATEX_TEMPLATE_ADDL_EXPERIENCE = generate_latex_experience_general(experiences_dict=addl_experiences_dict_list, 
                                                                           section_name="Additional Experiences")
        
        return(LATEX_TEMPLATE_ADDL_EXPERIENCE)


def generate_latex_experience_general(experiences_dict, section_name, 
                                      upper_left='position', upper_right='dates',
                                      lower_left='location', lower_right='address',
                                      flag_add_details=True):
    TEMPLATE_PREFIX=f"""
        %-----------{section_name.upper()}-----------------------

        \\section{{ {section_name} }}
        \\resumeHeadingListStart{{}}
        """
    
    TEMPLATE_SUFFIX="""
        \\resumeHeadingListEnd{{}}
        %---------------------------------------------
        """
    
    list_experience_templates = []

    for experience in experiences_dict:
        EXPERIENCE_TEMPLATE_DETAILS_LIST=[]
        EXPERIENCE_TEMPLATE_HEADER = f"""
                \\resumeQuadHeading{{ {experience[upper_left]} }}{{ {experience[upper_right]} }}
                {{ {experience[lower_left]} }}{{ {experience[lower_right]} }}
                """
        EXPERIENCE_TEMPLATE_DETAILS = "" # empty unless there are details to add
        
        # add details if there are any
        if flag_add_details:
            if len(experience['details'])>0:
                EXPERIENCE_TEMPLATE_DETAILS_LIST = []
                for bulletpoint in experience['details']:
                    EXPERIENCE_TEMPLATE_DETAILS_LIST.append(f"\\resumeItem{{ {bulletpoint} }}")

                JOINED_EXPERIENCE_TEMPLATE_DETAILS_LIST = "\n\t\t\t\t\t".join(EXPERIENCE_TEMPLATE_DETAILS_LIST)

                EXPERIENCE_TEMPLATE_DETAILS = f"""
                        \\resumeItemListStart{{}}
                        {JOINED_EXPERIENCE_TEMPLATE_DETAILS_LIST}
                        \\resumeItemListEnd{{}}
                        """
            
        EXPERIENCE_TEMPLATE = EXPERIENCE_TEMPLATE_HEADER + EXPERIENCE_TEMPLATE_DETAILS
        list_experience_templates.append(EXPERIENCE_TEMPLATE)

    JOINED_LIST_EXPERIENCE_TEMPLATES = "\n".join(list_experience_templates)
    LATEX_TEMPLATE_EXPERIENCE = f"""
    {TEMPLATE_PREFIX}
    {JOINED_LIST_EXPERIENCE_TEMPLATES}
    {TEMPLATE_SUFFIX}
    """

    return(LATEX_TEMPLATE_EXPERIENCE)


def create_bib_file(papers_dict):
    # Helps creates bib file which generate_latex_papers() needs
    # (call to write is in python_to_latex)
    biblio_text_list=[]

    for paper_id,paper_deets in papers_dict.items():
        new_paper=f"""
        @article{{{paper_id},
            author = {{ {paper_deets['author']} }},
            title = {{ {paper_deets['title']} }},
            journal = {{ {paper_deets['journal']} }},
            year = {{ {paper_deets['year']} }},
            volume = {{ {paper_deets['volume']} }},
            number = {{ {paper_deets['number']} }},
            pages = {{ {paper_deets['pages']} }},
            publisher = {{ {paper_deets['publisher']} }},
        }}
        """
        biblio_text_list.append(new_paper)

    biblio_text="\n".join(biblio_text_list)
    return(biblio_text)


def generate_latex_papers(papers_dict):
    LATEX_TEMPLATE_PAPERS_LIST=[f"""
    %-----------PAPERS-----------------------
    % List your papers here
    \\nobibliography{{ papers.bib  }} % disables automatic citation numbering
    \\bibliographystyle{{unsrt}} % specifies unsorted style

    \\section*{{Publications}}
    \\begin{{enumerate}}"""]

    for key, details in papers_dict.items():
        LATEX_TEMPLATE_PAPERS_LIST.append(f"""\n\t\t\\item \\bibentry{{{ key }}}""")
    
    LATEX_TEMPLATE_PAPERS_LIST.append("\n\t\\end{enumerate}") #("\n\t\\end{{enumerate}}")
    LATEX_TEMPLATE_PAPERS = "\n".join(LATEX_TEMPLATE_PAPERS_LIST)
    
    return(LATEX_TEMPLATE_PAPERS)


# MAIN TEMPLATE CREATION FUNC
def generate_latex_template_text(FULL_NAME, MY_ADDRESS, MY_CITY, MY_COUNTRY, MY_LINKEDIN,
                                 MY_GITHUB, MY_EMAIL, MY_PHONE_NUMBER,
                                 summary,
                                 papers_dict, experiences_dict_list, addl_experiences_dict_list,
                                 education_dict_list, skills_dict):

    
    # Concatenate it all together into one big string
    LATEX_TEMPLATE=f"""
    {LATEX_TEMPLATE_FORMATTING}
    %__________________RESUME____________________
    % You can rearrange sections in any order you may prefer
    \\begin{{document}}
    {generate_latex_contact(FULL_NAME, MY_ADDRESS, MY_CITY, MY_COUNTRY,
                           MY_LINKEDIN, MY_GITHUB, MY_EMAIL, MY_PHONE_NUMBER)}
    {generate_latex_summary(summary)}
    {generate_latex_skills(skills_dict)}
    {generate_latex_education(education_dict_list)}
    {generate_latex_experience(experiences_dict_list)}
    {generate_latex_addl_experience(addl_experiences_dict_list)}
    {generate_latex_papers(papers_dict)}
    \\end{{document}}
    """

    return(LATEX_TEMPLATE)

