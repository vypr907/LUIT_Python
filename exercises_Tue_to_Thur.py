##tuesday exercises

##to create a document with all the required dependencies to run code in your environment, to give to someone else using your code:
# pip freeze > requirements.txt

##to install all required dependencies in new virtual environment, the following code is used:
# pip install -r requirements.txt

##----------------------
##FUNCTIONS
##----------------------

##create a function
def greetings_terra():
    return 'bonjour'
##call a function
print("Calling a function:")
print()
salutations = greetings_terra()
print(salutations)
print("__________________________________________")
print()

##______________________boto3______________
import boto3
#client = boto3.client('translate')
#def translaterator():
#    response = client.translate_text(
#        Text = 'Halo is the best video game series',
#        SourceLanguageCode = 'en',
#        TargetLanguageCode = 'fr'
#        )
#    print(response)
#print("Calling a function that uses an AWS resource")
#translaterator()
#print("__________________________________________")
#print()
##__________________________________________

##________________________main()____________
#def main():
#    print("Now calling the function from the main()")
#    translaterator()
    
#if __name__=="__main__":
#    main()
#print("__________________________________________")
#print()
##____________________________________________

##-----------------------------------------------------
##ARGUMENTS AND PARAMETERS
##-----------------------------------------------------
#def translaterator(text, source_language_code, target_language_code):
#    client = boto3.client('translate')
#   response = client.translate_text(
#        Text = text,
#        SourceLanguageCode = source_language_code,
#        TargetLanguageCode = target_language_code
#    )
#    print(response)
#    
#def main():
#    translaterator('Halo is the best video game series','en','fr')

#modifying function to use keyword arguments
def translaterator(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)
kwargs = {
    "Text":"Halo is the best video game series.",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }  
    
##-------------------------------------------------------
##INPUTS
##-------------------------------------------------------

##____________________________user input__________________
#text = input("What do you want to translate: ")
#source_language_code = input("Source Language: ")
#target_language_code = input("Target Language: ")
##_________________________________________________________

##____________________________cli__________________________
import argparse

#parser = argparse.ArgumentParser(description="Provides translation between one source language and another.")

#parser.add_argument(
#    '--text',
#    dest="Text",
#    type=str,
#    help="The text to translate.",
#    required=True
#    )
    
#parser.add_argument(
#    '--source-language-code',
#    dest="SourceLanguageCode",
#    type=str,
#    help="Source Language",
#    required=True
#    )
    
#parser.add_argument(
#    '--target-language-code',
#    dest="TargetLanguageCode",
#    type=str,
#    help="Target Language",
#    required=True
#    )

##this will inspect the cmd line, convert each argument to the appropriate type
##and then invoke the appropriate action
#args = parser.parse_args()
##__________________________________________________________

##________________________________from a file_______________
def open_input(file):
    print("Reading input from a file:")
    print()
    with open(file,'r') as f:
        text = f.read() ##we use read() to read the actual contents of the file
        print(text)
##__________________________________________________________

##________________________________from JSON_________________
import json

json_str = """
{
   "Input":[
       {
       "Text":"Halo is the best video game series.",
       "SourceLanguageCode":"en",
       "TargetLanguageCode":"fr",
       "Required": true
       }
   ]
}
"""

##now we're going to actually pull data from an external JSON file
parser = argparse.ArgumentParser(description="Provides translation between one source language and another.")

parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. THe file should be valid JSON",
    required=True)
    
##this will inspect the cmd line, convert each argument to the appropriate type
##and then invoke the appropriate action
#args = parser.parse_args()
    
def open_json():
    with open(args.filename) as file_obj:
        contents = json.load(file_obj)
        return contents['Input'][0]

##__________________________________________________________


##--------------------------------------------------
##LOOPS
#---------------------------------------------------

print("looping through range:")
print()
for number in range(1,11):
    print(f'The next number is {number}')



##________________________________________________________________________________
##________________________________________________________________________________
##________________________________________________________________________________

def main():
    ##using kwargs 
    #translaterator(Text = 'Halo is the best video game series.',SourceLanguageCode='en',TargetLanguageCode='fr')
    
    ##using inputs
    #translaterator(
    #    Text=text,
    #    SourceLanguageCode=source_language_code,
    #    TargetLanguageCode=target_language_code
    #    )
    
    ##using cli
    ##vars is an inbuilt function that returns a dict object
    #translaterator(**vars(args))
    
    ##using a file
    #open_input("./LUIT_Python/textyMcTexterson.txt")
    print("__________________________________________")
    print()
    
    ##using JSON
    print("Loading a string from JSON input:")
    print()
    json_input = json.loads(json_str)
    indented_format = json.dumps(json_input, indent=2)
    print(json_input)
    print()
    print("Formatting the JSON input:")
    print()
    print(indented_format)
    
    print()
    #print("Reading JSON data from a file")
    print()
    #kwargs = open_json()
    #translaterator(**kwargs)
    
    print("__________________________________________")
    print()
    

    
if __name__=="__main__":
    main()
  