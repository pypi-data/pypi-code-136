from data.Frame import Frame
from geo.countries import Countries

# This function returns a dataframe with countries passed as an array (g) using the field specific in (column_name)
def extract_countries(g, column_name, df):
    n_df = Frame()
    c = Countries()
    
    names = []

    for ctr_name in g:
        ctr = c.get_country_by_name(ctr_name)
        names.append(ctr.name)

        for i in ctr.alias:
            names.append(i)

    for r in df.rows:          
        if (r.get_by_column_name(column_name).value.value in names):
            n_df.rows.append(r)
    
    return(n_df)