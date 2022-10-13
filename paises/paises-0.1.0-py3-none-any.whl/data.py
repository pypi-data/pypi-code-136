# -*- coding: utf-8 -*-
from country import Country
import json
import urllib.request
from geo.ccs import *

List = []

country_alias = {
    'Bahamas, The': ['Bahamas'],
    'Bolivia':['Bolivia (Plurinational State of)'],
    'Central African Republic': ['CAR'],
    'Congo, Dem. Rep.': ['Democratic Republic of the Congo', 'DR Congo', 'DRC', 'D.R. of the Congo'],
    'Congo': ['Republic of Congo'],
    'Gambia, The': ['Gambia', 'The Gambia', 'Gambia (Republic of The)'],
    'Guinea-Bissau': ['Guinea Bissau'],
    'Iran, Islamic Rep.':['Iran', 'Iran (Islamic Republic of)', 'Islamic Republic of Iran'],
    'Lao PDR': ["Lao People's Democratic Republic", 'Laos', 'Lao P.D.R.', "Lao People's DR"],
    'Micronesia, Fed. Sts.': ['Micronesia (Federated States of)'],
    'St. Vincent and the Grenadines':  ['Saint Vincent and the Grenadines'],
    'St. Kitts and Nevis': ['Saint Kitts and Nevis '],
    'St. Lucia': ['Saint Lucia'],
    'Sao Tome and Principe':["São Tomé and Príncipe", "SÃ£o TomÃ© and PrÃ­ncipe", "São Tomé and Principe"],
    'Syria': ['Syrian Arab Republic'],
    'Tanzania': ['United Republic of Tanzania', 'U.R. of Tanzania: Mainland'],
    'United Kingdom': ['United Kingdom of Great Britain and Northern Ireland'],
    'United States': ['United States of America'],
    'Venezuela': ['Venezuela, RB', 'Venezuela, Bolivarian Republic of', 'Venezuela (Bolivarian Republic of)', 'Venezuela(Bolivarian Republic of)'],
    'Vietnam': ['Viet Nam'],
    'Yemen, Rep.': ['Yemen'],
    "Egypt": ['Egypt, Arab Rep.'],
    "Korea, Dem. People's Rep.": ["Democratic People's Republic of Korea ", 'North Korea'],
    }

ldcs2025 = {
    'Angola', 'Benin', 'Burkina Faso', 'Burundi',
    'Central African Republic', 'Chad', 'Comoros',
    'Congo, Dem. Rep.', 'Djibouti',
    'Eritrea', 'Ethiopia', 'Gambia, The', 'Guinea',
    'Guinea-Bissau', 'Lesotho', 'Liberia', 'Madagascar',
    'Malawi', 'Mali', 'Mauritania', 'Mozambique',
    'Niger', 'Rwanda',
    'Senegal', 'Sierra Leone', 'Somalia', 'South Sudan',
    'Sudan', 'Togo', 'Tanzania', 'Uganda',
    'Zambia', 'Afghanistan', 'Cambodia', 'Kiribati', 'Lao PDR',
    'Myanmar', 'Nepal', 'Tuvalu', "Timor-Leste", 'Vanuatu',
    'Yemen, Rep.', 'Haiti'
}

ldcs2019 = [
    'Angola', 'Benin', 'Burkina Faso', 'Burundi',
    'Central African Republic', 'Chad', 'Comoros',
    'Congo, Dem. Rep.', 'Djibouti',
    'Eritrea', 'Ethiopia', 'Gambia, The', 'Guinea',
    'Guinea-Bissau', 'Lesotho', 'Liberia', 'Madagascar',
    'Malawi', 'Mali', 'Mauritania', 'Mozambique',
    'Niger', 'Rwanda', 'Sao Tome and Principe',
    'Senegal', 'Sierra Leone', 'Somalia', 'South Sudan',
    'Sudan', 'Togo', 'Tanzania', 'Uganda',
    'Zambia', 'Afghanistan', 'Bangladesh',
    'Bhutan', 'Cambodia', 'Kiribati', 'Lao PDR',
    'Myanmar', 'Nepal', 'Solomon Islands',
    'Tuvalu', "Timor-Leste", 'Vanuatu', 'Yemen, Rep.', 'Haiti']

ldcs2018 = [
    'Angola', 'Benin', 'Burkina Faso', 'Burundi',
    'Central African Republic', 'Chad', 'Comoros',
    'Congo, Dem. Rep.', 'Djibouti',
    'Eritrea', 'Ethiopia', 'Gambia, The', 'Guinea',
    'Guinea-Bissau', 'Lesotho', 'Liberia', 'Madagascar',
    'Malawi', 'Mali', 'Mauritania', 'Mozambique',
    'Niger', 'Rwanda', 'Sao Tome and Principe',
    'Senegal', 'Sierra Leone', 'Somalia', 'South Sudan',
    'Sudan', 'Togo', 'Tanzania', 'Uganda',
    'Zambia', 'Afghanistan', 'Bangladesh',
    'Bhutan', 'Cambodia', 'Kiribati', 'Lao PDR',
    'Myanmar', 'Nepal', 'Solomon Islands',
    'Tuvalu', "Timor-Leste", 'Vanuatu', 'Yemen, Rep.', 'Haiti']

ldcs2017 = [
    'Angola', 'Benin', 'Burkina Faso', 'Burundi',
    'Central African Republic', 'Chad', 'Comoros',
    'Congo, Dem. Rep.', 'Djibouti', 'Equatorial Guinea',
    'Eritrea', 'Ethiopia', 'Gambia, The', 'Guinea',
    'Guinea-Bissau', 'Lesotho', 'Liberia', 'Madagascar',
    'Malawi', 'Mali', 'Mauritania', 'Mozambique',
    'Niger', 'Rwanda', 'Sao Tome and Principe',
    'Senegal', 'Sierra Leone', 'Somalia', 'South Sudan',
    'Sudan', 'Togo', 'Tanzania', 'Uganda',
    'Zambia', 'Afghanistan', 'Bangladesh',
    'Bhutan', 'Cambodia', 'Kiribati', 'Lao PDR',
    'Myanmar', 'Nepal', 'Solomon Islands',
    'Tuvalu', "Timor-Leste", 'Vanuatu', 'Yemen, Rep.', 'Haiti']

# LLDCs

lldcs = [
    'Botswana', 'Burkina Faso', 'Burundi',
    'Central African Republic',
    'Chad', 'Ethiopia', 'Lesotho',
    'Malawi', 'Mali', 'Niger', 'Rwanda', 'South Sudan',
    'Eswatini', 'Uganda', 'Zambia',
    'Zimbabwe', 'Afghanistan', 'Bhutan',
    'Kazakhstan', 'Kyrgyz Republic', 'Lao PDR',
    'Mongolia', 'Nepal', 'Tajikistan', 'Turkmenistan',
    'Uzbekistan', 'Armenia', 'Azerbaijan', 'Moldova',
    'North Macedonia', 'Bolivia', 'Paraguay']

# SIDS

sids = [
    'Antigua and Barbuda', 'Bahamas', 'Bahrain', 'Barbados', 'Belize',
    'Cape Verde', 'Comoros', 'Cuba', 'Dominica', 'Dominican Republic',
    'Fiji', 'Grenada', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Jamaica',
    'Kiribati', 'Maldives', 'Marshall Islands',
    'Federated States of Micronesia', 'Mauritius', 'Nauru', 'Palau',
    'Papua New Guinea', 'Samoa', 'Sao Tome and Principe', 'Singapore',
    'St Kitts and Nevis',
    'St Lucia', 'St Vincent and the Grenadines', 'Seychelles',
    'Solomon Islands', 'Suriname', 'Timor-Leste', 'Tonga',
    'Trindad and Tobago', 'Tuvalu', 'Vanuatu', 'American Samoa',
    'Anguilla', 'Aruba', 'British Virgin Islands',
    'Commonwealth of Northern Marianas', 'Cook Islands',
    'French Polynesia', 'Guam', 'Montserrat', 'Netherlands Antilles',
    'New Caledonia', 'Niue', 'Puerto Rico', 'US Virgin Islands']

# this is the list of middle income List following the criteria of
# the World Bank, but excluding the LDCs in the Lower Middle-Income
# category

mics_lower = [
    'Albania', 'Indonesia', 'Armenia', 'India', 'Belize', 'Iraq',
    'Bolivia', 'Kosovo', 'Cameroon', 'Sri Lanka', 'Cape Verde',
    ' Rep Marshall Islands', 'Swaziland', 'Cote d\'Ivoire',
    'Micronesia, Fed Sts', 'Syrian Arab Republic', 'Moldova', 'Egypt',
    'Arab Rep', 'Mongolia', 'Tonga', 'El Salvador', 'Morocco', 'Ukraine',
    'Fiji', 'Nicaragua', 'Uzbekistan', 'Georgia', 'Nigeria', 'Ghana',
    'Pakistan', 'Vietnam', 'Guatemala', 'Papua New Guinea',
    'West Bank and Gaza', 'Guyana', 'Paraguay', 'Honduras', 'Philippines']

mics_upper = [
    'Ecuador', 'Palau', 'Algeria', 'Gabon', 'Panama', 'American Samoa',
    'Grenada', 'Peru',  'Antigua and Barbuda', 'Iran, Islamic Rep',
    'Romania', 'Argentina', 'Jamaica', 'Russian Federation',
    'Azerbaijan', 'Jordan', 'Serbia', 'Belarus', 'Kazakhstan',
    'Seychelles', 'Bosnia and Herzegovina', 'Latvia', 'South Africa',
    'Botswana', 'Lebanon', 'St Lucia', 'Brazil', 'Libya', 'St Vincent and the Grenadines',
    'Bulgaria', 'Lithuania', 'Suriname', 'Chile', 'Macedonia, FYR',
    'Thailand', 'China', 'Malaysia', 'Tunisia', 'Colombia',
    'Maldives', 'Turkey', 'Costa Rica', 'Mauritius',
    'Turkmenistan', 'Cuba', 'Mexico', 'Dominica', 'Montenegro',
    'Uruguay', 'Dominican Republic', 'Namibia', 'Venezuela, RB']

mics = mics_lower + mics_upper

# OECD List
oecd = [
    'Australia', 'Austria', 'Belgium', 'Canada', 'Chile', 'Czech Republic',
    'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece',
    'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Japan',
    'Korea, Rep.', 'Latvia', 'Luxembourg', 'Mexico', 'Netherlands', 'New Zealand',
    'Norway', 'Poland', 'Portugal', 'Slovak Republic', 'Slovenia', 'Spain',
    'Sweden', 'Switzerland', 'Turkey', 'United Kingdom', 'United States']

# Developed List

developed = [
    'Andorra', 'Australia', 'Austria', 'Belgium', 'Bulgaria', 'Bermuda',
    'Canada', 'Cyprus', 'Chile', 'Czech Republic', 'Denmark', 'Estonia',
    'Faeroe Islands', 'Finland', 'France', 'Germany', 'Gibraltar', 'Greece',
    'Holy See', 'Hungary', 'Iceland', 'Ireland', 'Israel',
    'Italy', 'Japan', 'Lithuania', 'Korea, Rep.', 'Luxembourg', 'Malta',
    'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Poland', 'Portugal',
    'Romania', 'San Marino', 'Slovak Republic', 'Slovenia', 'Spain', 'Sweden',
    'Switzerland', 'Turkey', 'Latvia', 'United Kingdom', 'United States']

# Developing
# According to UNSD classification available at:
# https://unstats.un.org/unsd/methodology/m49/

developing_unsd = [
'Afghanistan','Algeria','American Samoa','Angola','Anguilla',
'Antigua and Barbuda', 'Argentina','Armenia','Aruba','Azerbaijan','Bahamas',
'Bahrain','Bangladesh', 'Barbados', 'Belize','Benin','Bhutan',
'Bolivia (Plurinational State of)', 'Bonaire, Sint Eustatius and Saba',
'Botswana','Brazil','British Indian OceanTerritory','British Virgin Islands','Brunei Darussalam',
'Burkina Faso','Burundi','Cabo Verde','Cambodia','Cameroon','Cayman Islands','Central African Republic',
'Chad','Chile','China','China, Hong Kong Special Administrative Region',
'China, Macao Special Administrative Region',
'Colombia','Comoros','Congo','Cook Islands', 'Costa Rica','C&#244;te d&#39;Ivoire' ,'Cuba',
'Cura&#231;ao', 'Cyprus', 'Democratic People&#39;s Republic of Korea',
'Democratic Republic of the Congo','Djibouti','Dominica','Dominican Republic',
'Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Ethiopia',
'Falkland Islands (Malvinas)','Fiji','French Guiana','French Polynesia',
'French Southern Territories','Gabon','Gambia','Georgia',
'Ghana','Grenada','Guadeloupe','Guam','Guatemala','Guinea','Guinea-Bissau',
'Guyana','Haiti','Honduras','India','Indonesia', 'Iran (Islamic Republic of)',
'Iraq','Israel','Jamaica','Jordan','Kazakhstan','Kenya','Kiribati','Kuwait',
'Kyrgyzstan','Lao People&#39;s Democratic Republic','Lebanon','Lesotho',
'Liberia','Libya','Madagascar','Malawi','Malaysia','Maldives','Mali','Marshall Islands',
'Martinique','Mauritania','Mauritius','Mayotte','Mexico',
'Micronesia (Federated States of)','Mongolia','Montserrat','Morocco',
'Mozambique','Myanmar','Namibia','Nauru','Nepal','New Caledonia',
'Nicaragua','Niger','Nigeria','Niue','Northern Mariana Islands',
'Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru',
'Philippines','Pitcairn','Puerto Rico','Qatar','Republic of Korea','R&#233;union',
'Rwanda','Saint Barth&#233;lemy','Saint Helena','Saint Kitts and Nevis','Saint Lucia',
'Saint Martin (French Part)','Saint Vincent and the Grenadines','Samoa',
'Sao Tome and Principe','Saudi Arabia','Senegal','Seychelles','Sierra Leone',
'Singapore','Sint Maarten (Dutchpart)','Solomon Islands','Somalia','South Africa',
'South Georgia and the South Sandwich Islands','South Sudan','Sri Lanka',
'State of Palestine','Sudan','Suriname','Swaziland','Syria',
'Tajikistan','Thailand','Timor-Leste','Togo','Tokelau','Tonga',
'Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Turks and Caicos Islands',
'Tuvalu','Uganda','United Arab Emirates','United Republic of Tanzania',
'United States Minor Outlying Islands','United States Virgin Islands','Uruguay',
'Uzbekistan','Vanuatu','Venezuela (Bolivarian Republic of)','Viet Nam',
'Wallis and Futuna Islands','Western Sahara','Yemen, Rep.','Zambia','Zimbabwe'
]

# List of developing economies excludiong LDCs as used by UNCTAD
# for analytical purposes
# http://unctadstat.unctad.org/EN/Classifications.html

developing_excluding_ldcs = [
    'Algeria',
    'American Samoa',
    'Anguilla',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Aruba',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Barbados',
    'Belize',
    'Bolivia',
    'Bonaire, Sint Eustatius and Saba',
    'Botswana',
    'Brazil',
    'British Indian OceanTerritory',
    'British Virgin Islands',
    'Brunei Darussalam',
    'Cabo Verde',
    'Cameroon',
    'Cayman Islands',
    'Chile',
    'China',
    'China, Hong Kong Special Administrative Region',
    'China, Macao Special Administrative Region',
    'Colombia',
    'Republic of Congo',
    'Cook Islands',
    'Costa Rica',
    'C&#244;te d&#39;Ivoire' ,
    'Cuba',
    'Cura&#231;ao',
    'Cyprus',
    'Democratic People&#39;s Republic of Korea',
    'Dominica',
    'Dominican Republic',
    'Ecuador',
    'Equatorial Guinea',
    'Egypt',
    'El Salvador',
    'Falkland Islands (Malvinas)',
    'Fiji',
    'French Guiana',
    'French Polynesia',
    'French Southern Territories',
    'Gabon',
    'Georgia',
    'Ghana',
    'Grenada',
    'Guadeloupe',
    'Guam',
    'Guatemala',
    'Guyana',
    'Honduras',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Israel',
    'Jamaica',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kuwait',
    'Kyrgyzstan',
    'Lebanon',
    'Libya',
    'Malaysia',
    'Maldives',
    'Martinique',
    'Mauritius',
    'Mayotte',
    'Mexico',
    'Micronesia (Federated States of)',
    'Mongolia',
    'Montserrat',
    'Morocco',
    'Namibia',
    'Nauru',
    'New Caledonia',
    'Nicaragua',
    'Nigeria',
    'Niue',
    'Northern Mariana Islands',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Pitcairn',
    'Puerto Rico',
    'Qatar',
    'Republic of Korea',
    'R&#233;union',
    'Saint Barth&#233;lemy',
    'Saint Helena',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Martin (French Part)',
    'Saint Vincent and the Grenadines',
    'Saudi Arabia',
    'Senegal',
    'Seychelles',
    'Singapore',
    'Sint Maarten (Dutchpart)',
    'South Africa',
    'South Georgia and the South Sandwich Islands',
    'Sri Lanka',
    'State of Palestine',
    'Suriname',
    'Swaziland',
    'Syria',
    'Tajikistan',
    'Thailand',
    'Tokelau',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Turks and Caicos Islands',
    'United Arab Emirates',
    'United States Minor Outlying Islands',
    'United States Virgin Islands',
    'Uruguay',
    'Uzbekistan',
    'Venezuela (Bolivarian Republic of)',
    'Viet Nam',
    'Wallis and Futuna Islands',
    'Western Sahara',
    'Zimbabwe'
]

africa = [
    'Algeria', 'Angola', 'Benin', 'Botswana',
    'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde',
    'Central African Republic', 'Chad', 'Comoros', 'Congo, Dem. Rep.',
    'Republic of Congo', 'Cote d\'Ivoire', 'Djibouti', 'Egypt',
    'Equatorial Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia, The',
    'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya',
    'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali',
    'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia',
    'Niger', 'Nigeria', 'Rwanda', 'Saint Helena', 'Sao Tome and Principe',
    'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'Somaliland', 'South Africa',
    'South Sudan', 'Sudan', 'Swaziland', 'Tanzania', 'Togo', 'Tunisia',
    'Uganda', 'Western Sahara', 'Zambia', 'Zimbabwe', 'British Indian Ocean Territory']

eastern_africa = [
    'Burundi', 'Comoros', 'Djibouti', 'Eritrea', 'Ethiopia', 'Kenya',
    'Madagascar', 'Malawi', 'Mauritius', 'Mayotte', 'Mozambique',
    'Réunion', 'Rwanda', 'Seychelles', 'Somalia', 'South Sudan',
    'Uganda', 'United Republic of Tanzania', 'Zambia', 'Zimbabwe'
]

middle_africa = [
    'Angola', 'Cameroon', 'Central African Republic',
    'Democratic Republic of the Congo', 'Equatorial Guinea',
    'Gabon', 'Sao Tome and Principe'
]

northern_africa = [
    'Algeria', 'Egypt', 'Libya', 'Morocco', 'Sudan', 'Tunisia',
    'Western Sahara'
]

southern_africa = [
    'Botswana', 'Lesotho', 'Namibia', 'South Africa', 'Swaziland'
]

western_africa = [
    'Benin', 'Burkina Faso', 'Cabo Verde', 'Cote d\'Ivoire',
    'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Liberia',
    'Mali', 'Mauritania', 'Niger', 'Nigeria', 'Saint Elena',
    'Senegal', 'Sierra Leone', 'Togo'
]

asia = [
    'Palestine', 'Afghanistan', 'Bahrain', 'Bangladesh', 'Bhutan',
    'Brunei Darussalam', 'Myanmar', 'Cambodia', 'China', 'India',
    'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan',
    'Kazakhstan', 'North Korea', 'South Korea', 'Kuwait', 'Kyrgyzstan',
    'Lao PDR', 'Lebanon',
    'Malaysia', 'Maldives', 'Mongolia', 'Nepal', 'Oman', 'Pakistan',
    'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'Sri Lanka',
    'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste',
    'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam',
    'Yemen, Rep.', 'Hong Kong', 'Macau']

pacific_islands = [
    'Fiji', 'Kiribati', 'Marshall Islands',
    'Micronesia, Federated States of', 'Nauru', 'Palau',
    'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu'
    ]

asia_and_the_pacific = asia + pacific_islands

central_asia = [
    'Kazakhstan', 'Kyrgyzstan', 'Tajikistan', 'Uzbekistan'
]

eastern_asia = [
    'China', 'China, Hong Kong Special Administrative Region',
    'China, Macao Special Administrative Region',
    'Democratic People\'s Republic of Korea',
    'Japan', 'Mongolia', 'Republic of Korea'
]

south_east_asia = [
    'Brunei Darussalam', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia',
    'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Timor-Leste',
    'Vietnam'
]

western_asia = [
    'Armenia', 'Azerbaijan', 'Bahrain', 'Cyprus', 'Georgia', 'Iraq',
    'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Oman', 'Qatar',
    'Saudi Arabia', 'State of Palestine', 'Syria', 'Turkey',
    'United Arab Emirates', 'Yemen, Rep.'
]

caribbean = [
    'Anguilla', 'Antigua and Barbuda', 'Aruba', 'Bahamas', 'Barbados',
    'Bonaire, Sint Eustatius and Saba', 'British Virgin Islands',
    'Cayman Islands', 'Cuba', 'Curaçao', 'Dominica', 'Dominican Republic',
    'Grenada', 'Guadeloupe', 'Haiti', 'Jamaica', 'Martinique', 'Montserrat',
    'Puerto Rico', 'Saint-Barthélemi', 'Sanit Kitts and Nevis', 'Saint Lucia',
    'Saint Martin', 'Saint Vincent and the Grenadines', 'Sint Marteen',
    'Trinidad and Tobago', 'Turks and Caicos Islands', 'United States Virgin Islands'
]

central_america = [
    'Belize', 'Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Mexico',
    'Nicaragua', 'Panama'
]

north_america = [
    'Saint Martin', 'Anguilla', 'Antigua and Barbuda', 'Aruba', 'Bahamas',
    'Barbados', 'Bermuda', 'British Virgin Islands', 'Cayman Islands',
    'Cuba', 'Curacao', 'Dominica', 'Dominican Republic',
    'Grenada', 'Haiti', 'Jamaica', 'Montserrat', 'Puerto Rico',
    'Saint Barthelemy', 'Saint Kitts and Nevis', 'Saint Lucia', 'Sint Maarten',
    'Trinidad and Tobago', 'Turks and Caicos Islands', 'US Virgin Islands', 'United States']

south_america = [
    'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador',
    'Falkland Islands', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay',
    'Venezuela']

america = central_america + north_america  + south_america


europe = [
    'Aland Islands', 'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan',
    'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia',
    'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Faroe Islands',
    'Finland', 'France', 'Georgia', 'Germany', 'Gibraltar', 'Greece',
    'Guernsey', 'Vatican City', 'Hungary', 'Iceland', 'Ireland',
    'Isle of Man',
    'Italy', 'Jersey', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania',
    'Luxembourg', 'Macedonia', 'Malta', 'Moldova', 'Monaco', 'Montenegro',
    'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia',
    'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Svalbard',
    'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom',
    'Northern Cyprus']

eastern_europe = [
    'Belarus', 'Bulgaria', 'Czech Republic', 'Hungary', 'Poland',
    'Republic of Moldova', 'Romania', 'Russian Federation', 'Slovakia',
    'Ukraine'
    ]

northern_europe = [
    'Åland Islands', 'Channel Islands', 'Denmark', 'Estonia', 'Feroe Islands',
    'Finland', 'Guernsey', 'Iceland', 'Ireland', 'Isle of Man', 'Jersey',
    'Latvia', 'Lithuania', 'Norway', 'Sark', 'Svalbard and Jan Mayen Islands',
    'United Kingdom'
]

southern_europe = [
    'Albania', 'Andorra', 'Bosnia and Herzegovina', 'Croatia', 'Gibraltar',
    'Greece', 'Holy See', 'Italy', 'Malta', 'Montenegro', 'Portugal', 'San Marino',
    'Serbia', 'Slovenia', 'Spain', 'The former Yugoslav Republic of Macedonia'
]

western_europe = [
    'Austria', 'Belgium', 'France', 'Germany', 'Liechtenstein', 'Luxembourg',
    'Monaco', 'Netherlands', 'Switzerland'
]

central_america = [
    'Belize', 'Canada', 'Costa Rica', 'El Salvador', 'Greenland',
    'Guatemala', 'Honduras',
    'Mexico', 'Nicaragua', 'Panama', 'Saint Pierre and Miquelon',
    'Saint Vincent and the Grenadines']

antarctica = ['South Georgia and South Sandwich Islands',
              'French Southern and Antarctic Lands', 'Antarctica',
              'Heard Island and McDonald Islands']

world = europe + asia_and_the_pacific + america + antarctica + africa
