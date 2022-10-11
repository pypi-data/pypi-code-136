import  json 
from jsonschema import validate as json_schema_validate
from jsonschema.exceptions import ValidationError


from zohavi.zwebui.web_field import WebField
from zohavi.zbase.staple import ZStaple
# from _def.common.selector import Selector
from dataobjtools.selector import Selector
import importlib

from dataclasses import dataclass, field
from typing import List, Callable

@dataclass
class DataUI_Error():
	no: str
	message: str
	validation: dict= field(default_factory=dict)
	data: dict= field(default_factory=dict)

@dataclass
class DataUI_Response():
	success: bool
	dbrec_list: list
	request_id: str = ""
	schema: dict = field(default_factory=dict)
	http_status: int = 000
	error: DataUI_Error = None # DataUI_Error(no=None,message=None, validation={},data={} )

	def to_http(self):
		ret_data = {
					'request_id': self.request_id,
					'success': self.success,
					'data': self.data,
					'schema': self.schema
		}
		if self.error.no : ret_data['error'] = self.error.__dict__
		return json.dumps( ret_data ), self.http_status

	# def to_dict(self):


@dataclass
class DataUI_Response_List():
	success: bool
	response_list: List[DataUI_Response] = field(default_factory=list)
	http_status: int = 000
	error: DataUI_Error = None #DataUI_Error(no=None,message=None, validation={},data={} )

	def to_http(self):
		ret_data = { 'success': self.success, 'data_list':[]}

		for data_item in self.response_list:
			ret_data['data_list'].append( data_item.__dict__  )
		
		if self.error : ret_data['error'] = self.error.__dict__
		
		# breakpoint()
		return json.dumps( ret_data ), self.http_status
		


class DataUIModel(ZStaple):
	#####################################################################################
	def __init__(self,   form_field_validation_schema, session, logger ):

		super().__init__(app = None, logger = logger )

		DataUIModel.validate_schema( form_field_validation_schema )

		# self.update_obj_list = update_obj
		self.data_schema = form_field_validation_schema 
		
		self.web_schema = WebField( form_field_validation_schema, logger=logger )
		# self.logger = logger
		self.session = session

		# pass
	@staticmethod
	def validate_schema( json_input_schema):
		validation_schema = {
							"type": "array",
							"items": 
							{ 	"type" : "object",
								"properties" : 
								{ "module_name":{"type":"string" },
									"table_obj":{"type":"string" },
									"fields": 
									{ "type": "object",
										"patternProperties": 
										{	".*": 
											{ 	"type": "object",
												"properties": 
												{ 	"field_db":{"type":"string" },
													"key":{"type":"boolean" },
													"validation":{
																	"type": "object",
																	"properties": {
																					"required":{"type":"boolean"},
																					"text_min_len":{"type":"integer"},
																					"text_max_len":{"type":"integer"}
								} 	}	}	}	}	}	}	}
							}
		try:
			json_schema_validate( instance= json_input_schema , schema=validation_schema   )
		except  Exception as e:
			print(e)
			return False

		return True
	
	#####################################################################################
	def validate_schema_for_bulk_update(self, data ): 
		return True

	#####################################################################################
	def get_webfield_value( self, web_data, field_html_name):
		for field in web_data:	
			if field[ 'id'] == field_html_name: return field['value']
		
		return None

	#####################################################################################
	def get_field_schema( self, obj_name, field_html_name):
		
		for table_obj_rec in self.data_schema:
			if obj_name == table_obj_rec['table_obj']:
				return table_obj_rec['fields'].get(field_html_name)


		# table_obj_rec = self.data_schema.get( obj_name )

		# if table_obj_rec:
			
		return None

	#####################################################################################
	def _data_validate( self, submit_data ): 
		validation_result = {}
		self.log_debug("validating data")
		self.log_debug( submit_data )

		validation_result = self.web_schema.validate(  submit_data )
		if validation_result['success']: self.log_debug( 'Validation checks completed - result: passed' )
		else: self.log_error('Validation checks completed - result: failed')
		self.log_debug("****:" + json.dumps(   validation_result ) )
		
		return validation_result


	#####################################################################################
	def data_get_ajax( self, search_dict ):  
		
		data_obj_list = self.data_get( search_dict )
		
		if data_obj_list: return DataUI_Response(success=True, data_list=data_obj_list, schema=self.data_schema, http_status=200).to_http()
		
		return DataUI_Response(success=False, error=DataUI_Error(no='101', message='data not found'), http_status=500) 

	#####################################################################################
	def data_get( self, search_dict, ret_db_obj=False):
		data_obj_list = []
		## Example of talbe fields in self.data_schema
		# 	"SiteMain":{ 	
		# 		# "table":"SiteMain",
		# 		# "fields":{
		# 					"si_site_id":{"field_db":"site_id",   "key":True},
		# 					"si_site_name":{"field_db":"site_name", "validation":{"required":True, "text_min_len":3, "text_max_len":20} },
		# 					"si_site_code":{"field_db":"site_code",   "validation":{"required":True,  "text_max_len":5} },
		# 		# } }
		#Loop through each of the json table schame descriptions
		for obj_name, data_table in self.data_schema.items():
			# if obj_name in self.update_obj_list:
			db_fields = self.data_get_table_fields( data_table['fields'] , search_dict )
			self.log_debug(f"{obj_name} Read table: {data_table['module_name']}::{ data_table['table_obj'] } with search keys {db_fields['keys'] }" )	
			
			if db_fields:
				data_class_ref = getattr(importlib.import_module( data_table['module_name'] ), data_table['table_obj'] )	#Get ref to table object name dynamically
				data_obj = self.session.query( data_class_ref ).filter_by( **db_fields['keys'] ).all()

				for data_item in data_obj:
					if ret_db_obj: data_obj_list.append( data_item  )
					else: data_obj_list.append( data_item.to_dict()  )

		[ self.log_debug( f'Data from query: {data_item}')  for data_item in data_obj_list ] 
		return data_obj_list
				
	#####################################################################################
	def data_delete_ajax( self, submit_data: dict )-> str: 
		return self._data_process_ajax( submit_data, "del").to_http()

	#####################################################################################
	def data_update_ajax( self, submit_data:dict ): 
		return self._data_process_ajax( submit_data, "add").to_http()
		
	#####################################################################################
	def data_bulk_update_ajax( self, submit_data:dict )->DataUI_Response_List: 
		if not submit_data:
			self.log_error('No data given')  
			return json.dumps({'success':False}), 500 
		else:
			if not self.validate_schema_for_bulk_update(submit_data): 
				return DataUI_Response_List(success=False, error=DataUI_Error(no='001', message='Invalid Schema', validation=validation_result), http_status=500).to_http()

			return_data = []
			success = True
			
			for transaction in submit_data:	#Go through each transaction
				transcation_result = self._data_process_ajax( transaction['data'], transaction['transaction'] )
				if transcation_result:
					return_data.append( transcation_result )
					success = success & transcation_result.success	#see if successful or not
				else: 
					# breakpoint()
					success = False
			# if success_rate: return json.dumps( return_data ), 200
			if success: return DataUI_Response_List(success=True, response_list=return_data, http_status=200).to_http()

			return DataUI_Response_List(success=False, error=DataUI_Error(no='002', message='Some transactions failed'), response_list=return_data, http_status=500).to_http()


	#####################################################################################
	def _data_process_ajax( self, submit_data_row:dict, action:str )-> DataUI_Response: 
		if not submit_data_row:
			self.log_error('No data given')  
			return DataUI_Response(success=False, error=DataUI_Error(no='003', message='No data given'), http_status=500) 
		else:
			validation_result = self._data_validate( submit_data_row)
			if validation_result['success']:
				if action == 'add':
					data_obj_list = self.data_process( submit_data_row, self._data_process_add )
				elif action == 'edit':
					data_obj_list = self.data_process( submit_data_row, self._data_process_edit )
				elif action == 'del':
					data_obj_list = self.data_process( submit_data_row, self._data_process_del )
				else:
					self.log_error('No data given')  
					return DataUI_Response(success=False, error=DataUI_Error(no='004',message=f"Cannot recognize action[{action}]"), http_status=500) 
				
				if data_obj_list:
					return DataUI_Response(success=True, dbrec_list=data_obj_list, schema=self.data_schema, http_status=200) 
			else:
				return DataUI_Response(success=False, error=DataUI_Error(no='005',message=f"Validation failed", validation=validation_result), http_status=500) 
				

	#####################################################################################
	# 	"SiteMain":{ 	
	# 		# "table":"SiteMain",
	# 		# "fields":{
	# 					"si_site_id":{"field_db":"site_id",   "key":True},
	# 					"si_site_name":{"field_db":"site_name", "validation":{"required":True, "text_min_len":3, "text_max_len":20} },
	# 					"si_site_code":{"field_db":"site_code",   "validation":{"required":True,  "text_max_len":5} },
	# 		# } }
	#Loop through each of the json table schame descriptions
	def data_process(self, web_data:dict, fn_data_process: Callable)->list:
		data_obj_list = [] 
		# breakpoint()
		for data_table in self.data_schema : 
			db_fields = self.data_get_table_fields( data_table['fields'] , web_data )
			self.log_debug(f"Modify table: {data_table['module_name']}::{ data_table['table_obj'] } with search keys {db_fields['keys'] }" )	
			
			data_class_ref = getattr(importlib.import_module( data_table['module_name'] ), data_table['table_obj'] )	#Get ref to table object name dynamically
			
			data_obj = fn_data_process( db_fields, data_class_ref )
			if data_obj: data_obj_list.append( data_obj.to_dict()  )
			
		if data_obj: self.session.commit()
		
		return data_obj_list 

	#####################################################################################
	def _data_process_add(self, db_fields:dict, data_class_ref:ZStaple ):
		#If not found, create new object
		data_obj = data_class_ref( **db_fields['fields'] )
		self.session.add(data_obj)  
		# self.session.flush()	#specifically flush to get the ID number
		return data_obj

	#####################################################################################
	def _data_process_edit(self, db_fields:dict, data_class_ref:ZStaple ):
		#Search to see if the record exists
		data_obj = self.session.query( data_class_ref ).filter_by( **db_fields['keys'] ).first()
		
		if data_obj:  #If found, then update fields
			for db_field_name in db_fields['fields']:
				setattr( data_obj, db_field_name, db_fields['fields'][ db_field_name ]  )
		return data_obj

	#####################################################################################
	def _data_process_del(self, db_fields:dict, data_class_ref:ZStaple ):
	
		if db_fields['keys']: 
			data_obj = self.session.query( data_class_ref ).filter_by( **db_fields['keys'] ).first()
			
			self.session.query( data_class_ref ).filter_by( **db_fields['keys'] ).delete()
			# self.session.commit()
			return data_obj
		return None


	#####################################################################################
	def data_add(self, web_data):
		data_obj_list = []
		# breakpoint()
		## Example of talbe fields in self.data_schema
		# 	"SiteMain":{ 	
		# 		# "table":"SiteMain",
		# 		# "fields":{
		# 					"si_site_id":{"field_db":"site_id",   "key":True},
		# 					"si_site_name":{"field_db":"site_name", "validation":{"required":True, "text_min_len":3, "text_max_len":20} },
		# 					"si_site_code":{"field_db":"site_code",   "validation":{"required":True,  "text_max_len":5} },
		# 		# } }
		#Loop through each of the json table schame descriptions
		for data_table in self.data_schema :
			# if obj_name in self.update_obj_list:
			db_fields = self.data_get_table_fields( data_table['fields'] , web_data )
			self.log_debug(f"Modify table: {data_table['module_name']}::{ data_table['table_obj'] } with search keys {db_fields['keys'] }" )	
			
			data_class_ref = getattr(importlib.import_module( data_table['module_name'] ), data_table['table_obj'] )	#Get ref to table object name dynamically
			data_obj = None

			#If not found, create new object
			data_obj = data_class_ref( **db_fields['fields'] )
			self.session.add(data_obj)  
			self.session.flush()	#specifically flush to get the ID number
			data_obj_list.append( data_obj.to_dict()  )

		self.session.commit()
		
		return data_obj_list 

	#####################################################################################
	def data_update(self, web_data):
		data_obj_list = []
		# breakpoint()
		## Example of talbe fields in self.data_schema
		# 	"SiteMain":{ 	
		# 		# "table":"SiteMain",
		# 		# "fields":{
		# 					"si_site_id":{"field_db":"site_id",   "key":True},
		# 					"si_site_name":{"field_db":"site_name", "validation":{"required":True, "text_min_len":3, "text_max_len":20} },
		# 					"si_site_code":{"field_db":"site_code",   "validation":{"required":True,  "text_max_len":5} },
		# 		# } }
		#Loop through each of the json table schame descriptions
		for data_table in self.data_schema :
			# if obj_name in self.update_obj_list:
			db_fields = self.data_get_table_fields( data_table['fields'] , web_data )
			self.log_debug(f"Modify table: {data_table['module_name']}::{ data_table['table_obj'] } with search keys {db_fields['keys'] }" )	
			
			data_class_ref = getattr(importlib.import_module( data_table['module_name'] ), data_table['table_obj'] )	#Get ref to table object name dynamically
			data_obj = None

			#Search to see if the record exists
			data_obj = self.session.query( data_class_ref ).filter_by( **db_fields['keys'] ).first()
			
			if data_obj:  #If found, then update fields
				for db_field_name in db_fields['fields']:
					setattr( data_obj, db_field_name, db_fields['fields'][ db_field_name ]  )
			data_obj_list.append( data_obj.to_dict()  )

		self.session.commit()
		
		return data_obj_list 

	#####################################################################################
	def data_delete(self, web_data):
		for data_table in self.data_schema:
			db_fields = self.data_get_table_fields( data_table['fields'] , web_data )
			self.log_debug(f" Delete table: {data_table['module_name']}::{ data_table['table_obj'] } with search keys {db_fields['keys'] }" )

			data_class_ref = getattr(importlib.import_module( data_table['module_name'] ), data_table['table_obj']  )	#Get ref to table object name dynamically
			data_obj = None
			if db_fields['keys']: 
				data_obj = self.session.query( data_class_ref ).filter_by( **db_fields['keys'] ).delete()
				self.session.commit()
		return True


	#####################################################################################
	def data_get_table_fields(self, table_schema_fields, web_data ):
		data_obj_list = []
		db_fields = {'keys':{}, 'fields':{} } 
		# breakpoint()
		for field_name, field in table_schema_fields.items():	#Loop through each of the fields in a given table
			
			new_field = Selector().dict_search( web_data, {'id': field_name  } )
			if not new_field: 
				self.log_error(f'Could not find key [{field_name}] within web_data:[{web_data}]')
			else:
				# self.logger.debug(f"Adding field [{field_name}] value of: [{ new_field['value']  }]")
				if field.get("key") :
					if new_field['value']: db_fields[ "keys"][ field["field_db"] ] = new_field['value'] 
				else:
					db_fields[ "fields"][ field["field_db"] ] = new_field['value'] 

		self.log_debug(f"fields: {db_fields}")
		return db_fields 

 