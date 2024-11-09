# Load the formal context
import pandas as pd
from fcapy.context import FormalContext
url = 'https://raw.githubusercontent.com/EgorDudyrev/FCApy/main/data/animal_movement.csv'
K = FormalContext.from_pandas(pd.read_csv(url, index_col=0))
print(K)

# Create the concept lattice
from fcapy.lattice import ConceptLattice
L = ConceptLattice.from_context(K)