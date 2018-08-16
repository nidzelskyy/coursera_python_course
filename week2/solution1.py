import os
import tempfile
import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', "--key", help="The key of storage")
    parser.add_argument('-v', "--value", help="Inserted value")
    args = parser.parse_args()
    return [args.key, args.value]

def get_from_starage(key):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'a') as f:
        pass

    res = []
    with open(storage_path, 'r') as f:
        rows = f.readlines()
        for row in rows:
            r = json.loads(row)
            if key in r:
                res.append(r[key])

    return res

def write_to_starage(key, value):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'a') as f:
        obj = {key: value}
        f.write(json.dumps(obj) + '\n')


if __name__ == '__main__':
    key, value = parse_args()

    if key and value:
        write_to_starage(key, value)
    elif key:
        res = get_from_starage(key)
        if res:
            print(', '.join(res))
        else:
            print(None)
    else:
        pass