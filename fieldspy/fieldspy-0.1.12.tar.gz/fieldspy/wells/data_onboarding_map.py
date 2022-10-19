well_heads_kwargs = {
    'import_dtype' :{
        'BoreId':str,
        'WellId':str,
        'WellName':str
    },
    'dates':{
        'cols':['SpudDate'],
        'format':'%m/%d/%Y'
    },
    'mapping':{
        'name':'WellId',
        'easting':'Easting',
        'northing':'Northing',
        'rte':'Elevation',
        'coef_conversion': 0.3048
    },
    'fields':['WellName','MaxPressure','BoreId','Type']
}

survey_kwargs = {
    'import_dtype' :{
        'WellId':str,
    },
    'mapping':{
        'name':'WellId',
        'md':'MD',
        'tvd':'TVD',
        'easting':'EastDeparture',
        'northing':'NorthDeparture',
        'inc':'Deviation',
        'azi':'Azimuth'        
    }
}

formations_kwargs = {
    'import_dtype' :{
        'WellId':str
    },
    'dates':{
        'cols':['StartDate','EndDate'],
        'format':'%m/%d/%Y'
    },
    'mapping':{
        'well_id':'WellId',
        'name':'Reservoir',
        'md_top':'TopDepth',
        'md_bottom':'BottomDepth',
    },
    'fields':['TVDNetpayThickness','BoreId','FaultBlock','Compartment','AllocationRatio','StartDate','EndDate']
}

aqueon_mapping = {
    'well_heads_kwargs':well_heads_kwargs,
    'survey_kwargs':survey_kwargs,
    'formations_kwargs':formations_kwargs
}