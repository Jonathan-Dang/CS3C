from DataViewToolBox import *

def main():
    url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    data = obtainJSONData(url)
    viewJSONData(data)
    
main()