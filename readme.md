Edinet dictionary
===============================================================================

tags, Japanese and English dictionary for edinet.

1. Introduction

This is a dictionary for Edinet (Electronic Disclosure for Investors' NETwork) by Financial Services Agency of Japan.
This dictionary provides Edinet xbrl tag to Japanese and English for over 20000 categories on financial statement.

The official description for the format is available at https://www.fsa.go.jp/search/20201110.html.

2. Sample by Python

```
import json

if __name__=="__main__":

    JP = "様式ツリー-標準ラベル（日本語）"
    EN = "標準ラベル（英語）"

    data = open("edinet_tags.json").read()
    data_json = json.loads(data)

    print(data_json["jppfs_cor"]["Liabilities"][EN])
    print(data_json["jppfs_cor"]["Liabilities"][JP])
```

3. license
    MIT license
