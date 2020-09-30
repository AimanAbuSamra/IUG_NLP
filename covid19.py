import re
text="The emergence of COVID-19 we have seen instances of public stigmatization among specific populations, and the rise of harmful stereotypes. Stigmatization could potentially contribute to more severe health problems, ongoing transmission, and difficulties controlling infectious diseases during an epidemic. Please see the Subject in Focus section for more information on how to counter stigmatizing attitudes. New cases for today in Alexandria are 256 cases and 122 cases were registered as recovered. MOH thinking about major lockdown for 3 weeks. In Cairo there were registered 400 new cases and the recovered 350 but no lockdown is seen ahead."

def print_row(a,b,c):
    print(f"{a:20s}{b:20s}{c:20s}")

print_row("City","New Cases","Recovered Cases")
matches = re.findall("(Cairo|Alexandria)\D*(\d+)\D*(\d+)\D*\.",text)
for m in matches:
    print_row(m[0],m[1],m[2])    
