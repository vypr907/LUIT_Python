#tuesday exercises

#to create a document with all the required dependencies to run code in your environment, to give to someone else using your code:
# pip freeze > requirements.txt

#to install all required dependencies in new virtual environment, the following code is used:
# pip install -r requirements.txt

#----------------------
#FUNCTIONS
#----------------------

#create a function
def greetings_terra():
    return 'bonjour'
#call a function
print("Calling a function:")
salutations = greetings_terra()
print(salutations)
print("__________________________________________")
print()

#______________________boto3______________
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
#__________________________________________

#________________________main()____________
#def main():
#    print("Now calling the function from the main()")
#    translaterator()
    
#if __name__=="__main__":
#    main()
#print("__________________________________________")
#print()
#____________________________________________

#-----------------------------------------------------
#ARGUMENTS AND PARAMETERS
#-----------------------------------------------------
def translaterator(text, source_language_code, target_language_code):
    client = boto3.client('translate')
    response = client.translate_text(
        Text = text,
        SourceLanguageCode = source_language_code,
        TargetLanguageCode = target_language_code
    )
    print(response)
    
def main():
    translaterator('Halo is the best video game series','en','fr')
    
if __name__=="__main__":
    main()
        