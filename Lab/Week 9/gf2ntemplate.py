import math
import numpy as np
class Polynomial2:
    def __init__(self,coeffs):
        self.coeffs = coeffs

    def add(self,p2):
        len_1 = len(self.coeffs)
        len_2 = len(p2.coeffs)
        if len_1 > len_2:
            p2.coeffs += [0]*(len_1-len_2)
        elif len_1 < len_2:
            self.coeffs += [0]*(len_2-len_1)
        new_coeffs = [a ^ b for a,b in zip(self.coeffs, p2.coeffs)]
        return Polynomial2(new_coeffs[:])

    def sub(self,p2):
        return self.add(p2)

    def mul(self,p2,modp=None):
        partials = []
        if modp != None:
            modp_len = len(modp.coeffs)
            self = self.add(Polynomial2([0 for a in range(modp_len)]))
            p2 = p2.add(Polynomial2([0 for a in range(modp_len)]))
            for i in range(len(self.coeffs)):
                if i == 0:
                    result = p2.coeffs
                else:
                    result = [0] + result[:-1]
                    if result[-1] == 1:
                        result = (Polynomial2(result).sub(modp)).coeffs
                partials.append(result)

            new_p = Polynomial2([0])
            for i in range(len(self.coeffs)):
                if self.coeffs[i] == 1:
                    new_p = new_p.add(Polynomial2(partials[i]))
            return new_p
        else:
            for i in range(len(self.coeffs)):
                if self.coeffs[i] == 1:
                    partial = [0]*i + p2.coeffs[:]
                    partials.append(partial)
            new_p = Polynomial2([0])
            for partial in partials:
                new_p = new_p.add(Polynomial2(partial))
            return new_p

    def div(self,p2):
        q = Polynomial2([0])
        r = Polynomial2(self.coeffs[:])
        b = Polynomial2(p2.coeffs[:])
        d = b.deg()
        c = b.lc()

        while r.deg() >= d:
            s_coeffs = [0]*(r.deg() - d) + [r.lc()/c]
            s = Polynomial2(s_coeffs)
            q = q.add(s)
            r = r.sub(s.mul(b))
        return q, r

    def deg(self):
        for i in range(len(self.coeffs))[::-1]:
            if self.coeffs[i] == 1:
                return i-1
        return None

    def lc(self):
        for i in range(len(self.coeffs))[::-1]:
            if self.coeffs[i] == 1:
                return 1
        return 0

    def __str__(self):
        s = ""
        first_term = True
        for i in range(len(self.coeffs)):
            if self.coeffs[i] == 1:
                if first_term == False:
                    s = ("x^%d+")%(i) + s
                else:
                    s = ("x^%d")%(i) + s
                    first_term = False
        return s

    def getInt(p):
        r = 0
        for i in range(len(p.coeffs)):
            if p.coeffs[i] == 1: r += math.pow(2,i)



class GF2N:
    affinemat=[[1,0,0,0,1,1,1,1],
               [1,1,0,0,0,1,1,1],
               [1,1,1,0,0,0,1,1],
               [1,1,1,1,0,0,0,1],
               [1,1,1,1,1,0,0,0],
               [0,1,1,1,1,1,0,0],
               [0,0,1,1,1,1,1,0],
               [0,0,0,1,1,1,1,1]]

    def __init__(self,x,n=8,ip=Polynomial2([1,1,0,1,1,0,0,0,1])):
        self.x = x
        self.n = n
        self.ip = ip
        self.coeffs =[int(d) for d in bin(self.x)[2:][::-1]]

    def add(self,g2):
        p = Polynomial2(self.coeffs).add(Polynomial2(g2.coeffs))
        x = int("".join([str(a) for a in p.coeffs[::-1]]),2)
        return GF2N(x,self.n,self.ip)

    def sub(self,g2):
        p = Polynomial2(self.coeffs).add(Polynomial2(g2.coeffs))
        x = int("".join([str(a) for a in p.coeffs[::-1]]),2)
        return GF2N(x,self.n,self.ip)

    def mul(self,g2):
        p = Polynomial2(self.coeffs).mul(Polynomial2(g2.coeffs),self.ip)
        x = int("".join([str(a) for a in p.coeffs[::-1]]),2)
        return GF2N(x,self.n,self.ip)

    def div(self,g2):
        q,r = Polynomial2(self.coeffs).div(Polynomial2(g2.coeffs))
        q_x = int("".join([str(a) for a in q.coeffs[::-1]]),2)
        r_x = int("".join([str(a) for a in r.coeffs[::-1]]),2)
        return GF2N(q_x,self.n,self.ip), GF2N(r_x,self.n,self.ip)

    def getPolynomial2(self):
        s = ""
        first_term = True
        for i in range(len(self.coeffs)):
            if self.coeffs[i] == 1:
                if first_term == False:
                    s = ("x^%d+")%(i) + s
                else:
                    s = ("x^%d")%(i) + s
                    first_term = False
        return s

    def __str__(self):
        return str(self.x)

    def getInt(self):
        r = 0
        for i in range(len(self.coeffs)):
            if self.coeffs[i] == 1: r += math.pow(2,i)
        return int(r)

    def mulInv(self):
        r1 = self.ip
        r2 = Polynomial2(self.coeffs[:])
        t1 = Polynomial2([0]*len(r1.coeffs))
        t2 = Polynomial2([1]+([0]*(len(r1.coeffs)-1)))

        x = int("".join([str(a) for a in r2.coeffs[::-1]]),2)
        while (x != 0):
            q,r= r1.div(r2)
            r1 = r2
            r2 = r

            t = t1.sub(q.mul(t2))
            t1 = t2
            t2 = t

            x = int("".join([str(a) for a in r2.coeffs[::-1]]),2)

        if (int("".join([str(a) for a in r1.coeffs[::-1]]),2) == 1):
            x = int("".join([str(a) for a in t1.coeffs[::-1]]),2)
            return GF2N(x)
        else:
            print "cannot reduce..."
            return GF2N(0)


    def affineMap(self):
        mat = np.matrix(self.affinemat)
        add_zeros = 8 - len(self.coeffs)
        biprime = np.matrix(self.coeffs+[0]*add_zeros).getT()
        c = np.matrix([1,1,0,0,0,1,1,0]).getT()

        result = np.array(mat*biprime+c)
        result = result.reshape(-1).tolist()

        for i in range(len(result)):
            result[i] = result[i] % 2

        x = int("".join([str(a) for a in result[::-1]]),2)
        return GF2N(x)





print '\nTest 1'
print '======'
print 'p1=x^5+x^2+x'
print 'p2=x^3+x^2+1'
p1=Polynomial2([0,1,1,0,0,1])
p2=Polynomial2([1,0,1,1])
p3=p1.add(p2)
print 'p3= p1+p2 = ',p3

print '\nTest 2'
print '======'
print 'p4=x^7+x^4+x^3+x^2+x'
print 'modp=x^8+x^7+x^5+x^4+1'
p4=Polynomial2([0,1,1,1,1,0,0,1])
modp=Polynomial2([1,1,0,1,1,0,0,0,1])
p5=p1.mul(p4,modp)
print 'p5=p1*p4 mod (modp)=',p5

print '\nTest 3'
print '======'
print 'p6=x^12+x^7+x^2'
print 'p7=x^8+x^4+x^3+x+1'
p6=Polynomial2([0,0,1,0,0,0,0,1,0,0,0,0,1])
p7=Polynomial2([1,1,0,1,1,0,0,0,1])
p8q,p8r=p6.div(p7)
print 'q for p6/p7=',p8q
print 'r for p6/p7=',p8r

####
print '\nTest 4'
print '======'
g1=GF2N(100)
g2=GF2N(5)
print 'g1 = ',g1.getPolynomial2()
print 'g2 = ',g2.getPolynomial2()
g3=g1.add(g2)
print 'g1+g2 = ',g3

print '\nTest 5'
print '======'
ip=Polynomial2([1,1,0,0,1])
print 'irreducible polynomial',ip
g4=GF2N(0b1101,4,ip)
g5=GF2N(0b110,4,ip)
print 'g4 = ',g4.getPolynomial2()
print 'g5 = ',g5.getPolynomial2()
g6=g4.mul(g5)
print 'g4 x g5 = ',g6.getPolynomial2()

print '\nTest 6'
print '======'
g7=GF2N(0b1000010000100,13,None)
g8=GF2N(0b100011011,13,None)
print 'g7 = ',g7.getPolynomial2()
print 'g8 = ',g8.getPolynomial2()
q,r=g7.div(g8)
print 'g7/g8 ='
print 'q = ',q.getPolynomial2()
print 'r = ',r.getPolynomial2()

print '\nTest 7'
print '======'
ip=Polynomial2([1,1,0,0,1])
print 'irreducible polynomial',ip
g9=GF2N(0b101,4,ip)
print 'g9 = ',g9.getPolynomial2()
print 'inverse of g9 =',g9.mulInv().getPolynomial2()

print '\nTest 8'
print '======'
ip=Polynomial2([1,1,0,1,1,0,0,0,1])
print 'irreducible polynomial',ip
g10=GF2N(0xc2,8,ip)
print 'g10 = 0xc2'
g11=g10.mulInv()
print 'inverse of g10 = g11 =', hex(g11.getInt())
g12=g11.affineMap()
print 'affine map of g11 =',hex(g12.getInt())
