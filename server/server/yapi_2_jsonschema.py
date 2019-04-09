#!/usr/bin/env python3
import json
import sys


# 将YApi中导出的api.json转换为schema.py
# 使用方法
# python3 ./yapi_2_jsonschema.py api.json > schema.py
def main():
    with open(sys.argv[1]) as f:
        yapi = json.loads(f.read())
        for yapi_item in yapi:
            for list_item in yapi_item['list']:
                if list_item['method'] == 'POST':
                    name = list_item['query_path']['path'][1:].replace("/", "_")
                    print(name, "=", json.dumps(json.loads(list_item['req_body_other']), indent=4))


if __name__ == '__main__':
    main()
