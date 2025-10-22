__all__=["consumeMessages","relateFunction","assignHost"]
import radio
import random
from microbit import sleep
from machine import unique_id
#[micro... bit..... weirdnes] action.. sendiden recident datadata datadata
# 0b0  = call out into the void to ask for a channel+player id
# 0b1 = "ok"/"no-k", ok is >0 data
# 0b01 = turn and top card change (ppppdddd cccccccc)
# 0b11 = giving the host a played card (00000000 cccccccc)
radio.config(length=8,queue=3,channel=0)
radio.on()

random.seed(int.from_bytes(unique_id(),"big"))
ID = random.getrandbits(8)
MICROBIT_CALLSIGN = bytes([0b1,0b0,0b1])

messages = []
relatedFunctions={}


def send_bytes_call(byte:bytes):
    print(byte)
    byte2 = MICROBIT_CALLSIGN+byte
    radio.send_bytes(byte2)
def receive_bytes_call():
    byte = radio.receive_bytes()
    if type(byte) is bytes:
        print(byte[3:])
        return byte[3:]
    return None

    
def consumeMessages():
    while True:
        received = receive_bytes_call()
        if received is not None:
            messages.append(received)
        else:
            break
    for i in messages:
        if i[0] in relatedFunctions:
            for func in relatedFunctions[i[0]]:
                func(i[1:])
            messages.remove(i)
            
def relateFunction(b:int,func):
    assert 0<=b<=255
    tabl = relatedFunctions.setdefault(b,[])
    tabl.append(func)
    relatedFunctions[b] = tabl
    return len(tabl)
def UnrelateFunction(b:int,func:int):
    assert 0<=b<=255
    tabl: list = relatedFunctions.setdefault(b,[])
    try:
        tabl.pop(func)
        return True
    except ValueError:
        return False
def assignHost(password):
    invalid = False
    def setinvalid(byte:bytes):
        nonlocal invalid
        if byte[1] == ID:
            invalid=True
    relateFunction(0b0,setinvalid)
    send_bytes_call(bytes([0b0,0b0])+password.to_bytes(2,"big"))
    sleep(200)
    if invalid:
        return False, "Password in use"
    channelFine = True
    def channelinuse(byte:bytes):
        pass
