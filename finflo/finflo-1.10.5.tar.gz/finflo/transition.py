import json
from .models import (
    SignList,
    TransitionManager,
    Action,
    workevents,
    workflowitems,
    Flowmodel
)
from django.core import serializers as core_serializers
from .middleware import get_current_user
from .exception import (
    ModelNotFound,
    TransitionNotAllowed,
    ReturnModelNotFound,
)
from django.db.models import Q
from django.conf import settings
from collections import deque
from django.apps import apps
from django.forms.models import model_to_dict




####################################################
#############       CORE     #######################
####################################################


class FinFlotransition():

    # BASE CONSTRUCTORS # 
    
    def __init__(self, type, t_id , action = None ,source = None,interim = None, target = None, from_party = None, to_party = None):
        # typing support needed 
        self.type = type 
        self.t_id = t_id 
        self.action = action if action else None
        self.source = source if source else None
        self.interim = interim if interim else None
        self.target = target if target else None
        self.from_party = from_party if from_party else None
        self.to_party = to_party if to_party else None
        #  conditions
        gets_current_Action = None
        if action:
            gets_action = self.gets_base_action()
            base_model = self.gets_base_model()
            gets_return = self.gets_default_return_action()
            if gets_action.intermediator == True :
                self.intermediator_transition_handler(type = self.type, action = self.action , t_id = self.t_id)
            elif gets_return.description == action.upper():
                self.return_transition()
            else :
                self.transition()
        else:
            self.manualtransitions()
        # return None

    def __repr__(self):
        return "the id is %s and type is %s" % (self.t_id, self.type)

    
    def __str__(self):
        return "the id is %s and type is %s" % (self.t_id, self.type)


    # GETS THE ALL MODEL VALUE FOR TRANSITION #

    def gets_base_action(self):
        try:
            gets_action_data = Action.objects.get(description=self.action, model__description = self.type )
            return gets_action_data
        except:
            raise ModelNotFound()
    
    def gets_all_models(self):
        try:
            gets_model = TransitionManager.objects.get(type__icontains = self.type , t_id = self.t_id)
            gets_flows = Flowmodel.objects.get(description__icontains  = self.type)
            gets_action = Action.objects.get(Q(model = gets_flows.id ) | Q(model = None), description=self.action)
            gets_wf  = FinFlotransition.gets_wf_item(gets_model)
            sign_lists = sub_action_list = []
            try:
                for item in SignList.objects.all():
                    sign_lists.append(item.name)
                    if item.name == gets_action.stage_required.name :
                        break
                next_avail_trans = sign_lists[gets_model.sub_sign : ]
                next_avail_trans_value = deque(next_avail_trans)
                next_avail_trans_value.popleft()
                next_states = list(next_avail_trans_value)
                next_avail_Transition = {'values' : next_states}
            except:
                next_avail_Transition = None
                pass
            return gets_model , gets_action , gets_flows , gets_wf , sign_lists , next_avail_Transition
        except:
            raise ModelNotFound()

    # GETS TRANSITION MANAGER

    def gets_base_model(self):
        try:
            gets_model = TransitionManager.objects.get(type = self.type , t_id = self.t_id)
            return gets_model 
        except:
            ModelNotFound()


    # def get_action(self):
    #     self._action = None

    def get_record_datas(self):
        overall_model = FinFlotransition.gets_base_model(self)
        try:
            work_model = settings.FINFLO['WORK_MODEL']  
            for iter in work_model:
                gets_model =  apps.get_model(iter)
                query_data = gets_model.objects.filter(id = overall_model.workflowitems.transitionmanager.t_id)
                base_serialized_Data = core_serializers.serialize('json', query_data)
                if query_data.exists():
                    break
                continue
            return {"values" : json.loads(base_serialized_Data)}
        except:
            return {"values" : None}
           

    # action = property(get_action, set_action)

    

    # MANUAL TRANSITION WITH SOURCE , INTERIM , AND TARGET STATES

    def manualtransitions(self):
        try:
            queryset = TransitionManager.objects.get(t_id = self.t_id , type = self.type)
            wf = workflowitems.objects.update_or_create( transitionmanager= queryset , defaults= {"initial_state" : self.source, "interim_state" : self.interim ,
                    "final_state" : self.target, "model_type" : self.type, "event_user" : get_current_user() , "current_from_party " : self.from_party, "current_to_party " : self.to_party})
            wf.save()
            workevents.objects.create(workflowitems = wf , event_user=get_current_user(),  initial_state=self.source  , 
                    interim_state = self.interim , final_state=self.target ,type=self.type , record_datas = self.get_record_datas() , from_party = self.from_party , to_party = self.to_party)
        except:
            return None  
       



    # GETS THE DEFAULT RETURN ACTION #

    def gets_default_return_action(self):
        try:
            qs = Action.objects.get(id = 1)
            return qs
        except:
            raise ReturnModelNotFound()


    # VALUE FOR SIGN_LIST #

    def get_value(sign_list, i):
        try:
            return sign_list[i]
        except IndexError:
            return 0



    # GETS WORKFLOW MODEL ID #

    def gets_wf_item(gets_model):
        ws = workflowitems.objects.get(transitionmanager=gets_model.id)
        return ws
        
    
    

    # SPECIAL FUNCTION FOR RETURN TRANSITION  #

    def return_transition(self):
        
        overall_model = FinFlotransition.gets_all_models(self)
       
        if self.action == self.gets_default_return_action().description.upper():
            wf = workflowitems.objects.update_or_create( transitionmanager=overall_model[0] or overall_model[0].id, defaults= {"initial_state" : overall_model[3].initial_state, "interim_state" : overall_model[1].to_state.description ,
                    "final_state" : overall_model[1].to_state.description, "action" : self.action, "subaction" : self.action , "next_available_transitions" : None, "model_type" : self.type, "event_user" : get_current_user() , "current_from_party" : overall_model[1].from_party , "current_to_party" : overall_model[1].to_party})
            workevents.objects.create(workflowitems=overall_model[3] , event_user=get_current_user(),  initial_state=overall_model[3].initial_state,final_value = True , record_datas = self.get_record_datas() , 
                interim_state = overall_model[1].to_state.description , final_state=overall_model[1].to_state.description, action= self.action, subaction = self.action ,type=self.type, from_party = overall_model[1].from_party , to_party = overall_model[1].to_party)
            overall_model[0].sub_sign = 0
            overall_model[0].save()                      



    # INTERIM ACTION FOR THE TRANSITION HANDLING #

    def intermediator_transition_handler(self, type, action, t_id):
        overall_model = FinFlotransition.gets_all_models(type = type, action = action , t_id = t_id)
        
        # len action and sub_sign
        
        if overall_model.gets_model.sub_sign <= overall_model.gets_action.sign_required:
            def Transition_Handler():
                    gets_sign = overall_model.gets_action.sign_required
                    
                    
                    # if len(overall_model.sign_lists)-1 != overall_model.gets_model.sub_sign:
                    #     ws = workflowitems.objects.update_or_create( transitionmanager=overall_model.gets_model or overall_model.gets_model.id, defaults= {"initial_state" : gets_action.from_state.description, "interim_state" :  sign_lists[1 + gets_model.sub_sign], 
                    #         "final_state" : overall_model.gets_action.to_state.description, "action" : action, "subaction" : overall_model.sign_lists[1 + gets_model.sub_sign], "model_type" : type.upper(), "event_user" : get_current_user() , "current_from_party" : gets_action.from_party , "current_to_party" : gets_action.to_party})
                    #     we = workevents.objects.create(workflowitems=overall_model.gets_wf, event_user=get_current_user(),  initial_state=overall_model.gets_action.from_state.description,
                    #                               interim_state = overall_model.sign_lists[1 + overall_model.gets_model.sub_sign], final_state=overall_model.gets_action.to_state.description, action=action, subaction=sub_action[0], type=type.upper(), from_party = gets_action.from_party , to_party = gets_action.to_party)
                    #     overall_model.gets_model.sub_sign += 1
                    #     overall_model.gets_model.save()

                    # elif len(overall_model.sign_lists)-1 == int(overall_model.gets_model.sub_sign):
                    #     ws = workflowitems.objects.update_or_create( transitionmanager=overall_model.gets_model or gets_model.id, defaults= {"initial_state" : gets_action.from_state.description, "interim_state" : gets_action.to_state.description ,
                    #         "final_state" : overall_model.gets_action.to_state.description, "action" : action, "subaction" : sign_lists[1 + gets_model.sub_sign], "model_type" : type.upper(), "event_user" : get_current_user() , "current_from_party" : gets_action.from_party , "current_to_party" : gets_action.to_party})
                    #     workevents.objects.create(workflowitems=gets_wf, event_user=get_current_user(),  initial_state=gets_action.from_state.description,final_value = True , 
                    #                               interim_state = gets_action.to_state.description, final_state=gets_action.to_state.description, action=action, subaction=sub_action[0], type=type.upper(), from_party = gets_action.from_party , to_party = gets_action.to_party)
                    #     overall_model.gets_model.sub_sign += 1
                    #     overall_model.gets_model.save()
            return Transition_Handler()   
            
        else:
            raise TransitionNotAllowed()
        


    ## CORE TRANSITION ###

    def transition(self):
       
        overall_model = FinFlotransition.gets_all_models(self)
        
        # if ((gets_model.sub_sign <= gets_action.sign_required) and (gets_model.sub_sign != gets_action.sign_required)):
        if overall_model[0] is not None :
            def Transition_Handler():
        
                    # NO SIGN -> ONLY_MAKER TRANSITION 
                    
                    # if len(overall_model[4])  == 0:
                    #     # print("SET 1 ")
                    #     workflowitems.objects.update_or_create( transitionmanager=overall_model[0] or overall_model[0].id, defaults= {"initial_state" : overall_model[1].from_state.description, "interim_state" :  overall_model[1].from_state.description, 
                    #         "final_state" : overall_model[1].to_state.description, "action" : self.action, "subaction" : None, "model_type" : self.type, "event_user" : get_current_user() , "current_from_party" : overall_model[1].from_party , "current_to_party" : overall_model[1].to_party})
                    #     workevents.objects.create(workflowitems=overall_model[3], event_user=get_current_user(),  initial_state=overall_model[1].from_state.description,
                    #                               interim_state = overall_model[1].from_state.description, final_state=overall_model[1].to_state.description, action= self.action, subaction= None , type= self.type, from_party = overall_model[1].from_party , to_party = overall_model[1].to_party)
                    #     overall_model[0].sub_sign = 0
                    #     overall_model[0].save()

                    # # MAKER TRANSITION 

                    # elif overall_model[0].sub_sign == 0:
                    #     # print("SET 2 ")
                    #     ws = workflowitems.objects.update_or_create( transitionmanager=overall_model[0] or overall_model[0].id, defaults= {"initial_state" : overall_model[1].from_state.description, "interim_state" :  overall_model[4][1 + overall_model[0].sub_sign], 
                    #         "final_state" : overall_model[1].to_state.description, "next_available_transitions" : overall_model[5],"action" : self.action, "subaction" : overall_model[4][overall_model[0].sub_sign], "model_type" : self.type, "event_user" : get_current_user() , "current_from_party" : overall_model[1].from_party , "current_to_party" : overall_model[1].from_party})
                    #     workevents.objects.create(workflowitems=overall_model[3], event_user=get_current_user(),  initial_state=overall_model[1].from_state.description,
                    #                               interim_state = overall_model[4][1 + overall_model[0].sub_sign], record_datas = self.get_record_datas() , final_state=overall_model[1].to_state.description, action= self.action, subaction= self.action, type= self.type, from_party = overall_model[1].from_party , to_party = overall_model[1].from_party)
                    #     overall_model[0].sub_sign +=1
                    #     overall_model[0].save()

                    #  TRANSITION 

                    if len(overall_model[4]) != overall_model[0].sub_sign:
                        # print("SET 3 ")
                        # print(overall_model[0].sub_sign)
                        try:
                            ws = workflowitems.objects.update_or_create( transitionmanager=overall_model[0] or overall_model[0].id, defaults= {"initial_state" : overall_model[1].from_state.description, "interim_state" :  overall_model[4][1 + overall_model[0].sub_sign], 
                                "final_state" : overall_model[1].to_state.description, "next_available_transitions" : overall_model[5],"action" : self.action, "subaction" : overall_model[4][overall_model[0].sub_sign], "model_type" : self.type, "event_user" : get_current_user() , "current_from_party" : overall_model[1].from_party , "current_to_party" : overall_model[1].from_party})
                            workevents.objects.create(workflowitems=overall_model[3], event_user=get_current_user(),  initial_state=overall_model[1].from_state.description,
                                                    interim_state = overall_model[4][1 + overall_model[0].sub_sign], record_datas = self.get_record_datas() ,final_state=overall_model[1].to_state.description, action= self.action, subaction= self.action, type= self.type, from_party = overall_model[1].from_party , to_party = overall_model[1].from_party)
                            overall_model[0].sub_sign += 1 
                            overall_model[0].in_progress = True
                            overall_model[0].save()
                        except:
                            ws = workflowitems.objects.update_or_create( transitionmanager=overall_model[0] or overall_model[0].id, defaults= {"initial_state" : overall_model[1].from_state.description, "interim_state" :  overall_model[1].to_state.description, 
                            "final_state" : overall_model[1].to_state.description, "action" : self.action,  "next_available_transitions" : None , "subaction" : self.action, "model_type" : self.type, "event_user" : get_current_user() , "current_from_party" : overall_model[1].from_party , "current_to_party" : overall_model[1].to_party , "final_value" : True})
                            workevents.objects.create(workflowitems=overall_model[3], event_user=get_current_user(),  initial_state=overall_model[1].from_state.description,
                                                  interim_state = overall_model[1].to_state.description,record_datas = self.get_record_datas() ,  final_state=overall_model[1].to_state.description, action= self.action, subaction= self.action, type = self.type, from_party = overall_model[1].from_party , to_party = overall_model[1].to_party , final_value = True)
                            overall_model[0].sub_sign = 0
                            overall_model[0].in_progress = False
                            overall_model[0].save()

            return Transition_Handler()   
        else:
            raise TransitionNotAllowed()
