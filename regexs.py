import re

# Funções que realizam o parsing do html para pegar o id e nome do item

def get_itemID(msg):
    regex = re.compile(r"Item\sID:\s</strong>(.*)</td>")
    result = regex.findall(msg)
    if len(result) > 0:
        return result[0]
    else:
        return None

def get_itemName(msg):
    regex = re.compile(r"Item\sName:\s</strong>(.*)</td>")
    result = regex.findall(msg)
    if len(result) > 0:
        return result[0]
    else:
        return None

if __name__ == '__main__':
    msg = 'Mensagem'
    print(get_itemID(msg))
    print(get_itemName(msg))