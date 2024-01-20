# fill values that should be interpreted as "NULL" with None
def f_FillNull(vals: list) -> list:
    def bad(val):
        if isinstance(val, type(pd.NA)):
            return True
        # the list of values you want to interpret as 'NULL' should be 
        # tweaked to your needs
        return val in ['NULL', np.nan, 'nan', '', '', '-', '?']
    return tuple(i if not bad(i) else None for i in vals)
