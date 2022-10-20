import re
import unidecode as ud
from collections import Counter
from itertools import permutations




##############################  Template Questions/Sentences  ##############################

all_template_questions = [
    'What is the problem',
    'Location of the issue',
    'What is the address of the vehicle crossing',
    'What is the enquiry',
    "What is the customer's name",
    "What is the customer's contact number",
    'Are there roadwork signs in the problem area',
    'Did you see or obtain the registration number or signage of vehicle concerned',
    'What is the vehicle crossing application number',
    'What is the location',
    "What is the customer's physical address",
    "What is the customer's email address",
    'If person phoning is from the Police, do they have an event number associated with the call',
    'What is their permit number (if known)',
    'What is the vehicle licence plate number associated with the permit',
    'Has customer received their approved vehicle crossing permit',
    'What is the issue with the sign',
    'When would customer like to pour the concrete (date and time)',
    'When will vehicle crossing be ready for inspection by AT (must be before concrete pour)',
    'Vehicle registration number',
    'What is the vehicle crossing application number (refer to notes above)',
    'What type of sign is affected, e.g. street name, parking, bus stop, destination sign, give way',
    'Does the customer have an approved vehicle crossing permit',
    'How long has the road been like this',
    'Is the damage causing a trip hazard, making the area impassable, or caused injury',
    'Is the road sealed or unsealed',
    'What is the location of the street lights',
    'What damage has occurred to the footpath, off-road cycle path or road to road walkway, e.g. cracked, completely broken',
    'Do you know who caused damage to the footpath, offload cycle path or road to road walkway',
    'Is the light above a pedestrian crossing',
    'Is the light a belisha beacon (orange light) at a pedestrian crossing',
    'Is the location a rural intersection',
    'Location of the sign',
    'If graffiti etched into concrete, is it offensive',
    'What is the location of the streetlight',
    'Does this issue occur at all times, or does it only happen at a certain times of the day',
    'Has the problem made the road or footpath impassable, e.g. pole fallen across road',
    "Customer's email address",
    'Why does customer want increased monitoring at this site',
    'Is the problem on the road, footpath or cycleway',
    'What size is the pothole',
    'Location the car is parked in',
    'Is the pothole causing traffic to slow down or swerve',
    'Is the customer a resident at this location, regular visitor, workplace',
    'What is the road name',
    'How often does this occur, e.g. everyday once a week/twice a month',
    'Has there been an accident as a result of the issue',
    'Is the pothole in the main wheel-track of the road (in direct path of car wheels)',
    'How big is the issue, e.g. over 1m, over 1km',
    'Do you know who caused the spill',
    'Date of parking',
    'How is the issue causing an immediate hazard to vehicles or pedestrians',
    'When did the problem occur, or is it happening now',
    'Is grate partially or fully blocked',
    'Location of the cesspit/catchpit drain grate',
    'If unknown substance',
    'What is blocking the grate, e.g. dirt, leaves',
    'What type of phone is the customer using',
    'Is the blockage likely to cause flooding soon, e.g. is there heavy rain now or forecast today',
    'Why does customer want a refund',
    'Where was customer parked',
    'What time did customer start parking',
    'What time did customer leave the car park',
    'What time did AT Park parking session stop',
    'If the light is inside an AT bus shelter (a shelter with no advertising panels)',
    'If paint, is it still wet, or is it dry',
    'Time and date of transaction',
    'Location of the fallen branch or tree',
    'What is the problem, e.g. item fallen off trailer, colour of rubbish bags, debris from blown-out car tyre etc',
    'Is the fallen branch or tree causing an immediate health and safety risk to road or footpath users',
    "Customer's contact number",
    'What is the AT Park area ID number',
    'Has a pre-pour inspection been successfully completed for this crossing',
    'If yes, what is the risk/problem',
    'Is the issue causing cars to slow down or swerve',
    'What is the query, e.g. processing time, technical question',
    'When will the vehicle crossing be finished and ready for inspection by AT',
    'Does the road require grading or extra metal',
    'Are conditions causing a traffic hazard without warning',
    'What is the location of the sign',
    'How large is the problem',
    'How big is the pothole, or what area is uneven or needing metal',
    'Is the issue causing traffic to slow down or swerve',
    'Location of issue',
    'Can you describe the problem as fully as possible',
    'What is the address/approximate location of issue',
    'If shoulder damage, is the damage crossing the outer white line into the main part of the road',
    'What is the reason for this request',
    'What is the exact location of the traffic signal (obtain two road names at intersection)',
    'If pick-up is required',
    'Are all the traffic lights affected or only one',
    'What is the date/time that the issue is occurring',
    'What is the location of the problem',
    'Is the problem happening at a certain time of day',
    'Which road is the driver on',
    'Which direction is the customer travelling',
    'Is the problem causing traffic to queue longer than usual',
    'How many light changes does it take to get through',
    'Does customer know who has caused the damage',
    'What is the customer query',
    'Has the equipment been moved to a safe location',
    'Where is the work taking place on the road reserve, e.g. footpath, berm, traffic lanes',
    'Can the caller give you the name of the company that carried out the works',
    'Does caller know what works were being undertaken',
    'Are there any identifying company logos or markings on the equipment, e.g. on back of the sign or bottom of the road cone',
    'What is the name of the road or address of the piece of road (approximately)',
    'Are leaves covering or blocking one or more stormwater grates',
    "What is the customer's query",
    'Are leaves covering footpath, cycleway and/or road',
    'Has customer received a letter drop from Auckland Transport outlining the work details',
    'How large is the area covered with leaf fall, e.g. length of 2 houses',
    'Is the problem a result of an accident reported by the Police',
    'Location of the grass verge or berm',
    'When did the damage occur or is it happening now',
    'Is the grass berm or verge on a traffic island or median strip',
    'Where is the problem, e.g. road surface, footpath, vehicle crossing',
    'What are the works being undertaken',
    'What is the problem, e.g. trip hazard, loose stone, debris left behind, obstruction',
    'Has someone damaged the road as a result of works happening on the road or nearby, e.g. AT contractors, utility company, builders or private contractors',
    'Who is doing the activity, e.g. name of construction company',
    'Where is the work taking place, e.g. footpath, berm, traffic lanes',
    'Does caller have any other relevant information that they could provide, e.g. photos or video',
    'Does customer have any other information, e.g. photos, video',
    'What is the problem with the grass verge or berm, e.g. berm dug up, vehicle damage, large hole in berm or verge',
    'Are there existing broken yellow lines or white / hockey stick parking lines or restrictions on one or both sides of the driveway',
    'If vehicles are obstructing visibility, are they illegally parked ie within 1 meter of the driveway or on broken yellow lines',
    'What is the issue, e.g. road safety issue, congestion, blocked access, vehicle crossing or entranceway, requesting an extension to an existing Traffic Management Plan',
    'What direction is the light facing, e.g. facing traffic coming along Nelson St from motorway',
    'What is the query',
    'What is the issue, e.g. safety, congestion, blocked access, dangerous work site, vehicle crossing or entrance way blocked',
    'For road cones placed on the road to reserve parking (not associated with any road works etc.) i.e. placed out by a local resident or business to reserve parking spaces, does caller have the name of the business or the name and address of the resident, who is responsible',
    'What is obstructing visibility at this location, e.g. parked vehicles, road signs, fences or other barriers',
    'Is a bulb faulty or not working (single light/bulb out)',
    'Location of the dead animal',
    'Is the dead animal causing traffic to swerve',
    'Is the animal mutilated',
    'Type of animal, e.g. dog, cat, possum, horse, cow, sheep etc',
    'What colour is the animal',
    'What is the location of the street light',
    'Is the street light pole supporting a traffic signal',
    'Is the street light pole supporting overhead power lines',
    'Location of the ditch',
    'Location of the problem',
    'What is the customer query or issue with the works',
    'What is the name of the road or address of the piece of road (approximately) where the works are taking place',
    'When was the application lodged',
    'If it is a new sub-division, have the lights been turned on before',
    'Has customer received a letter drop or notification about the works from anyone',
    'Location of the road markings',
    'What is the name of the road or roads',
    'Is customer querying progress of their pre-permit inspection',
    'What is the nature of the customers concern',
    'What is the speed limit of the road(s)',
    'Is customer aware of any crashes at this location',
    'Nature of works, are contractors digging holes, digging trenches, laying pipes etc',
    'Customer contact number',
    'What is the safety issue at this location',
    'Is the speeding at a specific location or is it along the length of the road',
    'Customer email address',
    'What is wrong with the road markings, e.g. faded, missing, incorrect, need reinstatement after reseal',
    'Are there any existing speed calming measures on the road, e.g. speed humps, chicanes',
    'If the light is inside an Auckland Transport bus shelter (a shelter with no advertising panels)',
    'Is customer concerned that vehicles are exceeding the speed limit or are vehicles going too fast for the road environment, e.g. short road, lots of corners',
    'What is the address of the proposed vehicle crossing',
    'If markings missing',
    'If markings are incorrect',
    'What type of road marking is being requested, e.g. give way marking, centre line marking',
    'What is the customer name',
    'What is their contact phone number and email address',
    'List all streets with lights that are out',
    'If the concern relates to parked vehicles, does the issue occur during a particular time of day',
    'What is the location of the issue',
    'Is this a sealed or unsealed road',
    'Location of the bus shelter',
    'Does the shelter have advertising panels/posters',
    'Is the issue causing traffic to swerve',
    'Why is sweeping required',
    'Is the slip completely blocking the road, or just partially',
    'Location of the cesspit, catchpit, drain or sump',
    'Is resident trapped on their property or in their vehicle, on the road',
    'Full name (as shown on photo ID)',
    'SuperGold card client number (9 digit number found on the back of the card)',
    'Contact telephone number',
    'How would the customer like to be contacted',
    'Concession expiry date',
    'Are people or properties being impacted by this',
    'Police file/reference number',
    'Could signs be installed to prevent vehicles parking on the berm',
    'Is there an immediate safety risk, e.g. danger to cars running over it, children could fall in drain',
    'Location of the safety fence, traffic barrier or guardrail',
    'Date of birth',
    'Postal address',
    'Where in the fence or barrier is the damage',
    'Is this a vehicle crossing grate',
    'How big is the slip or subsidence, e.g over 1m, over 1km',
    'What is the location of the culvert, closet address and landmark',
    'How large is the issue e.g. 1 metre long',
    'Is the culvert blocked',
    'Do you know what caused the damage to the fence or barrier',
    'Does the damage present a health and safety risk to pedestrians',
    'Location and direction of travel',
    'Is the damage obstructing the road or footpath',
    'Are there roadworks signs warning of reseal',
    'When was the reseal done',
    'How much loose chip is there',
    'What is the address where the issue occurs (approximately)',
    'Not an immediate health and safety risk',
    'What is the problem, e.g',
    'Is the glass cracked or completely smashed',
    'What is the problem/issue',
    'Is the glass shattered but still in the frame, or has it fallen out of the frame onto the floor',
    'Is the smashed glass causing an immediate health and safety risk',
    'Where is the container, bin, skip or temporary structure',
    'How long has this been an issue',
    'If request for street light to be relocated, why does it need to be moved',
    'If congestion, what sort of delays are occurring',
    'If no incident, what are the safety concerns',
    'Is this caused by roadworks',
    'Is there any other relevant information the customer can supply',
    'What is the perceived cause of the problem',
    'What is the major reason for congestion at this roadworks site',
    'How long have you been In the queue',
    'Has any incident occurred, e.g. crash, injury, trip',
    'Is access blocked completely or is one lane still available',
    'How many vehicles are affected',
    'What is the problem with the tree or vegetation eg. overhanging or overgrowing encroaching footpath or road',
    'Location of vehicle crossing',
    'When did this occur or is it happening now',
    'What is the problem with the vehicle crossing',
    'What is it affecting',
    'Was there any prior notification',
    'Why are street lights needed at this location',
    'What are the incident details',
    'What is the address where the streetlight(s) or amenity light(s) are required',
    'How many streetlights are being requested',
    'What are the names of the roads at this intersection',
    'Is the light required at a rural intersection',
    'What is the address of the piece of road, approximately',
    'Is the intersection controlled by traffic lights',
    'If there was notification, what did it say and who sent it',
    'What is the reason customer wants their AT Park account disabled',
    'How long does it normally take at this location ( if applicable – trigger point is if more than 5 min)',
    'If occurred within the road corridor',
    'Does customer know who is doing the work',
    'Is the activity causing a problem, e.g. obstruction to traffic or pedestrians, trip hazard',
    'Machine number, or street address where machine is locate',
    'Date and time of transaction',
    'Method of payment (cash or card)',
    'Area ID number/location of pay by plate machine',
    "What is the customer's request",
    'How big is the problem',
    'Is the kerb or channel on a footpath, traffic island or roundabout',
    'What type of activity is taking place and where is it in the road reserve, e.g. digging in berm or footpath',
    'Is the culvert damaged',
    'If customer is having issues with their account, what are the issues',
    'Is a bulb faulty or not working',
    'Is this a request for new restrictions or change to existing',
    'Vehicle licence plate number',
    'Is the problem causing traffic to swerve',
    'What is the hazard',
    'Has the problem caused an injury or made the area impassable',
    'Has anyone been injured',
    'Details of any other vehicles involved',
    'What is the approximate address of the location concerned',
    'What is the problem with the coverplate (door to wiring at the bottom of the street light) or street light shield',
    'If occurred at an intersection',
    'What pedestrian facilities are at this location, if any',
    'Do you know who caused damage to the kerb or channel, e.g building site nearby, utility company',
    'What is the location of the flooding',
    'How much water is there',
    'Does the road have kerb and channel or is there a ditch beside road',
    'Is the flooding causing traffic to swerve',
    'Is flooding causing pedestrians to walk on road',
    'Is the issue causing an immediate health and safety issue',
    'Date of incident',
    'Is the flooding blocking accessibility to properties',
    'Is flooding emergency now or likely to worsen with weather conditions, e.g. heavy rain forecast today',
    'Date and time of the transaction',
    'How did the damage occur',
    'Is road completely blocked or partially blocked',
    'Is the machine beeping',
    "What is the caller's registration number",
    "Customer's name",
    "If paid by card, what are the last 4 digits of the card used (do not ask for full card number, AT will never ask for customer's full credit or debit card number)",
    'How long has the road been affected',
    'What is the name of the school',
    'What direction is the light facing, eg. facing traffic coming along Nelson St from motorway',
    'What type of sign is affected',
    "What is the value of the caller's transaction",
    'If customer can read it',
    'What is the location of the problem, e.g. street address, road names',
    'Is the problem ponding',
    'If on state highway or motorway',
    'What outcome is the customer expecting',
    'What is the fault with the machine',
    'What is the name of the street and suburb or approximate location of the road works',
    'How long has the noise been going on',
    'Did the customer receive a letter advising of the work',
    'Does customer know the name of contractor doing the job',
    'Which road is the driver on when visibility is restricted',
    'What is obstructing visibility at this location, e.g. parked vehicles, traffic signs, fences',
    'Are there any existing parking restrictions in the turning circle, e.g. signage or broken yellow lines',
    'Is there a particular time of day this issue occurs',
    'Does the problem occur at a particular time',
    'Do all vehicles have difficulty turning or just larger vehicles, e.g. refuse trucks',
    "Customer's email for contact",
    'What is the issue, e.g. vibrating, noise, time of works etc.',
    'Has customer witnessed an occasion when an emergency vehicle was unable to pass through the road',
    'Method of payment',
    "What is the nature of the customer's concern for emergency vehicles ability to access a road or other location",
    'Vehicle licence plate number and any other plate numbers that are used by customer',
    'Time of transaction',
    'Machine number',
    'What is the issue',
    'Indicate the type of fault',
    'If paid by card, what are the last 4 digits of the card used (do not ask for the full card number, AT does not ask for full credit or debit card number)',
    'What is the customers contact number',
    'Location of the street furniture or fittings',
    'When did the works start',
    'What is the problem with the furniture or fittings, e.g. seat broken',
    'If stolen motorbike',
    'Is the damage causing an immediate health and safety risk, e.g. seat will collapse if sat on',
    'What is the existing traffic control at this intersection, e.g. roundabout, stop, give way, no control',
    'What is the safety concern at this intersection',
    'What type of vehicles does the customer want restricted',
    'What is the reason for requesting a restriction of vehicle access',
    'Fault description',
    'If the wrong vehicle licence plate number was entered, what number plate was used, and what is the correct plate number',
    'Which car park building',
    'What is the extent of problem, eg entire road or just a section',
    'What is the marking or sign that needs to be removed',
    'Why do you believe it needs to be removed',
    'What is the vehicle license plate number associated with the permit',
    'What is the current speed limit',
    'What is the exact location of the pedestrian buzzer/button on the traffic signal (obtain two road names at intersection)',
    'What speed would customer suggest the limit be changed to',
    'What is the nature of the problem, e.g. speed humps/judder bars are too high or too close together',
    'What is the address and suburb',
    'What information do they require',
    'What assistance is required, e.g. temporary signage requested, needed urgently because of accident, road works',
    'If in AT car park ',
    'What is the section of roadside the customer is requesting a footpath',
    'Is there an existing footpath on the other side of the road',
    'What damage has occurred to the footpath',
    'Is information required regarding current operation, general, or for a future planned activity',
    'Car park building name and location',
    'Does the issue occur at a particular time of day',
    'Day and time of transaction (if possible)',
    'Date and time of malfunction',
    'Why is the customer requesting a refund',
    'How long have they been on, e.g. today, the past few days',
    'Customer contact details, including postal or physical address',
    'What is the dollar value of transaction',
    'How many street lights are always on',
    'What seems to be the cause of the congestion',
    'Form of payment, i.e. credit card or EFTPOS',
    'Are there any existing plantings',
    'Would this planting restrict visibility for motorists or pedestrians',
    'What is the vehicle crossing application or reference number',
    'What was the time and date of the originally booked inspection',
    'What inspection was originally booked, i.e. pre-pour or final',
    'Does customer have any idea when the vehicle crossing will be ready for inspection by AT',
    'What is the address where the issue occurs, approximately',
    'How did the customer pay, e.g. cash, credit card, voucher, parking debit card',
    'Where is the location, e.g. Landmark, street address, intersection of the road names',
    'If removal of plants or vegetation is being requested, why do they need to be removed',
    'Location of the retaining wall',
    'What is the CAR number',
    'What is the address/location of the car park building or car park',
    'Customer’s email address (having an email address is mandatory for AT to process the refund as quickly as possible, and is our preferred method of contact)',
    'If query is about a CCTV attached to street light        ',
    'What type of tree planting is requested, e.g. pohutukawa tree, hedge',
    'What is the address of the accessway',
    'What is the problem with the bus shelter',
    'What is the reason for requesting a barrier',
    'What is the address of the issue',
    'Why does the customer believe that the structure is illegal',
    'What is causing the car to scrape',
    'What is the structure that has been built on AT property, e.g. shed, fence, election sign',
    'Location of the vehicle crossing',
    'If customer regularly drives different vehicle(s), also provide the vehicle licence plate number(s), in case customer inadvertently entered the wrong vehicle details.   ',
    'What direction is the light facing',
    'Does the bus shelter have major structural damage, e.g. damage from a motor vehicle accident',
    'Is the structural damage causing an immediate health and safety risk',
    'Description of incident',
    'Location of works – e.g. footpath, grass berm, sealed road way, etc',
    'How long has the structure been there',
    'Do you know who caused damage to the retaining wall',
    'If stolen bicycle or scooter – make and model  ',
    'Customers name',
    'Is the vehicle crossing being used for residential or commercial purposes',
    'What is the issue with the vehicle crossing',
    'What is the problem with the retaining wall, e.g. falling over, blocking footpath/road',
    'What are the names of the roads at the intersection',
    'Customers contact phone number',
    'Does the customer want the information posted or emailed',
    'If stolen vehicle – year, make and model  ',
    'What brochure, document or form does the customer require',
    'How many copies does the customer require',
    'Vehicle details',
    'Preferred Method of Contact',
    'Where in the car park would they have lost their item',
    'What day and time was the item lost',
    'A description of what has been lost',
    'What is the exact location where the issue is occurring at this intersection',
    'Are vehicles parking legally or illegally (within 6 metres of an intersection)',
    'Is the volume of the water in the vehicle crossing increasing',
    'What is the customer contact number',
    'What is your concern with people parking at this location (if a visibility issue, log as Visibility on road or driveway)',
    'Location of the bridge',
    'What is the problem with the bridge',
    'Description of incident, e.g. road rage, theft, crash or accident etc.',
    'If at an intersection',
    'Has a vehicle hit the bridge',
    'Is there a high likelihood it could be dangerous',
    'Location of vehicle',
    'Has the problem caused injury or made the bridge impassable',
    'What is the customers name',
    'Date and time incident occurred',
    'What happened',
    'What is the pedestrian safety issue',
    'What is the address',
    'What is the road name or location of where the incident took place',
    'What is the problem with where or how the vehicle is parked',
    'Is vehicle blocking an entrance',
    'Has the problem made the road impassable, e.g. sign fallen across road',
    'Please explain in detail what you believe the issue is',
    'If query is about a CCTV attached to street light',
    'What is the customer contact phone number or email address',
    'Has someone damaged the road as a result of works happening on the road or nearby',
    'Physical description of contractor',
    'Has the problem made the road or footpath impassable',
    'If paid by card, ask caller for the last 4 digits of their card number (do not ask for the full card number)  ',
    'If observed, a vehicle description or name on vehicle',
    'Is this problem causing a safety issue to users',
    'If in AT car park',
    'What is the problem with the grass verge or berm',
    'Is the call from the Police',
    'Does vehicle pose a safety risk for other road users',
    'Where in the building is the problem, e.g. near entrance, car park space number',
    'Additional information',
    'What is the problem,',
    'What type of sign is affected,',
    'If the light is inside an AT bus shelter',
    'What is the name of the school the request is being made for',
    'What is the issue at this location',
    'Location of the speed hump/judder bar',
    'What is the extent of problem',
    'If paid by card, what are the last 4 digits of the card used',
    'Was payment made using the AT Park app or ATM machine',
    'Customers email address',
    'What is the exact location of the traffic signal',
    'What is the nature of the problem, e.g. damaged, trip hazard',
    'Is this a request for improved signage or is there currently no signage in place',
    'Where on the road is the no exit sign required, e.g. start of road or mid-block intersection',
    'What is the name of the street',
    'Which parking building or car park is the customer in',
    'What is the problem, e.g. barrier arm not rising',
    'Where is the work taking place on the road reserve',
    'Would customer like to purchase a pre-paid parking voucher',
    'Customer email or postal address',
    'What is the facility / business that signage is required for',
    'What is the requested location for this new signage, e.g. street address or intersection',
    'What is the reason this sign is wanted',
    'Are there any other lights in the area not working e.g, shops, houses',
    'Which car park building is the customer in',
    "Customer's email for contact ",
    'What is the issue the customer is concerned about',
    'Has customer lost their voucher',
    'If request is for renewal or replacement of the existing footpath, why does the caller believe this is necessary',
    'When will vehicle crossing be ready for inspection by AT',
    'Where is the problem',
    'What intersection is the sign required for',
    'Is there an existing street name blade for this street',
    'If request is to relocate a street name sign, why does it need to be relocated',
    'If request is for a new street name blade, why is it required',
    'List all streets that are out',
    'What is the issue with the traffic island, pedestrian refuge or chicane, e.g. damaged, trip hazard',
    'What is missing',
    'Has the street recently been resurfaced',
    'What is obstructing visibility at this location',
    'What is wrong with the road markings',
    'Is this a one-way or no-exit street',
    'What is the approximate location the customer feels the sign should be placed',
    'Customers contact number',
    'What is the address of the location that requires a fence',
    'Why is a fence required at this location',
    'Could signs be installed to prevent vehicles parking for sale',
    'What is the safety issue',
    'Is there a particular time of day the issue occurs',
    'If request is for renewal or replacement of the existing stormwater asset, why does the caller believe this is necessary',
    "Customer's car registration number",
    'Any other queries',
    'Can you identify the contractor',
    'What is the address of the pedestrian crossing (approximately)',
    'What is the name of the road',
    'Has this issue been raised with the NZ Police',
    'Has the problem made the sign unreadable',
    'Location of vehicle and/or incident within building, e.g. level, car park number, near exit',
    'Car details',
    'Where is the work taking place',
    'What is the NECAR number',
    'Are there any relevant signage and/or road markings at this location',
    'What is the intersection number and names of the roads at this intersection',
    'Are there any other lights in the area not working, e.g. shops, houses',
    'If the light is inside an Auckland Transport bus shelter',
    'How long does it normally take at this location',
    'What is the problem with the tree or vegetation',
    'What is the information for',
    'What is the location of the problem, e.g. street address or intersection',
    'What is the problem, ',
    'Date and time  ',
    'List all streets with lights that are out ',
    'Description of incident, e.g. road rage, theft, crash or accident etc. ',
    'What is the problem, e.g. spilt liquid, graffiti, litter',
    'If stolen vehicle – year, make and model',
    'What is the incident, e.g. vehicle damage, theft, breakdown',
    'What caused the incident',
    'Was the damage caused by parking building equipment or maintenance fault',
    'Location of works – e.g. footpath, grass berm, sealed road way, etc ',
    'If paid by coin',
    'Which approach to the intersection is a camera required',
    'What is the reason for a camera ie what did the caller observe at the intersection to suggest a new camera is required, did caller observe a crash or ongoing red light running',
    'What is the location of the street furniture or fittings',
    'What type of furniture or fitting is missing',
    'Is the missing item causing an immediate health and safety risk',
    'What is the facility that signage is required for',
    'Where is the signage required',
    'Was there a sign there previously',
    'What damage has occurred to the footpath, off-road cycle path or road to road walkway',
    'What is the reason for requesting the seat',
    'At what location is the customer intending to install the convex mirror',
    'Why is the convex mirror needed',
    'Does the customer have permission from the landowner',
    'What asset has been damaged',
    'What damage has been done',
    'Who is responsible for the damage',
    'What is the location or name of the development',
    'What is the Resource Consent or Land Use Consent number',
    'If damage to car, ask customer to detail damage to car',
    "Customer's name ",
    'Is this a private mirror',
    'Who installed the mirror, e.g. was it the property owner, Auckland Transport or a legacy Council',
    'What is the address of the mirror',
    'What is the location of the mirror in relation to the closet address, e.g. opposite side of road from given address',
    'If paid by card, ask caller for the last 4 digits of their card number (do not ask for the full card number)',
    'Do you know who caused damage to the footpath',
    'What is the address the customer would like the seat placed (approximately)',
    'Advise on the webform if you or the customer has spoken to anyone else associated with this project, i.e. Stakeholder Manager or Police.    Preferred Method of Contact',
    'What is the problem, e.g. pothole, broken door',
    'If theft, ask customer to provide list of what is missing and approximate value of each item',
    'What is the location you would like the traffic count data gathered',
    'What data does the customer request be gathered',
    'Who has previously maintained the mirror',
    'How long has this problem existed',
    'What kind of sign is required, e.g. ducks crossing, horses in area',
    'What is the vehicle crossing application number ',
    'Is an insurance company involved',
    "Please ensure that you have the entered the customer's contact details",
    'If damaged, do you know who caused the damage',
    'List all streets that are out.',
    'How long has this been a problem',
    'Is the damage causing a trip hazard',
    'What type of road marking is being requested, e.g. give way marking, center line marking',
    'What is the customers query',
    'Can you describe the problem as fully as possible, i.e. is the street light, pole or fittings or exterior damaged',
    "AT machine/meter number, this is a four-digit number displayed in the top left-hand corner of the machine's screen",
    'Postal Address',
    'What is their permit number',
    'Customer query',
    'Advise on the webform if you or the customer has spoken to anyone else associated with this project, i.e. Stakeholder Manager.',
    'Urgent cleaning',
    'What time of day does the issue occur',
    'What is the wait time or length of queue at the intersection, approximately',
    'What type of road marking is being requested',
    'Is there an immediate safety risk',
    "AT machine/meter number, this is a four-digit number displayed in the top left-hand corner of the machine's screen  ",
    'Additional Information',
    'If request is for renewal or replacement of an existing infrastructure asset, why does the caller believe this is necessary',
    "What is the customer's relationship to the development or project, i.e. land owner or developer",
    'Was the website accessed on a mobile device (phone/tablet) or computer (desktop/laptop)',
    'What is the existing traffic control at the intersection, e.g. give way, roundabout, stop, no control',
    'What is the building consent number',
    'If yes, what is the vehicle crossing application number',
    'What is the problem ',
    'Is the request for maintenance or replacement of an existing sign',
    'Is the request for a new sign',
    'Ask caller for the Police event number associated with the call and record the number in your notes.',
    'What type of sign is affected, ',
    'Is the blockage likely to cause flooding soon',
    'List all streets with lights that are out  ',
    'Does customer have photos',
    'What direction is the light facing, e.g. facing traffic coming along Nelson Street from motorway',
    'If call is about a damaged CCTV camera, which floor is the camera located on and where',
    'How large is the issue',
    'If customer regularly drives different vehicle(s), also provide the vehicle licence plate number(s), in case customer inadvertently entered the wrong vehicle details',
    'How big is the issue',
    'Customer name',
    'What is the query regarding',
    'If customer regularly drives different vehicle(s), also provide the vehicle licence plate number(s), in case customer inadvertently entered the wrong vehicle details. N/A  ',
    'What is the section heading, e.g. Parking in Auckland',
    'What browser was customer using, e.g. Internet Explorer, Chrome, Firefox, Safari',
    'What is the issue/suggestion',
    'Did customer get any error messages when trying to perform the task',
    'How frequently does the congestion / delay occur',
    'If stolen bicycle or scooter – make and model ',
    'How big is the slip or subsidence',
    'What is the address of the piece of road concerned, approximately',
    'What does the customer think is required at this location',
    'What is the location of the culvert',
    'Vehicle license plate number',
    'What type of sign is required',
    'Why is the sign required',
    'Where is the signage required in the car park building or car park',
    'What is the issue,',
    'Ask caller for the Police event number associated with the call and record the number in your notes',
    'Location of works',
    'What is the issue, ',
    'Advise on the webform if you or the customer has spoken to anyone else associated with this project, i.e. Stakeholder Manager',
    'Who is doing the activity',
    'Description of incident, e.g. road rage, theft, crash or accident etc',
    'What is the page link (URL) or name of online service, e.g. Journey Planner',
    'If query is about a CCTV attached to street light N/A        ',
    'What is the problem with the cover plate (door to wiring at the bottom of the street light) or street light shield',
    'On which approach(es) to the intersection does the congestion / delay occur',
    'If stolen vehicle – year, make and model ',
    'If for a re-inspection, why was it originally failed',
    'When would customer like to pour the concrete',
    'Does customer know what type of work was being carried out',
    "Customer's contact number ",
    'What is the name of the road or address of the piece of road',
    'Type of animal',
    'How big is the pothole',
    'Check the query is not covered under any other maintenance process or new request.    ',
    'Which road safety program is the customer querying',
    'Nature of works',
    'Date and time',
    'What is the customer',
    'In 2022, vouchers may be offered through the AT Park app, to help the team prepare for the transition, ask customer',
    'How often does this occur',
    'If paid by card, ask caller for the last 4 digits of their card number (do not ask for the full card number) N/A  ',
    'If customer is requesting multiple receipts, ensure all dates and relevant vehicle licence plate numbers are listed (only one case is required)',
    'If paid by card, ask caller for the last 4 digits of their card number (do not ask for the full card number) n/a  ',
    'Date, time and location of incident',
    'If slippery',
    'If trip hazard',
    'Does customer have any other information',
    'What is obstructing visibility at this location,',
    'Is the pothole in the main wheel-track of the road',
    'Where is the work taking place on the road reserve, ',
    'Location of works – e.g. footpath, grass berm, sealed road way, etc  ',
    'Where is the clock',
    'What is the problem with the clock',
    'If query is about a CCTV attached to street light ',
    'How large is the area covered with leaf fall',
    'Level 2 Complaint',
    'What is the current speed limit on the road',
    'Is the sign missing or damaged',
    'Location of the issue ',
    'Length of abandonment',
    'Customer’s email address',
    'Name or area of consultation',
    'List all streets that are out.  ',
    'What is the address of the crane',
    'What is their contact phone number',
    'What type of sign is affected, e.g. street name',
    'If person phoning is from the Police',
    'Why are the markings required',
    'What is the address where the cross or sign is required, approximately',
    'Where on the road reserve would the cross or sign be placed',
    'What is the address of the scaffolding and/or gantry',
    'Are leaves covering or blocking one or more storm water grates',
    'Check the query is not covered under any other maintenance process or new request.  ',
    'What direction is the light facing, ',
    'Location of works – e.g. footpath, grass berm, sealed road way, etc Road  ',
    'Where in the car park building',
    'What is the location of the CCTV camera',
    'What is the issue with the camera',
    'What is the issue with the tactile indicator, e.g. damage, trip hazard, slippery',
    'What is blocking the grate',
    'What direction is the light facing,',
    'If the request is for renewal or replacement of an existing infrastructure asset, why does the caller believe this is necessary',
    'Any other relevant details.    Preferred Method of Contact',
    'If paid by card, what are the last 4 digits of the card used ',
    'Location of works – Road  ',
    'Check this is an AT car park.  ',
    'How large is the issue e.g. 1 meter long',
    'What is the address where angle parking is required, approximately',
    'What is the current parking at this location',
    'If customer regularly drives different vehicle(s), also provide the vehicle licence plate number(s), in case customer inadvertently entered the wrong vehicle details.  ',
    'If customer is requesting a free hi-vis vest  ',
    'What type of activity is taking place and where is it in the road reserve',
    'If customer regularly drives different vehicle(s), also provide the vehicle licence plate number(s), in case customer inadvertently entered the wrong vehicle details. NA  ',
    'Are there any identifying company logos or markings on the equipment',
    'What is the query,',
    "Customer's name  ",
    'Any other relevant details',
    "What is the customer's relationship to the development or project, i.e. land owner, neighbour or developer",
    'What asset or facility is the customer querying',
    'How is the caller impacted',
    'Location of problem',
    'Vehicle details (if possible)',
    'What is or was the problem',
    'What is the problem with the retaining wall',
    'Which school program is the customer querying',
    'What damage has occurred to the footpath, ',
    'If in AT car park N/A ',
    'What is the name of the road or address of the piece of road ',
    'Where in the building is the lift',
    'What is the lift number (if it is visible)',
    'Advise on the webform if you or the customer has spoken to anyone else associated with this project',
    'Check the query is not covered under any other maintenance process or new request',
    'Location of works – e.g. footpath, grass berm, sealed road way, etc Road   ',
    'What is the problem with the tree',
    'What type of road marking is being requested,',
    'What damage has occurred to the footpath,',
    'Is the problem on the road',
    'If stolen bicycle or scooter – make and model',
    'Where is the rubbish',
    'What type of litter is it',
    'Is it a single bit of rubbish or does the whole street in general need a clean up',
    'How much litter is there',
    'In 2022, vouchers may be offered through the AT Park app, to help the team prepare for the transition, ask customer (still a work in progress)',
    'If customer is requesting a free hi-vis vest ',
    'How long does it normally take at this location',
 
                         ]


##############################  Email Variables  ##############################

at_email_domain = ["at.govt.nz", "at.co.nz", "govt.nz", "athop.co.nz", "aucklandtransport.govt.nz", 
                   "aucklandcouncil.govt.nz", "snapsendsolve.com"]
staff_template_text = ["please leave the subject line of this email intact",
                       "started working on your case",
                       "please contact the auckland transport",
                       "20 viaduct harbour avenue",
                       "thanks for getting in touch with auckland rransport",
                       "We’ve started working on your case"
                      ]
pronouns = ["i", "iam", "am", "me", "my", "im"]
email_pat = r'[\w.+-]+@[a-zA-Z0-9\-]+\.[\w.-]+'
email_text_to_be_removed = ["To:", "Subject:", "Sent:", "Received:", "Date:", "Re:", "Fw:", "RE:", "FW:", "Fwd:", "<", ">"]




##############################  Web Variables  ##############################

pat1_rephrase = {"Route Number :": ". The route number is ",
                 "Station name :": ". In station ",
                 "Date and time:": ". The date time is ", 
                 "What does the problem relate to?:": ". The problem relates to ", 
                 "Have you reported this issue before?:": "The issue has been reported before. ",
                 "Have you requested this before?:": ". I have requested this before. ",
                 "Do you know who caused this? :": ". This cause by ",
                 "Issue description :": ". ", 
                 "What is the problem?:": ". ",
                 "What would you like to request? :": ". The request is ",
                 "What would you like to ask? :": ". ",
                 "What would you like to tell us? :": ". ",
                 "Does your request relate to a specific location? :": ". The location is ",
                 "Information requested :": ". The information request is ",
                 "What does your request relate to?:": ". The request relates to ",
                 "Let us know any other information OR if you would like to request inspection for more than one vehicle crossing located in the same area then please provide details here. :": " ",
                 "Let us know of any additional information :": ". ",
                 "Additional location information :": ". Additional location information is ",
                 "Let us know the details of your feedback or suggestions :": " ",
                 "Bus stop number :": ". The bus stop number is ",
                 "Suggested bus stop name :": ". The suggested bus stop name is ",
                 "Bus stop name :": ". The bus stop name ",
                 "Route:": ". In route ",
                 "Description:": ". ",
                 "Desired Outcome:": ". The desired outcome is ",
                 "Lost property description :": ". ",
                 "Park & Ride name :": ". At ",
                 "Direction of travel:": ". Travel direction"
                }

personal_other_fields = [
"Type of inspection required:",
"Concrete pour date :",
"Vehicle crossing application reference number :",
"First name :",
"Last name :",
"Your preferred date:",
"Contact phone number:",
"Customer contact details:",
"Date of birth:",
"client number:",
"Business phone:",
"Name on SuperGold card :",
"Level 2 Complaint:",
"Preferred Method of Contact:"
]

AT_template_sentences = ["Ask for route or schedule information",
"Ask for accessible travel information",
"Ask for accessible travel information"
"Ask for on-board bus information",
"FINAL INSPECTION REQUEST",
"FINAL INSPECTION BOOKING",
"PREPOUR INSPECTION BOOKING",
"Official information LGOIMA",
"Update AT HOP SuperGold concession details",
"Request maintenance or report damage to off street carpark",
"- nearest address or landmark",
"nearest address or landmark"
]


##############################  Phone Variables  ##############################


questions_to_remove_with_answers = [
    "What is the customer name",
    "What is the address of the proposed vehicle crossing",
    "What is the customer's name",
    "What is the customer's contact number",
    "What is the address of the vehicle crossing",
    "What is the customer's physical address",
    "What is the customer's email address",
    "What is the AT Park area ID number",
    "What is the vehicle licence plate number associated with the permit",
    "What is their permit number",
    "What type of phone is the customer using",
    "When will vehicle crossing be ready for inspection by AT",
    "When will the vehicle crossing be finished and ready for inspection by AT",
    "When would customer like to pour the concrete",
    "Date of parking",
    "Time and date of transaction",
    "Vehicle registration number",
    "If person phoning is from the Police, do they have an event number associated with the call",
    "Has customer received their approved vehicle crossing permit",
    "Does the customer have an approved vehicle crossing permit",
                                    
                      ]

questions_to_rephrased = {
    "What is the issue with the sign": ". The sign is ",
    "What time did AT Park parking session stop": ". The park session stoped at ",
    "What is the query": ". The query is ",
    "What is the vehicle crossing application number": ". vehicle crossing application number is ",
    "What is the customer's request": ". ",
    "What type of sign is affected": ". The sign affected is ",
    "What damage has occurred to the footpath, off-road cycle path or road to road walkway": ". The damage is ",
    "What is the problem": ". The problem is ",
    "What is the enquiry": ". The enquiry is ",
    "What is the road name": ". The road name is ",
    "What is the address/approximate location of issue": ". The location is ",
    "What is the location": ". The location is ",
    "What is the location - nearest street address or landmark": ". The location is ",
    "What is blocking the grate": ". The grate is blocked by ",
    "What size is the pothole": ". The size of the pothole is ",
    "What time did customer start parking": ". The customer started parking ",
    "Why does customer want increased monitoring at this site": ". Reason for increased monitoring ",
    "Why does customer want a refund": ". Customer wants refund because ",
    "What is the location of the streetlight": ". The location of the streetlight ",
    "Where was customer parked": ". The customer parked at ",
    "How big is the issue": ". The issue is ",
    "How often does this occur": ". This occurs ",
    "How long has the road been like this": ". The road has been like this for ",
    "How large is the problem": ". The problem is ",
    "Does this issue occur at all times, or does it only happen at a certain times of the day": ". The issue occurs ",
    "Do you know who caused damage to the footpath, offload cycle path or road to road walkway": ". The damage caused by ",
    "Can you describe the problem as fully as possible": ". ",
    "Location": ". Location is ",
    "Location of the sign": ". Location of the sign is ",
    "Is the damage causing a trip hazard, making the area impassable, or caused injury": ". The damage cause ",
    "Is the road sealed or unsealed": ". The road is ",
    "Is the light above a pedestrian crossing": ". The light above a pedestrian crossing",
    "Is the light a belisha beacon (orange light) at a pedestrian crossing": ". The light is a belisha beacon at pedestrian crossing ",
    "Is the location a rural intersection": ". The location is a rural intersection ",
    "Is the problem on the road, footpath or cycleway": ". The problem on ",
    "If graffiti etched into concrete, is it offensive": ". ",
    "Has the problem made the road or footpath impassable": ". The problem caused " 
    
    }

yes_or_no_rephrase = {"Are there": ". Yes there are",
 "Are there any": ". Yes there are",
 "Are": ". Yes",
 "Is the": ". Yes the",
 "Is": ". Yes the",
 "Has": ". Yes",
 "Does": ". Yes",
 "Has anyone": ". Yes someone"
}

template_sentences_to_be_removed = [
    "Pre-pour inspection booking process - all questions need to be answered.", 
    "Preferred Method of Contact: E-mail",
    "Preferred Method of Contact: Mobile Phone",
    "If no or customer unsure, record this in the job notes.",
    "If customer is unable to locate their application number on their form, refer to legacy council table to assist them.",
    "(quite often the name or company logo is on the equipment i.e. cones, vehicles and signs)",
    "Has any action been taken (e.g. emergency services, doctors visit etc)",
    "If no, what is the likelihood that someone would be injured and if so, how serious would that be",
    "Why and how is it dangerous Yes anyone been injured",
    "( if applicable - trigger point is if more than 5 min)",
    "(this is so that AT can compare with what the delay times are)",
    "(10s, 100s, 1000s)",
    "n/a",
    "What is the problem with the grass verge or berm, Tree near the lamb post the logs are rotten and sharp pointing out and in the edge between the footpath and the berm, the tree need trimming along the edge of the berm."
                                   ]



############################## Utility functions  ##############################


def regex_escape(text):
    text = text.replace("(", "\(")
    text = text.replace(")", "\)")
    text = text.replace("+", "\+")
    text = text.replace("[", "\[")
    text = text.replace("]", "\]")
    text = text.replace("?", "\?")
    text = text.replace("*", "\*")
    text = text.replace("$", "\$")
    
    return text

def regex_escape_reverse(text):
    text = text.replace("\(", "(")
    text = text.replace("\)", ")")
    text = text.replace("\+", "+")
    text = text.replace("\[", "[")
    text = text.replace("\]", "]")
    text = text.replace("\?", "?")
    text = text.replace("\*", "*")
    text = text.replace("\$", "$")
    
    return text


############################## Email Channel Processing Function   ##############################



def merge_writer_header(s1, s2):
    i = 0
    while not s2.startswith(s1[i:]):
        i += 1
    return s1[:i] + s2
    
    
def check_owner(body, from_email=None):
    
    if from_email:
        email = re.findall(email_pat, from_email)
        if email:
            email = email[0]
            if email[email.index('@') + 1 : ] in at_email_domain:
                return "staff"
            else:
                return "customer"
    
    if any(substr.lower() in body.lower() for substr in staff_template_text):
        return "staff"
    elif any(substr in body.split() for substr in pronouns):
        return "customer"
    else:
        return "unknown"
    
            
def get_subject_body(writer, email, header=None):
    
    
    sub_body = email
    if header:
        sub_body = sub_body.replace(merge_writer_header(writer,header), '')

        
    
    for text in email_text_to_be_removed:
        sub_body = sub_body.replace(text, '')
        
    email_addrs = re.findall(email_pat, sub_body)
    if email_addrs:
        for addr in email_addrs:
            sub_body = sub_body.replace(addr, '')
    
    sub_body = sub_body.strip()
    
    return sub_body    
    
    

def parse_email(writer, email):
    
    from_match = None
    to_match = None

    header_pat = ["From:(.*?)Sent:(.*?)To:(.*?)Subject:",
                   "From:(.*?)Received:(.*?)To:(.*?)Subject:",
                   "From:(.*?)Date:(.*?)To:(.*?)Subject:",
                   "From:(.*?)To:(.*?)Sent:(.*?)Subject:",
                   "From:(.*?)To:(.*?)Date:(.*?)Subject:",
                   "From:(.*?)Date:(.*?)Subject:(.*?)To:",
                   "From:(.*?)Subject:(.*?)Date:(.*?)To:",
                   "From:(.*?)To:(.*?)Subject:",
                   "From:(.*?)To:(.*?)Date:",
                   "From:(.*?)Received:(.*?)To:",
                   "From:(.*?)Sent:(.*?)To:",
                   "From:(.*?)To:"
                  ]
    


    header_pat_no_to = [
                        "From:(.*?)Date:(.*?)Subject Line:",
                        "From:(.*?)Date:(.*?)Subject:",
                        "From:(.*?)Received:(.*?)Subject:",
                        "From:(.*?)Sent:(.*?)Subject:",
                        "From:(.*?)Sent:",
                        "From:(.*?)Date:"
                       ]
    
    
    match = []
    if "To:" in email:
        for pat_ in header_pat:
            if re.findall(f'({pat_})', email): 
                match = re.findall(f'({pat_})', email)
                from_match = match[0][1] 
                if not pat_.split("(.*?)")[-1] == "To:":
                    to_match = re.findall("(\s?To:.*?(?:Sent:|Date:|Subject:))", match[0][0])[0]

                break
    else:
        for pat_ in header_pat_no_to:
            if re.findall(f'({pat_})', email):
                match = re.findall(f'({pat_})', email)
                from_match = match[0][1]
        

    if match:
        sub_body = get_subject_body(writer, email, header=match[0][0])
        owner = check_owner(sub_body, from_email=match[0][1])
    else:

        sub_body = get_subject_body(writer, email)
        owner = check_owner(sub_body)

    return from_match, to_match, sub_body, owner
 
    
       
def get_email_attributes(writer, email): 
    
    from_match = None
    to_match = None
    sub_body = None
    
    
    if "From:" in writer:
        from_match, to_match, sub_body, owner = parse_email(writer, email)
    elif "wrote:" in writer:
        sub_body = email.replace(writer, '')
        if re.findall(email_pat, writer):
            from_match = re.findall(email_pat, writer)[0]
            owner = check_owner(sub_body, from_email=from_match)
        else:
            owner = check_owner(sub_body)
            
    else:
        print("Came Else of get_email_attributes, please check")
    
    return from_match, to_match, sub_body, owner
    
    
def parse_case(split_email): 
    
    from_ = []
    to_ = []
    sub_body_ = []
    owner_ = []
    
    ord_ = 0
    i = 0
    while i < len(split_email):
        if ("From:" in split_email[i]) or ("wrote:" in split_email[i]):
          
            order = ord_
            if i+1 < len(split_email):
                
                from_match, to_match, sub_body, owner = get_email_attributes(split_email[i], split_email[i]+split_email[i+1])
                
                from_.append(from_match)
                to_.append(to_match)
                sub_body_.append(sub_body)
                owner_.append(owner)
            
            i += 2
            
        else:
            order = ord_
            if split_email[i] != ' ' or split_email[i] != '  ':
            
                from_match = None 
                to_match = None
                sub_body = split_email[i]
                owner = check_owner(sub_body)

                from_.append(from_match)
                to_.append(to_match)
                sub_body_.append(sub_body)
                owner_.append(owner)
            
            i += 1
        ord_ += 1
        
    return from_, to_, sub_body_, owner_


def break_multi_wrote(text):
    
    x = re.findall('wrote:', text)
    wrote_pat = [
                 "On\s((?:\S+(?:\s+|$)){,17})wrote:",
                 "<*[\w.+-]+@[a-zA-Z0-9\-]+\.[\w.-]+>* wrote:"
                ]
    result = []

    for m in re.finditer('wrote:', text):
        tmp = text[:m.end()]
        y = re.findall(f'({"|".join(wrote_pat)})', tmp)
        if y:
            result.append(y[0][0])
        else:
            result.append("wrote:")

        text = text.replace(tmp, '')

    return result


### Main Function
def process_email_channel(s):
    
    if "From:" in s or "wrote:" in s:

        s = str(s)
        s = s.replace("'", "")

        if "(at) wrote:" in s or "(AT) wrote:" in s:
            s = s.replace("(at) wrote:", "someone@aucklandtransport.govt.nz wrote:")
            s = s.replace("(AT) wrote:", "someone@aucklandtransport.govt.nz wrote:")

        at_name_replace_pattern = re.findall('From:(\s?(?:\w+(?:\s?)){0,5}\(AT\))', s)

        if at_name_replace_pattern:
            for l in at_name_replace_pattern:
                s = s.replace(l, '.'.join(l.replace("(AT)", "").split())+"@at.govt.nz")


        from_wrote_pat = [
                       "wrote:",
                       "From:",
                       "[ ]?[-]{1,}[ ]*Original Message[ ]*[-]{1,}[ ]{1,7}From:",
                       "[ ]?[-]{1,}[ ]*Original message[ ]*[-]{1,}[ ]{1,7}From:",
                       "[ ]?[-]{1,}[ ]*Original email below[ ]*[-]{1,}[ ]{1,7}From:",
                       "[ ]?[-]{1,}[ ]*Original Message[ ]*[-]{1,} > From:",
                       "[ ]?[-]{1,}[ ]*Original message[ ]*[-]{1,} > From:"
                      ]

        from_wrote_matchs = re.findall(f'({"|".join(from_wrote_pat)})', s)
        from_wrote_matchs = list(set(from_wrote_matchs))

        from_wrote_matchs_new = []

        for match in from_wrote_matchs:
            if "From:" in match:
                from_wrote_matchs_new.append(match)
            elif "wrote:" in match:
                wrote_pat = [
                             "On\s((?:\S+(?:\s+|$)){,20})wrote:",
                             "<*[\w.+-]+@[a-zA-Z0-9\-]+\.[\w.-]+>* wrote:"
                            ]
                wrote_match = re.findall(f'({"|".join(wrote_pat)})', s)
                if wrote_match:
                    for match in wrote_match:
                        if len(re.findall('wrote:', wrote_match[0][0])) > 1:
                            for result in break_multi_wrote(wrote_match[0][0]):
                                from_wrote_matchs_new.append(result)
                        else:
                            from_wrote_matchs_new.append(match[0])

                else:
                    from_wrote_matchs_new.append('wrote:')
            else:
                print("No From: Wrote: matches found, please check")



        from_wrote_matchs_new = [w.replace("(", "\(") for w in from_wrote_matchs_new]
        from_wrote_matchs_new = [w.replace(")", "\)") for w in from_wrote_matchs_new]
        from_wrote_matchs_new = [w.replace("+", "\+") for w in from_wrote_matchs_new]
        from_wrote_matchs_new = [w.replace("[", "\[") for w in from_wrote_matchs_new]
        from_wrote_matchs_new = [w.replace("]", "\]") for w in from_wrote_matchs_new]

        if len(from_wrote_matchs_new) > 1:
            pattern = "|".join(from_wrote_matchs_new)
        else:
            pattern = from_wrote_matchs_new[0]

        split_email = re.split(f"({pattern})", s)
        split_email = list(filter(lambda x: x if not x.isspace() else x.strip(), split_email))
        split_email = list(filter(None, split_email))

        from_emails, to_emails, sub_body_email, owner_label = parse_case(split_email)

        customer_content_list = []
        staff_content_list = []
        if owner_label:
            for i in range(len(owner_label)):
                if owner_label[i] == "customer" or owner_label[i] == "unknown":
                    customer_content_list.append(sub_body_email[i])
                elif owner_label[i] == "staff":
                    staff_content_list.append(sub_body_email[i])
        
        return staff_content_list, customer_content_list
                    
    else:
        return [], [s]


    






############################## Phone Channel Processing Function   ##############################



def phone_channel_pattern_match(text):

    pat2 = r'(?:^|\s)\d{1,2}[.]\s{1,}(.*?)(?:\:|\?| -|\d{1,2}[.])' 
    pat4 = r'Name:(.*?)Phone:(.*?)Location:(.*?)Preferred Method of Contact:'
    pat5 = r'From:|wrote:'
    pat6 = ["Graphical ID:", "Transaction Date:", "Process Date:", "Refund ID:"]
    pat7 = ["Parking - Request for review of Infringement", "Enforcement stationary and abandoned vehicle", 
            "2122-Parking Request - Vehicle Towing"]

    pat2_matchs = re.compile(pat2).findall(text)
    pat4_matchs = re.findall(pat4, text)
    pat5_matchs = re.findall(pat5, text)
    pat6_matchs = re.findall(f"{'|'.join(pat6)}", text)
    pat7_matchs = re.findall(f"{'|'.join(pat7)}", text)
    
    return pat2_matchs, pat4_matchs, pat5_matchs, pat6_matchs, pat7_matchs



def remove_question_pat(question, questions, check_answer=False):
    
    s_marker = regex_escape(question)
    if questions.index(question)+1 < len(questions):
        e_marker = questions[questions.index(question)+1]
        e_marker = regex_escape(e_marker)
        
        if not check_answer:
            pat = "((?:^|\s)\d{1,2}[.]\s*" + s_marker + ".*?)" + "(?:" + "\d{1,2}[.]\s*" + e_marker + ")"
        else:
            pat = "(?:^|\s)\d{1,2}[.]\s*" + s_marker + "\?*(.*?)" + "(?:" + "\d{1,2}[.]\s*" + e_marker + ")"
            
    else:
        if not check_answer:
            pat = "((?:^|\s)\d{1,2}[.]\s*" + s_marker + ".*?)" + "(?:Preferred Method of Contact|$)"
        else:
            pat = "(?:^|\s)\d{1,2}[.]\s*" + s_marker + "\?*(.*?$)"
    
    return pat


def get_question(question, text):
    
    pat = r'(?:^|\s)\d{1,2}[.]\s{1,}'+ regex_escape(question) + '.*?(?:\:|\?| -)'
    if re.findall(pat, text):
        return re.findall(pat, text)[0]
    else:
        return None
    
    

def clean_template_question(questions, text):
    

    sentence_to_be_removed = []
    sentence_to_be_rephrased = {}
    
    for question in questions:

        ### Questions to be removed
        if question in questions_to_remove_with_answers:
            pat = remove_question_pat(question, questions)

            if re.compile(pat).findall(text):
                sentence_to_be_removed.append(re.compile(pat).findall(text)[0])
                
            else:
                print("Else remove question case-", text)

        ### Questions to be rephrased
        if any(question.startswith(ques_) for ques_ in list(questions_to_rephrased.keys())):
            
            matched_question = list(filter(None, [ques_ if question.startswith(ques_) else None for ques_ in list(questions_to_rephrased.keys())]))[0]
            pat = remove_question_pat(question, questions, check_answer=True)
            
            if re.compile(pat).findall(text):
                ans_to_question = re.compile(pat).findall(text)[0]
                ans_to_question = ' '.join(ans_to_question.split())
                ## Checking if answer is not empty if empty remove the question
                if re.findall('\w+', ans_to_question):
                    
                    if get_question(question, text):
                        sentence_to_be_rephrased[get_question(question, text)] = questions_to_rephrased[matched_question]
                    else:
                        sentence_to_be_rephrased[question] = questions_to_rephrased[matched_question]
                else:
                    pat = remove_question_pat(question, questions)
                    sentence_to_be_removed.append(re.compile(pat).findall(text)[0])
                    
            else:
                print("Else rephrase question case-", text)

                    
    
        ### Yes or No Questions            
        if re.findall('^(\s*Is|\s*Are|\s*Has|\s*Does)', question):

            pat = remove_question_pat(question, questions, check_answer=True)
            if re.compile(pat).findall(text):
                ans_to_question = re.compile(pat).findall(text)[0]
                
                try:

                    ## Checking if answer is 'no' if 'no' remove the question with answer
                    if re.findall('\w+', ans_to_question):
                        first_word_of_ans = re.findall('\w+', ans_to_question)[0]
                        if first_word_of_ans.lower() == "no":


                            if len(re.findall('\w+', ans_to_question)) > 2: 
                                match_yes_or_no_phrase = re.findall('^'+'|'.join(list(yes_or_no_rephrase.keys())), question)[0]
                                ques_with_ans = re.findall(regex_escape(question)+".*?"+regex_escape(ans_to_question), text)[0]
                                to_replace_sentence = re.findall(regex_escape(question)+".*?"+regex_escape(first_word_of_ans), ques_with_ans)[0]
                                reconstructed_sentence = ' ' + ans_to_question.replace(first_word_of_ans, '', 1)


                                pat = remove_question_pat(question, questions)
                                if re.compile(pat).findall(text):
                                    sentence_to_be_rephrased[re.compile(pat).findall(text)[0]] = reconstructed_sentence
                                else:
                                    sentence_to_be_rephrased[ques_with_ans] = reconstructed_sentence


                            else:

                                pat = remove_question_pat(question, questions)
                                sentence_to_be_removed.append(re.compile(pat).findall(text)[0])

                        if first_word_of_ans.lower() == "yes":

                            if re.findall('^'+'|'.join(list(yes_or_no_rephrase.keys())), question):

                                match_yes_or_no_phrase = re.findall('^'+'|'.join(list(yes_or_no_rephrase.keys())), question)[0]
                                ques_with_ans = re.findall(regex_escape(question)+".*?"+regex_escape(ans_to_question), text)[0]



                                to_replace_sentence = re.findall(regex_escape(question)+".*?"+regex_escape(first_word_of_ans), ques_with_ans)[0]



                                reconstructed_sentence = question.replace(match_yes_or_no_phrase, yes_or_no_rephrase[match_yes_or_no_phrase]) + ' ' + ans_to_question.replace(first_word_of_ans, '', 1)


                                pat = remove_question_pat(question, questions)
                                if re.compile(pat).findall(text):
                                    #text = text.replace(re.compile(pat).findall(text)[0], reconstructed_sentence)
                                    sentence_to_be_rephrased[re.compile(pat).findall(text)[0]] = reconstructed_sentence
                                else:
                                    sentence_to_be_rephrased[ques_with_ans] = reconstructed_sentence
                                    #text = text.replace(ques_with_ans, reconstructed_sentence)


                    else:
                        pat = remove_question_pat(question, questions)
                        sentence_to_be_removed.append(re.compile(pat).findall(text)[0])
                except:
                    print("Failed at clean template function-", text)
                
            else:
                print("Else Yes or No question case-", text)
                

    if sentence_to_be_removed:
        for sent_ in sentence_to_be_removed:
            text = text.replace(sent_.strip(), '')

    if sentence_to_be_rephrased:
        for ques_,sent_ in sentence_to_be_rephrased.items():
            text = text.replace(ques_, sent_)
            
    for ques_ in questions:
        
        if ques_ in all_template_questions:
            
            try:
                text = re.sub("((\d{1,2}[.]\s{1,}|)"+regex_escape(ques_)+"(\?|:|\?:| -|))", '. ', text)
            except:
                
                text = text.replace(ques_, '. ')
    
    text = re.sub('\?', '', text)

    return text



def process_phone_channel(text):
    

    pat2_matchs, pat4_matchs, pat5_matchs, pat6_matchs, pat7_matchs = phone_channel_pattern_match(text)
    

    ### Dealing with Pattern 1 
    pat1_matchs = []
    for sent_ in list(pat1_rephrase.keys())+personal_other_fields:
        if sent_ in text:
            pat1_matchs.append(regex_escape(sent_))

    if (pat1_matchs and not pat2_matchs) or (len(pat1_matchs) > len(pat2_matchs)):
        text = clean_form_type(pat1_matchs, text)

    ###Dealing with Templating Questions 
    elif (pat2_matchs and not pat1_matchs) or (len(pat2_matchs) > len(pat1_matchs)):
        text = clean_template_question(pat2_matchs, text)
        
    elif pat1_matchs:
        text = clean_form_type(pat1_matchs, text)
    else:
        pass
        

    ### Dealing with Pattern 4     
    if pat4_matchs:

        if re.findall("(Name:.*?Phone:.*?)Location:", text):
            text = text.replace(re.findall("(Name:.*?Phone:.*?)Location:", text)[0], '')

        text = text.replace("Location:", "The location is ")
        text = text.replace("Issue:", "The issue is ")
        text = text.replace("Road:", "The road is ")

    ### Dealing with Pattern 5 (Email)     
    if pat5_matchs:
        staff_, customer_ = process_email_channel(text)
        return staff_, customer_

    if pat6_matchs:

        text = re.sub("Transaction Date:\s*\d{1,2}-\d{1,2}-\d{1,4}\s\d{1,2}:\d{1,2}:\d{1,2}", '', text)
        text = re.sub("Process Date:\s*\d{1,2}-\d{1,2}-\d{1,4}", '', text)
        text = re.sub("Graphical ID:\s*\d{1,22}\s", '', text)
        text = re.sub("Refund ID:\s*\d{1,10}\s", '', text)
        text = re.sub("Card ID:\s*\d{1,19}\s", '', text)
        text = re.sub("((?:^|\s|-)\d{1,21}\s*)(?:OTHER|FORGOT|WRONG_FARE|;|From)", '', text)
        tmp = re.findall("FRM\[.*?\]TO\[.*?\]", text)
        if tmp:
            frm_ = re.findall("FRM\[(.*?)\]TO\[(.*?)\]", tmp[0])[0][0]
            to_ = re.findall("FRM\[(.*?)\]TO\[(.*?)\]", tmp[0])[0][1]
            text = text.replace(tmp[0], f" From {frm_} to {to_}")
        
        reason_template_words = re.findall("OTHER|FORGOT|WRONG_FARE|LOST_STOLEN_CARD", text)
        if reason_template_words:
            for word_ in list(set(reason_template_words)):
                text = text.replace(word_, f"Because {word_} reason")
                
        text = text.replace("[", ' ')
        text = text.replace("]", ' ')
        text = text.replace(";", ',')
        text = text.strip(',')     
        
    if pat7_matchs:
        for sent_ in pat7_matchs:
            text = text.replace(sent_, '')
            
    
    text = text.replace(" . ", '. ')
    text = text.replace("..", '.')
    
    for sent_ in template_sentences_to_be_removed:
        text = text.replace(sent_, '')
        

    staff_content = re.findall('|'.join(AT_template_sentences), text)
    if staff_content:
        for sent_ in staff_content:
            text = text.replace(sent_, '')
            
            
    customer_content = [text]
    
    return staff_content, customer_content





############################## Web Channel Processing Function   ##############################




def clean_form_type(pat_found, text, pat1_rephrase=pat1_rephrase, personal_other_fields=personal_other_fields):
    
    to_be_removed = []
    
    
    for comb_ in list(permutations(pat_found, len(pat_found))):
        pat_ = re.findall('(.*?)'.join(comb_)+'(.*?)$', text)
        
        if pat_:
            if isinstance(pat_[0], tuple):
                pat_ = pat_[0]

            for iter_ in range(len(pat_)):

                if regex_escape_reverse(comb_[iter_]) in personal_other_fields:
                    if regex_escape_reverse(comb_[iter_]) == pat_found[-1]:
                        to_be_removed.append(comb_[iter_])
                    else:
                        to_be_removed.append(comb_[iter_]+regex_escape(pat_[iter_]))
                    
                else:
                    try:

                        if re.findall('\w+', pat_[iter_]):
                            if re.findall('\w+', comb_[iter_])[0] in ["Has", "Is", "Are", "Have"]:
                                first_word_of_ans = re.findall('\w+', pat_[iter_])[0]
                                if first_word_of_ans.lower() != "no":
                                    if first_word_of_ans.lower() == "yes":
                                        replace_untill = re.findall(f"((?:^|\s){first_word_of_ans}|.+?{first_word_of_ans})", pat_[iter_])[0]
                                        text = re.sub(comb_[iter_]+regex_escape(replace_untill), pat1_rephrase[regex_escape_reverse(comb_[iter_])], text)
                                    else:
                                        text = re.sub(comb_[iter_], pat1_rephrase[regex_escape_reverse(comb_[iter_])], text)
                                else: #add yes or no question along with answer to remove list

                                    replace_untill = re.findall(f"((?:^|\s){first_word_of_ans}|.+?{first_word_of_ans})", pat_[iter_])[0]
                                    to_be_removed.append(comb_[iter_]+regex_escape(replace_untill))
                            else:
                                text = re.sub(comb_[iter_], pat1_rephrase[regex_escape_reverse(comb_[iter_])], text)
                        else:
                            to_be_removed.append(comb_[iter_]+regex_escape(pat_[iter_]))
                    
                    except:
                        print("Failed at clean_form_type function-", text)

    if to_be_removed:                    
        for sent_ in to_be_removed:
            try:
                text = re.sub(sent_, '', text)
            except:
                text = text.replace(regex_escape_reverse(sent_), '')
            
    return text


def process_web_channel(text):
        

    ### Cleaning Pattern 1
    pat1 = ["Graphical ID:", "Transaction Date:", "Process Date:", "Refund ID:", 
            "FRM\[", "TO\[", "OTHER", "FORGOT", "WRONG_FARE"]

    pat1_matchs = re.findall('|'.join(pat1), text)
    if len(pat1_matchs) > 2:
        text = re.sub("Transaction Date:\s*\d{1,2}-\d{1,2}-\d{1,4}\s\d{1,2}:\d{1,2}:\d{1,2}", '', text)
        text = re.sub("Process Date:\s*\d{1,2}-\d{1,2}-\d{1,4}", '', text)
        text = re.sub("Graphical ID:\s*\d{1,22}\s", '', text)
        text = re.sub("Refund ID:\s*\d{1,10}\s", '', text)
        text = re.sub("Card ID:\s*\d{1,19}\s", '', text)
        text = re.sub("((?:^|\s|-)\d{1,21}\s*)(?:OTHER|FORGOT|WRONG_FARE|;|From)", '', text)
        tmp = re.findall("FRM\[.*?\]TO\[.*?\]", text)
        if tmp:
            frm_ = re.findall("FRM\[(.*?)\]TO\[(.*?)\]", tmp[0])[0][0]
            to_ = re.findall("FRM\[(.*?)\]TO\[(.*?)\]", tmp[0])[0][1]
            text = text.replace(tmp[0], f" From {frm_} to {to_}")
        
        reason_template_words = re.findall("OTHER|FORGOT|WRONG_FARE|LOST_STOLEN_CARD", text)
        if reason_template_words:
            for word_ in list(set(reason_template_words)):
                text = text.replace(word_, f"Because {word_} reason")
                
        text = text.replace("[", ' ')
        text = text.replace("]", ' ')
        text = text.replace(";", ',')
        text = text.strip(',')
        


    ### Cleaning Pattern 3
    pat3_matchs = []
    for sent_ in list(pat1_rephrase.keys())+personal_other_fields:
        if sent_ in text:
            pat3_matchs.append(regex_escape(sent_))

    if pat3_matchs:
        text = clean_form_type(pat3_matchs, text)

    
    text = text.strip('.')    
    staff_content = re.findall('|'.join(AT_template_sentences), text)
    if staff_content:
        for sent_ in staff_content:
            text = text.replace(sent_, '')
            
    customer_content = [text]
    

    return staff_content, customer_content




############################## WalkIn Channel Processing Function   ##############################


def process_walkin_channel(text):
        
    not_needed_fields = [
        "AT HOP card number?:",
        "AT HOP card number? :",
        "AT HOP card number:",
        "Cancelled card:",
        "Active card:",
        "Card:",
        "Account Name:",
        "Trip ID:",
        "Time of top up / transaction:",
        "Mailing preference:",
        "Date and time printed:",
        "Date and Time:",
        "Trip Start Time:",
        "Time :",
        "Date :",
        "Customer's name:"
    ]

    phrase_fields = {
        "Location :": ". At ",
        "Operator :": ". operator ",
        "Note:": '. ',
        "Concession:": ". Concession type ",
        "Reason for dispute:": ". Dispute is ",
        "Amount:": ". Amount charged ",
        "Description:": '. ',
        "Trip Incident:": '. ',
        "Trip Information:": '. Trip information ',
        "Description of incident:": ". Incident description ",
        "Date of incident:": "Incident date ",
        "Time of incident:": "Incident time ",
        "Location of incident:": ". Incident location ",
        "Depot:": ". depot ",
        "Travel Direction:": ". Travel direction is"

    }
    
    walkin_matchs = []
    for sent_ in list(phrase_fields.keys())+not_needed_fields:
        if sent_ in text:
            walkin_matchs.append(regex_escape(sent_))
            

    if walkin_matchs:
        text = clean_form_type(walkin_matchs, text, pat1_rephrase=phrase_fields, personal_other_fields=not_needed_fields)
        
    
    return text



############################## Other Channels (Twitter, Webchat, Facebook) Processing Function   ##############################

