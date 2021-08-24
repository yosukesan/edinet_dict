
import json

if __name__=="__main__":

    JP = "様式ツリー-標準ラベル（日本語）"
    EN = "標準ラベル（英語）"

    data = open("edinet_tags.json").read()
    data_json = json.loads(data)

    print(data_json["jppfs_cor"]["Liabilities"][EN])
    print(data_json["jppfs_cor"]["Liabilities"][JP])
