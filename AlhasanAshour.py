import re

sampletxt = "The emergence of COVID-19 we have seen instances of public stigmatization among specific populationsand the rise of harmful stereotypes. Stigmatization could potentially contribute to more severe health problems, ongoing transmission, and difficulties controlling infectious diseases during an epidemic. Please see the Subject in Focus section for more information on how to counter stigmatizing attitudes. New cases for today in Alexandria are 256 cases and 122 cases were registered as recovered. MOH thinking about major lockdown for 3 weeks. In Cairo there were registered 400 new cases and the recovered 350 but no lockdown is seen ahead. "

Needed = 'New cases.as recovered.|In Cairo.\d'

print(re.findall(Needed, sampletxt))