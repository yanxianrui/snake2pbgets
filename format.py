#coding=utf-8

import os
import sys
import json


output = {}

def underscore_to_camelcase(value):
    value = "Get_" + value
    output = ""
    parts = value.split("_")
    for word in parts:
        output += word.capitalize()
    return output


def change_form(inputs):
    if isinstance(inputs,dict):
        outputs = {}
        for key,value in inputs.items():
            newValue = change_form(value)
            newKey = underscore_to_camelcase(key)

            # print(key, newKey)
            outputs[newKey] = newValue
        return outputs

    elif isinstance(inputs,list):
        outputs = []
        for i in inputs:
            outputs.append(change_form(i))
        return outputs

    else:
        return inputs

inputs = json.loads(open(sys.argv[1], "r").read())
res = json.dumps(change_form(inputs))

with open(sys.argv[2], "w") as fp:
    fp.write(res)












# print(underscore_to_camelcase("asdf_asdf_asdf"))