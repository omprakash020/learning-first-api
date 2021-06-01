import pandas as pd 
import numpy as np
import requests
from flashtext.keyword import KeywordProcessor
from nltk.corpus import stopwords

forum_posts = pd.read_csv('F:\python_data\myFile.csv')

new = pd.read_csv('F:/python_data/top_packages.csv')

def create_keywordprocessor(list_of_terms , remove_stopwords = True,
                            custom_stopwords_list=  ['']):
    
    keyword_processor = KeywordProcessor()
    
    keyword_processor.add_keywords_from_list(list_of_terms)
    
    if remove_stopwords == True:
        keyword_processor.remove_keywords_from_list(stopwords.words('english'))
        
    keyword_processor.remove_keywords_from_list(custom_stopwords_list)
    
    
    return(keyword_processor)
  
  def apply_keywordprocessor(keyword_processor, text ,span_info = True):
    keyword_found = keyword_processor.extract_keywords(text, span_info = span_info)
    
    return (keyword_found)

py_packages_processor = create_keywordprocessor(list_of_packages, custom_stopwords_list = 
                                               ['https','kaggle'])


for post in forum_posts:
    text = apply_keywordprocessor(py_packages_processor, post, span_info = False)
    
    print(text)
