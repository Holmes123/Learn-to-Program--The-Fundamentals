####################################################
############## Longest city name ###################
##############         by        ###################
##############       Holmes      ###################
####################################################

""" Description:
By use of the 2 functions longest_city_name and
country_to_city the functions choose the country
with the longest capital city name.

Test the function by calling longest_city_name("Denmark", "Norway").
Note that the parameters are casesensitive. Writing
norway creates an error.
"""

# First we create a small dictionary.

country_city = {'Denmark' : "Copenhagen", 'Norway' : "Oslo", 'Sweden' : "Stockholm", 'Island' : "Reyjavik", "Zuomi" : "Helsinki"}

# Then we declare a global variable country.

country = ""

# Then we define the function longest_city_name

def longest_city_name(country_1, country_2):
    '''(str, str) -> str '''
    global country  # Loading the global variable country into the function.
    if len(country_city[country_1]) > len(country_city[country_2]): # Evaluates the length by calling the country in the dictionary.
        country = country_1     # Assigns the global varable country the value country_1.
        country_to_city(country)       # Calls country_to_city function.        
    elif len(country_city[country_1]) == len(country_city[country_2]): # Checks if citynames of the countries are of equal length.
        print ("The length of the cities are equal.")   # Prints the result if citynames are of equal length.
        print ("The cities are", country_city[country_1], "and", country_city[country_2])
    else:
        country = country_2 # Assigns the global varable country the value country_2. Result if country_2 city is longer than country_1 city.
        country_to_city(country)    # Calls country_to_city function.

def country_to_city(country):
    '''Prints the result of the evaluations done in longest_city_name. '''
    print ("The longest cityname is", country_city[country], "- the capital of", country)
