import re

def extract_markdown_images(text):   
    pattern = r"!\[([^\]]+)]\(([^)]+)\)" # RegExp pattern that extracting [alt_text] and (url) of image in markdown into tuple              
    matches = re.findall(pattern, text) # Creating a tuples of [alt_text] and (url) that's matching the pattern
    return matches

def extract_markdown_links(text):
    pattern= r"\[([^\]]+)]\(([^)]+)\)" # RegExp pattern that extracting [link_text] and (url) of image in markdown into tuple 
    matches = re.findall(pattern, text) # Creating a tuples of [alt_text] and (url) that's matching the pattern
    return matches


