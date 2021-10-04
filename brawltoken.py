import requests
import json
while True:
    api=input("to get your profile data we need a token(you can get it in https://developer.brawlstars.com).To quit the program type quit.Type your token:")
    if api=='quit':
        quit()
    playername=input("type your profile tag:")
    headers={'Authorization': 'Bearer '+api}
    try:
        answ=requests.get("https://api.brawlstars.com/v1/players/%23"+playername,headers=headers)
        name=json.loads(answ.text)
        print(answ.text)
        print("name: ",name['name'])
        print("----------")
        print("club: ",name['club']['name'])
        print('trophies: ',name['trophies'])
    except:
        print("try again:")

