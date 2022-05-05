from sklearn.ensemble import RandomForestClassifier

f = open('trainingdata.txt', 'r')
hero_db = {}
train_data = []

for line in f: # read all the data
    data = line.split(',')
    train_data.append(data)
f.close()
    
    
custom_id = 0
for entry in train_data: #loop through all the games, and assign a unique ID to each hero
    for i in range(10):
        if entry[i] not in hero_db.keys():
            hero_db[entry[i]] = custom_id
            custom_id += 1

x_train, y_train = [], []

for entry in train_data: # map each hero to its unique id
    for i in range(10):
        hero = entry[i]
        entry[i] = hero_db[hero]
    x_train.append(entry[:10])
    y_train.append(int(entry[-1]))

clf = DecisionTreeClassifier()

clf.fit(x_train, y_train) 

num_games = int(input())

x_test = []
for i in range(num_games):
    game_info = input().split(',')
    game_heroes = []
    for hero in game_info:
        game_heroes.append(hero_db[hero])
    x_test.append(game_heroes)

preds = clf.predict(x_test)

for pred in preds:
    print(pred)
