import pymongo
import os
import json
if __name__ == "__main__":
    db_name = "tekken7"
    host_name = '127.0.0.1'
    port = 27017
    client = pymongo.MongoClient(host_name, port)
    db = client[db_name]
    char_coll = db['characters']
    data_dir = 'tekken7Data/'
    char_files = [data_dir + f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir,f))]
    charcs = {}
    for char_file in char_files:
        name = char_file.replace(data_dir,'').replace('-basic.json','').replace('-special.json','')
        with open(char_file) as f:
            data = json.load(f)
        if name not in charcs:
            charcs[name] = {}

        charcs[name].update(data)


    for char in charcs:
        print(char)
        post = {'name':char, 'moves':charcs[char]}
        post_id = char_coll.insert_one(post).inserted_id


