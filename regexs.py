import re

# Funções que realizam o parsing do html para pegar o id e nome do item

def get_itemID(msg):
    regex = re.compile(r"Item\sID:\s</strong>(.*)</td>")
    result = regex.findall(msg)
    return result[0]

def get_itemName(msg):
    regex = re.compile(r"Item\sName:\s</strong>(.*)</td>")
    result = regex.findall(msg)
    return result[0]