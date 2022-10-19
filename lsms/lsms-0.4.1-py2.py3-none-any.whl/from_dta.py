import pandas as pd

def from_dta(fn,convert_categoricals=True):
    sr=pd.io.stata.StataReader(fn)

    df = sr.read(convert_categoricals=False)

    values = sr.value_labels()

    var_to_label = dict(zip(sr.varlist,sr.lbllist))    

    if convert_categoricals:
        for var in sr.varlist: # Check mapping for each variable with values
            if len(var_to_label[var]):
                try:
                    code2label = values[var_to_label[var]]
                    df[var] = df[var].map(code2label)
                except KeyError:
                    print('Issue with categorical mapping: %s' % var)

    return df
