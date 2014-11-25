#constants
fullround=31

#S-Box Layer
sbox=[0xC,0x5,0x6,0xB,0x9,0x0,0xA,0xD,0x3,0xE,0xF,0x8,0x4,0x7,0x1,0x2]
sbox_inv = [sbox.index(x) for x in xrange(16)]

#PLayer
pmt=[0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,\
     4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,\
     8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,\
     12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63]

pmt_inv = [pmt.index(x) for x in xrange(64)]

# Rotate left: 0b1001 --> 0b0011
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def genRoundKeys(key):
    roundkeys = []

    for i in xrange(1, fullround + 2):
        roundkeys.append(key >> 16)
        new_key= rol(key,61,80)

        new_key = format(new_key, "080b")
        new_key04 = sbox[int(new_key[0:4],2)]
        new_key = format(new_key04,"04b") + new_key[4:80]
        new_key = int(new_key, 2)

        new_key = new_key ^ (i << 15)

        key = new_key


    return roundkeys




def addRoundKey(state,Ki):
    state = state ^ Ki
    return state

def sBoxLayer(state):
    state = format(state,"016x")
    newstate = ""
    for c in state:
        c = "0x"+c
        x = int(c,16)
        newstate = newstate + str(hex(sbox[x]))[2]
    newstate = int(newstate,16)
    return newstate

def sBoxLayer_dec(state):
    state = format(state,"016x")
    newstate = ""
    for c in state:
        c = "0x"+c
        x = int(c,16)
        newstate = newstate + str(hex(sbox_inv[x]))[2]
    newstate = int(newstate,16)
    return newstate


def pLayer(state):
    new_state = [None]*64

    bits = format(state,"064b")
    for i in range(len(bits)):
        new_pos = pmt[i]
        new_state[new_pos] = bits[i]

    new_state = "".join(new_state)
    new_state = int(new_state,2)
    return new_state

def pLayer_dec(state):
    new_state = [None]*64

    bits = format(state,"064b")
    for i in range(len(bits)):
        new_pos = pmt_inv[i]
        new_state[new_pos] = bits[i]

    new_state = "".join(new_state)
    new_state = int(new_state,2)
    return new_state

def present_rounds(plain, key, rounds):
    roundkeys = genRoundKeys(key)
    state = plain
    for i in xrange(rounds):
        state = addRoundKey(state, roundkeys[i])
        state = sBoxLayer(state)
        state = pLayer(state)
    state = addRoundKey(state,roundkeys[-1])

    return state

def present_inv_rounds(cipher, key, rounds):
    state = cipher
    roundkeys = genRoundKeys(key)

    for i in xrange(rounds):
        state = addRoundKey(state, roundkeys[-i-1])
        state = pLayer_dec(state)
        state = sBoxLayer_dec(state)
    decipher = addRoundKey(state, roundkeys[0])
    return decipher



def present(plain, key):
    return present_rounds(plain, key, fullround)

def present_inv(cipher, key):
    return present_inv_rounds(cipher, key, fullround)

if __name__=="__main__":
    plain1=0x0000000000000000
    key1=0x00000000000000000000
    cipher1= present(plain1,key1)
    plain11 = present_inv(cipher1,key1)
    print format(cipher1,'x')
    print format(plain11,'x')
    plain2=0x0000000000000000
    key2=0xFFFFFFFFFFFFFFFFFFFF
    cipher2= present(plain2,key2)
    plain22 = present_inv(cipher2,key2)
    print format(cipher2,'x')
    print format(plain22,'x')
    plain3=0xFFFFFFFFFFFFFFFF
    key3=0x00000000000000000000
    cipher3= present(plain3,key3)
    plain33 = present_inv(cipher3,key3)
    print format(cipher3,'x')
    print format(plain33,'x')
    plain4=0xFFFFFFFFFFFFFFFF
    key4=0xFFFFFFFFFFFFFFFFFFFF
    cipher4= present(plain4,key4)
    plain44 = present_inv(cipher4,key4)
    print format(cipher4,'x')
    print format(plain44,'x')