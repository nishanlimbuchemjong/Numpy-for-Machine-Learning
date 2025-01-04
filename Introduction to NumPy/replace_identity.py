import numpy as np

# creating 5 X 5 identity matrix
np1 = np.eye(5)
print(f"Before replacing '1' with '7', we get\n{np1}")

# replacing diagonal element '1' with '7'
np1[np.diag_indices_from(np1)] = 7
print(f"\nAfter replacing '1' with '7', we get\n{np1}")