
import numpy as np   # modulo necessario alla funzione salvata

# ------------------------------- r_minmax

def r_minmax(min=0,max=127,n=3):                                    
    '''Genera un numero di interi n
       compreso tra min e max
    '''
    rng = np.random.default_rng() 
    seq = rng.integers(min,max,size=n)    
    return seq  

# ------------------------------- trasp

def trasp(seq=np.array([60,61,62]), semit=0):                                    
    '''Traspone una sequenza in semitoni
    '''
    seq = seq + semit   
    return seq     
