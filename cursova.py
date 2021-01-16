import tkinter as tk
import datetime
from random import randrange, getrandbits, randint

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("{0}x{1}".format(1480, 500))

root.title("Woo-Lam_Suprun-Anna")

root.configure(background='#e3aab4')


xx = 150
xb = 170
click3gen = 0

#ALICE
alicePublicKey = None
alicePrivateKey = None
bobPublicKeyinAlice = None
trentPublicKeyinAlice = None

#BOB
bobPublicKey = None
bobPrivateKey = None
alicePublicKeyinBob = None
trentPublicKeyinBob = None

#TRENT
trentPublicKey = None
trentPrivateKey = None
alicePublicKeyinTrent = None
bobPublicKeyinTrent = None


        # ZERO STEP
whatToDo = None
generateAliceKeyButton = None
generateBobKeyButton = None
generateTrentKeyButton = None

alicePublicKeyValue = tk.StringVar()
alicePrivateKeyValue = tk.StringVar()
alicePublicKeyinBobValue = tk.StringVar()
alicePublicKeyinTrentValue = tk.StringVar()
alicePublicKeyinBobText = None
alicePublicKeyinBobLable = None
alicePublicKeyinTrentText = None
alicePublicKeyinTrentLable = None

bobPublicKeyValue = tk.StringVar()
bobPrivateKeyValue = tk.StringVar()
bobPublicKeyinAliceValue = tk.StringVar()
bobPublicKeyinTrentValue = tk.StringVar()
bobPublicKeyinAliceText = None
bobPublicKeyinAliceLable = None
bobPublicKeyinTrentText = None
bobPublicKeyinTrentLable = None

trentPublicKeyValue = tk.StringVar()
trentPrivateKeyValue = tk.StringVar()
trentPublicKeyinAliceValue = tk.StringVar()
trentPublicKeyinBobValue = tk.StringVar()
trentPublicKeyinAliceText = None
trentPublicKeyinAliceLable = None
trentPublicKeyinBobText = None
trentPublicKeyinBobLable = None


        # FIRST STEP
aliceSendValue = tk.StringVar()
aliceSendButton = None


        # SECOND STEP
addBobPublicKeyinTrentButton = None
trentSendValue = tk.StringVar()
trentSendButton = None
trentSendToAlice = None

        # THIRD STEP
aliceRandomValueValue = tk.StringVar()
addAliceRandomValueButton = None
aliceRandomValue = None
aliceSendToBob = None

        # FOURHT STEP
aliceRandomValueinBobValue = tk.StringVar() 
bobSendButton = None
bobSendValue = tk.StringVar()
aliceRandomValueinBob = None
bobSendToTrent = None


        # FIFTH STEP
aliceRandomValueinTrentValue = tk.StringVar() 
aliceRandomValueinTrent = None
addAlicePublicKeyinTrentButton= None
trentSendToBob = None
sessionKeyinTrentValue = tk.StringVar()
sessionKeyinTrent = None
addSessioninTrentButton = None
addAliceRandomValueinTrentButton = None


        # SIXTH STEP
sessionKeyBobValue = tk.StringVar() 
sessionKeyBob = None
bobRandomValueValue = tk.StringVar()
bobRandomValue = None
addBobRandomValueButton = None


        # SEVENTH STEP
bobRandomValueinAliceValue = tk.StringVar() 
bobRandomValueinAlice = None 
sessionKeyAliceValue = tk.StringVar() 
sessionKeyAlice = None
addBobRandomValueinAliceButton = None
___ = None

tryAgainButton = None
##################RSA######################

#Test if a number is prime
def is_prime(n, k=256):
    
    #n the number to test
    #k the number of tests to do
        
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

# Generate an odd integer randomly
def generate_prime_candidate(length):
    # length - the length of the number to generate, in bits
    
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
# Generate a prime
def generate_prime_number(length=128):
    # length - the length of the number to generate, in bits

    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 256):
        p = generate_prime_candidate(length)
    return p

# calculates the modular inverse from e and phi
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# calculates the gcd of two ints
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_keyPairs():
    while True:
        p = generate_prime_number()
        q = generate_prime_number()
        
        n = p*q
        # print("n ",n)
        phi = (p-1) * (q-1) 
        # print("phi ",phi)
        
        # choose e coprime to n and 1 > e > phi  
        e = randint(1, phi)
        g = gcd(e,phi)
        while g != 1:
            e = randint(1, phi)
            g = gcd(e, phi)
            
        # print("e=",e," ","phi=",phi)
        # d[1] = modular inverse of e and phi
        d = egcd(e, phi)[1]
        
        # make sure d is positive
        d = d % phi
        if(d < 0):
            d += phi
        
        # if hash(12345678) == decrypt(encrypt(hash(12345678), (d,n)), (e,n)): 
        return ((e,n),(d,n))
        
def decrypt(ctext,private_key):
    key,n = private_key
    if isinstance(ctext, int): return pow(ctext,key,n)
    else:
        text = [chr(pow(char,key,n)) for char in ctext]
        return "".join(text)
    

def encrypt(text,public_key):
    key,n = public_key
    if isinstance(text, int): return pow(text,key,n)
    else: 
        ctext = [pow(ord(char),key,n) for char in text]
        return ctext
##############################################################









def createButton(t, cmd, h=1, w=5, f=('calibri', 12, 'bold')):
    return tk.Button(
        root,
        font=f,
        bg='#852c3b',
        fg="white",
        activebackground='#217560',
        activeforeground='white',
        highlightthickness=0,
        text=t,
        borderwidth='0',
        width=w,
        command=cmd,
        height=h)

def makeLabel(t, f = ('calibri', 12, 'bold'), w = 17, h=None ):
    return tk.Label(
        root, 
        text=t,
        font=f,
        fg="white",
        width=w,
        height=h,
        bg='#852c3b',
        highlightthickness=0,
        borderwidth='1')

def makeEntry(v, w=None):
    return tk.Entry(
        root, 
        width=w,
        font=('calibri', 12, 'bold'),
        fg="black",
        bg='white',
        highlightthickness=0,
        textvariable=v)



def generateAliceKey(): 
    global click3gen
    global alicePublicKey
    global alicePublicKeyValue
    global alicePrivateKey
    global alicePrivateKeyValue
    global alicePublicKeyinTrentValue
    global alicePublicKeyinTrent

    generateAliceKeyButton.place_forget()
    alicePublicKey, alicePrivateKey = generate_keyPairs() 
    print("Alice Public: ",alicePublicKey, alicePublicKey[0].bit_length(), alicePublicKey[1].bit_length())
    print("Alice Private: ",alicePrivateKey, alicePrivateKey[0].bit_length(), alicePrivateKey[1].bit_length())

    # alicePublicKeyinBob = alicePublicKey
    alicePublicKeyinTrent = alicePublicKey
    print("adsfasdf", alicePublicKeyinBob, alicePublicKeyinTrent)

    alicePublicKeyinTrentText = makeLabel("Alice Public key").place(relx=0.5, y=40+29*2, x=-110, anchor=tk.N)
    alicePublicKeyinTrentLable = makeEntry(alicePublicKeyinTrentValue).place(relx=0.5, y=40+29*2, x=xx+6-110, anchor=tk.N)

    alicePublicKeyValue.set(alicePublicKey)
    alicePrivateKeyValue.set(alicePrivateKey)
    # alicePublicKeyinBobValue.set(str(alicePublicKey[0]) + " " + str(alicePublicKey[1]))
    alicePublicKeyinTrentValue.set(alicePublicKey)
    click3gen += 1
    if click3gen == 3: firstStep()

def generateBobKey(): 
    global click3gen
    global bobPublicKey
    global bobPublicKeyValue
    global bobPrivateKey
    global bobPrivateKeyValue
    global bobPublicKeyinTrentValue
    global bobPublicKeyinTrent

    generateBobKeyButton.place_forget()
    bobPublicKey, bobPrivateKey = generate_keyPairs() 
    print("Bob's Public: ",bobPublicKey)
    print("Bob's Private: ",bobPrivateKey)

    # bobPublicKeyinAlice = bobPublicKey
    bobPublicKeyinTrent = bobPublicKey

    bobPublicKeyinTrentText = makeLabel("Bob's Public key").place(relx=0.5, y=40+29*3, x=-110, anchor=tk.N)
    bobPublicKeyinTrentLable = makeEntry(bobPublicKeyinTrentValue).place(relx=0.5, y=40+29*3, x=xx+6-110, anchor=tk.N)

    bobPublicKeyValue.set(bobPublicKey)
    bobPrivateKeyValue.set(bobPrivateKey)
    # bobPublicKeyinAliceValue.set(str(bobPublicKey[0]) + " " + str(bobPublicKey[1]))
    bobPublicKeyinTrentValue.set(bobPublicKey)
    click3gen += 1
    if click3gen == 3: firstStep()

def generateTrentKey(): 
    global click3gen
    global trentPublicKey
    global trentPublicKeyValue
    global trentPrivateKey
    global trentPrivateKeyValue
    global trentPublicKeyinAliceValue
    global trentPublicKeyinBobValue
    global trentPublicKeyinAlice
    global trentPublicKeyinBob

    generateTrentKeyButton.place_forget()
    trentPublicKey, trentPrivateKey = generate_keyPairs() 
    print("Trent's Public: ",trentPublicKey)
    print("Trent's Private: ",trentPrivateKey)

    trentPublicKeyinAlice = trentPublicKey
    trentPublicKeyinBob = trentPublicKey



    trentPublicKeyinAliceText = makeLabel("Trent Public key").place(x=5, y=40+29*2)
    trentPublicKeyinAliceLable = makeEntry(trentPublicKeyinAliceValue).place(x=xx, y=40+29*2)
    trentPublicKeyinBobText = makeLabel("Trent Public key").place(relx=1, y=40+29*2, x=-5, rely=0, anchor=tk.NE)
    trentPublicKeyinBobLable = makeEntry(trentPublicKeyinBobValue).place(relx=1, y=40+29*2, x=-xx, rely=0, anchor=tk.NE)

    trentPublicKeyValue.set(trentPublicKey)
    trentPrivateKeyValue.set(trentPrivateKey)
    trentPublicKeyinAliceValue.set(trentPublicKey)
    trentPublicKeyinBobValue.set(trentPublicKey)
    click3gen += 1
    if click3gen == 3: firstStep()

def aliceFirstStepSendClick(): secondStep()

def trentSecondStepSignClick():
    global trentSendToAlice

    sign = abs(hash(bobPublicKeyinTrent))
    print(sign)
    encryptedSign = encrypt(sign, trentPrivateKey)
    print(encryptedSign)
    trentSendValue.set((encryptedSign, bobPublicKeyinTrent))
    trentSendToAlice = (encryptedSign, bobPublicKeyinTrent)

    trentSendButton['text'] = 'Send'
    trentSendButton['command'] = trentSecondStepSendClick
    print(decrypt(encryptedSign, trentPublicKey))

def trentSecondStepSendClick(): thirdStep()

def aliceThirdStepVerifyClick():
    global addAliceRandomValueButton

    selfSign = abs(hash(bobPublicKeyinAlice))
    decryptedSign = decrypt(trentSendToAlice[0], trentPublicKeyinAlice)
    if selfSign == decryptedSign: 
        print("Verification successful")
        aliceSendValue.set("Verification successful")
    else: aliceSendValue.set("Verification failed")
    print(selfSign, decryptedSign)
    aliceSendButton.place_forget()

    addAliceRandomValueButton = createButton("Gen", genAliceRandomValueClick, None, None)
    addAliceRandomValueButton.place(y=40+29*4, x=xx+170)

def aliceThirdStepCryptClick():
    global aliceSendToBob
    aliceSendButton['text'] = "Send"
    aliceSendButton['command'] = aliceThirdStepSendClick

    aliceSendToBob = encrypt(aliceRandomValue, bobPublicKeyinAlice)
    aliceSendValue.set(str(aliceSendToBob)+", Alice")

def aliceThirdStepSendClick(): fourthStep()

def bobFourthStepDecryptClick():
    global aliceRandomValueinBob
    global aliceRandomValueinBobValue

    aliceRandomValueinBob = decrypt(aliceSendToBob, bobPrivateKey)

    aliceRandomValueinBobText = makeLabel("Alice Time value").place(relx=1, y=40+29*4, x=-5, rely=0, anchor=tk.NE)
    aliceRandomValueinBobLable = makeEntry(aliceRandomValueinBobValue).place(relx=1, y=40+29*4, x=-xx, rely=0, anchor=tk.NE)
    aliceRandomValueinBobValue.set(datetime.datetime(int(str(aliceRandomValueinBob)[0:4]), int(str(aliceRandomValueinBob)[4:6]), int(str(aliceRandomValueinBob)[6:8]), int(str(aliceRandomValueinBob)[8:10]), int(str(aliceRandomValueinBob)[10:12]), int(str(aliceRandomValueinBob)[12:14])))

    bobSendValue.set(datetime.datetime(int(str(aliceRandomValueinBob)[0:4]), int(str(aliceRandomValueinBob)[4:6]), int(str(aliceRandomValueinBob)[6:8]), int(str(aliceRandomValueinBob)[8:10]), int(str(aliceRandomValueinBob)[10:12]), int(str(aliceRandomValueinBob)[12:14])))
    bobSendButton['text'] = "Crypt Trent's PubKey"
    bobSendButton['command'] = bobFourthStepCryptClick

def bobFourthStepCryptClick():
    global bobSendToTrent

    bobSendToTrent = encrypt(aliceRandomValueinBob, trentPublicKeyinBob)
    bobSendValue.set(str(bobSendToTrent)+", Alice, Bob")
    bobSendButton['text'] = "Send"
    bobSendButton['command'] = bobFourthStepSendClick

def bobFourthStepSendClick(): fifthStep()

def trentFifthStepDecryptClick(): 
    global aliceRandomValueinTrentValue
    global aliceRandomValueinTrent
    global addAlicePublicKeyinTrentButton

    trentSendValue.set("")
    trentSendButton.place_forget()

    aliceRandomValueinTrent = encrypt(bobSendToTrent, trentPrivateKey)

    # trentPrivateKeyText = makeLabel("Trent's Private key").place(relx=0.5, y=40+29*4, x=-110, anchor=tk.N)
    # trentPrivateKeyLable = makeEntry(trentPrivateKeyValue).place(relx=0.5, y=40+29*4, x=xx+6-110, anchor=tk.N)


    aliceRandomValueinTrentText = makeLabel("Alice Time value").place(relx=0.5, y=40+29*4, x=-110, anchor=tk.N)
    aliceRandomValueinTrentLable = makeEntry(aliceRandomValueinTrentValue).place(relx=0.5, y=40+29*4, x=xx+6-110, anchor=tk.N)
    aliceRandomValueinTrentValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))

    addAlicePublicKeyinTrentButton = createButton("Add to send", addAlicePublicKeyinTrentButtonClick, None, None)
    addAlicePublicKeyinTrentButton.place(relx=0.5, y=40+29*2, x=xx-5-110+140, anchor=tk.N)

def trentFifthStepFirstSignClick():
    global trentSendToBob
    trentSendToBob = [[],[]]

    sign = abs(hash(alicePublicKeyinTrent))
    print(sign)
    encryptedSign = encrypt(sign, trentPrivateKey)
    print(encryptedSign)
    trentSendToBob[0] = (encryptedSign, alicePublicKeyinTrent)
    trentSendValue.set(trentSendToBob[0])
    trentSendButton['text'] = 'Send'
    trentSendButton['command'] = trentFifthStepFirstSendClick
    print(decrypt(encryptedSign, trentPublicKey))

def trentFifthStepFirstSendClick():
    global sessionKeyinTrentValue
    global addSessioninTrentButton

    trentSendValue.set("")
    trentSendButton.place_forget()

    sessionKey = makeLabel("Session Key").place(relx=0.5, y=40+29*5, x=-110, anchor=tk.N)
    sessionKeyLable = makeEntry(sessionKeyinTrentValue).place(relx=0.5, y=40+29*5, x=xx+6-110, anchor=tk.N)
    addSessioninTrentButton = createButton("Gen", genSessioninTrentButtonClick, None, None)
    addSessioninTrentButton.place(relx=0.5, y=40+29*5, x=xx+6-110+130, anchor=tk.N)

def trentFifthStepSecondSignClick():
    encryptedSignSession = encrypt(abs(hash(sessionKeyinTrent)), trentPrivateKey)
    encryptedSignRandom = encrypt(abs(hash(aliceRandomValueinTrent)), trentPrivateKey)
    trentSendToBob[1] = (encryptedSignSession, encryptedSignRandom)
    trentSendValue.set(trentSendToBob[1])

    trentSendButton.place(relx=0.5, y=5, x=-110+350, anchor=tk.N)
    trentSendButton['text'] = "Crypt with Bob's PubKey"
    trentSendButton['command'] = trentFifthStepCryptClick
    print(decrypt(encryptedSignSession, trentPublicKey), decrypt(encryptedSignRandom, trentPublicKey))

def trentFifthStepCryptClick():
    global trentSendToBob
    encryptBobSes = encrypt(sessionKeyinTrent, bobPublicKeyinTrent)
    encryptBobRand = encrypt(aliceRandomValueinTrent, bobPublicKeyinTrent)
    trentSendToBob = (trentSendToBob[0], ((encryptBobSes, trentSendToBob[1][0]), (encryptBobRand, trentSendToBob[1][1])))
    trentSendValue.set(trentSendToBob[1])

    trentSendButton.place(relx=0.5, y=5, x=-110+280, anchor=tk.N)
    trentSendButton['text'] = "Send"
    trentSendButton['command'] = trentFifthStepSendClick

def trentFifthStepSendClick(): sixthStep()


def bobsixthStepVerifyClick():
    global alicePublicKeyinBobValue
    global alicePublicKeyinBob
    global sessionKeyBobValue
    global sessionKeyBob

    selfSignAlicePublicKey = abs(hash(trentSendToBob[0][1]))
    decryptedSignAlicePublicKey = decrypt(trentSendToBob[0][0], trentPublicKeyinBob)

    if selfSignAlicePublicKey == decryptedSignAlicePublicKey: 
        print("Verification successful")
        bobSendValue.set("Verification successful")

        alicePublicKeyinBobText = makeLabel("Alice Public key").place(relx=1, y=40+29*3, x=-5, rely=0, anchor=tk.NE)
        alicePublicKeyinBobLable = makeEntry(alicePublicKeyinBobValue).place(relx=1, y=40+29*3, x=-xx, rely=0, anchor=tk.NE)
        alicePublicKeyinBob = trentSendToBob[0][1]
        alicePublicKeyinBobValue.set(alicePublicKeyinBob)
    else: aliceSendValue.set("Verification failed")
    print(selfSignAlicePublicKey, decryptedSignAlicePublicKey)


    decryptSessionKey = decrypt(trentSendToBob[1][0][0], bobPrivateKey)
    selfSignSessionKey = abs(hash(decryptSessionKey))
    decryptedSignSessionKey = decrypt(trentSendToBob[1][0][1], trentPublicKeyinBob)

    if selfSignSessionKey == decryptedSignSessionKey: 
        print("Verification successful")
        bobSendValue.set("Verification successful")

        sessionKeyBob1 = makeLabel("Session Key").place(relx=1, y=40+29*6, x=-5, rely=0, anchor=tk.NE)
        sessionKeyBobLable = makeEntry(sessionKeyBobValue).place(relx=1, y=40+29*6, x=-xx, rely=0, anchor=tk.NE)
        sessionKeyBob = decryptSessionKey
        sessionKeyBobValue.set(sessionKeyBob)
    else: aliceSendValue.set("Verification failed")
    print(decryptSessionKey, selfSignSessionKey, decryptedSignSessionKey)

    bobSendButton['text'] = "Add Trent 2nd Msg"
    bobSendButton['command'] = addTrentSecondMessage

def bobSixthStepSendClick(): seventhStep()

def bobseventhStepVerifyClick():
    global bobRandomValueinAliceValue
    global bobRandomValueinAlice
    global sessionKeyAliceValue
    global sessionKeyAlice
    global addBobRandomValueinAliceButton


    bobRandomValueinAliceText = makeLabel("Bob Time value").place(x=5, y=40+29*5)
    bobRandomValueinAliceLable = makeEntry(bobRandomValueinAliceValue).place(x=xx, y=40+29*5)
    bobRandomValueinAlice = bobSendToAlice[0]
    bobRandomValueinAliceValue.set(datetime.datetime(int(str(bobRandomValueinAlice)[0:4]), int(str(bobRandomValueinAlice)[4:6]), int(str(bobRandomValueinAlice)[6:8]), int(str(bobRandomValueinAlice)[8:10]), int(str(bobRandomValueinAlice)[10:12]), int(str(bobRandomValueinAlice)[12:14])))


    decryptSessionKey = decrypt(bobSendToAlice[1][0][0], alicePrivateKey)
    selfSignSessionKey = abs(hash(decryptSessionKey))
    decryptedSignSessionKey = decrypt(bobSendToAlice[1][0][1], trentPublicKeyinAlice)

    if selfSignSessionKey == decryptedSignSessionKey: 
        print("Verification successful")
        aliceSendValue.set("Verification successful")

        sessionKeyAlice = makeLabel("Session Key").place(x=5, y=40+29*6)
        sessionKeyAliceLable = makeEntry(sessionKeyAliceValue).place(x=xx, y=40+29*6)

        sessionKeyAlice = decryptSessionKey
        sessionKeyAliceValue.set(sessionKeyAlice)
    else: aliceSendValue.set("Verification failed")
    print(decryptSessionKey, selfSignSessionKey, decryptedSignSessionKey)

    aliceSendButton.place_forget()

    addBobRandomValueinAliceButton = createButton("Add to send", addBobRandomValueinAliceButtonClick, None, None)
    addBobRandomValueinAliceButton.place(x=xx+170, y=40+29*5)
    
def aliceSeventhStepCryptClick():
    global aliceSendToBob
    addBobRandomValueinAliceButton.place_forget()

    aliceSendToBob = bobRandomValueinAlice * sessionKeyAlice
    aliceSendValue.set(int(aliceSendToBob))
    aliceSendButton['text'] = "Send"
    aliceSendButton['command'] = aliceSendToBobFinal

def aliceSendToBobFinal(): finalStep()

def bobFinalStepDecryptClick():
    global tryAgainButton

    zxc = aliceSendToBob/sessionKeyBob
    bobSendValue.set(datetime.datetime(int(str(zxc)[0:4]), int(str(zxc)[4:6]), int(str(zxc)[6:8]), int(str(zxc)[8:10]), int(str(zxc)[10:12]), int(str(zxc)[12:14])))
    bobSendButton.place_forget()
    whatToDo['text'] =  "Автентифікація прошла успішно!"

    tryAgainButton = createButton("Try Again", tryAgain, None, None)
    tryAgainButton.place(relx=0.5, x = -30, rely = 0.9)


def addBobRandomValueinAliceButtonClick():
    addBobRandomValueinAliceButton.place_forget()
    aliceSendValue.set(datetime.datetime(int(str(bobRandomValueinAlice)[0:4]), int(str(bobRandomValueinAlice)[4:6]), int(str(bobRandomValueinAlice)[6:8]), int(str(bobRandomValueinAlice)[8:10]), int(str(bobRandomValueinAlice)[10:12]), int(str(bobRandomValueinAlice)[12:14])))

    aliceSendButton['text'] = "Crypt with Session's key"
    aliceSendButton['command'] = aliceSeventhStepCryptClick
    aliceSendButton.place(x=5+315, y=5-1)


def genAliceRandomValueClick():
    global aliceRandomValue

    aliceRandomValue = int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    aliceRandomValueValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))

    addAliceRandomValueButton['text'] = "Add to send"
    addAliceRandomValueButton['command'] = addAliceRandomValueClick

def addAliceRandomValueClick():
    addAliceRandomValueButton.place_forget()
    aliceSendValue.set("{Alice, "+str(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))+"}")

    aliceSendButton['text'] = "Crypt Bob's key"
    aliceSendButton['command'] = aliceThirdStepCryptClick
    aliceSendButton.place(x=5+315, y=5-1)

def addBobPublicKeyinTrentButtonClick():
    global trentSendButton
    global trentSendValue

    addBobPublicKeyinTrentButton.place_forget()
    trentSendLable = makeEntry(trentSendValue, 29).place(relx=0.5, y=9, x=-110+121, anchor=tk.N)
    trentSendButton = createButton("Sign", trentSecondStepSignClick, None, None, ('calibri', 14, 'bold'))
    trentSendButton.place(relx=0.5, y=5, x=-110+280, anchor=tk.N)
    trentSendValue.set(bobPublicKeyinTrent)

def addAlicePublicKeyinTrentButtonClick():
    addAlicePublicKeyinTrentButton.place_forget()

    trentSendButton['text'] = "Sign"
    trentSendButton['command'] = trentFifthStepFirstSignClick
    trentSendButton.place(relx=0.5, y=5, x=-110+280, anchor=tk.N)
    trentSendValue.set(alicePublicKeyinTrent)

def genSessioninTrentButtonClick():
    global sessionKeyinTrent

    sessionKeyinTrent = randrange(2**32, 2**33)
    sessionKeyinTrentValue.set(sessionKeyinTrent)
    addSessioninTrentButton['text'] = "Add to send"
    addSessioninTrentButton['command'] = addSessioninTrentButtonClick

def addSessioninTrentButtonClick():
    global addAliceRandomValueinTrentButton

    addSessioninTrentButton.place_forget()
    trentSendValue.set(sessionKeyinTrent)
    addAliceRandomValueinTrentButton = createButton("Add to send", addAliceRandomValueinTrentButtonClick, None, None)
    addAliceRandomValueinTrentButton.place(relx=0.5, y=40+29*4, x=xx+6-110+130, anchor=tk.N)


def addAliceRandomValueinTrentButtonClick():
    addAliceRandomValueinTrentButton.place_forget()
    trentSendValue.set((sessionKeyinTrent, aliceRandomValueinTrent))

    trentSendButton['text'] = "Sign"
    trentSendButton['command'] = trentFifthStepSecondSignClick
    trentSendButton.place(relx=0.5, y=5, x=-110+280, anchor=tk.N)

def addTrentSecondMessage():
    global bobSendToAlice
    global bobRandomValueValue
    global bobRandomValue
    global addBobRandomValueButton

    bobSendToAlice = ((encrypt(decrypt(trentSendToBob[1][0][0], bobPrivateKey), alicePublicKeyinBob), trentSendToBob[1][0][1]), (encrypt(decrypt(trentSendToBob[1][1][0], bobPrivateKey), alicePublicKeyinBob), trentSendToBob[1][1][1]))
    bobSendValue.set(bobSendToAlice) 

    bobSendButton.place_forget()

    bobRandomValueText = makeLabel("Bob Time value").place(relx=1, y=40+29*5, x=-5, rely=0, anchor=tk.NE) 
    bobRandomValueLable = makeEntry(bobRandomValueValue).place(relx=1, y=40+29*5, x=-xx, rely=0, anchor=tk.NE)

    addBobRandomValueButton = createButton("Gen", genBobRandomValueClick, None, None)
    addBobRandomValueButton.place(relx=1, y=40+29*5, x=-xx-170, rely=0, anchor=tk.NE)

def genBobRandomValueClick():
    global bobRandomValueValue
    global bobRandomValue

    addBobRandomValueButton['text'] = "Add to send"
    addBobRandomValueButton['command'] = addBobRandomValueClick

    bobRandomValue = int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    bobRandomValueValue.set(datetime.datetime(int(str(bobRandomValue)[0:4]), int(str(bobRandomValue)[4:6]), int(str(bobRandomValue)[6:8]), int(str(bobRandomValue)[8:10]), int(str(bobRandomValue)[10:12]), int(str(bobRandomValue)[12:14])))


def addBobRandomValueClick():
    global bobSendToAlice
    addBobRandomValueButton.place_forget()

    bobSendToAlice = (bobRandomValue, bobSendToAlice)
    bobSendValue.set(bobSendToAlice)

    bobSendButton['text'] = "Send"
    bobSendButton['command'] = bobSixthStepSendClick
    bobSendButton.place(relx=1, y=5-1, x=-5-315, rely=0, anchor=tk.NE)



# PROGRAM ENTRY
def startGen():



    global generateAliceKeyButton
    global generateBobKeyButton
    global generateTrentKeyButton
    global whatToDo

    alice = makeLabel("ID:Alice", ('calibri', 16, 'bold'), 6).place(x=5, y=5)
    alicePublicKeyText = makeLabel("Alice Public key").place(x=5, y=40)
    alicePublicKeyLable = makeEntry(alicePublicKeyValue).place(x=xx, y=40)

    alicePrivateKeyText = makeLabel("Alice Private key").place(x=5, y=40+29)
    alicePrivateKeyLable = makeEntry(alicePrivateKeyValue).place(x=xx, y=40+29)
    generateAliceKeyButton = createButton("Gen", generateAliceKey, 2)
    generateAliceKeyButton.place(x=xx+xb, y=40+4)


    bob = makeLabel("ID:Bob", ('calibri', 16, 'bold'), 6).place(relx=1, y=5, x=-5, rely=0, anchor=tk.NE)
    bobPublicKeyText = makeLabel("Bob's Public key").place(relx=1, y=40, x=-5, rely=0, anchor=tk.NE)
    bobPublicKeyLable = makeEntry(bobPublicKeyValue).place(relx=1, y=40, x=-xx, rely=0, anchor=tk.NE)

    bobPrivateKeyText = makeLabel("Bob's Private key").place(relx=1, y=40+29, x=-5, rely=0, anchor=tk.NE) 
    bobPrivateKeyLable = makeEntry(bobPrivateKeyValue).place(relx=1, y=40+29, x=-xx, rely=0, anchor=tk.NE)
    generateBobKeyButton = createButton("Gen", generateBobKey, 2)
    generateBobKeyButton.place(relx=1, y=40+4, x=-xx-xb, rely=0, anchor=tk.NE)


    trent = makeLabel("ID:Trent", ('calibri', 16, 'bold'), 6).place(relx=0.5, y=5, x=-110-35, anchor=tk.N)
    trentPublicKeyText = makeLabel("Trent's Public key").place(relx=0.5, y=40, x=-110, anchor=tk.N)
    trentPublicKeyLable = makeEntry(trentPublicKeyValue).place(relx=0.5, y=40, x=xx+6-110, anchor=tk.N)
    generateTrentKeyButton = createButton("Gen", generateTrentKey, 2)
    generateTrentKeyButton.place(relx=0.5, x=-164+xx+xb, y=40+4, anchor=tk.N)

    trentPrivateKeyText = makeLabel("Trent's Private key").place(relx=0.5, y=40+29, x=-110, anchor=tk.N)
    trentPrivateKeyLable = makeEntry(trentPrivateKeyValue).place(relx=0.5, y=40+29, x=xx+6-110, anchor=tk.N)

    whatToDo = makeLabel("Крок 0", ('calibri', 14, 'bold'))
    whatToDo.place(relx=0.5, y=140, x=-50, rely=0.6, anchor=tk.W)


def firstStep():
    global aliceSendValue
    global aliceSendButton
    global ___

    alicePublicKeyValue.set(alicePublicKey)
    alicePrivateKeyValue.set(alicePrivateKey)
    alicePublicKeyinTrentValue.set(alicePublicKey)

    bobPublicKeyValue.set(bobPublicKey)
    bobPrivateKeyValue.set(bobPrivateKey)
    bobPublicKeyinTrentValue.set(bobPublicKey)

    trentPublicKeyValue.set(trentPublicKey)
    trentPrivateKeyValue.set(trentPrivateKey)
    trentPublicKeyinAliceValue.set(trentPublicKey)
    trentPublicKeyinBobValue.set(trentPublicKey)


    whatToDo['text'] = "Крок 1"

    aliceSendLable = makeEntry(aliceSendValue, 29).place(x=5+74, y=5+3)
    aliceSendButton = createButton("Send", aliceFirstStepSendClick, None, None, ('calibri', 14, 'bold'))
    aliceSendButton.place(x=5+315, y=5-1)
    aliceSendValue.set("{Alice, Bob}")

    ___ = tk.Label(
        root, 
        text="------------------------------------->",
        font=('calibri', 14, 'bold'),
        fg="white",
        bg='#852c3b',
        highlightthickness=0,
        borderwidth='1')
    ___.place(y=240, x=320)
    
   
def secondStep():
    global addBobPublicKeyinTrentButton
    global ___

    aliceSendButton.place_forget()
    aliceSendValue.set("")

    alicePublicKeyValue.set(alicePublicKey)
    alicePrivateKeyValue.set(alicePrivateKey)
    alicePublicKeyinTrentValue.set(alicePublicKey)

    bobPublicKeyValue.set(bobPublicKey)
    bobPrivateKeyValue.set(bobPrivateKey)
    bobPublicKeyinTrentValue.set(bobPublicKey)

    trentPublicKeyValue.set(trentPublicKey)
    trentPrivateKeyValue.set(trentPrivateKey)
    trentPublicKeyinAliceValue.set(trentPublicKey)
    trentPublicKeyinBobValue.set(trentPublicKey)  

    whatToDo['text'] = "Крок 2"
    ___['text'] = "<-------------------------------------"
    ___.place(y=240, x=320)
   

    addBobPublicKeyinTrentButton = createButton("Add to send", addBobPublicKeyinTrentButtonClick, None, None)
    addBobPublicKeyinTrentButton.place(relx=0.5, y=40+29*3, x=xx+6-110+130, anchor=tk.N)

def thirdStep():
    global bobPublicKeyinAliceValue
    global bobPublicKeyinAlice
    global aliceRandomValueValue
    global ___

    trentSendButton.place_forget()
    aliceSendValue.set(trentSendToAlice)
    trentSendValue.set("")

    alicePublicKeyValue.set(alicePublicKey)
    alicePrivateKeyValue.set(alicePrivateKey)
    alicePublicKeyinTrentValue.set(alicePublicKey)

    bobPublicKeyValue.set(bobPublicKey)
    bobPrivateKeyValue.set(bobPrivateKey)
    bobPublicKeyinTrentValue.set(bobPublicKey)

    trentPublicKeyValue.set(trentPublicKey)
    trentPrivateKeyValue.set(trentPrivateKey)
    trentPublicKeyinAliceValue.set(trentPublicKey)
    trentPublicKeyinBobValue.set(trentPublicKey)

    whatToDo['text'] = "Крок 3"

    bobPublicKeyinAlice = trentSendToAlice[1]
    bobPublicKeyinAliceText = makeLabel("Bob's Public key").place(x=5, y=40+29*3)
    bobPublicKeyinAliceLable = makeEntry(bobPublicKeyinAliceValue).place(x=xx, y=40+29*3)
    bobPublicKeyinAliceValue.set(bobPublicKeyinAlice)

    aliceSendButton['text'] = "Verify"
    aliceSendButton['command'] = aliceThirdStepVerifyClick
    aliceSendButton.place(x=5+315, y=5-1)

    aliceRandomValueText = makeLabel("Alice Time value").place(x=5, y=40+29*4)
    aliceRandomValueLable = makeEntry(aliceRandomValueValue).place(x=xx, y=40+29*4)

    ___['text'] = "------------------------------------------------------------------------------------------------------------------------------------------>",
    ___.place(y=240, x=320)

def fourthStep():
    global bobSendButton
    global bobSendValue
    global ___

    aliceSendButton.place_forget()
    aliceSendValue.set("")

    alicePublicKeyValue.set(alicePublicKey)
    alicePrivateKeyValue.set(alicePrivateKey)
    alicePublicKeyinTrentValue.set(alicePublicKey)
    aliceRandomValueValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))

    bobPublicKeyValue.set(bobPublicKey)
    bobPrivateKeyValue.set(bobPrivateKey)
    bobPublicKeyinAliceValue.set(bobPublicKeyinAlice)
    bobPublicKeyinTrentValue.set(bobPublicKey)

    trentPublicKeyValue.set(trentPublicKey)
    trentPrivateKeyValue.set(trentPrivateKey)
    trentPublicKeyinAliceValue.set(trentPublicKey)
    trentPublicKeyinBobValue.set(trentPublicKey)

    whatToDo['text'] = "Крок 4"

    ___['text'] = "<----------------------------------------------"
    ___.place(y=240, x=870)


    bobSendLable = makeEntry(bobSendValue, 29).place(relx=1, y=5+3, x=-5-74, rely=0, anchor=tk.NE)
    bobSendButton = createButton("Decrypt with Bob's PrKey", bobFourthStepDecryptClick, None, None, ('calibri', 14, 'bold'))
    bobSendButton.place(relx=1, y=5-1, x=-5-315, rely=0, anchor=tk.NE)
    bobSendValue.set(aliceSendToBob)


def fifthStep():
    global ___
    bobSendButton.place_forget()
    bobSendValue.set("")

    alicePublicKeyValue.set(alicePublicKey)
    alicePrivateKeyValue.set(alicePrivateKey)
    alicePublicKeyinTrentValue.set(alicePublicKey)
    aliceRandomValueValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))
    aliceRandomValueinBobValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))

    bobPublicKeyValue.set(bobPublicKey)
    bobPrivateKeyValue.set(bobPrivateKey)
    bobPublicKeyinAliceValue.set(bobPublicKeyinAlice)
    bobPublicKeyinTrentValue.set(bobPublicKey)

    trentPublicKeyValue.set(trentPublicKey)
    trentPrivateKeyValue.set(trentPrivateKey)
    trentPublicKeyinAliceValue.set(trentPublicKey)
    trentPublicKeyinBobValue.set(trentPublicKey)

    trentSendValue.set(bobSendToTrent)
    trentSendButton['text'] = "Decrypt with Trent's PrKey"
    trentSendButton['command'] = trentFifthStepDecryptClick
    trentSendButton.place(relx=0.5, y=5, x=-154+395, anchor=tk.N)

    whatToDo['text'] = "Крок 5"

    ___['text'] = "---------------------------------------------->"
    ___.place(y=240, x=870)


def sixthStep():
    trentSendButton.place_forget()
    trentSendValue.set("")

    alicePublicKeyValue.set(alicePublicKey)
    alicePrivateKeyValue.set(alicePrivateKey)
    alicePublicKeyinTrentValue.set(alicePublicKey)
    aliceRandomValueValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))
    aliceRandomValueinBobValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))
    aliceRandomValueinTrentValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))

    bobPublicKeyValue.set(bobPublicKey)
    bobPrivateKeyValue.set(bobPrivateKey)
    bobPublicKeyinAliceValue.set(bobPublicKeyinAlice)
    bobPublicKeyinTrentValue.set(bobPublicKey)

    trentPublicKeyValue.set(trentPublicKey)
    trentPrivateKeyValue.set(trentPrivateKey)
    trentPublicKeyinAliceValue.set(trentPublicKey)
    trentPublicKeyinBobValue.set(trentPublicKey)
    sessionKeyinTrentValue.set(sessionKeyinTrent)

    bobSendValue.set(trentSendToBob)
    bobSendButton['text'] = "Verify"
    bobSendButton['command'] = bobsixthStepVerifyClick
    bobSendButton.place(relx=1, y=5-1, x=-5-315, rely=0, anchor=tk.NE)

    whatToDo['text'] =  "Крок 6"

    global ___
    ___['text'] = "<------------------------------------------------------------------------------------------------------------------------------------------",
    ___.place(y=240, x=320)

def seventhStep():
    bobSendButton.place_forget()
    bobSendValue.set("")

    alicePublicKeyValue.set(alicePublicKey)
    alicePrivateKeyValue.set(alicePrivateKey)
    alicePublicKeyinTrentValue.set(alicePublicKey)
    alicePublicKeyinBobValue.set(alicePublicKeyinBob)
    aliceRandomValueValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))
    aliceRandomValueinBobValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))
    aliceRandomValueinTrentValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))

    bobPublicKeyValue.set(bobPublicKey)
    bobPrivateKeyValue.set(bobPrivateKey)
    bobPublicKeyinAliceValue.set(bobPublicKeyinAlice)
    bobPublicKeyinTrentValue.set(bobPublicKey)
    bobRandomValueValue.set(datetime.datetime(int(str(bobRandomValue)[0:4]), int(str(bobRandomValue)[4:6]), int(str(bobRandomValue)[6:8]), int(str(bobRandomValue)[8:10]), int(str(bobRandomValue)[10:12]), int(str(bobRandomValue)[12:14])))
    sessionKeyBobValue.set(sessionKeyBob)

    trentPublicKeyValue.set(trentPublicKey)
    trentPrivateKeyValue.set(trentPrivateKey)
    trentPublicKeyinAliceValue.set(trentPublicKey)
    trentPublicKeyinBobValue.set(trentPublicKey)
    sessionKeyinTrentValue.set(sessionKeyinTrent)

    aliceSendValue.set(bobSendToAlice)
    aliceSendButton['text'] = "Verify"
    aliceSendButton['command'] = bobseventhStepVerifyClick
    aliceSendButton.place(x=5+315, y=5-1)

    whatToDo['text'] =  "Крок 7"

    global ___
    ___['text'] = "------------------------------------------------------------------------------------------------------------------------------------------>",
    ___.place(y=240, x=320)

def finalStep():
    aliceSendValue.set("")
    aliceSendButton.place_forget()
    ___.place_forget()
    whatToDo.place_forget()

    alicePublicKeyValue.set(alicePublicKey)
    alicePrivateKeyValue.set(alicePrivateKey)
    alicePublicKeyinTrentValue.set(alicePublicKey)
    alicePublicKeyinBobValue.set(alicePublicKeyinBob)
    aliceRandomValueValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))
    aliceRandomValueinBobValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))
    aliceRandomValueinTrentValue.set(datetime.datetime(int(str(aliceRandomValue)[0:4]), int(str(aliceRandomValue)[4:6]), int(str(aliceRandomValue)[6:8]), int(str(aliceRandomValue)[8:10]), int(str(aliceRandomValue)[10:12]), int(str(aliceRandomValue)[12:14])))
    sessionKeyAliceValue.set(sessionKeyAlice)

    bobPublicKeyValue.set(bobPublicKey)
    bobPrivateKeyValue.set(bobPrivateKey)
    bobPublicKeyinTrentValue.set(bobPublicKey)
    bobRandomValueValue.set(datetime.datetime(int(str(bobRandomValue)[0:4]), int(str(bobRandomValue)[4:6]), int(str(bobRandomValue)[6:8]), int(str(bobRandomValue)[8:10]), int(str(bobRandomValue)[10:12]), int(str(bobRandomValue)[12:14])))
    bobPublicKeyinAliceValue.set(bobPublicKeyinAlice)
    sessionKeyBobValue.set(sessionKeyBob)
    bobRandomValueinAliceValue.set(datetime.datetime(int(str(bobRandomValue)[0:4]), int(str(bobRandomValue)[4:6]), int(str(bobRandomValue)[6:8]), int(str(bobRandomValue)[8:10]), int(str(bobRandomValue)[10:12]), int(str(bobRandomValue)[12:14])))

    trentPublicKeyValue.set(trentPublicKey)
    trentPrivateKeyValue.set(trentPrivateKey)
    trentPublicKeyinAliceValue.set(trentPublicKey)
    trentPublicKeyinBobValue.set(trentPublicKey)
    sessionKeyinTrentValue.set(sessionKeyinTrent)

    bobSendValue.set(aliceSendToBob)
    bobSendButton['text'] = "Decrypt"
    bobSendButton['command'] = bobFinalStepDecryptClick
    bobSendButton.place(relx=1, y=5-1, x=-5-315, rely=0, anchor=tk.NE)

    # whatToDo['text'] =  "Кінець"

def tryAgain():
    global click3gen
    aliceSendValue.set("")
    alicePublicKeyValue.set("")
    alicePrivateKeyValue.set("")
    alicePublicKeyinTrentValue.set("")
    alicePublicKeyinBobValue.set("")
    aliceRandomValueValue.set("")
    aliceRandomValueinBobValue.set("")
    aliceRandomValueinTrentValue.set("")
    sessionKeyAliceValue.set("")

    bobSendValue.set("")
    bobPublicKeyValue.set("")
    bobPrivateKeyValue.set("")
    bobPublicKeyinTrentValue.set("")
    bobPublicKeyinAliceValue.set("")
    bobRandomValueValue.set("")
    sessionKeyBobValue.set("")
    bobRandomValueinAliceValue.set("")

    trentSendValue.set("")
    trentPublicKeyValue.set("")
    trentPrivateKeyValue.set("")
    trentPublicKeyinAliceValue.set("")
    trentPublicKeyinBobValue.set("")
    sessionKeyinTrentValue.set("")
    tryAgainButton.place_forget()

    click3gen = 0
    startGen()

alicePublicKeyinTrentText = makeLabel("Alice Public key").place(relx=0.5, y=40+29*2, x=-110, anchor=tk.N)
alicePublicKeyinTrentLable = makeEntry(alicePublicKeyinTrentValue).place(relx=0.5, y=40+29*2, x=xx+6-110, anchor=tk.N)
bobPublicKeyinTrentText = makeLabel("Bob's Public key").place(relx=0.5, y=40+29*3, x=-110, anchor=tk.N)
bobPublicKeyinTrentLable = makeEntry(bobPublicKeyinTrentValue).place(relx=0.5, y=40+29*3, x=xx+6-110, anchor=tk.N)
bobPublicKeyinAliceText = makeLabel("Bob's Public key").place(x=5, y=40+29*3)
bobPublicKeyinAliceLable = makeEntry(bobPublicKeyinAliceValue).place(x=xx, y=40+29*3)
trentPublicKeyinAliceText = makeLabel("Trent Public key").place(x=5, y=40+29*2)
trentPublicKeyinAliceLable = makeEntry(trentPublicKeyinAliceValue).place(x=xx, y=40+29*2)
trentPublicKeyinBobText = makeLabel("Trent Public key").place(relx=1, y=40+29*2, x=-5, rely=0, anchor=tk.NE)
trentPublicKeyinBobLable = makeEntry(trentPublicKeyinBobValue).place(relx=1, y=40+29*2, x=-xx, rely=0, anchor=tk.NE)
aliceRandomValueText = makeLabel("Alice Time value").place(x=5, y=40+29*4)
aliceRandomValueLable = makeEntry(aliceRandomValueValue).place(x=xx, y=40+29*4)
aliceRandomValueinBobText = makeLabel("Alice Time value").place(relx=1, y=40+29*4, x=-5, rely=0, anchor=tk.NE)
aliceRandomValueinBobLable = makeEntry(aliceRandomValueinBobValue).place(relx=1, y=40+29*4, x=-xx, rely=0, anchor=tk.NE)
aliceRandomValueinTrentText = makeLabel("Alice Time value").place(relx=0.5, y=40+29*4, x=-110, anchor=tk.N)
aliceRandomValueinTrentLable = makeEntry(aliceRandomValueinTrentValue).place(relx=0.5, y=40+29*4, x=xx+6-110, anchor=tk.N)
sessionKey = makeLabel("Session Key").place(relx=0.5, y=40+29*5, x=-110, anchor=tk.N)
sessionKeyLable = makeEntry(sessionKeyinTrentValue).place(relx=0.5, y=40+29*5, x=xx+6-110, anchor=tk.N)
alicePublicKeyinBobText = makeLabel("Alice Public key").place(relx=1, y=40+29*3, x=-5, rely=0, anchor=tk.NE)
alicePublicKeyinBobLable = makeEntry(alicePublicKeyinBobValue).place(relx=1, y=40+29*3, x=-xx, rely=0, anchor=tk.NE)
sessionKeyBob1 = makeLabel("Session Key").place(relx=1, y=40+29*6, x=-5, rely=0, anchor=tk.NE)
sessionKeyBobLable = makeEntry(sessionKeyBobValue).place(relx=1, y=40+29*6, x=-xx, rely=0, anchor=tk.NE)
bobRandomValueinAliceText = makeLabel("Bob Time value").place(x=5, y=40+29*5)
bobRandomValueinAliceLable = makeEntry(bobRandomValueinAliceValue).place(x=xx, y=40+29*5)
sessionKeyAlice = makeLabel("Session Key").place(x=5, y=40+29*6)
sessionKeyAliceLable = makeEntry(sessionKeyAliceValue).place(x=xx, y=40+29*6)
bobRandomValueText = makeLabel("Bob Time value").place(relx=1, y=40+29*5, x=-5, rely=0, anchor=tk.NE) 
bobRandomValueLable = makeEntry(bobRandomValueValue).place(relx=1, y=40+29*5, x=-xx, rely=0, anchor=tk.NE)

startGen()


root.mainloop()
