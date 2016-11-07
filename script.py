
#Does a beautiful key_gen have beautiful code?

lookup_table = list('!$%&/()=?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
serial = list()
import sys

def keygen(username):
        username = list(username)
        serial.append(username[0])
        for i in range(1,9):
                if (i<len(username)):
                        A = ord(serial[i-1])+ord(username[i])
                        B = hex(A * (0xe6c2b448))[2:4]

                else:
                        A = ord(serial[i-1])
                        B = hex(A * (0xe6c2b448))[2:4]

                C = int(B,16)
                D = C>>6
                saved = D
                E = D<<3
                H = E + saved
                G = H<<3
                F = G-saved
                K = A - F
                lookup = lookup_table[K]
                serial.append(lookup)
        A = ~ord(serial[8])
        B = hex(A & (2**32-1))
        C = hex(int(B,16)*(int('e6c2b449',16)))[2:10]
        D = int(C,16)
        E = D>>6
        saved = E
        F = E<<3
        G = F+saved
        K = G<<3
        K = hex(K)[4:]
        lala = int(K,16) - saved
        K=(lookup_table[A-lala])
        serial.append(K)
        return serial
keygen(sys.argv[1])
print("".join(serial))
