import math
import primes

def find_m(p):
    return int(math.floor(math.pow(p-1,0.5)))

def baby_step(alpha,beta,p,m,baby_list):
    for i in xrange(m):
        # res = math.pow(alpha,i)*beta
        res = (primes.square_multiply(alpha,i,p) * beta ) % p
        baby_list.append(res)

def giant_step(alpha,p,m,giant_list):
    for i in xrange(m):
        res = primes.square_multiply(alpha, (m*i), p)
        giant_list.append(res)

def baby_giant(alpha,beta,p):
    baby_list = []
    giant_list = []
    m = find_m(p)
    baby_step(alpha,beta,p,m,baby_list)
    giant_step(alpha,p,m,giant_list)
    xg = 0
    xb = 0
    found = False
    for i in xrange(len(baby_list)):
        if found == True:
            break
        for j in xrange(len(giant_list)):
            if baby_list[i] == giant_list[j]:
                xg,xb = j, i
                found = True
                # print i, baby_list[i]
                # print j, giant_list[j]
                break

    # print "xg:",xg, "xb:", xb
    answer = xg * m - xb
    return answer


if __name__=="__main__":
    """
    test 1
    My private key is:  264
    Test other private key is:  7265

    """
    p=17851
    print find_m(p)
    alpha=17511
    A=2945
    B=11844
    sharedkey=1671
    a=baby_giant(alpha,A,p)
    b=baby_giant(alpha,B,p)
    print a, b
    guesskey1=primes.square_multiply(A,b,p)
    guesskey2=primes.square_multiply(B,a,p)
    print 'Guess key 1:',guesskey1
    print 'Guess key 2:',guesskey2
    print 'Actual shared key :',sharedkey

