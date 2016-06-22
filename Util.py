#*-coding utf8-*
from binascii import hexlify,  unhexlify


def checkData(data, _type):
    if data == '':
        return False, u"数据不能为空"

    errch, msg = None, "success"
    if _type == "hex":
        data = ''.join(data.split())
        if len(data) % 2 != 0:
            errch, msg = True, u"HEX模式下，数据长度必须为偶数"
        else:
            for ch in data.upper():
                if not ('0' <= ch <= '9' or 'A' <= ch <= 'F'):
                    errch, msg = ch, u"数据中含有非法的HEX字符"
                    break
                    
    return not errch, msg

toVisualHex = lambda data: b' '.join([hexlify(c.encode()) for c in data]).upper()
toHex = lambda data: b''.join([unhexlify(data[i:i+2]) for i in range(0, len(data), 2)])
