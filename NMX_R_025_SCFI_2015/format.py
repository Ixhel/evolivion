import re #regular expresions

def valid_text (text):
    
    formatted_text = re.match("[a-zA-Z]+", text)
    
    if formatted_text:
        content = formatted_text.group(0)
    else:
        content = 'null'
    
    return content

