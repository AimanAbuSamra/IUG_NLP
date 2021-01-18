import re

# Done By Mohammed Hamada , student ID : 120201362 , to be deliverd to Dr.Ayman Abu samra

# Original Text 
originalText = 'The emergence of COVID-19 we have seen instances of public stigmatization among specific populations, and the rise of harmful stereotypes. Stigmatization could potentially contribute to more severe health problems, ongoing transmission, and difficulties controlling infectious diseases during an epidemic. Please see the Subject in Focus section for more information on how to counter stigmatizing attitudes. New cases for today in Alexandria are 256 cases and 122 cases were registered as recovered. MOH thinking about major lockdown for 3 weeks. In Cairo there were registered 400 new cases and the recovered 350 but no lockdown is seen ahead.'


# First Pattern checked to extract cities and the numbers
pattern = 'New cases.*as recovered.|In Cairo.*\d{3}'


# execute the result of 
result = re.findall(pattern,originalText)



# Mapping the result of array which containing both 2 cities results
for i in result:
    #Get the new cases and recoverd number from the result array and execute the regx
    numberPattern = '\d{3}|\d{3}'
    checkedText = re.findall(numberPattern,i)
    #Get 2 cities from the result and execute the regx
    checkedCityPattern = 'Alexandria|Cairo'
    cityText  = re.findall(checkedCityPattern,i)

    # Printing the query with reformatting the text .
    print("The New Casse in", cityText[0] , " is", checkedText[0], "and the recovered cases is", checkedText[1])
