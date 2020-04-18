import createDatabasefile
import informationGathering as searchFile
import requests
import json
import urllib.request

def getJson(url):
    response = requests.get(url)
    return json.loads(response.text)

#TODO   create the correct samples 
createDatabasefile.createStandardFiles()
createDatabasefile.extractimg()

try:
    os.mkdir("DB")
except:
    # shutil.rmtree("DB")
    # os.mkdir("DB")
    pass

#TODO   download the correct samples


#TODO   get all the possible links
gen1 = 151
pokeapi = 'https://pokeapi.co/api/v2/pokemon/'
log = ''
threshold = 100000000

def getPoke(pokemonIndex):
    global log
    pokemonInfo = getJson(pokeapi+str(pokemonIndex))
    searchparam = [pokemonInfo["name"], 'pokemon-{}'.format(pokemonInfo["name"])]
    links = []
    count = 1
    for search in searchparam:
        links += searchFile.find(search)
    for l in links:
        linkFormat = l.split('.')[len(l.split('.'))-1]
        Mini, Maxi = createDatabasefile.compare(pokemonIndex, l)
        if Maxi > threshold:
            print("Fail: {}||{}||{}||count:{}| SSD:{} {}".format(l,pokemonInfo["name"], pokemonIndex,count,Mini,Maxi))
            log+="Fail: {}||{}||{}||count:{}| SSD:{} {}".format(l,pokemonInfo["name"], pokemonIndex,count,Mini,Maxi)
            log += '\n'
        else:
            print("OK: {} retrieved as database of {} Pokedex No.{}|| SSD:{} {}".format(l,pokemonInfo["name"],pokemonIndex,Mini,Maxi))
            log += "OK: {} retrieved as database of {} Pokedex No.{}|| SSD:{} {}".format(l,pokemonInfo["name"],pokemonIndex,Mini,Maxi)
            log += '\n'
            urllib.request.urlretrieve(l,'DB/'+'{}-{}.{}'.format(pokemonIndex, count,linkFormat))
        count+=1

#you can chnage the range right here to get the pokemon you want
for index in range(gen1):
    pokemonIndex = index+1
    getPoke(pokemonIndex)
    
    #TODO download the possible image crop filter and compare
    #TODO if pass threshold save in the folder

file = open('log.txt','wb')
file.write(log.encode('UTF-8'))
