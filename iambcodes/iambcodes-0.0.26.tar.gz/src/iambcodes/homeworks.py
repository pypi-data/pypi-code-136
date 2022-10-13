import ipywidgets as widgets
import random as rd
import numpy as np

class homework_three():
    def __init__(self, stdID):
        # Check if Student-ID is an integer and if the function is to be run in "test-mode"
        
        #'TEst-Mode' is activated by the Std-ID input: 123456789
        # For this to be viable, 123456789 CANNEVER be a viable student-id
        if type(stdID) == int and stdID == 123456789:
            self.stdID = "testing"
        elif type(stdID) == int and stdID != 123456789:
            self.stdID = stdID
        else:
            print("Student ID required to be an integer.\nPlease try again!\n\n")
            pass
        
        # How many rngs are to be created for new/changed parameters
        self.numberofrandomnumbers = 6
        
        # Create RNs on the basis of the studentID
        self.initiate_homework()
        
        # Create variables using the generated RNs
        self.create_question_variables()
        
        # List of self.parameters:
        #self.stID
        #self.listofrndms
        
        #self.newYxs
        #self.newH
        #self.newO
        #self.newN
        
        #self.newRO2
        #self.newRCO2
        
        self.hq1tgl = 0 #help_question_1_toggle
        self.hq2tgl = 0 #help_question_2_toggle
        
        # build widgets for the questions
        self.question_one_display = self.build_question_one()
        self.question_two_display = self.build_question_two()
        
        
    def initiate_homework(self):
    # Parameters:
    # stdID is an integer used to seed the rng
        # IF stdID is given the string "test", it's supposed to return the string "test"
        # This string is then used to thest functions using standard values
    # counter is an integer used to define how many rngs are created.
        #print("Matriculation-Number accepted.\n\nGenerating random numbers..")
        #print("Matriculation-Number accepted.\n\nGenerating personalized homework parameters..")
        if self.stdID == "testing":
            print("#####\n\nTesting functionality\n\n#####")
            print("#####\n\The Std-ID is not a valid Student-ID\n and CAN'T generate a valid code!\n\n#####")
            # NOTE: no self.listofrndms is created in test mode
        else:
        #RNG for this homework
            rd.seed(self.stdID)
            self.listofrndms = [rd.random() for i in range(self.numberofrandomnumbers)] #create new random numbers that can be used to modify parameters
        return
    
    def create_question_variables(self):
        #function returns all generated homework parameters and a boolean 
        #thats used to toggls help_question_1_toggle to  0 (helpoption was not used)
        if self.stdID != "testing":
            #print("\nGenerating personalized homework parameters...\n")
            ###PARAMATERS for QUESTION 1
            self.newYxs = 1+round(self.listofrndms[0],1) #range 1.0-2.0
            self.newH = 1.5+round((self.listofrndms[1]*0.5),1) #range 1.5-2.0
            self.newO = 0.3+round((self.listofrndms[2]*0.4),1) #range 0.3-0.7
            self.newN = 0.1+round((self.listofrndms[3]*0.2),1) #range 0.1-0.3

            ###PARAMATERS for QUESTION 2
            self.newRO2 = 3000+round((self.listofrndms[4]*500)) #range 3000-3500)
            self.newRCO2 = 8000+round((self.listofrndms[5]*500)) #range 8000-8500)
        
        elif self.stdID == "testing":
            ###PARAMATERS for QUESTION 1
            self.newYxs = 2
            self.newH = 1.8
            self.newO = 0.5
            self.newN = 0.2
            
            ###PARAMATERS for QUESTION 2
            self.newRO2 = 3300
            self.newRCO2 = 8300
        return
    
    
###############
###############
###############
    def correct_homework_three_question_one(self, RQ):
        #Parameters:
        #RQ: Student solution. Will be comparied with opimal solution and decides if task was done correctly or not
        
        #newYxs, newH, newO, newN: changed parameters based on the seed.
            #are needed to calculate the opimal solution
        #hq1tgl: boolean. Decides if the student used the help-option or not

        #output formula:
        # X-YZ
        # X: was the help used? yes or no
        #    -> randomint
        # YZ: Summ(studentID[0]+studentID[1]) <10 OR >= 10:
        #    -> 2x randomint
        if self.stdID == "testing":
            with self.question_one_display.children[0]:
                print('\nTesting solution calculation...\n')
                print("#####\n\nThe Std-ID is not a valid Student-ID\n and CAN'T generate a valid code!\n\n#####")

                Yxc = self.newYxs - 1
                print("\nYxc:",Yxc)
                Yxn = self.newN
                Yxw = (self.newYxs*2 + Yxn*3 - self.newH)/2
                print("\nYxw:",Yxw)
                Yxo = (-self.newYxs + Yxw + 2*Yxc + self.newO)/2
                print("\nYxo:",Yxo)

                realRQ = Yxc/Yxo
                print("\nrealRQ:",realRQ)        
        
        
        if type(self.stdID) == int:
            stdIDstr = str(self.stdID)


            #Calculation of the solution:
            with self.question_one_display.children[-1]:

                Yxc = self.newYxs - 1
                #print(Yxc)
                Yxn = self.newN
                Yxw = (self.newYxs*2 + Yxn*3 - self.newH)/2
                #print(Yxw)
                Yxo = (-self.newYxs + Yxw + 2*Yxc + self.newO)/2
                #print(Yxo)

                realRQ = Yxc/Yxo
                #print(realRQ)

                #Check if student solution is correct
                #Assumes aswer was rounded to 2 decimals
                if round(realRQ,2) == RQ:
                    self.question_one_display.children[-3].children[0].disabled = True
                    self.question_one_display.children[-3].children[1].disabled = True
                    print("Solution corect! RQ is {}".format(realRQ))

                    solcode = ""
                     #Help-option was not used
                    if self.hq1tgl == 0:
                        solcode+=(str(rd.randrange(0,4)))
                    #Help-option was used
                    elif self.hq1tgl == 1:
                        solcode+=(str(rd.randrange(5,9)))

                    if int(stdIDstr[-1])+int(stdIDstr[-2]) < 10:
                        solcode+=(str(rd.randrange(0,4)))
                        solcode+=(str(rd.randrange(0,4)))
                    elif int(stdIDstr[-1])+int(stdIDstr[-2]) >= 10:
                        solcode+=(str(rd.randrange(5,9)))
                        solcode+=(str(rd.randrange(5,9)))    
                    # PRINT THE CODE
                    print("Here's your code!\n\n"+solcode+"\n\nPlease upload it in the designated Moodle-Task.") 

                #If the solution was not correct, the students can try again
                else:
                    print("Solution WRONG!\nDon't give up and try again!")

###############
###############
###############
    def correct_homework_three_question_two(self,Yield_Ethanol, Yield_Substrate):
        #Parameters:
        #Yield_Ethanol, Yield_Substrate: Student solution. Will be comparied with opimal solution and decides if task was done correctly or not
        #ewYxs, newH, newO, newN, newRO2, newRCO2: changed parameters based on the seed.
            #are needed to calculate the opimal solution
        #hq2tgl: boolean. Decides if the student used the help-option or not

        #output formula:
        # X-YZ
        # X: was the help used? yes or no
        #    -> randomint
        # YZ: Summ(studentID[0]+studentID[1]) <10 OR >= 10:
        #    -> 2x randomint

        if self.stdID == "testing":
            with self.question_two_display.children[0]:
                print('\nTesting solution calculation...\n')
                print("#####\n\nThe Std-ID is not a valid Student-ID\n and CAN'T generate a valid code!\n\n#####")


                #1. Converting biomass concentration from g/l to c-mol
                Xn = (round(46.5/(1*12+self.newH*1+self.newO*16+self.newN*14),2)*10000) 
                print("\nXn:",Xn)
                #Xn = ((50 g/L - 7 % ash)/(masses of C_1+H_newH+O_newO+N_newN) g/mol) * 10000 L = x cmol
                # 12, 1, 16, and 14 are the assumed molecular masses of the specific elements

                #2. Normalizing gas exchange rates
                rO2 = round(self.newRO2/Xn,2)
                rCO2 = round(self.newRCO2/Xn,2)
                print("\nrO2:",rO2)
                print("\nrCO2:",rCO2)

                #3. Calculating Yields, YXO, YXC
                mu = 0.35 #Growthrate = 0.35 1/h
                Yxo = rO2/mu
                Yxc = rCO2/mu
                Yxn = self.newN
                print("\nYxo:",Yxo)
                print("\nYxc:",Yxc)
                Ymatrixvar = np.array([[2,1],[1,-0.5]])
                Ymatrixsolvd = np.array([-1*(self.newH-2-2*Yxc-3*Yxn), -1*(self.newO+1*Yxc-1-2*Yxo)])
                Ymatrix = np.linalg.solve(Ymatrixvar,Ymatrixsolvd)
                Yxw,Yxe = Ymatrix
                Yxs = Yxe+1+Yxc
                print("\nYxe:",Yxe)
                print("\nYxs:",Yxs)

        if type(self.stdID) == int:
            stdIDstr = str(self.stdID)
            
            #Calculation of the solution:
            with self.question_two_display.children[-1]:

                #1. Converting biomass concentration from g/l to c-mol
                Xn = (round(46.5/(1*12+self.newH*1+self.newO*16+self.newN*14),2)*10000) 
                #Xn = ((50 g/L - 7 % ash)/(masses of C_1+H_newH+O_newO+N_newN) g/mol) * 10000 L = x cmol
                # 12, 1, 16, and 14 are the assumed molecular masses of the specific elements

                #2. Normalizing gas exchange rates
                rO2 = round(self.newRO2/Xn,2)
                rCO2 = round(self.newRCO2/Xn,2)

                #3. Calculating Yields, YXO, YXC
                mu = 0.35 #Growthrate = 0.35 1/h
                Yxo = rO2/mu
                Yxc = rCO2/mu
                Yxn = self.newN

                Ymatrixvar = np.array([[2,1],[1,-0.5]])
                Ymatrixsolvd = np.array([-1*(self.newH-2-2*Yxc-3*Yxn), -1*(self.newO+1*Yxc-1-2*Yxo)])
                Ymatrix = np.linalg.solve(Ymatrixvar,Ymatrixsolvd)
                Yxw,Yxe = Ymatrix
                Yxs = Yxe+1+Yxc

                #Check if student solution is correct
                #Assumes aswer was rounded to 2 decimals
                if round(Yxs,2) == Yield_Substrate and round(Yxe,2) == Yield_Ethanol:
                    self.question_two_display.children[-3].children[0].disabled = True
                    self.question_two_display.children[-3].children[1].disabled = True
                    print("Solution corect! Substrate yield is {}\nand Ethanol yield is {}".format(Yxs,Yxe))

                    solcode = ""
                    #Help-option was not used
                    if self.hq2tgl == 0:
                        solcode+=(str(rd.randrange(0,4)))
                    #Help-option was used
                    elif self.hq2tgl == 1:
                        solcode+=(str(rd.randrange(5,9)))

                    if int(stdIDstr[-1])+int(stdIDstr[-2]) < 10:
                        solcode+=(str(rd.randrange(0,4)))
                        solcode+=(str(rd.randrange(0,4)))
                    elif int(stdIDstr[-1])+int(stdIDstr[-2]) >= 10:
                        solcode+=(str(rd.randrange(5,9)))
                        solcode+=(str(rd.randrange(5,9)))    
                    # PRINT THE CODE
                    print("Here's your code!\n\n"+solcode+"\n\nPlease upload it in the designated Moodle-Task.") 

                #If the solution was not correct, the students can try again
                elif round(Yxs,2) == Yield_Substrate and round(Yxe,2) != Yield_Ethanol:
                    print("Ethanol yield WRONG!\nPlease try again!")
                elif round(Yxs,2) != Yield_Substrate and round(Yxe,2) == Yield_Ethanol:
                    print("Substrate yield WRONG!\nPlease try again!")
                else:
                    #print("Real Yxe={}\nStudent_Ethanol_Yield={}".format(Yxe,Yield_Ethanol))
                    #print("Real Yxs={}\nStudent_Substrate_Yield={}".format(Yxs,Yield_Substrate))
                    print("Solution WRONG!\nDon't give up and try again!")

    ######
    # functions that create widgets
    #
    #
    #
    ###
    
    def build_question_one(self):
        listofwidgets = []
        
        # build question label/output (top 0)
        # build answer input (top 1)
        # build 'Check Answer button' (top 2.hbox-0)
        # build 'Get help button' (top 2. hbox-1)
        # build output (for commentsof help button) (top 3)
        # build output (for answer button feedback) (top 4)
        
        listofwidgets.append(widgets.Output(
        ))
        with listofwidgets[0]:
            #print("##########\n\nParameters for Question 1:\n\n"\
            #"Your glucose yield Y_(XS) is {} C-mol glucose/C-mol biomass\n\n"\
            #"Your biomass composition is CH_({})O_({})N_({})\n\n##########".format(self.newYxs,self.newH,self.newO,self.newN))
            print("")
            
        listofwidgets.append(widgets.FloatText(
            value=0.00,
            description='RQ:',
            disabled=False,
            display='flex',
            flex_flow='column',
            align_items='stretch',
            style= {'description_width': 'initial'},
            layout = widgets.Layout(width='200px', height='40px')
        ))


        
        i = []
        i.append(widgets.Button(
            value=False,
            description='Check RQ',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click to check solution',
            #     icon='check' # (FontAwesome names without the `fa-` prefix)
        ))
                             
        i.append(widgets.Button(
            value=False,
            description='Calculation Help',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click to get a tipp',
        #     icon='check' # (FontAwesome names without the `fa-` prefix)
        ))
                 
        listofwidgets.append(widgets.HBox(i))
        
        listofwidgets.append(widgets.Output())
        listofwidgets.append(widgets.Output())
        
        disp = widgets.VBox(listofwidgets)
        return disp
###############
###############
###############
    def build_question_two(self):
            listofwidgets = []

            # build question label/output (top 0)
            # build answer input for Ethanol Yield (top 1)
            # build answer input for Substrate Yield (top 2)
            # build 'Check Answer button' (top 3.hbox-0)
            # build 'Get help button' (top 3. hbox-1)
            # build output (for commentsof help button) (top 4)
            # build output (for answer button feedback) (top 5)

            listofwidgets.append(widgets.Output(
            ))
            with listofwidgets[0]:
                #print("##########\n\nParameters for Question 2:\n\n"\
                #"Your O_2 Exchange-Rate is {} mol/h\n\n"\
                #"Your CO_2 Exchange-Rate is {} mol/h\n\n##########".format(self.newRO2,self.newRCO2))
                print("")
                
            listofwidgets.append(widgets.FloatText(
                value=0.00,
                description='Ethanol Yield:',
                disabled=False,
                display='flex',
                flex_flow='column',
                align_items='stretch',
                style= {'description_width': 'initial'},
                layout = widgets.Layout(width='200px', height='40px')
            ))
            
            listofwidgets.append(widgets.FloatText(
                value=0.00,
                description='Substrate Yield:',
                disabled=False,
                display='flex',
                flex_flow='column',
                align_items='stretch',
                style= {'description_width': 'initial'},
                layout = widgets.Layout(width='200px', height='40px')
            ))


            i = []
            i.append(widgets.Button(
                value=False,
                description='Check Yields',
                disabled=False,
                button_style='', # 'success', 'info', 'warning', 'danger' or ''
                tooltip='Click to check solution',
                #     icon='check' # (FontAwesome names without the `fa-` prefix)
            ))

            i.append(widgets.Button(
                value=False,
                description='Calculation Help',
                disabled=False,
                button_style='', # 'success', 'info', 'warning', 'danger' or ''
                tooltip='Click to get a tipp',
            #     icon='check' # (FontAwesome names without the `fa-` prefix)
            ))

            listofwidgets.append(widgets.HBox(i))

            listofwidgets.append(widgets.Output())
            listofwidgets.append(widgets.Output())

            disp = widgets.VBox(listofwidgets)
            return disp
    
    ######
    # ON-CLICK functions
    # 2 per question
    #
    #
    ###
    def on_question_one_help_button_clicked(self, click):
        self.hq1tgl = 1
        self.question_one_display.children[-3].children[1].disabled = True
        with self.question_one_display.children[-2]:
            txt = "##########\n" \
            "The RQ is rate of CO_2 production divivided by the rate of O_2 production\n" \
            "RQ = r(CO_2)/r(O_2)\n" \
            "Yields correlate directly to rates\n" \
            "RQ = r(CO_2)/r(O_2) = Y(CO_2)/Y(O_2)\n\n" \
            "By calculating all yields for the known reaction, you will be able to identify the required yields\n" \
            "##########"
            print(txt)
    def on_question_one_answer_button_clicked(self, click):
        student_answer = self.question_one_display.children[1].value
        self.correct_homework_three_question_one(student_answer)
        
    def on_question_two_help_button_clicked(self, click):
        self.hq2tgl = 1
        self.question_two_display.children[-3].children[1].disabled = True
        with self.question_two_display.children[-2]:
            txt = "##########\n" \
            "Don't forget, that for Question 2, Ethanol is an additional product!\nYou also need to subtract the ash from the assumed Biomass.\n\n"\
            "First, convert the biomass concentration from g/L to c-mol\n" \
            "and normalize the gas exchange rates for  O_2 and CO_2\n" \
            "You already have the growth rate. You can use it to and the exchange rates to determine the\nyields of O_2 and CO_2\n" \
            "With that, the rest of the stoichiometric matrix for the equation is solvable\n"
            "##########\n"
            print(txt)
    def on_question_two_answer_button_clicked(self, click):
        student_answer_ethanol_yield = self.question_two_display.children[1].value
        student_answer_substrate_yield = self.question_two_display.children[2].value
        self.correct_homework_three_question_two(student_answer_ethanol_yield, student_answer_substrate_yield)
