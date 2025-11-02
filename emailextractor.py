import re

def extract(inpfile, outfile):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'    
    try:
        
        with open(inpfile, 'r') as infile:
            content = infile.read()
        emails_found = re.findall(email_pattern, content)
        collection = list(dict.fromkeys(emails_found))
        with open(outfile, 'w') as outfile:
            for email in collection:
                outfile.write(email + '\n')
                
        print(f"Successfully extracted {len(collection)} email(s) and saved them to '{outfile}'.")
        
    except FileNotFoundError:
        print(f"Error: The file '{inpfile}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

extract('emailstext.txt', 'emails.txt')
