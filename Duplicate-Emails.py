# Import your libraries
import pandas as pd

# Start writing code
## Method 1
# Find duplicates on 'email' column
df = employee[employee.email.duplicated()]
#df.email.iloc[0]

# Find the df with duplicate rows removed.
df.email.drop_duplicates()
