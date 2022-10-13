from countries import Countries

def get_group(group_name):
    all_countries = Countries()
    all_countries.load_wb()
    # all_countries.load_fao_code()
    all_countries.load_country_alias()
    
    cs = Countries()

    for c in all_countries:
        if group_name in c.groups:
            cs.append(c)
    
    return cs




