__all__=["consumeMessages","relateFunction"]
import radio
radio.config(length=7,queue=3)
radio.on()

messages = []
relatedFunctions={}
def consumeMessages():
    while True:
        received = radio.receive_bytes()
        if received is not None:
            messages.append(received[3:])
        else:
            break
    for i in messages:
        if i[0] in relatedFunctions:
            for func in relatedFunctions[i[0]]:
                func(i[2:3])
            messages.remove(i)
def relateFunction(b:int,func):
    assert 0<=b<=255
    tabl = relatedFunctions.setdefault(b,[])
    tabl.append(func)
    relatedFunctions[b] = func
