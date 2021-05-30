
import json

if __name__=="__main__":

    data = open("edinet_tags.json").read()
    data_json = json.loads(data)
    print(data_json["jppfs_cor"]["Liabilities"]["en"])
    print(data_json["jppfs_cor"]["Liabilities"]["jp"])
