from matplotlib import pyplot
from TermoCount import TermoCount

def TermoGraph():
    
    E = TermoCount("E")
    J = TermoCount("J")
    N = TermoCount("N")
    T = TermoCount("T")
    K = TermoCount("K")

    pyplot.plot(E)
    pyplot.text(150,E[150], r'E')
    pyplot.plot(J)
    pyplot.text(150,J[150], r'J')
    pyplot.plot(N)
    pyplot.text(150,N[150], r'N')
    pyplot.plot(T)
    pyplot.text(150,T[150], r'T')
    pyplot.plot(K)
    pyplot.text(150,K[150], r'K')

    pyplot.show()
