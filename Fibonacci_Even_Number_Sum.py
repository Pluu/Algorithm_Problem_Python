from itertools import ifilter, takewhile

def fibGenerator():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b
        
def isEven(num):
    return num % 2 == 0
    
def main():
    evenfibs = ifilter(isEven, fibGenerator())
    m_list = list(takewhile(lambda x: x < 4000000, evenfibs))
    
    for x in m_list:
        print x
        
    print sum(m_list)

if __name__ == '__main__':
    main()
