from matplotlib import pyplot
from TermoCount import TermoCount

def TermoGraph():
    
    E = TermoCount("E")
    J = TermoCount("J")
    N = TermoCount("N")
    T = TermoCount("T")
    K = TermoCount("K")

    pyplot.plot(E)
    pyplot.text(300,E[300], r'E')
    pyplot.plot(J)
    pyplot.text(300,J[300], r'J')
    pyplot.plot(N)
    pyplot.text(300,N[300], r'N')
    pyplot.plot(T)
    pyplot.text(300,T[300], r'T')
    pyplot.plot(K)
    pyplot.text(300,K[300], r'K')

    pyplot.show()
