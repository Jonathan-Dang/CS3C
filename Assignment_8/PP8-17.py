##
#    Author: Jonathan Dang
#    Project: PP8-17
#    Date: 3/14/2022
#
'''
This assignment was created and written with my own work 
and I promise that I held academic integrity at all times during this assignment.
If I have been inclined to create something based of off another's work, I will include 
specific details pertaining to the assignment within the .py file of each project.
I did not seek outside assistance that would violate academic integrity at any point in time, before and to the future
of this class.
-Jonathan Dang
'''

import csv

def main():
     try:
          filename = input("Please input a valid .csv file: ")
          csvDictionaryList = csvToDictionary(filename)
          while True:
               countryNames = []
               for item in csvDictionaryList:
                    print(item["country"])
               while 'next' not in countryNames:
                    countryNames.append(input("Please enter the country names to see their statstics [enter \"next\" to continue]: "))
               countryNames.pop()
          
               for item in csvDictionaryList:
                    if item["country"] in countryNames or countryNames is item["country"][0]:
                         print('-'*75)
                         printFormattedDictionary(item)
                    
               UserOp = input("Do you want to quit? [type \"quit\" to exit the program, anything else to continue]: ")
               if "quit" in UserOp:
                    break;
     except Exception as e:
          print(e)
          return;
          
     
    
##
#    csvToDictionary(filename)
#         Input: a valid CSV file
#         Output: a list containing multiple dictionaries.
#
def csvToDictionary(filename):
    if filename[-4::1] != ".csv":
        raise Exception("Wrong File Type!")

    with open(filename) as insfile:
        dict = csv.DictReader(insfile)
        listOfDictionaries = []
        for line in dict:
            listOfDictionaries.append(line)
        return listOfDictionaries

##
#    printFormattedDictionary(dictionary)
#         Input: a dictionary
#         Output: Prints to screen a dictionary formatted differently than default print
#
def printFormattedDictionary(dictionary):
    for key in dictionary:
        print(key)
        print(' '*5, end = '')
        print(dictionary[key])

main()

'''
Sample Run

Please input a valid .csv file: Assignment_8/cia_factbook.csv
Russia
Canada
United States
China
Brazil
Australia
India
Argentina
Kazakhstan
Algeria
Congo, Democratic Republic of the
Greenland
Saudi Arabia
Mexico
Indonesia
Sudan
Libya
Iran
Mongolia
Peru
Chad
Niger
Angola
Mali
South Africa
Colombia
Ethiopia
Bolivia
Mauritania
Egypt
Tanzania
Nigeria
Venezuela
Namibia
Mozambique
Pakistan
Turkey
Chile
Zambia
Burma
Afghanistan
South Sudan
France
Somalia
Central African Republic
Ukraine
Madagascar
Botswana
Kenya
Yemen
Thailand
Spain
Turkmenistan
Cameroon
Papua New Guinea
Sweden
Uzbekistan
Morocco
Iraq
Paraguay
Zimbabwe
Japan
Germany
Congo, Republic of the
Finland
Vietnam
Malaysia
Norway
Cote d'Ivoire
Poland
Oman
Italy
Philippines
Ecuador
Burkina Faso
New Zealand
Gabon
Western Sahara
Guinea
United Kingdom
Uganda
Ghana
Romania
Laos
Guyana
Belarus
Kyrgyzstan
Senegal
Syria
Cambodia
Uruguay
Suriname
Tunisia
Nepal
Bangladesh
Tajikistan
Greece
Nicaragua
Korea, North
Malawi
Eritrea
Benin
Honduras
Liberia
Bulgaria
Cuba
Guatemala
Iceland
Korea, South
Hungary
Portugal
Jordan
Azerbaijan
Austria
United Arab Emirates
Czech Republic
Serbia
Panama
Sierra Leone
Ireland
Georgia
Sri Lanka
Lithuania
Latvia
Svalbard
Togo
Croatia
Bosnia and Herzegovina
Costa Rica
Slovakia
Dominican Republic
Estonia
Denmark
Netherlands
Switzerland
Bhutan
Guinea-Bissau
Taiwan
Moldova
Belgium
Lesotho
Armenia
Solomon Islands
Albania
Equatorial Guinea
Burundi
Haiti
Rwanda
Macedonia
Djibouti
Belize
El Salvador
Israel
Slovenia
New Caledonia
Fiji
Kuwait
Swaziland
Timor-Leste
Bahamas, The
Montenegro
Puerto Rico
Vanuatu
Falkland Islands (Islas Malvinas)
Qatar
Gambia, The
Jamaica
Kosovo
Lebanon
Cyprus
West Bank
Brunei
Trinidad and Tobago
French Polynesia
Cabo Verde
Samoa
Luxembourg
Comoros
Mauritius
Virgin Islands
Faroe Islands
Hong Kong
Sao Tome and Principe
Turks and Caicos Islands
Kiribati
Bahrain
Dominica
Tonga
Micronesia, Federated States of
Singapore
Saint Lucia
Isle of Man
Guam
Andorra
Northern Mariana Islands
Palau
Seychelles
Curacao
Antigua and Barbuda
Barbados
Saint Vincent and the Grenadines
Gaza Strip
Grenada
Malta
Saint Helena, Ascension, and Tristan da Cunha
Maldives
Cayman Islands
Saint Kitts and Nevis
Niue
Saint Pierre and Miquelon
Cook Islands
American Samoa
Marshall Islands
Aruba
Liechtenstein
British Virgin Islands
Wallis and Futuna
Christmas Island
Jersey
Montserrat
Anguilla
Guernsey
San Marino
Saint Martin
Bermuda
Pitcairn Islands
Norfolk Island
Sint Maarten
Macau
Tuvalu
Nauru
Cocos (Keeling) Islands
Tokelau
Gibraltar
Monaco
Holy See (Vatican City)
Jan Mayen
Howland Island
Heard Island and McDonald Islands
South Georgia and South Sandwich Islands
Spratly Islands
Midway Islands
Clipperton Island
British Indian Ocean Territory
Johnston Atoll
Ashmore and Cartier Islands
Jarvis Island
Coral Sea Islands
French Southern and Antarctic Lands
Navassa Island
Wake Island
Kingman Reef
United States Pacific Island Wildlife Refuges
Dhekelia
Bouvet Island
Palmyra Atoll
Akrotiri
European Union
Saint Barthelemy
Please enter the country names to see their statstics [enter "next" to continue]: Wake Island
Please enter the country names to see their statstics [enter "next" to continue]: Dhekelia
Please enter the country names to see their statstics [enter "next" to continue]: European Union
Please enter the country names to see their statstics [enter "next" to continue]: next
---------------------------------------------------------------------------
country
     Wake Island
area
     7
birth_rate
     NA
death_rate
     NA
infant_mortality_rate
     NA
internet_users
     NA
life_exp_at_birth
     NA
maternal_mortality_rate
     NA
net_migration_rate
     NA
population
     NA
population_growth_rate
     NA
---------------------------------------------------------------------------
country
     Dhekelia
area
     131
birth_rate
     NA
death_rate
     NA
infant_mortality_rate
     NA
internet_users
     NA
life_exp_at_birth
     NA
maternal_mortality_rate
     NA
net_migration_rate
     NA
population
     NA
population_growth_rate
     NA
---------------------------------------------------------------------------
country
     European Union
area
     NA
birth_rate
     NA
death_rate
     NA
infant_mortality_rate
     4.33
internet_users
     NA
life_exp_at_birth
     80.02
maternal_mortality_rate
     NA
net_migration_rate
     NA
population
     511434812
population_growth_rate
     NA
Do you want to quit? [type \"quit\" to exit the program, anything else to continue]: quit
'''