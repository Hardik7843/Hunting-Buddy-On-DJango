# Code for Processing the Text
import pandas as pd
import spacy
from collections import defaultdict
import re
from pandas import json_normalize
# from django.conf import settings

# Load the spacy model using the path from Django settings
# nlp = spacy.load(settings.SPACY_MODEL_PATH)


def examine(raw_text):
    nlp = spacy.load(r'C:\Users\hardi\OneDrive\Desktop\Hardik stuff\Hunting Buddy on Django\model')
    # nlp = spacy.load('en_core_web_sm')
    text = re.sub('[^a-zA-Z0-9 \n\.]', '', raw_text)
    doc = nlp(text)
    out =  defaultdict(list)
    for w in doc.ents:
        out[w.label_].append(w.text)
    
    for skill in out.keys():
        # Removing the duplicates in output for each skills
        out[skill] = list(set(out[skill]))
    

    # df = pd.json_normalize(out)
    
    return out


text = """We are seeking a skilled and experienced Data Engineer specializing in Apache Spark to join our team. The ideal candidate will possess a deep understanding of data engineering principles, coupled with substantial experience in Apache Spark. The Data Engineer will be primarily responsible for the design, development, and maintenance of our data pipelines and infrastructure. Collaborating closely with other members of the data engineering team, they will contribute to the creation and implementation of innovative data-driven solutions.

Responsibilities:
• Design, develop, and maintain data pipelines and infrastructure.
• Collaborate with other data engineering team members to devise and execute new data-driven solutions.
• Liaise with stakeholders to gather requirements and translate them into technical specifications.
• Troubleshoot and debug data pipelines and infrastructure.
• Monitor and optimize data pipelines and infrastructure.
• Keep abreast of the latest data engineering technologies and trends.

Qualifications:
• Bachelor's degree in computer science, information technology, or a related field.
• 3+ years of experience in data engineering.
• Proficiency with Apache Spark.
• Prior experience with Databricks data platform is a must.
• Familiarity with Azure Data toolset.
• Knowledge of big data technologies such as Hadoop and Kafka.
• Experience with data warehousing and data lakes.
• Competence in data modeling and ensuring data quality.
• Proficiency in SQL and NoSQL databases.
• Familiarity with cloud computing platforms like AWS, Azure, and GCP.
• Strong problem-solving and analytical skills.
• Excellent communication and interpersonal abilities.

Desired Qualifications:
• Master's degree in computer science, information technology, or a related field.
• Additional 3+ years of experience in data engineering.
• Exposure to machine learning and artificial intelligence would be advantageous.
• Familiarity with distributed systems.
• Experience with open-source software development.
• Knowledge of Agile development methodologies"""


# output = examine(raw_text=text)
# print(output)
# for category in output:
#     print(f"category: {category}")
#     for requirement in output[f'{category}']:
#         print(f"Requiement: {requirement}")

