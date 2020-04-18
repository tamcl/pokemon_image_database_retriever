import requests, json
import informationGathering as searchFile
import os 
from downloadImage import download as download
import threading
import timeit
from concurrent.futures import ThreadPoolExecutor
import createDatabasefile
from createDatabasefile import compare
from tqdm import tqdm

gen1 = 151

def standard():
    startTimer = timeit.default_timer()
    createDatabasefile.createStandardFiles()
    with ThreadPoolExecutor(gen1) as executor: 
        for i in range(gen1):   
            executor.submit(createDatabasefile.extractimg,i) #0 == pokemon index 1
    stopTimer = timeit.default_timer()
    print("-- Complete download standard files")
    print('-- Time used: {}s'.format(stopTimer - startTimer))

def getJson(url):
    response = requests.get(url)
    return json.loads(response.text)

def getlinks(pokemonIndex):
    pokeapi = 'https://pokeapi.co/api/v2/pokemon/'
    pokemonInfo = getJson(pokeapi+str(pokemonIndex))
    searchparam = [pokemonInfo["name"], 'pokemon-{}'.format(pokemonInfo["name"])]#, '{}-pokemon'.format(pokemonInfo["name"]), 'cartoon-{}'.format(pokemonInfo["name"]), 'pokedex-{}'.format(pokemonInfo["name"]), 'pokemon-serebii-{}'.format(pokemonInfo["name"]),'serebii-{}'.format(pokemonInfo["name"]), 'gamefreak-{}'.format(pokemonInfo["name"]), 'nds-{}'.format(pokemonInfo["name"])] #add more parameter to enlarge your search area
    links = []
    for search in searchparam:
        links += searchFile.find(search)
    correctFormats = ["jpg", 'png', 'PNG', 'JPEG', 'jpeg', "JPG"]
    outputlinks = []
    linksid = 1
    for l in links:
        if l.split('.')[len(l.split('.'))-1] in correctFormats:
            outputlinks.append((l,pokemonIndex,linksid,l.split('.')[len(l.split('.'))-1]))
            linksid+=1
    return outputlinks

if __name__ == "__main__":
    gogogogo = True
    stan = True
    resear = True
    gather = True
    Filter = True
    if gogogogo == True:
        if stan == True:
            standard()
        t = []
        contact = []
        try:
            os.mkdir('DB')
        except:
            print('DB folder has already been made')
        if resear == True:
            print('-- initiate research process')
            startTimer = timeit.default_timer()
            for c in range(gen1):
                contact += getlinks(c+1)
            stopTimer = timeit.default_timer()
            print('-- research process complete')
            print('-- Time used: {}s'.format(stopTimer - startTimer))  
            try:
                researchResult = ''
                for i in contact:
                    l, index, identity, formatfile = i
                    researchResult += '{}|{}|{}|{}\n'.format(index,identity,formatfile,l)
                file = open('researchLog.txt', 'wb')
                file.write(researchResult.encode('UTF-8'))
                file.close()
                print('-- research result has been saved in {}'.format('researchLog.txt'))
            except:
                pass

        if gather == True:
            print('-- initiating thread pool')
            startTimer = timeit.default_timer()
            with ThreadPoolExecutor(50) as executor:
                # for i in contact:
                #     l, index, identity, formatfile = i
                #     executor.submit(download,'DB', '{}-{}.{}'.format(index,identity,formatfile),l)
                list(tqdm(executor.map(download, contact), total=len(contact)))
            stopTimer = timeit.default_timer()
            print("-- complete image download")
            print('-- Time used: {}s'.format(stopTimer - startTimer))

        if Filter == True:
            print("-- check image quality")
            startTimer = timeit.default_timer()
            with ThreadPoolExecutor(200) as executor:
                for fileI in os.listdir('DB'):
                    pokdexI = int(fileI.split('-')[0])
                    executor.submit(compare,pokdexI, 'DB/{}'.format(fileI),53500000)
            stopTimer = timeit.default_timer()
            print('-- Time used: {}s'.format(stopTimer - startTimer))
        print('-- Process finish please manual check in DB')
        total = set()
        for fileI in os.listdir('DB'):
            total.add(int(fileI.split('-')[0]))
        loss = []
        for number in range(gen1):
            if (number+1) not in total:
                loss.append(number+1)
        for number in loss:
            print(number)
        print(total)
        



