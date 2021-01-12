
# Squared Euclidean Distance

import sys
import json

def sqed( N, M, K, p, q ):
    total = 0
    try:
        for i in xrange(N*M): 
            for k in xrange(K):
                total += (p[k][i]-q[k][i]) ** 2
    except IndexError:
        pass 
    d = total / (N*M*K)
    return d

#def main(N, M, K, pfilename, qfilename):
def main():
    try:
        N = int(sys.argv[1])
        M = int(sys.argv[2])
        K = int(sys.argv[3])
        pfilename = sys.argv[4]
        qfilename = sys.argv[5]
    except IndexError:
        print >>sys.stderr, "usage: {0} N M K p.json q.json".format(sys.argv[0])
        return

    with open(pfilename) as f:
        p = json.load(f)

    with open(qfilename) as f:
        q = json.load(f)

    print sqed( N, M, K, p[1:], q[1:len(p)])

def mean_error_calculator(N, M, K, pfilename, qfilename):


    with open(pfilename) as f:
        p = json.load(f)

    with open(qfilename) as f:
        q = json.load(f)



    return sqed( N, M, K, p[1:], q[1:])



if __name__ == "__main__":
    main()