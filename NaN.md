##  Handling NaN value data types 
Problem: 

The `_extract_dtype()function directly specifies Microsoft Access DB's item attribute long (..32-bit long integer type) as int_, 
which corresponds to NumPy's integer type (whose bit-length varies by machine, 32/64 bits) 
and the array item type parameter dtypes implemented in pandas using Python's built-in type int.
However, in actual Microsoft Access DBs, items of the long integer type can accept NULL values, often resulting in errors.

## Solution : Use 'Int64'

To solve this problem, one approach is to use the np.float_ type instead of np.int_. However, if you
want to maintain integer handling, this can be inconvenient. Alternatively, you could use Pandas's 
Int64 type to accommodate NaN values. The "Int64" type supports missing values (NaN) for integers.

