"""A Python wrapper for the LADOK3 API"""
# -*- coding: utf-8 -*-
import cachetools
import datetime
import functools
import html
import json
import operator
import re
import requests
import urllib.parse

class LadokSession:
  """This is an interface for reading and writing data from and to LADOK."""
  def __init__(self, test_environment=False):
    """Log in and fetch base data"""
    self.__session = None
    self.__login_time = None
    self.base_url = "https://www.start.ladok.se" if not test_environment \
      else "https://www.test.ladok.se"
    self.base_gui_url = self.base_url + "/gui"
    self.base_gui_proxy_url = self.base_gui_url + "/proxy"
    self.headers = { 'Accept' : 'application/vnd.ladok-resultat+json, \
    application/vnd.ladok-kataloginformation+json, \
    application/vnd.ladok-studentinformation+json, \
    application/vnd.ladok-studiedeltagande+json, \
    application/vnd.ladok-utbildningsinformation+json, \
    application/vnd.ladok-examen+json, application/vnd.ladok-extintegration+json, \
    application/vnd.ladok-uppfoljning+json, application/vnd.ladok-extra+json, \
    application/json, text/plain' }
    self.cache = {}

  def login(self):
    """Log in to LADOK"""
    self.__login_time = datetime.datetime.now()
    try:
      self.session = requests.session()
      response = self.session.get(url = self.base_gui_url+'/loggain')
      response = self.session.get(url = self.base_gui_url+'/shiblogin')
              
      shibstate = re.search('return=(.*?)(&|$)', response.url).group(1)
      url = urllib.parse.unquote(shibstate)
      response = self.saml_login(url)
      if 'Din användare finns inte i Ladok' in response.text:
        raise Exception('Signed in successfully, but not as a teacher.')
    except Exception as err:
      self.__login_time = None
      raise err

  def saml_login(self, url):
    """Perform authentication to university CAS"""
    raise NotImplementedError()

  def logged_in(self):
    """Check if we have an active, logged-in session"""
    if self.__login_time:
      timeout = datetime.timedelta(minutes=15)
      return datetime.datetime.now() - self.__login_time < timeout
    return False

  def logout(self):
    """Close the session"""
    self.__login_time = None
    def logout(self):
      response = self.session.get(
        url=self.base_gui_proxy_url + '/logout',
        headers=self.headers)

      if response.status_code == 200:
        self.session.close()
        self.session = None
      else:
        raise Exception("Failed to log out of LADOK.")

  @property
  def session(self):
    """A guaranteed to be active and logged in requests session to LADOK"""
    if not self.logged_in():
      self.login()
    self.__login_time = datetime.datetime.now()
    return self.__session

  @property
  def xsrf_token(self):
    cookies = self.session.cookies.get_dict()
    return next(cookies[cookie] for cookie in cookies if cookie == 'XSRF-TOKEN')

  @session.setter
  def session(self, new_value):
    self.__session = new_value

  @cachetools.cachedmethod(
    operator.attrgetter("cache"),
    key=functools.partial(cachetools.keys.hashkey, "grade_scale"))
  def get_grade_scales(self, /, **kwargs):
    """Return a list of (un)filtered grade scales"""
    if len(kwargs) == 0:
      return [GradeScale(**scale_data)
                for scale_data in self.grade_scales_JSON()]

    return filter_on_keys(self.get_grade_scales(), **kwargs)
  @cachetools.cachedmethod(
    operator.attrgetter("cache"),
    key=functools.partial(cachetools.keys.hashkey, "get_student"))
  def get_student(self, id):
    """Get a student by unique ID, returns a Student object"""
    # note that self is the required LadokSession object
    return Student(ladok=self, id=id)
  @cachetools.cachedmethod(
    operator.attrgetter("cache"),
    key=functools.partial(cachetools.keys.hashkey, "search_courses"))
  def search_course_rounds(self, /, **kwargs):
    """Query LADOK about course rounds, possible keys:
    code, round_code, name
    """
    url = self.base_gui_proxy_url + "/resultat/kurstillfalle/filtrera?"

    if "code" in kwargs:
      url += f"kurskod={kwargs['code']}&"
    if "name" in kwargs:
      url += f"benamning={kwargs['name']}&"
    if "round_code" in kwargs:
      url += f"tillfalleskod={kwargs['round_code']}&"

    url += "page=1&limit=400&skipCount=false&sprakkod=sv"

    response = self.session.get(
      url=url,
      headers=self.headers)

    results = response.json()["Resultat"]
    
    return [CourseRound(ladok=self, **result) for result in results]
  def get_query(self, path, content_type="application/vnd.ladok-resultat+json"):
    """Returns GET query response for path on the LADOK server"""
    headers = self.headers.copy()
    headers["Content-Type"] = content_type

    return self.session.get(
      url=self.base_gui_proxy_url + path,
      headers=headers)

  def put_query(self, path, put_data,
    content_type="application/vnd.ladok-resultat+json"):
    """Returns PUT query response for path on the LADOK server"""
    headers = self.headers.copy()
    headers["Content-Type"] = content_type
    headers["X-XSRF-TOKEN"] = self.get_xsrf_token()
    headers["Referer"] = self.base_gui_url

    return self.session.put(
      url=self.base_gui_proxy_url + path,
      json=put_data,
      headers=headers)

  def post_query(self, path, post_data,
    content_type="application/vnd.ladok-resultat+json"):
    """Returns POST query response for path on the LADOK server"""
    headers = self.headers.copy()
    headers["Content-Type"] = content_type
    headers["X-XSRF-TOKEN"] = self.get_xsrf_token()
    headers["Referer"] = self.base_gui_url

    return self.session.post(
      url=self.base_gui_proxy_url + path,
      json=post_data,
      headers=headers)
  def grade_scales_JSON(self):
    response = self.get_query('/resultat/grunddata/betygsskala')

    if response.status_code == 200:
      return response.json()["Betygsskala"]
    return None
  def registrations_JSON(self, student_id):
    """Return all registrations for student with ID student_id."""
    response = self.get_query(
      '/studiedeltagande/tillfallesdeltagande/kurstillfallesdeltagande/student/'+
        student_id,
      "application/vnd.ladok-studiedeltagande+json")

    if response.status_code == 200:
      return response.json()["Tillfallesdeltaganden"]
    return None
  def registrations_on_course_JSON(self,
      course_education_id, student_id):
    """Return a list of registrations on course with education_id for student 
    with student_id. JSON format."""
    response = self.get_query(
      "/studiedeltagande/tillfallesdeltagande"
        f"/utbildning/{course_education_id}/student/{student_id}",
      "application/vnd.ladok-studiedeltagande+json")
    
    if response.status_code == 200:
      return response.json()["Tillfallesdeltaganden"]
    return None
  def course_rounds_JSON(self, course_instance_id):
    """Requires course instance ID"""
    response = self.get_query(
      f"/resultat/kurstillfalle/kursinstans/{course_instance_id}")

    if response.status_code == 200:
      return response.json()["Utbildningstillfalle"]
    return None
  def course_instance_JSON(self, instance_id):
    """Returns course instance data for a course with instance ID instance_id"""
    response = self.get_query(
      f"/resultat/utbildningsinstans/kursinstans/{instance_id}")

    if response.status_code == 200:
      return response.json()
    return None
  def course_round_components_JSON(self, round_id):
    response = self.put_query(
      "/resultat/kurstillfalle/moment",
      {"Identitet": [round_id]}
    )

    if response.status_code == 200:
      return response.json()["MomentPerKurstillfallen"]
    raise Exception(response.json()["Meddelande"])
  def course_instance_components_JSON(self, course_instance_id):
    response = self.put_query(
      "/resultat/utbildningsinstans/moduler",
      {"Identitet": [course_instance_id]}
    )

    if response.status_code == 200:
      return response.json()["Utbildningsinstans"][0]
    raise Exception(response.json()["Meddelande"])
  def search_reported_results_JSON(self, course_round_id, component_instance_id):
    """Requires:
    course_round_id: round_id for a course,
    component_instance_id: instance_id for a component of the course.
    """
    put_data = {
      "Filtrering": ["OBEHANDLADE", "UTKAST", "ATTESTERADE"],
      "KurstillfallenUID": [course_round_id],
      "OrderBy": [
        "EFTERNAMN_ASC",
        "FORNAMN_ASC",
        "PERSONNUMMER_ASC"
      ],
      "Limit": 400,
      "Page": 1,
      "StudenterUID": []
    }

    response = self.put_query(
      '/resultat/studieresultat/rapportera/utbildningsinstans/' +
        component_instance_id + '/sok',
      put_data)

    if response.status_code == 200:
      return response.json()["Resultat"]
    return None
  def search_course_results_JSON(self, course_round_id, component_instance_id):
    put_data = {
      "KurstillfallenUID": [course_round_id],
      "Tillstand": ["REGISTRERAD", "AVKLARAD", "AVBROTT"],
      "OrderBy": ["EFTERNAMN_ASC", "FORNAMN_ASC"],
      "Limit": 400,
      "Page": 1,
    }

    response = self.put_query(
      "/resultat/resultatuppfoljning/resultatuppfoljning/sok",
      put_data)

    if response.status_code == 200:
      return response.json()["Resultat"]
    return None
  def student_results_JSON(self, student_id, course_round_id):
    """Returns the results for a student on a course round"""
    response = self.get_query(
      '/resultat/studieresultat/student/' + student_id +
          '/utbildningstillfalle/' + course_round_id
    )

    if response.status_code == 200:
      return response.json()
    raise Exception(response.json()["Meddelande"])
  def create_result_JSON(self,
        grade_id, grade_scale_id, date,
        study_result_id, instance_id,
        notes=[]):
    """Creates a new result"""
    response = self.post_query(
      "/resultat/studieresultat/skapa",
      {"Resultat": [{
        "Betygsgrad": grade_id,
        "BetygsskalaID": grade_scale_id,
        "Examinationsdatum": date,
        "Noteringar": notes,
        "StudieresultatUID": study_result_id,
        "UtbildningsinstansUID": instance_id
      }]}
    )

    if response.status_code == 200:
      return response.json()["Resultat"]
    raise Exception(response.json()["Meddelande"])
  def update_result_JSON(self,
        grade_id, grade_scale_id, date,
        result_id, last_modified, notes=[]):
    response = self.put_query(
      '/resultat/studieresultat/uppdatera',
      {
        'Resultat': [{
          'ResultatUID': result_id,
          'Betygsgrad': grade_id,
          'BetygsskalaID': grade_scale_id,
          'Noteringar': notes,
          'Examinationsdatum': date,
          'SenasteResultatandring': last_modified
        }]
      }
    )

    if response.status_code == 200:
      return response.json()["Resultat"]
    raise Exception(response.json()["Meddelande"])
  def result_attestants_JSON(self, result_id):
    """Returns a list of result attestants"""
    response = self.put_query(
      "/resultat/anvandare/resultatrattighet/attestanter/kurstillfallesrapportering",
      {"Identitet": [result_id]}
    )

    if response.status_code == 200:
      return response.json()["Anvandare"]
    raise Exception(response.json()["Meddelande"])
  def result_reporters_JSON(self, organization_id):
    """Returns a list of who can report results in an organization"""
    response = self.get_query(
      "/kataloginformation/anvandare/organisation/" +
        organization_id + "/resultatrapportorer",
      "application/vnd.ladok-kataloginformation+json"
    )

    if response.status_code == 200:
      return response.json()["Anvandare"]
    raise Exception(response.text)
  def user_info_JSON(self):
    response = self.get_query(
      "/kataloginformation/anvandare/anvandarinformation",
      "application/vnd.ladok-kataloginformation+json"
    )

    if response.status_code == 200:
      return response.json()
    raise Exception(response.text)
  def finalize_result_JSON(self,
      result_id, last_modified, reporter_id, attestant_id=None):
    """Marks a result as finalized (klarmarkera)"""
    response = self.put_query(
      f"/resultat/studieresultat/resultat/{result_id}/klarmarkera",
      {
        "Beslutsfattare": [attestant_id] if attestant_id else [],
        "RattadAv": [reporter_id],
        "ResultatetsSenastSparad": last_modified
      }
    )

    if response.status_code == 200:
      return response.json()
    raise Exception(response.json()["Meddelande"])
  def participants_JSON(self, course_round_id, /, **kwargs):
    """Returns JSON record containing participants in a course identified by 
    round ID.
    Filters in kwargs: not_started, ongoing, registered, finished, cancelled"""
    participants_types = []
    if "not_started" in kwargs and kwargs["not_started"]:
      participants_types.append("EJ_PABORJAD")
    if "ongoing" in kwargs and kwargs["ongoing"]:
      participants_types.append("PAGAENDE")
    if "registered" in kwargs and kwargs["registered"]:
      participants_types.append("REGISTRERAD")
    if "finished" in kwargs and kwargs["finished"]:
      participants_types.append("AVKLARAD")
    if "cancelled" in kwargs and kwargs["cancelled"]:
      participants_types.append("AVBROTT")
    # 'ATERBUD', # Withdrawal
    # 'PAGAENDE_MED_SPARR', # on-going block exists
    # 'EJ_PAGAENDE_TILLFALLESBYTE', # not on-going due to instance exchange
    # 'UPPEHALL', # not on-going due to approved leave from studies

    if not kwargs:
      participants_types = ["PAGAENDE", "REGISTRERAD", "AVKLARAD"]

    put_data = {
      'page': 1,
      'limit': 400,
      'orderby': ['EFTERNAMN_ASC',
                  'FORNAMN_ASC',
                  'PERSONNUMMER_ASC',
                  'KONTROLLERAD_KURS_ASC'],
      'deltagaretillstand': participants_types,
      'utbildningstillfalleUID': [course_round_id]
    }

    response = self.put_query(
      '/studiedeltagande/deltagare/kurstillfalle',
      put_data,
      "application/vnd.ladok-studiedeltagande+json")
    if response.status_code == 200:
      return response.json()["Resultat"]
    return None
  ##############################################################
  #
  # LadokSession
  #
  # get_results      returnerar en dictionary med momentnamn och resultat
  # save_result      sparar resultat för en student som utkast
  #
  # The original LadokSession code is from Alexander Baltatzis <alba@kth.se> on 
  # 2020-07-20
  #
  # I (Gerald Q. Maguire Jr.) have extended on 2020-07-21 and later with the code 
  # as noted below.
  #
  # I (Daniel Bosk) adapted (on 2021-01-08) the methods to a refactored 
  # LadokSession class.

  #####################################################################
  #
  # get_results
  #
  # person_nr          - personnummer, siffror i strängformat
  #            t.ex. 19461212-1212
  # course_code          - kurskod t.ex. DD1321
  #
  # RETURNERAR en dictionary från ladok med momentnamn, resultat
  #
  # {'LABP': {'date': '2019-01-14', 'grade': 'P', 'status': 'attested'},
  #  'LABD': {'date': '2019-03-23', 'grade': 'E', 'status': 'pending(1)'},
  #  'TEN1': {'date': '2019-03-13', 'grade': 'F', 'status': 'pending(2)'}}
  #
  #  status:  kan ha följande värden vilket gissningsvis betyder: 
  #           attested   - attesterad
  #           pending(1) - utkast
  #           pending(2) - klarmarkerad
  #
  def get_results(self, person_nr_raw, course_code):
    person_nr_raw = str(person_nr_raw)
    person_nr =  format_personnummer(person_nr_raw)
    if not person_nr: raise Exception('Invalid person nr ' + person_nr_raw)
    
    student_data = self.__get_student_data(person_nr)

    student_course = next(x
      for x in self.__get_student_courses(student_data['id'])
        if x['code'] == course_code)

    # get attested results
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/resultat/studentresultat/attesterade/student/' +
          student_data['id'],
      headers=self.headers).json()
    
    results_attested_current_course = None
    results = {}  # return value
    
    for course in r['StudentresultatPerKurs']:
      if course['KursUID'] == student_course['education_id']:
        results_attested_current_course = course['Studentresultat']
        break


    if results_attested_current_course:
      for result in results_attested_current_course:
        try:
            d = { 'grade' : result['Betygsgradskod'],
                  'status': 'attested',
                  'date'  : result['Examinationsdatum'] }
            results[ result['Utbildningskod'] ] = d
        except:
            pass  # tillgodoräknanden har inga betyg och då är result['Utbildningskod'] == None

    # get pending results
    r = self.session.get(
      url=self.base_gui_proxy_url + '/resultat/resultat/resultat/student/' +
        student_data['id'] + '/kurs/' + student_course['education_id'] +
          '?resultatstatus=UTKAST&resultatstatus=KLARMARKERAT',
      headers=self.headers).json()
    
    for result in r['Resultat']:
        r = self.session.get(
          url=self.base_gui_proxy_url + '/resultat/utbildningsinstans/' +
            result['UtbildningsinstansUID'],
          headers=self.headers).json()
        d_grade = result['Betygsgradsobjekt']['Kod']
        d_status = "pending(" + str(result['ProcessStatus']) + ")"
        # utkast har inte datum tydligen ...
        d_date = "0" if 'Examinationsdatum' not in result \
                      else result['Examinationsdatum']
        d = { 'grade' : d_grade ,
              'status': d_status,
              'date'  : d_date      } 
        results[ r['Utbildningskod'] ] = d
    return results

  #####################################################################
  #
  # save_result
  #
  # person_nr           - personnummer, flera format accepteras enligt regex:
  #                       (\d\d)?(\d\d)(\d\d\d\d)[+\-]?(\w\w\w\w)
  # course_code         - kurskod t.ex. DD1321
  # course_moment       - ladokmoment/kursbetyg t.ex. TEN1, LAB1, DD1321 (!)
  #                       om labmomententet är samma som course_code så sätts kursbetyg!
  # result_date         - betygsdatum, flera format accepteras enligt regex
  #                       (\d\d)?(\d\d)-?(\d\d)-?(\d\d)
  # grade_code          - det betyg som ska sättas
  # grade_scale         - betygsskala t.ex. AF eller PF. Möjliga betygsskalor
  #                       listas i self.__grade_scales. 
  #
  # RETURNERAR True om det gått bra, kastar (förhoppningsvis) undantag
  #            om det går dåligt. 
  def save_result(self, person_nr_raw, course_code, course_moment,
    result_date_raw, grade_raw, grade_scale):
    if grade_raw in ["AF", "PF"]:
        raise Exception('Invalid grade: ' + grade_raw + ' looks like a grade_scale') 

    if (grade_raw == 'P' and grade_scale == "AF") or \
       (grade_raw in "ABCDE" and grade_scale == "PF"):
      raise Exception('Invalid grade: ' + grade_raw +
        ' does not match grade_scale ' + grade_scale)
    
    person_nr =  format_personnummer(person_nr_raw)
    if not person_nr: raise Exception('Invalid person nr ' + person_nr_raw)
    
    result_date = self.__validate_date(result_date_raw)
    if not result_date:
      raise Exception('Invalid grade date: ' + result_date_raw + ' pnr: ' +
        person_nr_raw + ' moment: ' + course_moment)
    
    student_data = self.__get_student_data(person_nr)
    student_course = next(x
      for x in self.__get_student_courses(student_data['id'])
        if x['code'] == course_code)
    
    # momentkod = kurskod => vi hanterar kursbetyg
    if course_moment == student_course['code']:
        course_moment_id = student_course['instance_id']
    else:
        for x in self.__get_student_course_moments(student_course['round_id'], 
          student_data['id']):
          if x['code'] == course_moment:
            course_moment_id = x['course_moment_id']
        
    student_course_results = self.__get_student_course_results(
      student_course['round_id'], student_data['id'])
    
    grade_scale = self.__get_grade_scale_by_code(grade_scale)
    grade = grade_scale.grades(code=grade_raw)[0]
                
    headers = self.headers.copy()
    headers['Content-Type'] = 'application/vnd.ladok-resultat+json'
    headers['X-XSRF-TOKEN'] = self.__get_xsrf_token()
    headers['Referer'] = self.base_gui_url
    
    previous_result = None
    
    for result in student_course_results['results']:
        if result['pending'] is not None:
            if result['pending']['moment_id'] == course_moment_id:
                previous_result = result['pending']
                break
    
    # uppdatera befintligt utkast
    if previous_result:
        put_data = {
            'Resultat': [{
                'ResultatUID': previous_result['id'],
                'Betygsgrad': grade.id,
                'Noteringar': [],
                'BetygsskalaID': grade_scale.id,
                'Examinationsdatum': result_date,
                'SenasteResultatandring': previous_result['last_modified']
            }]
        }
        
        r = self.session.put(
          url=self.base_gui_proxy_url + '/resultat/studieresultat/uppdatera',
          json=put_data,
          headers=headers)
    
    # lägg in nytt betygsutkast
    else:
        post_data = {
            'Resultat': [{
                'StudieresultatUID': student_course_results['id'],
                'UtbildningsinstansUID': course_moment_id,
                'Betygsgrad': grade.id,
                'Noteringar': [],
                'BetygsskalaID': grade_scale.id,
                'Examinationsdatum': result_date
            }]
        }
        r = self.session.post(
          url=self.base_gui_proxy_url + '/resultat/studieresultat/skapa',
          json=post_data,
          headers=headers)
    
    if not 'Resultat' in r.json():
      raise Exception("Couldn't register " +
        course_moment + "=" + grade_raw + " " + result_date_raw + ": " +
          r.json()["Meddelande"])
    
    return True
  #####################################################################
  #
  # get_student_data
  #
  # person_nr           - personnummer, flera format accepteras enligt regex:
  #                       (\d\d)?(\d\d)(\d\d\d\d)[+\-]?(\w\w\w\w)
  #
  # RETURNERAR {'id': 'xxxx', 'first_name': 'x', 'last_name': 'y', 'person_nr': 'xxx', 'alive': True}

  def get_student_data(self, person_nr_raw):
    person_nr =  format_personnummer(person_nr_raw)
    
    if not person_nr: raise Exception('Invalid person nr ' + person_nr_raw)
    
    student_data = self.__get_student_data(person_nr)
    return student_data

  #####################################################################
  #
  # get_student_name
  #
  # person_nr          - personnummer, flera format accepteras enligt regex:
  #                      (\d\d)?(\d\d)(\d\d\d\d)[+\-]?(\w\w\w\w)
  #
  # RETURNERAR en dictionary med för- och efternamn
  #
  # {"first_name" : 'Anna', "last_name : 'Andersson'}
  #
  def get_student_name(self, person_nr_raw):
    person_nr =  format_personnummer(person_nr_raw)
    
    if not person_nr: raise Exception('Invalid person nr ' + person_nr_raw)
    
    student_data = self.__get_student_data(person_nr)
    return {
      "first_name": student_data["first_name"],
      "last_name" : student_data["last_name"]
    }
  # added by GQMJr
  #####################################################################
  #
  # get_student_data_JSON
  #
  # person_nr          - personnummer, flera format accepteras enligt regex:
  #                      (\d\d)?(\d\d)(\d\d\d\d)[+\-]?(\w\w\w\w)
  #
  # lang               - language code 'en' or 'sv', defaults to 'sv'
  #
  # RETURNERAR en dictionary med för- och efternamn and more
  def get_student_data_JSON(self, person_nr_raw, lang = 'sv'):
    person_nr =  format_personnummer(person_nr_raw)
    
    if not person_nr: raise Exception('Invalid person nr ' + person_nr_raw)

    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/studentinformation/student/filtrera?limit=2&orderby=EFTERNAMN_ASC&orderby=FORNAMN_ASC&orderby=PERSONNUMMER_ASC&page=1&personnummer='
          + person_nr + '&skipCount=false&sprakkod='+lang,
      headers=self.headers)
    
    if r.status_code == requests.codes.ok:
        return r.json()
    return None
  #####################################################################
  #
  # get_student_data_by_uid_JSON
  #
  # uid                - Ladok ID
  #
  # RETURNERAR en dictionary med för- och efternamn and more
  def get_student_data_by_uid_JSON(self, uid):
    r = self.session.get(
      url = self.base_gui_proxy_url +
        '/studentinformation/student/'+uid, headers = self.headers)
    if r.status_code == requests.codes.ok:
      return r.json()
    return None
  # added by GQMJr
  #####################################################################
  #
  # all_grading_scale
  #
  #
  # RETURNERAR en dictionary of the grading scales
  def all_grading_scale(self):
    return self.get_grade_scales()
  # added by GQMJr
  #####################################################################
  #
  # grading_rights
  #
  #
  # RETURNERAR en dictionary of the grading rights (of the logged in user)
  def grading_rights(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/resultat/resultatrattighet/listaforinloggadanvandare',
      headers=self.headers).json()
    return r['Resultatrattighet']
  # added by GQMJr
  #####################################################################
  #
  # change_locale
  #
  # lang               - language code 'en' or 'sv', defaults to 'sv'
  #
  # RETURNERAR reponse to the request
  def change_locale(self, lang = 'sv'):
    r = self.session.get(
      url=self.base_gui_url+'/services/i18n/changeLocale?lang='+lang,
      headers=self.headers).json()
    return r
  # added by GQMJr
  #####################################################################
  #
  # course_instances_JSON
  #
  # course_code        - course code, such as "II2202"
  #
  # lang               - language code 'en' or 'sv', defaults to 'sv'
  #
  # RETURNERAR JSON of resultat/kurstillfalle
  #
  # Example: ladok_session.course_instances('II2202', 'en')
  def course_instances_JSON(self, course_code, lang = 'sv'):
    # note that there seems to be a limit of 403 for the number of pages
    r = self.session.get(
      url=self.base_gui_proxy_url + '/resultat/kurstillfalle/filtrera?kurskod=' +
        course_code + '&page=1&limit=100&skipCount=false&sprakkod=' + lang,
      headers=self.headers).json()
    return r
  # added by GQMJr
  #####################################################################
  #
  # organization_info_JSON
  #
  # RETURNERAR en dictionary of organization information for the entire institution of the logged in user
  def organization_info_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url + '/resultat/organisation/utanlankar',
      headers=self.headers).json()
    return r
  # added by GQMJr
  #####################################################################
  #
  # period_info_JSON
  #
  # RETURNERAR JSON of /resultat/grunddata/period
  def period_info_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url + '/resultat/grunddata/period',
      headers=self.headers).json()
    return r
  # added by GQMJr
  #####################################################################
  #
  # instance_info
  #
  # course_code        - course code, such as "II2202"
  #
  # instance_code      - instance of the course ('TillfallesKod')
  # 
  # lang               - language code 'en' or 'sv', defaults to 'sv'
  #
  # RETURNERAR en dictionary of course instance information
  #
  # Example: ii=ladok_session.instance_info('II2202', instance_code, 'en')
  def instance_info(self, course_code, instance_code, lang = 'sv'):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/resultat/kurstillfalle/filtrera?kurskod=' + course_code +
          '&page=1&limit=25&skipCount=false&sprakkod=' + lang,
      headers=self.headers)
    if r.status_code == requests.codes.ok:
      rj=r.json()
      for course in rj['Resultat']:
        if course['TillfallesKod'] == instance_code:
          return course
    return None
  # added by GQMJr
  #####################################################################
  #
  # instance_info_uid
  #
  # instance_uid       -- course's Uid (from course_integration_id)
  # 
  # RETURNERAR en dictionary of course instance information
  #
  # Example: ii=ladok_session.instance_info_uid(instance_uid)
  def instance_info_uid(self, instance_uid):
    r = self.session.get(
      url=self.base_gui_proxy_url + '/resultat/kurstillfalle/'+instance_uid,
      headers=self.headers).json()
    return r
  # added by GQMJr
  #####################################################################
  #
  # studystructure_student_JSON
  #
  # uid                -  uid of a student
  #
  # RETURNERAR en dictionary of student information
  def studystructure_student_JSON(self, uid):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/studiedeltagande/studiestruktur/student/'+uid,
      headers=self.headers)
    if r.status_code == 200:
      return r.json()
    return None
  # added by GQMJr
  #####################################################################
  #
  # larosatesinformation_JSON
  #
  # RETURNERAR JSON of the university or college information
  def larosatesinformation_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/larosatesinformation',
      headers=self.headers).json()
    return r

  # {   'Larosatesinformation': [   {   'Benamning': {   'en': 'Royal Institute of '
  #                                                            'Technology',
  #                                                      'sv': 'Kungliga Tekniska '
  #                                                            'högskolan'},
  #                                     'Beskrivning': {},
  #                                     'Giltighetsperiod': {'link': []},
  #                                     'ID': '29',
  #                                     'Kod': 'KTH',
  #                                     'LarosateID': 29,
  #                                     'OrtID': 18,
  #                                     'link': []}],
  #     'link': []}
  # added by GQMJr
  #####################################################################
  #
  # undervisningssprak
  #
  # RETURNERAR en dictionary of languages used for instruction
  def undervisningssprak_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/undervisningssprak',
      headers=self.headers).json()
    return r
  # {   'Undervisningssprak': [   {   'Benamning': {   'en': 'English',
  #                                                'sv': 'Engelska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '2',
  #                               'Kod': 'ENG',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {'en': 'Russian', 'sv': 'Ryska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '4',
  #                               'Kod': 'RUS',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {   'en': 'Sign Language',
  #                                                'sv': 'Teckenspråk'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '5',
  #                               'Kod': 'SGN',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {   'en': 'Spanish',
  #                                                'sv': 'Spanska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '3',
  #                               'Kod': 'SPA',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {   'en': 'Swedish',
  #                                                'sv': 'Svenska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '1',
  #                               'Kod': 'SWE',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {'en': 'Danish', 'sv': 'Danska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '109804',
  #                               'Kod': 'DAN',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {   'en': 'Finnish',
  #                                                'sv': 'Finska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '109805',
  #                               'Kod': 'FIN',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {   'en': 'Italian',
  #                                                'sv': 'Italienska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '109806',
  #                               'Kod': 'ITA',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {   'en': 'Japanese',
  #                                                'sv': 'Japanska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '109807',
  #                               'Kod': 'JPN',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {   'en': 'Norwegian',
  #                                                'sv': 'Norska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '109808',
  #                               'Kod': 'NOR',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {   'en': 'Portugese',
  #                                                'sv': 'Portugisiska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '109809',
  #                               'Kod': 'POR',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {   'en': 'French',
  #                                                'sv': 'Franska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '109810',
  #                               'Kod': 'FRE',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {'en': 'German', 'sv': 'Tyska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '109811',
  #                               'Kod': 'GER',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {   'en': 'Chinese',
  #                                                'sv': 'Kinesiska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '111033',
  #                               'Kod': 'CHI',
  #                               'LarosateID': -1,
  #                               'link': []},
  #                           {   'Benamning': {   'en': 'Arabic',
  #                                                'sv': 'Arabiska'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'ID': '111032',
  #                               'Kod': 'ARA',
  #                               'LarosateID': -1,
  #                               'link': []}],
  # 'link': []}
  # added by GQMJr
  #####################################################################
  #
  # i18n_translation_JSON
  #
  # lang               - language code 'en' or 'sv', defaults to 'sv'
  # RETURNERAR JSON of i18n translations used in Ladok3
  def i18n_translation_JSON(self, lang = 'sv'):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/i18n/oversattningar/sprakkod/' + lang,
      headers=self.headers).json()
    return r

  # the above i18n translations are used for example in:
  # 'Utbildningstillfallestyp': {   'Benamningar': {   'en': 'Course instance', 'sv': 'Kurstillfälle'},
  #                                                    'Giltighetsperiod': {   'link': [   ]},
  #                                                    'Grundtyp': 'KURS',
  #                                                    'ID': 52,
  #                                                    'Kod': '2007KTF',
  #                                                    'RegelverkForUtbildningstyp': {   'Regelvarden': [   {   'Regelnamn': 'commons.domain.regel.ingar.i.grupp.overfors.till.nya', 'link': [   ]},
  #                                                                                                         {   'Regelnamn': 'commons.domain.regel.informationsbehorighet.grundavancerad', 'Varde': 'true', 'link': [   ]},
  #                                                                                                         {   'Regelnamn': 'commons.domain.regel.kan.utannonseras', 'Varde': 'true', 'link': [   ]},
  #                                                                                                         {   'Regelnamn': 'commons.domain.regel.grupp.for.utsokning',
  #                                                                                                             'Varde': 'grupp.for.utsokning.grundavanceradniva', 'link': [   ]}],
  # All of the things of the form "commons-domain.*" are i18n keys to look the actual text to be used.
  # for example:
  # in Swedish:
  #{   'I18nNyckel': 'commons.domain.regel.ingar.i.grupp.overfors.till.nya',
  #    'Text': 'Ingår i grupp: Överförs till NyA',
  #    'link': []},
  # In English:
  # {   'I18nNyckel': 'commons.domain.regel.ingar.i.grupp.overfors.till.nya',
  #     'Text': 'Part of group: Transferred to NyA',
  #     'link': []},
  # added by GQMJr
  #####################################################################
  #
  # svenskorter_JSON
  #
  # RETURNERAR JSON of places in Sweden with their KommunID
  def svenskorter_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url + '/kataloginformation/grunddata/svenskort',
      headers=self.headers).json()
    return r

  # returns:
  # {   'SvenskOrt': [   {   'Benamning': {   'en': 'Stockholm (Botkyrka)',
  #                                           'sv': 'Stockholm (Botkyrka)'},
  #                          'Beskrivning': {},
  #                          'Giltighetsperiod': {'link': []},
  #                          'ID': '110990',
  #                          'Kod': 'L0127',
  #                          'KommunID': '8',
  #                          'LarosateID': -1,
  #                          'link': []},
  # ... ], 'link': []}
  # added by GQMJr
  #####################################################################
  #
  # kommuner_JSON
  #
  # RETURNERAR JSON of places in Sweden with their KommunID
  def kommuner_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url + '/kataloginformation/grunddata/kommun',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Kommun': [   {   'Benamning': {'en': 'Knivsta', 'sv': 'Knivsta'},
  #                   'Beskrivning': {},
  #                   'Giltighetsperiod': {'link': []},
  #                   'ID': '29',
  #                   'Kod': '0330',
  #                   'LanID': 2,
  #                   'LarosateID': -1,
  #                   'link': []},
  #               {   'Benamning': {'en': 'Heby', 'sv': 'Heby'},
  #                   'Beskrivning': {   'sv': 'Överförd från Västmanlands '
  #                                            'till Uppsala län'},
  #                   'Giltighetsperiod': {   'Startdatum': '2007-01-01',
  #                                           'link': []},
  #                   'ID': '30',
  #                   'Kod': '0331',
  #                   'LanID': 2,
  #                   'LarosateID': -1,
  #                   'link': []},
  # ], 'link': []}
  # added by GQMJr
  #####################################################################
  #
  # lander_JSON
  #
  # RETURNERAR JSON of countries
  def lander_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url + '/kataloginformation/grunddata/land',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Land': [   {   'Benamning': {'en': 'Bolivia', 'sv': 'Bolivia'},
  #                     'Beskrivning': {},
  #                     'Giltighetsperiod': {'link': []},
  #                     'ID': '20',
  #                     'Kod': 'BO',
  #                     'LarosateID': -1,
  #                     'link': []},
  #                 {   'Benamning': {'en': 'Brazil', 'sv': 'Brasilien'},
  #                     'Beskrivning': {},
  #                     'Giltighetsperiod': {'link': []},
  #                     'ID': '21',
  #                     'Kod': 'BR',
  #                     'LarosateID': -1,
  #                     'link': []},
  # ... ],    'link': []}
  # added by GQMJr
  #####################################################################
  #
  # undervisningstid_JSON
  #
  # RETURNERAR JSON of teaching times
  def undervisningstid_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/undervisningstid',
      headers=self.headers).json()
    return r

  #returns:
  # {   'Undervisningstid': [   {   'Benamning': {   'en': 'Mixed-time',
  #                                                  'sv': 'Blandad '
  #                                                  'undervisningstid'},
  #                                 'Beskrivning': {},
  #                                 'Giltighetsperiod': {'link': []},
  #                                 'ID': '101051',
  #                                 'Kod': 'BLA',
  #                                 'LarosateID': -1,
  #                                 'link': []},
  #                             {   'Benamning': {'en': 'Day-time', 'sv': 'Dagtid'},
  #                                 'Beskrivning': {},
  #                                 'Giltighetsperiod': {'link': []},
  #                                 'ID': '101052',
  #                                 'Kod': 'DAG',
  #                                 'LarosateID': -1,
  #                                 'link': []},
  #                             {   'Benamning': {   'en': 'Afternoon-time',
  #                                                  'sv': 'Eftermiddagstid'},
  #                                 'Beskrivning': {},
  #                                 'Giltighetsperiod': {'link': []},
  #                                 'ID': '101053',
  #                                 'Kod': 'EFT',
  #                                 'LarosateID': -1,
  #                                 'link': []},
  #                             {   'Benamning': {   'en': 'No teaching',
  #                                                  'sv': 'Ingen '
  #                                                  'undervisningstid'},
  #                                 'Beskrivning': {},
  #                                 'Giltighetsperiod': {   'Slutdatum': '2016-04-30',
  #                                                         'link': []},
  #                                 'ID': '101054',
  #                                 'Kod': 'ING',
  #                                 'LarosateID': -1,
  #                                 'link': []},
  #                             {   'Benamning': {   'en': 'Evening-time',
  #                                                  'sv': 'Kvällstid'},
  #                                 'Beskrivning': {},
  #                                 'Giltighetsperiod': {'link': []},
  #                                 'ID': '101055',
  #                                 'Kod': 'KVÄ',
  #                                 'LarosateID': -1,
  #                                 'link': []},
  #                             {   'Benamning': {   'en': 'Weekends',
  #                                                  'sv': 'Veckoslut'},
  #                                 'Beskrivning': {},
  #                                 'Giltighetsperiod': {'link': []},
  #                                 'ID': '101056',
  #                                 'Kod': 'VSL',
  #                                 'LarosateID': -1,
  #                                 'link': []}],
  #     'link': []}
  # added by GQMJr
  #####################################################################
  #
  # successivfordjupning_JSON
  #
  # RETURNERAR JSON of Successive Specializations
  def successivfordjupning_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/successivfordjupning',
      headers=self.headers).json()
    return r

  #returns:
  # {   'SuccessivFordjupning': [   {   'Benamning': {   'en': 'Second cycle, '
  #                                                            'contains degree '
  #                                                            'project for Master '
  #                                                            'of Arts/Master of '
  #                                                            'Science (60 '
  #                                                            'credits)',
  #                                                      'sv': 'Avancerad nivå, '
  #                                                            'innehåller '
  #                                                            'examensarbete för '
  #                                                            'magisterexamen'},
  #                                     'Beskrivning': {},
  #                                     'Giltighetsperiod': {'link': []},
  #                                     'ID': '1',
  #                                     'Kod': 'A1E',
  #                                     'LarosateID': -1,
  #                                     'NivaInomStudieordningID': 2,
  #                                     'link': []},
  #                                 {   'Benamning': {   'en': 'Second cycle, has '
  #                                                            'second-cycle '
  #                                                            'course/s as entry '
  #                                                            'requirements',
  #                                                      'sv': 'Avancerad nivå, '
  #                                                            'har kurs/er på '
  #                                                            'avancerad nivå som '
  #                                                            'förkunskapskrav'},
  #                                     'Beskrivning': {},
  #                                     'Giltighetsperiod': {'link': []},
  #                                     'ID': '2',
  #                                     'Kod': 'A1F',
  #                                     'LarosateID': -1,
  #                                     'NivaInomStudieordningID': 2,
  #                                     'link': []},
  # ... ], 'link': []}
  # added by GQMJr
  #####################################################################
  #
  # undervisningsform_JSON
  #
  # RETURNERAR JSON of forms of education
  def undervisningsform_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/undervisningsform',
      headers=self.headers).json()
    return r

  #returns:
  # {   'Undervisningsform': [   {   'Benamning': {   'en': '- No translation '
  #                                                         'available -',
  #                                                   'sv': 'IT-baserad distans'},
  #                                  'Beskrivning': {},
  #                                  'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                                          'link': []},
  #                                  'ID': '133253',
  #                                  'Kod': 'ITD',
  #                                  'LarosateID': 29,
  #                                  'link': []},
  #                              {   'Benamning': {   'en': '- No translation '
  #                                                         'available -',
  #                                                   'sv': 'Undervisningsområdet'},
  #                                  'Beskrivning': {},
  #                                  'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                                          'link': []},
  #                                  'ID': '133252',
  #                                  'Kod': 'LU',
  #                                  'LarosateID': 29,
  #                                  'link': []},
  #                              {   'Benamning': {   'en': 'Distance learning',
  #                                                   'sv': 'Distans'},
  #                                  'Beskrivning': {   'sv': 'Obligatoriska '
  #                                                           'träffar kan '
  #                                                           'förekomma'},
  #                                  'Giltighetsperiod': {'link': []},
  #                                  'ID': '2',
  #                                  'Kod': 'DST',
  #                                  'LarosateID': -1,
  #                                  'link': []},
  #                              {   'Benamning': {   'en': 'No teaching',
  #                                                   'sv': 'Ingen undervisning'},
  #                                  'Beskrivning': {},
  #                                  'Giltighetsperiod': {   'Slutdatum': '2016-04-30',
  #                                                          'link': []},
  #                                  'ID': '4',
  #                                  'Kod': 'ING',
  #                                  'LarosateID': -1,
  #                                  'link': []},
  #                              {   'Benamning': {   'en': 'Web-based distance '
  #                                                         'learning',
  #                                                   'sv': 'IT-baserad '
  #                                                         'distansutbildning'},
  #                                  'Beskrivning': {   'sv': 'Ingen platsbunden '
  #                                                           'undervisning'},
  #                                  'Giltighetsperiod': {   'Slutdatum': '2016-04-30',
  #                                                          'link': []},
  #                                  'ID': '3',
  #                                  'Kod': 'ITD',
  #                                  'LarosateID': -1,
  #                                  'link': []},
  #                              {   'Benamning': {   'en': 'Normal teaching',
  #                                                   'sv': 'Normal'},
  #                                  'Beskrivning': {},
  #                                  'Giltighetsperiod': {'link': []},
  #                                  'ID': '1',
  #                                  'Kod': 'NML',
  #                                  'LarosateID': -1,
  #                                  'link': []}],
  #     'link': []}
  # added by GQMJr
  #####################################################################
  #
  # LokalaPerioder_JSON
  #
  # RETURNERAR JSON of local periods
  def LokalaPerioder_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url + '/kataloginformation/grunddata/period',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Period': [
  #...
  #                {   'Benamning': {   'en': 'Calendar year 2020',
  #                                    'sv': 'Kalenderår 2020'},
  #                   'Beskrivning': {},
  #                   'FromDatum': '2020-01-01',
  #                   'Giltighetsperiod': {   'Slutdatum': '2020-12-31',
  #                                           'Startdatum': '2020-01-01',
  #                                           'link': []},
  #                   'ID': '29151',
  #                   'Kod': '2020',
  #                   'LarosateID': 29,
  #                   'PeriodtypID': 1,
  #                   'TomDatum': '2020-12-31',
  #                   'link': []},
  #               {   'Benamning': {   'en': 'Last six months of 2020',
  #                                    'sv': 'Andra halvår 2020'},
  #                   'Beskrivning': {},
  #                   'FromDatum': '2020-07-01',
  #                   'Giltighetsperiod': {   'Slutdatum': '2020-12-31',
  #                                           'Startdatum': '2020-07-01',
  #                                           'link': []},
  #                   'ID': '29252',
  #                   'Kod': '2020H',
  #                   'LarosateID': 29,
  #                   'PeriodtypID': 3,
  #                   'TomDatum': '2020-12-31',
  #                   'link': []},
  #               {   'Benamning': {   'en': 'First six months of 2020',
  #                                    'sv': 'Första halvår 2020'},
  #                   'Beskrivning': {},
  #                   'FromDatum': '2020-01-01',
  #                   'Giltighetsperiod': {   'Slutdatum': '2020-06-30',
  #                                           'Startdatum': '2020-01-01',
  #                                           'link': []},
  #                   'ID': '29324',
  #                   'Kod': '2020V',
  #                   'LarosateID': 29,
  #                   'PeriodtypID': 3,
  #                   'TomDatum': '2020-06-30',
  #                   'link': []},
  #...
  # 'link': []}
  # added by GQMJr
  #####################################################################
  #
  # nivainomstudieordning_JSON
  #
  # RETURNERAR JSON of education levels
  def nivainomstudieordning_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/nivainomstudieordning',
      headers=self.headers).json()
    return r

  # returns:
  # {   'NivaInomStudieordning': [   {   'Benamning': {   'en': 'First cycle',
  #                                                       'sv': 'Grundnivå'},
  #                                      'Beskrivning': {},
  #                                      'Giltighetsperiod': {   'Startdatum': '2007-07-01', 'link': []},
  #                                      'ID': '1',
  #                                      'Kod': '1',
  #                                      'LarosateID': -1,
  #                                      'link': []},
  #                                  {   'Benamning': {   'en': 'Second cycle',
  #                                                       'sv': 'Avancerad nivå'},
  #                                      'Beskrivning': {},
  #                                      'Giltighetsperiod': {   'Startdatum': '2007-07-01', 'link': []},
  #                                      'ID': '2',
  #                                      'Kod': '2',
  #                                      'LarosateID': -1,
  #                                      'link': []},
  #                                  {   'Benamning': {   'en': 'Third cycle',
  #                                                       'sv': 'Forskarnivå'},
  #                                      'Beskrivning': {},
  #                                      'Giltighetsperiod': {   'Startdatum': '2007-07-01', 'link': []},
  #                                      'ID': '3',
  #                                      'Kod': '3',
  #                                      'LarosateID': -1,
  #                                      'link': []},
  #                                  {   'Benamning': {   'en': 'Postgraduate '
  #                                                             'level',
  #                                                       'sv': 'Forskarutbildning'},
  #                                      'Beskrivning': {},
  #                                      'Giltighetsperiod': {   'Slutdatum': '2007-06-30',
  #                                                              'Startdatum': '1977-07-01', 'link': []},
  #                                      'ID': '5',
  #                                      'Kod': 'F',
  #                                      'LarosateID': -1,
  #                                      'link': []},
  #                                  {   'Benamning': {   'en': 'Undergraduate '
  #                                                             'level',
  #                                                       'sv': 'Grundutbildning'},
  #                                      'Beskrivning': {},
  #                                      'Giltighetsperiod': {   'Slutdatum': '2007-06-30',
  #                                                              'Startdatum': '1977-07-01', 'link': []},
  #                                      'ID': '4',
  #                                      'Kod': 'G',
  #                                      'LarosateID': -1,
  #                                      'link': []}],
  #     'link': []}
  # added by GQMJr
  #####################################################################
  #
  # amnesgrupp_JSON
  #
  # RETURNERAR JSON of subject area groups
  def amnesgrupp_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url + '/kataloginformation/grunddata/amnesgrupp',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Amnesgrupp': [   {   'Benamning': {   'en': 'Archival Science',
  #                                            'sv': 'Arkivvetenskap'},
  #                           'Beskrivning': {},
  #                           'Giltighetsperiod': {'link': []},
  #                           'ID': '10',
  #                           'Kod': 'AV1',
  #                           'LarosateID': -1,
  #                           'link': []},
  # ...
  #                       {   'Benamning': {'en': 'Philosophy', 'sv': 'Filosofi'},
  #                           'Beskrivning': {},
  #                           'Giltighetsperiod': {'link': []},
  #                           'ID': '42',
  #                           'Kod': 'FI2',
  #                           'LarosateID': -1,
  #                           'link': []},
  # ...
  #                       {   'Benamning': {   'en': 'Informatics/Computer and '
  #                                                  'Systems Sciences',
  #                                            'sv': 'Informatik/data- och '
  #                                                  'systemvetenskap'},
  #                           'Beskrivning': {},
  #                           'Giltighetsperiod': {'link': []},
  #                           'ID': '68',
  #                           'Kod': 'IF1',
  #                           'LarosateID': -1,
  #                           'link': []},
  # ...
  #                       {   'Benamning': {   'en': 'Electronics',
  #                                            'sv': 'Elektronik'},
  #                           'Beskrivning': {},
  #                           'Giltighetsperiod': {'link': []},
  #                           'ID': '30',
  #                           'Kod': 'EL1',
  #                           'LarosateID': -1,
  #                           'link': []},
  # ... ],
  #     'link': []}
  # added by GQMJr
  #####################################################################
  #
  # studietakt_JSON
  #
  # RETURNERAR JSON of study tempos
  def studietakt_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url + '/kataloginformation/grunddata/studietakt',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Studietakt': [   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Noll'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133268',
  #                       'Kod': '0',
  #                       'LarosateID': 29,
  #                       'Takt': 0,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133270',
  #                       'Kod': '1',
  #                       'LarosateID': 29,
  #                       'Takt': 1,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133282',
  #                       'Kod': '11',
  #                       'LarosateID': 29,
  #                       'Takt': 11,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133281',
  #                       'Kod': '13',
  #                       'LarosateID': 29,
  #                       'Takt': 13,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133278',
  #                       'Kod': '14',
  #                       'LarosateID': 29,
  #                       'Takt': 14,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133283',
  #                       'Kod': '15',
  #                       'LarosateID': 29,
  #                       'Takt': 15,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133280',
  #                       'Kod': '16',
  #                       'LarosateID': 29,
  #                       'Takt': 16,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133289',
  #                       'Kod': '18',
  #                       'LarosateID': 29,
  #                       'Takt': 18,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133279',
  #                       'Kod': '19',
  #                       'LarosateID': 29,
  #                       'Takt': 19,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133271',
  #                       'Kod': '2',
  #                       'LarosateID': 29,
  #                       'Takt': 2,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133285',
  #                       'Kod': '20',
  #                       'LarosateID': 29,
  #                       'Takt': 20,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133287',
  #                       'Kod': '21',
  #                       'LarosateID': 29,
  #                       'Takt': 21,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133290',
  #                       'Kod': '22',
  #                       'LarosateID': 29,
  #                       'Takt': 22,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133284',
  #                       'Kod': '23',
  #                       'LarosateID': 29,
  #                       'Takt': 23,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133286',
  #                       'Kod': '24',
  #                       'LarosateID': 29,
  #                       'Takt': 24,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133288',
  #                       'Kod': '26',
  #                       'LarosateID': 29,
  #                       'Takt': 26,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133291',
  #                       'Kod': '27',
  #                       'LarosateID': 29,
  #                       'Takt': 27,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133292',
  #                       'Kod': '28',
  #                       'LarosateID': 29,
  #                       'Takt': 28,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133294',
  #                       'Kod': '29',
  #                       'LarosateID': 29,
  #                       'Takt': 29,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133274',
  #                       'Kod': '3',
  #                       'LarosateID': 29,
  #                       'Takt': 3,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133293',
  #                       'Kod': '30',
  #                       'LarosateID': 29,
  #                       'Takt': 30,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133296',
  #                       'Kod': '31',
  #                       'LarosateID': 29,
  #                       'Takt': 31,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133295',
  #                       'Kod': '32',
  #                       'LarosateID': 29,
  #                       'Takt': 32,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133299',
  #                       'Kod': '34',
  #                       'LarosateID': 29,
  #                       'Takt': 34,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133298',
  #                       'Kod': '35',
  #                       'LarosateID': 29,
  #                       'Takt': 35,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133297',
  #                       'Kod': '36',
  #                       'LarosateID': 29,
  #                       'Takt': 36,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133307',
  #                       'Kod': '37',
  #                       'LarosateID': 29,
  #                       'Takt': 37,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133303',
  #                       'Kod': '38',
  #                       'LarosateID': 29,
  #                       'Takt': 38,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133300',
  #                       'Kod': '39',
  #                       'LarosateID': 29,
  #                       'Takt': 39,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133269',
  #                       'Kod': '4',
  #                       'LarosateID': 29,
  #                       'Takt': 4,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133302',
  #                       'Kod': '40',
  #                       'LarosateID': 29,
  #                       'Takt': 40,
  #                       'link': []},
  #                   {   'Benamning': {   'en': 'One-tenth-time',
  #                                        'sv': 'Tiondelsfart'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {'link': []},
  #                       'ID': '8',
  #                       'Kod': '10',
  #                       'LarosateID': -1,
  #                       'Takt': 10,
  #                       'link': []},
  #                   {   'Benamning': {'en': 'Full-time', 'sv': 'Helfart'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {'link': []},
  #                       'ID': '1',
  #                       'Kod': '100',
  #                       'LarosateID': -1,
  #                       'Takt': 100,
  #                       'link': []},
  #                   {   'Benamning': {   'en': 'One-eight-time',
  #                                        'sv': 'Åttondelsfart'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {'link': []},
  #                       'ID': '128190',
  #                       'Kod': '12',
  #                       'LarosateID': -1,
  #                       'Takt': 12,
  #                       'link': []},
  #                   {   'Benamning': {   'en': 'One-sixth-time',
  #                                        'sv': 'Sjättedelsfart'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {'link': []},
  #                       'ID': '7',
  #                       'Kod': '17',
  #                       'LarosateID': -1,
  #                       'Takt': 17,
  #                       'link': []},
  #                   {   'Benamning': {   'en': 'One-quarter-time',
  #                                        'sv': 'Kvartsfart'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {'link': []},
  #                       'ID': '6',
  #                       'Kod': '25',
  #                       'LarosateID': -1,
  #                       'Takt': 25,
  #                       'link': []},
  #                   {   'Benamning': {   'en': 'One-third-time',
  #                                        'sv': 'Tredjedelsfart'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {'link': []},
  #                       'ID': '5',
  #                       'Kod': '33',
  #                       'LarosateID': -1,
  #                       'Takt': 33,
  #                       'link': []},
  #                   {   'Benamning': {'en': 'Half-time', 'sv': 'Halvfart'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {'link': []},
  #                       'ID': '4',
  #                       'Kod': '50',
  #                       'LarosateID': -1,
  #                       'Takt': 50,
  #                       'link': []},
  #                   {   'Benamning': {   'en': 'Two-thirds-time',
  #                                        'sv': 'Tvåtredjedelsfart'},
  #                       'Beskrivning': {   'sv': 'Ändras till '
  #                                                '"Tvåtredjedelsfart" efter '
  #                                                'fullbordad '
  #                                                'produktionssättning.'},
  #                       'Giltighetsperiod': {'link': []},
  #                       'ID': '3',
  #                       'Kod': '67',
  #                       'LarosateID': -1,
  #                       'Takt': 67,
  #                       'link': []},
  #                   {   'Benamning': {   'en': 'Three-quarters-time',
  #                                        'sv': 'Trekvartsfart'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {'link': []},
  #                       'ID': '2',
  #                       'Kod': '75',
  #                       'LarosateID': -1,
  #                       'Takt': 75,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133304',
  #                       'Kod': '41',
  #                       'LarosateID': 29,
  #                       'Takt': 41,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133305',
  #                       'Kod': '42',
  #                       'LarosateID': 29,
  #                       'Takt': 42,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133301',
  #                       'Kod': '43',
  #                       'LarosateID': 29,
  #                       'Takt': 43,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133312',
  #                       'Kod': '44',
  #                       'LarosateID': 29,
  #                       'Takt': 44,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133308',
  #                       'Kod': '45',
  #                       'LarosateID': 29,
  #                       'Takt': 45,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133306',
  #                       'Kod': '46',
  #                       'LarosateID': 29,
  #                       'Takt': 46,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133310',
  #                       'Kod': '47',
  #                       'LarosateID': 29,
  #                       'Takt': 47,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133309',
  #                       'Kod': '48',
  #                       'LarosateID': 29,
  #                       'Takt': 48,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133311',
  #                       'Kod': '49',
  #                       'LarosateID': 29,
  #                       'Takt': 49,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133276',
  #                       'Kod': '5',
  #                       'LarosateID': 29,
  #                       'Takt': 5,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133318',
  #                       'Kod': '51',
  #                       'LarosateID': 29,
  #                       'Takt': 51,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133315',
  #                       'Kod': '52',
  #                       'LarosateID': 29,
  #                       'Takt': 52,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133314',
  #                       'Kod': '53',
  #                       'LarosateID': 29,
  #                       'Takt': 53,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133313',
  #                       'Kod': '54',
  #                       'LarosateID': 29,
  #                       'Takt': 54,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133316',
  #                       'Kod': '55',
  #                       'LarosateID': 29,
  #                       'Takt': 55,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133319',
  #                       'Kod': '56',
  #                       'LarosateID': 29,
  #                       'Takt': 56,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133317',
  #                       'Kod': '57',
  #                       'LarosateID': 29,
  #                       'Takt': 57,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133320',
  #                       'Kod': '58',
  #                       'LarosateID': 29,
  #                       'Takt': 58,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133322',
  #                       'Kod': '59',
  #                       'LarosateID': 29,
  #                       'Takt': 59,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133272',
  #                       'Kod': '6',
  #                       'LarosateID': 29,
  #                       'Takt': 6,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133323',
  #                       'Kod': '60',
  #                       'LarosateID': 29,
  #                       'Takt': 60,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133321',
  #                       'Kod': '61',
  #                       'LarosateID': 29,
  #                       'Takt': 61,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133332',
  #                       'Kod': '62',
  #                       'LarosateID': 29,
  #                       'Takt': 62,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133331',
  #                       'Kod': '63',
  #                       'LarosateID': 29,
  #                       'Takt': 63,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133325',
  #                       'Kod': '64',
  #                       'LarosateID': 29,
  #                       'Takt': 64,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133324',
  #                       'Kod': '65',
  #                       'LarosateID': 29,
  #                       'Takt': 65,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133327',
  #                       'Kod': '66',
  #                       'LarosateID': 29,
  #                       'Takt': 66,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133328',
  #                       'Kod': '68',
  #                       'LarosateID': 29,
  #                       'Takt': 68,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133329',
  #                       'Kod': '69',
  #                       'LarosateID': 29,
  #                       'Takt': 69,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133277',
  #                       'Kod': '7',
  #                       'LarosateID': 29,
  #                       'Takt': 7,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133330',
  #                       'Kod': '70',
  #                       'LarosateID': 29,
  #                       'Takt': 70,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133326',
  #                       'Kod': '71',
  #                       'LarosateID': 29,
  #                       'Takt': 71,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Halvtid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133333',
  #                       'Kod': '72',
  #                       'LarosateID': 29,
  #                       'Takt': 72,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133334',
  #                       'Kod': '73',
  #                       'LarosateID': 29,
  #                       'Takt': 73,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133342',
  #                       'Kod': '74',
  #                       'LarosateID': 29,
  #                       'Takt': 74,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133335',
  #                       'Kod': '76',
  #                       'LarosateID': 29,
  #                       'Takt': 76,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133347',
  #                       'Kod': '77',
  #                       'LarosateID': 29,
  #                       'Takt': 77,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133339',
  #                       'Kod': '78',
  #                       'LarosateID': 29,
  #                       'Takt': 78,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133338',
  #                       'Kod': '79',
  #                       'LarosateID': 29,
  #                       'Takt': 79,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133275',
  #                       'Kod': '8',
  #                       'LarosateID': 29,
  #                       'Takt': 8,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133337',
  #                       'Kod': '80',
  #                       'LarosateID': 29,
  #                       'Takt': 80,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133336',
  #                       'Kod': '81',
  #                       'LarosateID': 29,
  #                       'Takt': 81,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133340',
  #                       'Kod': '82',
  #                       'LarosateID': 29,
  #                       'Takt': 82,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133345',
  #                       'Kod': '83',
  #                       'LarosateID': 29,
  #                       'Takt': 83,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133341',
  #                       'Kod': '84',
  #                       'LarosateID': 29,
  #                       'Takt': 84,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133343',
  #                       'Kod': '85',
  #                       'LarosateID': 29,
  #                       'Takt': 85,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133344',
  #                       'Kod': '86',
  #                       'LarosateID': 29,
  #                       'Takt': 86,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133346',
  #                       'Kod': '87',
  #                       'LarosateID': 29,
  #                       'Takt': 87,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133348',
  #                       'Kod': '88',
  #                       'LarosateID': 29,
  #                       'Takt': 88,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133349',
  #                       'Kod': '89',
  #                       'LarosateID': 29,
  #                       'Takt': 89,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Kvartstid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133273',
  #                       'Kod': '9',
  #                       'LarosateID': 29,
  #                       'Takt': 9,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133350',
  #                       'Kod': '90',
  #                       'LarosateID': 29,
  #                       'Takt': 90,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133352',
  #                       'Kod': '91',
  #                       'LarosateID': 29,
  #                       'Takt': 91,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133358',
  #                       'Kod': '92',
  #                       'LarosateID': 29,
  #                       'Takt': 92,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133353',
  #                       'Kod': '93',
  #                       'LarosateID': 29,
  #                       'Takt': 93,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133354',
  #                       'Kod': '94',
  #                       'LarosateID': 29,
  #                       'Takt': 94,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133351',
  #                       'Kod': '95',
  #                       'LarosateID': 29,
  #                       'Takt': 95,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133355',
  #                       'Kod': '96',
  #                       'LarosateID': 29,
  #                       'Takt': 96,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133357',
  #                       'Kod': '97',
  #                       'LarosateID': 29,
  #                       'Takt': 97,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133356',
  #                       'Kod': '98',
  #                       'LarosateID': 29,
  #                       'Takt': 98,
  #                       'link': []},
  #                   {   'Benamning': {   'en': '- No translation available -',
  #                                        'sv': 'Nästan heltid'},
  #                       'Beskrivning': {},
  #                       'Giltighetsperiod': {   'Slutdatum': '2018-06-19',
  #                                               'link': []},
  #                       'ID': '133359',
  #                       'Kod': '99',
  #                       'LarosateID': 29,
  #                       'Takt': 99,
  #                       'link': []}],
  # 'link': []}
  # added by GQMJr
  #####################################################################
  #
  # finansieringsform_JSON
  #
  # RETURNERAR JSON forms of financing
  def finansieringsform_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/finansieringsform',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Finansieringsform': [   {   'Benamning': {   'en': '- No translation '
  #                                                     'available -',
  #                                               'sv': 'Alumn, med examen fr '
  #                                                     'KTH (ej HST-HPR)'},
  #                              'Beskrivning': {},
  #                              'Giltighetsperiod': {'link': []},
  #                              'ID': '131704',
  #                              'Kod': 'ALU',
  #                              'LarosateID': 29,
  #                              'link': []},
  #                          {   'Benamning': {   'en': '- No translation '
  # ...
  # added by GQMJr
  #####################################################################
  #
  # utbildningsomrade_JSON
  #
  # RETURNERAR JSON of subjects
  def utbildningsomrade_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/utbildningsomrade',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Utbildningsomrade': [   {   'Benamning': {   'en': 'Dance',
  #                                               'sv': 'Dansområdet'},
  #                              'Beskrivning': {   'sv': 'Infördes från '
  #                                                       'budgetåret 1994/95. '
  #                                                       'Tidigare fanns bara '
  #                                                       'ett konstnärligt '
  #                                                       'utbildningsområde '
  #                                                       '(vars '
  #                                                       'ersättningsbelopp '
  #                                                       'varierade mellan '
  #                                                       'lärosätena).'},
  #                              'Giltighetsperiod': {   'Startdatum': '1994-07-01',
  #                                                      'link': []},
  #                              'ID': '1',
  #                              'Kod': 'DA',
  #                              'LarosateID': -1,
  #                              'link': []},
  # ...
  #                          {   'Benamning': {   'en': 'Education',
  #                                               'sv': 'Undervisningsområdet'},
  #                              'Beskrivning': {   'sv': 'Avser utbildning '
  #                                                       'inom det allmänna '
  #                                                       'utbildningsområdet '
  #                                                       'och den '
  #                                                       'utbildningsvetenskapliga '
  #                                                       'kärnan. T.o.m. '
  #                                                       '2012-12-31 avsågs '
  #                                                       'även övrig '
  #                                                       'verksamhetsförlagd '
  #                                                       'utbildning (se '
  #                                                       'VU).'},
  #                              'Giltighetsperiod': {   'Startdatum': '1993-07-01',
  #                                                      'link': []},
  #                              'ID': '9',
  #                              'Kod': 'LU',
  #                              'LarosateID': -1,
  #                              'link': []},
  # ...
  #                          {   'Benamning': {   'en': 'Natural sciences',
  #                                               'sv': 'Naturvetenskapliga '
  #                                                     'området'},
  #                              'Beskrivning': {},
  #                              'Giltighetsperiod': {   'Startdatum': '1993-07-01',
  #                                                      'link': []},
  #                              'ID': '13',
  #                              'Kod': 'NA',
  #                              'LarosateID': -1,
  #                              'link': []},
  # ...
  #                          {   'Benamning': {   'en': 'Technology',
  #                                               'sv': 'Tekniska området'},
  #                              'Beskrivning': {},
  #                              'Giltighetsperiod': {   'Startdatum': '1993-07-01',
  #                                                      'link': []},
  #                              'ID': '19',
  #                              'Kod': 'TE',
  #                              'LarosateID': -1,
  #                              'link': []},
  # ... ],
  # 'link': []}
  # added by GQMJr
  #####################################################################
  #
  # kravpatidigarestudier_JSON
  #
  # RETURNERAR JSON of krequirements for earlier studies
  def kravpatidigarestudier_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/kravpatidigarestudier',
      headers=self.headers).json()
    return r

  # returns
  # {   'KravPaTidigareStudier': [   {   'Benamning': {   'en': 'University '
  #                                                         'studies required',
  #                                                   'sv': 'Tidigare '
  #                                                         'högskolestudier '
  #                                                         'krävs'},
  #                                  'Beskrivning': {},
  #                                  'Emilvarde': 'uh',
  #                                  'Giltighetsperiod': {'link': []},
  #                                  'ID': '1',
  #                                  'Kod': 'UH',
  #                                  'LarosateID': -1,
  #                                  'link': []},
  #                              {   'Benamning': {   'en': 'Upper secondary '
  #                                                         'or equivalent',
  #                                                   'sv': 'Inga tidigare '
  #                                                         'högskolestudier '
  #                                                         'krävs'},
  #                                  'Beskrivning': {},
  #                                  'Emilvarde': 'grundlaggande',
  #                                  'Giltighetsperiod': {'link': []},
  #                                  'ID': '2',
  #                                  'Kod': 'GR',
  #                                  'LarosateID': -1,
  #                                  'link': []},
  #                              {   'Benamning': {   'en': 'No general entry '
  #                                                         'requirements '
  #                                                         'needed',
  #                                                   'sv': 'Ingen '
  #                                                         'grundläggande '
  #                                                         'behörighet krävs'},
  #                                  'Beskrivning': {},
  #                                  'Emilvarde': 'inga',
  #                                  'Giltighetsperiod': {'link': []},
  #                                  'ID': '3',
  #                                  'Kod': 'IN',
  #                                  'LarosateID': -1,
  #                                  'link': []}],
  # 'link': []}
  # added by GQMJr
  #####################################################################
  #
  # studieordning_JSON
  #
  # RETURNERAR JSON of study regulation
  def studieordning_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/studieordning',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Studieordning': [   {   'Benamning': {   'en': 'Higher education, study '
  #                                                     'regulation of 1993',
  #                                               'sv': 'Högskoleutbildning, 1993 '
  #                                                     'års studieordning'},
  #                              'Beskrivning': {   'sv': 'Avser i Ladok 1993 års '
  #                                                       'studieordning inklusive '
  #                                                       'dess föregångare'},
  #                              'EnhetID': 9,
  #                              'Giltighetsperiod': {'link': []},
  #                              'ID': '2',
  #                              'Kod': 'HÖ93',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 1,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Higher education, study '
  #                                                     'regulation of 2007',
  #                                               'sv': 'Högskoleutbildning, 2007 '
  #                                                     'års studieordning'},
  #                              'Beskrivning': {},
  #                              'EnhetID': 2,
  #                              'Giltighetsperiod': {   'Startdatum': '2007-07-01',
  #                                                      'link': []},
  #                              'ID': '1',
  #                              'Kod': 'HÖ07',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 1,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Access education (hours)',
  #                                               'sv': 'Behörighetsgivande '
  #                                                     'förutbildning (timmar)'},
  #                              'Beskrivning': {},
  #                              'EnhetID': 5,
  #                              'Giltighetsperiod': {'link': []},
  #                              'ID': '12',
  #                              'Kod': 'ÖVBT',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100970,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Access education (fup)',
  #                                               'sv': 'Behörighetsgivande '
  #                                                     'förutbildning (poäng)'},
  #                              'Beskrivning': {   'sv': 'Utbildning enligt '
  #                                                       'förordning (2018:1519) '
  #                                                       'om behörighetsgivande '
  #                                                       'och '
  #                                                       'högskoleintroducerande '
  #                                                       'utbildning resp. '
  #                                                       'tidigare gällande '
  #                                                       'förordning (2007:432) '
  #                                                       'om behörighetsgivande '
  #                                                       'förutbildning vid '
  #                                                       'universitet och '
  #                                                       'högskolor'},
  #                              'EnhetID': 4,
  #                              'Giltighetsperiod': {'link': []},
  #                              'ID': '3',
  #                              'Kod': 'FÖPO',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 2,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Access education (weeks)',
  #                                               'sv': 'Behörighetsgivande '
  #                                                     'förutbildning (veckor)'},
  #                              'Beskrivning': {   'sv': 'Utbildning enligt '
  #                                                       'förordning (2018:1519) '
  #                                                       'om behörighetsgivande '
  #                                                       'och '
  #                                                       'högskoleintroducerande '
  #                                                       'utbildning resp. '
  #                                                       'tidigare gällande '
  #                                                       'förordning (2007:432) '
  #                                                       'om behörighetsgivande '
  #                                                       'förutbildning vid '
  #                                                       'universitet och '
  #                                                       'högskolor'},
  #                              'EnhetID': 1,
  #                              'Giltighetsperiod': {'link': []},
  #                              'ID': '4',
  #                              'Kod': 'FÖVE',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 2,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Internal education (ORU)',
  #                                               'sv': 'Högskoleintern utbildning '
  #                                                     '(ORU)'},
  #                              'Beskrivning': {   'sv': 'Intern utbildning vid '
  #                                                       'Örebro universitet'},
  #                              'EnhetID': 6,
  #                              'Giltighetsperiod': {   'Slutdatum': '2007-06-30',
  #                                                      'Startdatum': '2004-01-01',
  #                                                      'link': []},
  #                              'ID': '15',
  #                              'Kod': 'ÖVHI',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100970,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Older defence education',
  #                                               'sv': 'Äldre utbildning vid '
  #                                                     'Försvarshögskolan'},
  #                              'Beskrivning': {   'sv': 'Utbildning enligt '
  #                                                       'förordningen '
  #                                                       '(1996:1476) med '
  #                                                       'instruktion för '
  #                                                       'Försvarshögskolan'},
  #                              'EnhetID': 10,
  #                              'Giltighetsperiod': {   'Slutdatum': '2007-12-31',
  #                                                      'link': []},
  #                              'ID': '16',
  #                              'Kod': 'ÖVFU',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100970,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Post-secondary vocational '
  #                                                     'education and training',
  #                                               'sv': 'Kvalificerad '
  #                                                     'yrkesutbildning'},
  #                              'Beskrivning': {   'sv': 'Utbildning enligt '
  #                                                       'förordningen '
  #                                                       '(2001:1131) om '
  #                                                       'kvalificerad '
  #                                                       'yrkesutbildning '
  #                                                       '(upphävd 2009-04-15)'},
  #                              'EnhetID': 7,
  #                              'Giltighetsperiod': {   'Slutdatum': '2013-12-31',
  #                                                      'link': []},
  #                              'ID': '13',
  #                              'Kod': 'KY02',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100968,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Preparatory education',
  #                                               'sv': 'Preparandutbildning'},
  #                              'Beskrivning': {   'sv': 'Utbildning enligt '
  #                                                       'förordningen (1985:681) '
  #                                                       'om preparandutbildning '
  #                                                       'i svenska (upphävd '
  #                                                       '1993-07-01)'},
  #                              'EnhetID': 6,
  #                              'Giltighetsperiod': {   'Slutdatum': '1993-06-30',
  #                                                      'link': []},
  #                              'ID': '14',
  #                              'Kod': 'ÖVPR',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100970,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Contract education '
  #                                                     '(hours)',
  #                                               'sv': 'Uppdragsutbildning, Övrig '
  #                                                     'utbildning (timmar)'},
  #                              'Beskrivning': {},
  #                              'EnhetID': 5,
  #                              'Giltighetsperiod': {   'Slutdatum': '2018-12-31',
  #                                                      'link': []},
  #                              'ID': '9',
  #                              'Kod': 'ÖVUT',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100970,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Higher vocational '
  #                                                     'education',
  #                                               'sv': 'Yrkeshögskoleutbildning'},
  #                              'Beskrivning': {   'sv': 'Utbildning enligt '
  #                                                       'förordning (2009:130) '
  #                                                       'om yrkeshögskolan'},
  #                              'EnhetID': 8,
  #                              'Giltighetsperiod': {   'Startdatum': '2009-07-01',
  #                                                      'link': []},
  #                              'ID': '5',
  #                              'Kod': 'YH09',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 4,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Contract education '
  #                                                     '(credits)',
  #                                               'sv': 'Uppdragsutbildning '
  #                                                     '(högskolepoäng)'},
  #                              'Beskrivning': {},
  #                              'EnhetID': 2,
  #                              'Giltighetsperiod': {   'Startdatum': '2007-07-01',
  #                                                      'link': []},
  #                              'ID': '17',
  #                              'Kod': 'UPHP',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100928,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Contract education '
  #                                                     '(weeks)',
  #                                               'sv': 'Uppdragsutbildning '
  #                                                     '(veckor)'},
  #                              'Beskrivning': {},
  #                              'EnhetID': 1,
  #                              'Giltighetsperiod': {'link': []},
  #                              'ID': '18',
  #                              'Kod': 'UPVE',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100928,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Police education',
  #                                               'sv': 'Polisutbildning'},
  #                              'Beskrivning': {   'sv': 'Polisutbildning som ej '
  #                                                       'uppfyller alla '
  #                                                       'kvalitetskrav för '
  #                                                       'högskoleutbildning.'},
  #                              'EnhetID': 2,
  #                              'Giltighetsperiod': {'link': []},
  #                              'ID': '109831',
  #                              'Kod': 'PU99',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100969,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Police education, equal '
  #                                                     'to Higher education',
  #                                               'sv': 'Polisutbildning, '
  #                                                     'motsvarande '
  #                                                     'högskoleutbildning'},
  #                              'Beskrivning': {   'sv': 'Polisutbildning som '
  #                                                       'uppfyller '
  #                                                       'kvalitetskraven för '
  #                                                       'högskoleutbildning'},
  #                              'EnhetID': 2,
  #                              'Giltighetsperiod': {   'Startdatum': '2018-07-01',
  #                                                      'link': []},
  #                              'ID': '135370',
  #                              'Kod': 'PU18',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100969,
  #                              'link': []},
  #                          {   'Benamning': {'en': 'Ö-Fel', 'sv': 'Ö-Fel'},
  #                              'Beskrivning': {},
  #                              'EnhetID': 1,
  #                              'Giltighetsperiod': {   'Slutdatum': '1900-01-01',
  #                                                      'link': []},
  #                              'ID': '138710',
  #                              'Kod': 'FEL',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100970,
  #                              'link': []},
  #                          {   'Benamning': {   'en': 'Contract education '
  #                                                     '(hours)',
  #                                               'sv': 'Uppdragsutbildning '
  #                                                     '(timmar)'},
  #                              'Beskrivning': {},
  #                              'EnhetID': 5,
  #                              'Giltighetsperiod': {   'Startdatum': '2019-01-01',
  #                                                      'link': []},
  #                              'ID': '147898',
  #                              'Kod': 'UPTI',
  #                              'LarosateID': -1,
  #                              'UtbildningsformID': 100928,
  #                              'link': []}],
  #     'link': []}
  # added by GQMJr
  #####################################################################
  #
  # enhet_JSON
  #
  # RETURNERAR JSON of units
  def enhet_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url + '/kataloginformation/grunddata/enhet',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Enhet': [   {   'Benamning': {   'en': 'Credit points',
  #                                   'sv': 'Poäng (Övrig utbildning)'},
  #                  'Beskrivning': {},
  #                  'Giltighetsperiod': {   'Slutdatum': '2018-01-01',
  #                                          'link': []},
  #                  'Helarsvarde': 40,
  #                  'ID': '6',
  #                  'Kod': 'AUP',
  #                  'LarosateID': -1,
  #                  'link': []},
  #              {   'Benamning': {   'en': 'Pre-education credits',
  #                                   'sv': 'Förutbildningspoäng'},
  #                  'Beskrivning': {},
  #                  'Giltighetsperiod': {'link': []},
  #                  'Helarsvarde': 60,
  #                  'ID': '4',
  #                  'Kod': 'FUP',
  #                  'LarosateID': -1,
  #                  'link': []},
  #              {   'Benamning': {'en': 'Credits', 'sv': 'Högskolepoäng'},
  #                  'Beskrivning': {   'sv': 'Översattes 2007-2010 med Higher '
  #                                           'education credits'},
  #                  'Giltighetsperiod': {   'Startdatum': '2007-07-01',
  #                                          'link': []},
  #                  'Helarsvarde': 60,
  #                  'ID': '2',
  #                  'Kod': 'HP',
  #                  'LarosateID': -1,
  #                  'link': []},
  #              {   'Benamning': {   'en': 'Converted credits',
  #                                   'sv': 'Konverterade högskolepoäng'},
  #                  'Beskrivning': {   'sv': 'Enheten poäng konverterades '
  #                                           'till högskolepoäng i Ladok för '
  #                                           '1993 års studieordning i '
  #                                           'samband med övergången till '
  #                                           '2007 års studieordning'},
  #                  'Giltighetsperiod': {   'Slutdatum': '2007-06-30',
  #                                          'link': []},
  #                  'Helarsvarde': 60,
  #                  'ID': '9',
  #                  'Kod': 'HP-K',
  #                  'LarosateID': -1,
  #                  'link': []},
  #              {   'Benamning': {   'en': 'Internal credits',
  #                                   'sv': 'Interna poäng'},
  #                  'Beskrivning': {   'sv': 'Har enbart använts av '
  #                                           'Försvarshögskolan'},
  #                  'Giltighetsperiod': {   'Slutdatum': '2016-07-01',
  #                                          'link': []},
  #                  'Helarsvarde': 60,
  #                  'ID': '10',
  #                  'Kod': 'IP',
  #                  'LarosateID': -1,
  #                  'link': []},
  #              {   'Benamning': {'en': 'KY credits', 'sv': 'KY-poäng'},
  #                  'Beskrivning': {},
  #                  'Giltighetsperiod': {   'Slutdatum': '2013-12-31',
  #                                          'Startdatum': '2002-01-01',
  #                                          'link': []},
  #                  'Helarsvarde': 40,
  #                  'ID': '7',
  #                  'Kod': 'KYP',
  #                  'LarosateID': -1,
  #                  'link': []},
  #              {   'Benamning': {'en': 'Hours', 'sv': 'Timmar'},
  #                  'Beskrivning': {},
  #                  'Giltighetsperiod': {'link': []},
  #                  'Helarsvarde': 1600,
  #                  'ID': '5',
  #                  'Kod': 'T',
  #                  'LarosateID': -1,
  #                  'link': []},
  #              {   'Benamning': {'en': 'Weeks', 'sv': 'Veckor'},
  #                  'Beskrivning': {},
  #                  'Giltighetsperiod': {'link': []},
  #                  'Helarsvarde': 40,
  #                  'ID': '1',
  #                  'Kod': 'V',
  #                  'LarosateID': -1,
  #                  'link': []},
  #              {   'Benamning': {   'en': 'HVE credits',
  #                                   'sv': 'Yrkeshögskolepoäng'},
  #                  'Beskrivning': {},
  #                  'Giltighetsperiod': {   'Startdatum': '2009-07-01',
  #                                          'link': []},
  #                  'Helarsvarde': 200,
  #                  'ID': '8',
  #                  'Kod': 'YHP',
  #                  'LarosateID': -1,
  #                  'link': []}],
  # 'link': []}
  # added by GQMJr
  #####################################################################
  #
  # studielokalisering_JSON
  #
  # RETURNERAR JSON of study location
  def studielokalisering_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/studielokalisering',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Studielokalisering': [   {   'Benamning': {   'en': 'Botkyrka',
  #                                                    'sv': 'Botkyrka'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '1997-12-31',
  #                                                           'Startdatum': '1997-08-01',
  #                                                           'link': []},
  #                                   'ID': '131772',
  #                                   'Kod': '0127',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 110990,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/110990'}]},
  #                               {   'Benamning': {   'en': 'Haninge',
  #                                                    'sv': 'Haninge'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '2016-06-30',
  #                                                           'Startdatum': '1994-08-01',
  #                                                           'link': []},
  #                                   'ID': '131773',
  #                                   'Kod': '0136',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 110991,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/110991'}]},
  #                               {   'Benamning': {   'en': 'Nyköping',
  #                                                    'sv': 'Nyköping'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '2005-06-30',
  #                                                           'Startdatum': '2005-01-01',
  #                                                           'link': []},
  #                                   'ID': '131777',
  #                                   'Kod': '0480',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 44,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/44'}]},
  #                               {   'Benamning': {   'en': 'Valdemarsvik',
  #                                                    'sv': 'Valdemarsvik'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '1999-12-31',
  #                                                           'link': []},
  #                                   'ID': '131780',
  #                                   'Kod': '0563',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 60,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/60'}]},
  #                               {   'Benamning': {'en': 'Visby', 'sv': 'Visby'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '2000-12-31',
  #                                                           'Startdatum': '1991-08-01',
  #                                                           'link': []},
  #                                   'ID': '131781',
  #                                   'Kod': '0980',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 108,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/108'}]},
  #                               {   'Benamning': {   'en': 'Ängelholm',
  #                                                    'sv': 'Ängelholm'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '1997-12-31',
  #                                                           'Startdatum': '1997-12-31',
  #                                                           'link': []},
  #                                   'ID': '131782',
  #                                   'Kod': '1292',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 154,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/154'}]},
  #                               {   'Benamning': {'en': 'Falun', 'sv': 'Falun'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '1998-12-31',
  #                                                           'Startdatum': '1994-08-01',
  #                                                           'link': []},
  #                                   'ID': '131787',
  #                                   'Kod': '2080',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 263,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/263'}]},
  #                               {   'Benamning': {'en': 'Gävle', 'sv': 'Gävle'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '1998-12-31',
  #                                                           'Startdatum': '1997-08-01',
  #                                                           'link': []},
  #                                   'ID': '131784',
  #                                   'Kod': '2180',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 273,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/273'}]},
  #                               {   'Benamning': {   'en': 'Stockholm School of '
  #                                                          'Economics',
  #                                                    'sv': 'Handelshögskolan'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Startdatum': '2018-06-20',
  #                                                           'link': []},
  #                                   'ID': '135191',
  #                                   'Kod': 'HANDELS',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 18,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/18'}]},
  #                               {   'Benamning': {   'en': 'KI Flemingsberg',
  #                                                    'sv': 'KI Flemingsberg'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Startdatum': '2018-06-20',
  #                                                           'link': []},
  #                                   'ID': '135192',
  #                                   'Kod': 'KI_FLEMINGS',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 7,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/7'}]},
  #                               {   'Benamning': {   'en': 'University of Arts, '
  #                                                          'Crafts and Design',
  #                                                    'sv': 'Konstfack'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Startdatum': '2018-08-27',
  #                                                           'link': []},
  #                                   'ID': '147750',
  #                                   'Kod': 'KONSTFACK',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 18,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/18'}]},
  #                               {   'Benamning': {   'en': 'KTH Campus',
  #                                                    'sv': 'KTH Campus'},
  #                                   'Beskrivning': {   'sv': '"Campus" '
  #                                                            'Valhallavägen'},
  #                                   'Giltighetsperiod': {   'Startdatum': '2018-06-20',
  #                                                           'link': []},
  #                                   'ID': '135195',
  #                                   'Kod': 'KTHCAMPUS',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 18,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/18'}]},
  #                               {   'Benamning': {'en': 'Täby', 'sv': 'Täby'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '1999-12-31',
  #                                                           'link': []},
  #                                   'ID': '131774',
  #                                   'Kod': '0160',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 14,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/14'}]},
  #                               {   'Benamning': {   'en': 'Stockholm',
  #                                                    'sv': 'Stockholm'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '2019-01-14',
  #                                                           'Startdatum': '1917-10-19',
  #                                                           'link': []},
  #                                   'ID': '131778',
  #                                   'Kod': '0180',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 18,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/18'}]},
  #                               {   'Benamning': {   'en': 'Sundsvall',
  #                                                    'sv': 'Sundsvall'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '1997-12-31',
  #                                                           'Startdatum': '1996-08-01',
  #                                                           'link': []},
  #                                   'ID': '131785',
  #                                   'Kod': '2281',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 281,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/281'}]},
  #                               {   'Benamning': {   'en': 'Örnsköldsvik',
  #                                                    'sv': 'Örnsköldsvik'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '1997-12-31',
  #                                                           'Startdatum': '1997-01-01',
  #                                                           'link': []},
  #                                   'ID': '131788',
  #                                   'Kod': '2284',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 284,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/284'}]},
  #                               {   'Benamning': {   'en': 'KTH Solna',
  #                                                    'sv': 'KTH Solna'},
  #                                   'Beskrivning': {   'en': 'SciLife Labs, '
  #                                                            'Solna',
  #                                                      'sv': 'SciLife Labs, '
  #                                                            'Solna'},
  #                                   'Giltighetsperiod': {   'Startdatum': '2018-06-18',
  #                                                           'link': []},
  #                                   'ID': '135610',
  #                                   'Kod': 'SCILIFELAB',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 25,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/25'}]},
  #                               {   'Benamning': {   'en': 'KTH Södertälje',
  #                                                    'sv': 'KTH Södertälje'},
  #                                   'Beskrivning': {'sv': '"Campus" Södertälje'},
  #                                   'Giltighetsperiod': {   'Startdatum': '2018-06-20',
  #                                                           'link': []},
  #                                   'ID': '135196',
  #                                   'Kod': 'SODERTALJE',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 20,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/20'}]},
  #                               {   'Benamning': {   'en': 'Järfälla',
  #                                                    'sv': 'Järfälla'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '1996-06-30',
  #                                                           'Startdatum': '1994-08-01',
  #                                                           'link': []},
  #                                   'ID': '131775',
  #                                   'Kod': '0123',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 5,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/5'}]},
  #                               {   'Benamning': {   'en': 'Huddinge',
  #                                                    'sv': 'Huddinge'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '2019-01-14',
  #                                                           'Startdatum': '2002-01-01',
  #                                                           'link': []},
  #                                   'ID': '131779',
  #                                   'Kod': '0126',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 109830,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/109830'}]},
  #                               {   'Benamning': {   'en': 'Södertälje',
  #                                                    'sv': 'Södertälje'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '2019-01-14',
  #                                                           'Startdatum': '1987-01-01',
  #                                                           'link': []},
  #                                   'ID': '131771',
  #                                   'Kod': '0181',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 20,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/20'}]},
  #                               {   'Benamning': {   'en': 'Norrtälje',
  #                                                    'sv': 'Norrtälje'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '2005-06-30',
  #                                                           'Startdatum': '1997-08-01',
  #                                                           'link': []},
  #                                   'ID': '131776',
  #                                   'Kod': '0188',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 28,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/28'}]},
  #                               {   'Benamning': {'en': 'Örebro', 'sv': 'Örebro'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '1998-06-30',
  #                                                           'Startdatum': '1996-08-01',
  #                                                           'link': []},
  #                                   'ID': '131786',
  #                                   'Kod': '1880',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 237,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/237'}]},
  #                               {   'Benamning': {   'en': 'Västerås',
  #                                                    'sv': 'Västerås'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Slutdatum': '1999-12-31',
  #                                                           'Startdatum': '1994-08-01',
  #                                                           'link': []},
  #                                   'ID': '131783',
  #                                   'Kod': '1980',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 248,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/248'}]},
  #                               {   'Benamning': {   'en': 'AlbaNova',
  #                                                    'sv': 'AlbaNova'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Startdatum': '2018-06-20',
  #                                                           'link': []},
  #                                   'ID': '135190',
  #                                   'Kod': 'ALBANOVA',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 18,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/18'}]},
  #                               {   'Benamning': {   'en': 'KTH Flemingsberg',
  #                                                    'sv': 'KTH Flemingsberg'},
  #                                   'Beskrivning': {   'sv': '"campus" '
  #                                                            'Flemingsberg'},
  #                                   'Giltighetsperiod': {   'Startdatum': '2018-06-20',
  #                                                           'link': []},
  #                                   'ID': '135198',
  #                                   'Kod': 'FLEMINGSB',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 7,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/7'}]},
  #                               {   'Benamning': {   'en': 'KI Solna',
  #                                                    'sv': 'KI Solna'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Startdatum': '2018-06-20',
  #                                                           'link': []},
  #                                   'ID': '135193',
  #                                   'Kod': 'KI_SOLNA',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 25,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/25'}]},
  #                               {   'Benamning': {   'en': 'KTH Kista',
  #                                                    'sv': 'KTH Kista'},
  #                                   'Beskrivning': {'sv': '"Campus" Kista'},
  #                                   'Giltighetsperiod': {   'Startdatum': '2018-06-20',
  #                                                           'link': []},
  #                                   'ID': '135194',
  #                                   'Kod': 'KISTA',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 18,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/18'}]},
  #                               {   'Benamning': {   'en': 'Stockholm University',
  #                                                    'sv': 'Stockholms '
  #                                                          'universitet'},
  #                                   'Beskrivning': {},
  #                                   'Giltighetsperiod': {   'Startdatum': '2018-06-20',
  #                                                           'link': []},
  #                                   'ID': '135197',
  #                                   'Kod': 'SU',
  #                                   'LarosateID': 29,
  #                                   'OrtID': 18,
  #                                   'link': [   {   'mediaType': 'application/vnd.ladok+xml',
  #                                                   'method': 'GET',
  #                                                   'rel': 'svenskort',
  #                                                   'uri': 'https://api.ladok.se:443/kataloginformation/svenskort/18'}]}],
  #     'link': []}
  # added by GQMJr
  #####################################################################
  #
  # antagningsomgang_JSON
  #
  # RETURNERAR JSON of admission round
  def antagningsomgang_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/antagningsomgang',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Antagningsomgang': [   {   'Benamning': {   'en': 'Application to courses '
  #                                                    'within programme at '
  #                                                    'KTH HT2020',
  #                                              'sv': 'Anmälan till kurs inom '
  #                                                    'program på KTH HT2020'},
  #                             'Beskrivning': {},
  #                             'Giltighetsperiod': {'link': []},
  #                             'ID': '150233',
  #                             'Kod': '29AKPHT20',
  #                             'LarosateID': 29,
  #                             'SistaAnmalningsdag': '2020-05-15',
  #                             'SistaAnnonseringsdag': '2021-05-15',
  #                             'Studieavgiftsbelagd': True,
  #                             'link': []},
  #                         {   'Benamning': {   'en': 'Application to courses '
  #                                                    'within programme at '
  #                                                    'KTH VT2019',
  #                                              'sv': 'Antagning till kurs '
  #                                                    'inom program KTH '
  #                                                    'VT2019'},
  #                             'Beskrivning': {},
  #                             'Giltighetsperiod': {'link': []},
  #                             'ID': '142134',
  #                             'Kod': '29AKPVT19',
  #                             'LarosateID': 29,
  #                             'SistaAnmalningsdag': '2018-11-15',
  #                             'SistaAnnonseringsdag': '2019-02-28',
  #                             'Studieavgiftsbelagd': True,
  #                             'link': []},
  # ... ],
  # 'link': []}
  # added by GQMJr
  #####################################################################
  #
  # organisation_by_uid_JSON
  #
  # organisationUid           -- organization's UID
  #
  # RETURNERAR JSON of selected organization
  def organisation_by_uid_JSON(self, organisationUid):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/organisation/'+organisationUid,
      headers=self.headers).json()
    return r

  # returns:
  # {   'Benamning': {'en': 'EECS/Computer Science', 'sv': 'EECS/Datavetenskap'},
  # 'Giltighetsperiod': {'Startdatum': '2019-01-01', 'link': []},
  # 'Organisationsenhetstyp': 1,
  # 'Organisationskod': 'JH',
  # 'Uid': '2474f616-dc41-11e8-8cc1-eaeeb71b497f',
  # 'link': [   {   'mediaType': 'application/vnd.ladok+xml,application/vnd.ladok-kataloginformation+xml,application/vnd.ladok-kataloginformation+json',
  #                 'method': 'GET',
  #                 'rel': 'self',
  #                 'uri': 'https://api.ladok.se:443/kataloginformation/organisation/2474f616-dc41-11e8-8cc1-eaeeb71b497f'}]}
  # added by GQMJr
  #####################################################################
  #
  # utbildningstyp_JSON
  #
  # RETURNERAR JSON of types of education
  # for information about these see https://ladok.se/wp-content/uploads/2018/01/Funktionsbeskrivning_095.pdf
  def utbildningstyp_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/utbildningstyp',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Utbildningstyp': [   {   'AvserTillfalle': False,
  #                               'Benamning': {   'en': 'Module without scope',
  #                                                'sv': 'Modul utan omfattning'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'Grundtyp': 'MODUL',
  #                               'ID': '3',
  #                               'Kod': '2007MUO',
  #                               'LarosateID': -1,
  #                               'Regelverk': {   'Regelvarden': [   {   'Regelnamn': 'commons.domain.regel.ingar.i.grupp.overfors.till.nya',
  #                                                                       'Uid': 'd31a4080-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'true',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.informationsbehorighet.forskarutbildning',
  #                                                                       'Uid': 'd31a4084-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'true',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.sjalvstandig',
  #                                                                       'Uid': 'd31a4086-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'false',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.informationsbehorighet.grundavancerad',
  #                                                                       'Uid': 'd31a4085-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'true',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.har.omfattning',
  #                                                                       'Uid': 'd31a4082-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'false',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.grupp.for.utsokning',
  #                                                                       'Uid': 'd31a196f-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'grupp.for.utsokning.forskarniva',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.grupp.for.utsokning',
  #                                                                       'Uid': 'd31a4081-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'grupp.for.utsokning.grundavanceradniva',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.versionshanteras',
  #                                                                       'Uid': 'd31a4083-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'false',
  #                                                                       'link': [   ]}],
  #                                                'Uid': '0441f5ba-1b3f-11e6-aff0-464044604cb6',
  #                                                'link': []},
  #                               'Sorteringsordning': 50,
  #                               'StudieordningID': 1,
  #                               'TillfalleInomUtbildningstyper': [],
  #                               'UtbildningstyperInomUtbildningstyp': [],
  #                               'link': []},
  #                           {   'AvserTillfalle': False,
  #                               'Benamning': {'en': 'Module', 'sv': 'Modul'},
  #                               'Beskrivning': {},
  #                               'Giltighetsperiod': {'link': []},
  #                               'Grundtyp': 'MODUL',
  #                               'ID': '4',
  #                               'Kod': '2007MOD',
  #                               'LarosateID': -1,
  #                               'Regelverk': {   'Regelvarden': [   {   'Regelnamn': 'commons.domain.regel.versionshanteras',
  #                                                                       'Uid': 'b18301be-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'false',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.informationsbehorighet.forskarutbildning',
  #                                                                       'Uid': 'b18301c1-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'true',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.ingar.i.grupp.overfors.till.nya',
  #                                                                       'Uid': 'b18301bb-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'true',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.sjalvstandig',
  #                                                                       'Uid': 'b18301bf-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'false',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.grupp.for.utsokning',
  #                                                                       'Uid': 'b18301bd-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'grupp.for.utsokning.grundavanceradniva',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.informationsbehorighet.grundavancerad',
  #                                                                       'Uid': 'b18301bc-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'true',
  #                                                                       'link': [   ]},
  #                                                                   {   'Regelnamn': 'commons.domain.regel.grupp.for.utsokning',
  #                                                                       'Uid': 'b18301c0-e80a-11e8-b1f1-65de97d74aa5',
  #                                                                       'Varde': 'grupp.for.utsokning.forskarniva',
  #                                                                       'link': [   ]}],
  #                                                'Uid': '0461b2c4-1b3f-11e6-aff0-464044604cb6',
  #                                                'link': []},
  #                               'Sorteringsordning': 50,
  #                               'StudieordningID': 1,
  #                               'TillfalleInomUtbildningstyper': [],
  #                               'UtbildningstyperInomUtbildningstyp': [],
  #                               'link': []},
  # ...
  # ],
  #     'link': []}
  # added by GQMJr
  #####################################################################
  #
  # aktivitetstillfallestyp_JSON
  #
  # RETURNERAR JSON of activities
  def aktivitetstillfallestyp_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/aktivitetstillfallestyp',
      headers=self.headers).json()
    return r

  # returns:
  # {   'Aktivitetstillfallestyp': [   {   'Benamning': {   'en': 'Partial Exam',
  #                                                     'sv': 'Kontrollskrivning'},
  #                                    'Beskrivning': {},
  #                                    'Giltighetsperiod': {   'Startdatum': '2018-06-20', 'link': []},
  #                                    'ID': '135201',
  #                                    'Kod': 'KS',
  #                                    'LarosateID': 29, 'link': []},
  #                                {   'Benamning': {   'en': 'Re-examination',
  #                                                     'sv': 'Omtentamen'},
  #                                    'Beskrivning': {},
  #                                    'Giltighetsperiod': {   'Startdatum': '2018-06-20', 'link': []},
  #                                    'ID': '135200',
  #                                    'Kod': 'OMTENTA',
  #                                    'LarosateID': 29, 'link': []},
  #                                {   'Benamning': {   'en': 'Examination',
  #                                                     'sv': 'Tentamen'},
  #                                    'Beskrivning': {},
  #                                    'Giltighetsperiod': {   'Startdatum': '2018-06-20', 'link': []},
  #                                    'ID': '135199',
  #                                    'Kod': 'TENTAMEN',
  #                                    'LarosateID': 29, 'link': []},
  #                                {   'Benamning': {   'en': 'Unspecified '
  #                                                           'activity',
  #                                                     'sv': 'Övrigt '
  #                                                           'aktivitetstillfälle'},
  #                                    'Beskrivning': {},
  #                                    'Giltighetsperiod': {'link': []},
  #                                    'ID': '1',
  #                                    'Kod': 'ÖV',
  #                                    'LarosateID': -1, 'link': []}],
  # 'link': []}
  # added by GQMJr
  #####################################################################
  #
  # catalog_service_index__JSON
  #
  # RETURNERAR JSON of admission round
  def catalog_service_index__JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url + '/kataloginformation/service/index',
      headers=self.headers).json()
    return r

  # returns:
  # {   'ServiceName': 'Ladok3 REST-tjänst för kataloginformation',
  # 'link': [   {   'mediaType': 'application/vnd.ladok+xml,application/vnd.ladok-kataloginformation+xml,application/vnd.ladok-kataloginformation+json',
  #                 'method': 'GET',
  #                 'rel': 'http://relations.ladok.se/kataloginformation/utbildningstyp',
  #                 'uri': 'https://api.ladok.se:443/kataloginformation/grunddata/utbildningstyp'},
  #             {   'mediaType': 'application/vnd.ladok+xml,application/vnd.ladok-kataloginformation+xml,application/vnd.ladok-kataloginformation+json',
  #                 'method': 'GET',
  #                 'rel': 'http://relations.ladok.se/kataloginformation/betygsskala',
  #                 'uri': 'https://api.ladok.se:443/kataloginformation/grunddata/betygsskala'},
  # ...
  #             {   'mediaType': 'application/vnd.ladok+xml,application/vnd.ladok-kataloginformation+xml,application/vnd.ladok-kataloginformation+json',
  #                 'method': 'GET',
  #                 'rel': 'http://relations.ladok.se/kataloginformation/anvandarbehorighetlista',
  #                 'uri': 'https://api.ladok.se:443/kataloginformation/behorigheter'}]}
  # added by GQMJr
  #####################################################################
  #
  # omradesbehorighet_JSON
  #
  # RETURNERAR JSON of "omradesbehorighet"
  # for information see https://antagning.se/globalassets/omradesbehorigheter-hogskolan.pdf
  def omradesbehorighet_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/kataloginformation/grunddata/omradesbehorighet',
      headers=self.headers).json()
    return r
  # added by GQMJr
  #####################################################################
  #
  # hamtaStudieResultatForStudent_JSON 
  #
  # studentUID             -- student's UID
  # RETURNERAR JSON of results

  # NOTE: These are a work in progress and not ready yet
  # def hamtaStudieResultatForStudent_JSON (self, studentUID):
  #     r = self.session.get(url = self.base_gui_proxy_url + '/resultat/studieresultat/resultat/student/'+studentUID, headers = self.headers).json()
  #     return r

  # def student_participation_JSON (self, studentUID):
  #     headers = self.headers.copy()
  #     headers['Content-Type'] = 'application/vnd.ladok-studiedeltagande'
  #     headers['Accept'] = headers['Accept']+', application/vnd.ladok-studiedeltagande'
  #     r = self.session.get(url = self.base_gui_proxy_url + '/studiedeltagande/tillfallesdeltagande/kurstillfallesdeltagande/'+studentUID, headers = self.headers)
  #     return {r.status_code, r.text}
  # added by GQMJr
  #####################################################################
  #
  # examen_student_uid_JSON
  #
  # studentUID             -- student's UID
  # RETURNERAR JSON of admission round
  def examen_student_uid_JSON(self):
    r = self.session.get(
      url=self.base_gui_proxy_url + 'examen/student/+studentUID',
      headers=self.headers).json()
    return r
  #################################################################
  ##
  ## private methods
  ##

  def __get_xsrf_token(self):
    cookies = self.session.cookies.get_dict()
    return next(cookies[cookie] for cookie in cookies if cookie == 'XSRF-TOKEN')

  def get_xsrf_token(self):
    return self.__get_xsrf_token()


  # returns None or a LADOK-formated date
  def __validate_date(self, date_raw):
    datregex = re.compile("(\d\d)?(\d\d)-?(\d\d)-?(\d\d)")
    dat = datregex.match(date_raw)
    if dat:
      if dat.group(1) == None: # add 20, ladok3 won't survive till 2100
        return "20" + dat.group(2) + "-" + dat.group(3) + "-" + dat.group(4)
      else:
        return dat.group(1) + dat.group(2) + \
          "-" + dat.group(3) + "-" + dat.group(4)
    else:
      return None

  def __get_grade_scale_by_id(self, grade_scale_id):
    return next(grade_scale
      for grade_scale in self.get_grade_scales()
        if grade_scale.id == grade_scale_id)


  def __get_grade_scale_by_code(self, grade_scale_code):
    return next(grade_scale
      for grade_scale in self.get_grade_scales()
        if grade_scale.code == grade_scale_code)


  def __get_grade_by_id(self, grade_id):
    for grade_scale in self.get_grade_scales():
      for grade in grade_scale.grades():
        if grade.id == grade_id:
          return grade
    
    return None


  def __get_student_data(self, person_nr):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/studentinformation/student/filtrera?limit=2&orderby=EFTERNAMN_ASC&orderby=FORNAMN_ASC&orderby=PERSONNUMMER_ASC&page=1&personnummer='
          + person_nr + '&skipCount=false&sprakkod=sv',
      headers=self.headers).json()['Resultat']
    
    if len(r) != 1: return None
    
    r = r[0]
    # from schemas/schemas.ladok.se-studentinformation.xsd
    #   <xs:complexType name="Student">
    #   <xs:complexContent>
    #     <xs:extension base="base:BaseEntitet">
    #       <xs:sequence>
    #         <xs:element name="Avliden" type="xs:boolean"/>
    #         <xs:element minOccurs="0" name="Efternamn" type="xs:string"/>
    #         <xs:element minOccurs="0" name="ExterntUID" type="xs:string"/>
    #         <xs:element name="FelVidEtableringExternt" type="xs:boolean"/>
    #         <xs:element minOccurs="0" name="Fodelsedata" type="xs:string"/>
    #         <xs:element minOccurs="0" name="Fornamn" type="xs:string"/>
    #         <xs:element minOccurs="0" name="KonID" type="xs:int"/>
    #         <xs:element minOccurs="0" name="Personnummer" type="xs:string"/>
    #         <xs:element minOccurs="0" name="Skyddsstatus" type="xs:string"/>
    #         <xs:element minOccurs="0" ref="si:UnikaIdentifierare"/>
    #       </xs:sequence>
    #     </xs:extension>
    #   </xs:complexContent>
    # </xs:complexType>

    return {
      'id':         r['Uid'], # Ladok-ID
      'first_name': r['Fornamn'],
      'last_name':  r['Efternamn'],
      'person_nr':  r['Personnummer'], # tolv siffror, utan bindestreck eller plustecken
      'alive':  not r['Avliden']
    }

  # detta är egentligen kurstillfällen, inte kurser (ID-numret är alltså ett ID-nummer för ett kurstillfälle)
  def __get_student_courses(self, student_id):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/studiedeltagande/tillfallesdeltagande/kurstillfallesdeltagande/student/'
          + student_id,
      headers=self.headers).json()
    
    results = []
    
    for course in r['Tillfallesdeltaganden']:
      if not course['Nuvarande'] or \
         'Utbildningskod' not in course['Utbildningsinformation']:
        continue
      
      results.append({
        'id': course['Uid'],
        'round_id': course['Utbildningsinformation']['UtbildningstillfalleUID'], # ett Ladok-ID för kursomgången
        'education_id': course['Utbildningsinformation']['UtbildningUID'], # ett Ladok-ID för något annat som rör kursen
        'instance_id': course['Utbildningsinformation']['UtbildningsinstansUID'], # ett Ladok-ID för att rapportera in kursresultat
        'code': course['Utbildningsinformation']['Utbildningskod'], # kurskod KOPPS
        'name': course['Utbildningsinformation']['Benamning']['sv']
      })
    
    return results


  def __get_student_course_moments(self, course_round_id, student_id):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/resultat/kurstillfalle/' + str(course_round_id) +
          '/student/' + str(student_id) + '/moment',
      headers=self.headers).json()
    
    return [{
      'course_moment_id': moment['UtbildningsinstansUID'],
      'code': moment['Utbildningskod'],
      'education_id': moment['UtbildningUID'],
      'name': moment['Benamning']['sv']
    } for moment in r['IngaendeMoment']]


  def __get_student_course_results(self, course_round_id, student_id):
    r = self.session.get(
      url=self.base_gui_proxy_url +
        '/resultat/studieresultat/student/' + student_id +
          '/utbildningstillfalle/' + course_round_id,
      headers=self.headers).json()
    
    return {
      'id': r['Uid'],
      'results': [{
        'education_id': result['UtbildningUID'],
        'pending': {
          'id': result['Arbetsunderlag']['Uid'],
          'moment_id': result['Arbetsunderlag']['UtbildningsinstansUID'],
          'grade': self.__get_grade_by_id(result['Arbetsunderlag']['Betygsgrad']),
          'date': result['Arbetsunderlag']['Examinationsdatum'],
          'grade_scale': self.__get_grade_scale_by_id(result['Arbetsunderlag']['BetygsskalaID']),
          # behövs vid uppdatering av betygsutkast
          'last_modified': result['Arbetsunderlag']['SenasteResultatandring']
        } if 'Arbetsunderlag' in result else None,
        'attested': {
          'id': result['SenastAttesteradeResultat']['Uid'],
          'moment_id': result['SenastAttesteradeResultat']['UtbildningsinstansUID'],
          'grade': self.__get_grade_by_id(result['SenastAttesteradeResultat']['Betygsgrad']),
          'date': result['SenastAttesteradeResultat']['Examinationsdatum'],
          'grade_scale': self.__get_grade_scale_by_id(result['SenastAttesteradeResultat']['BetygsskalaID'])
        } if 'SenastAttesteradeResultat' in result else None
      } for result in r['ResultatPaUtbildningar']]
    }

class LadokSessionKTH(LadokSession):
  def __init__(self, username, password, test_environment=False):
    """Initialize KTH version of LadokSession"""
    super().__init__(test_environment=test_environment)
    self.__username = username
    self.__password = password

  def ladok_run_shib_login(self, url):
    response = self.session.get(
      url=url+'&entityID=https://saml.sys.kth.se/idp/shibboleth')
            
    action = re.search(
      '<form ?[^>]* action="(.*?)"',
      response.text).group(1)

    csrf_token = re.search(
      '<input ?[^>]* name="csrf_token" ?[^>]* value="(.*?)"',
      response.text).group(1)

    post_data = {
      'csrf_token': csrf_token,
      'shib_idp_ls_exception.shib_idp_session_ss': '',
      'shib_idp_ls_success.shib_idp_session_ss': 'true',
      'shib_idp_ls_value.shib_idp_session_ss': '',
      'shib_idp_ls_exception.shib_idp_persistent_ss': '',
      'shib_idp_ls_success.shib_idp_persistent_ss': 'true',
      'shib_idp_ls_value.shib_idp_persistent_ss': '',
      'shib_idp_ls_supported': 'true',
      '_eventId_proceed': ''
    }

    response = self.session.post(
      url="https://saml-5.sys.kth.se" + action,
      data=post_data)

    return response
  def ug_post_user_pass(self, shib_response):
    action = re.search('<form ?[^>]* id="loginForm" ?[^>]* action="(.*?)"',
      shib_response.text).group(1)

    post_data = {
      'username': self.__username if "@" in self.__username \
                                  else self.__username + "@ug.kth.se",
      'password': self.__password,
      'Kmsi': True,
      'AuthMethod': "FormsAuthentication"
    }

    response = self.session.post(
      url='https://login.ug.kth.se' + action,
      data=post_data)

    return response
  def perform_redirects_back_to_ladok(self, ug_response):
    action = re.search('<form ?[^>]* action="(.*?)"',
      ug_response.text)
    if action is None:
      raise Exception('Invalid username or password OR possibly the SAML \
        configuration has changed, manually login an accept the changed \
        information.')
    action = html.unescape(action.group(1))

    relay_state = re.search(
      '<input ?[^>]* name="RelayState" ?[^>]* value="(.*?)"',
      ug_response.text)
    try:
      relay_state = html.unescape(relay_state.group(1))
    except AttributeError:
      raise Exception(
        "Try to log in using a web browser and accept sharing data.")

    saml_response = re.search(
      '<input ?[^>]* name="SAMLResponse" ?[^>]* value="(.*?)"',
      ug_response.text)
    saml_response = html.unescape(saml_response.group(1))

    post_data = {
        'RelayState': relay_state,
        'SAMLResponse': saml_response
    }

    response = self.session.post(url=action, data=post_data)

    ladok_action = re.search(
      '<form ?[^>]* action="(.*?)"',
      response.text)
    ladok_action = html.unescape(ladok_action.group(1))

    relay_state = re.search(
      '<input ?[^>]* name="RelayState" ?[^>]* value="([^"]+)"',
      response.text)
    relay_state = html.unescape(relay_state.group(1))

    saml_response = re.search(
      '<input ?[^>]* name="SAMLResponse" ?[^>]* value="(.*?)"',
      response.text)
    saml_response = html.unescape(saml_response.group(1))

    post_data = {
        'RelayState': relay_state,
        'SAMLResponse': saml_response
    }

    response = self.session.post(url=ladok_action, data=post_data)

    return response

  def saml_login(self, url):
    """Do the CAS login"""
    response = self.ladok_run_shib_login(url)
    response = self.ug_post_user_pass(response)
    response = self.perform_redirects_back_to_ladok(response)
    return response
class LadokData:
  """Base class for LADOK data"""
  def __init__(self, /, **kwargs):
    pass

  def make_properties(self, kwargs):
    """Turn keywords into private attributes and read-only properties"""
    for attribute in kwargs:
      # private attributes are named on the form _class__attribute
      priv_attr_prefix = f"_{type(self).__name__}__"
      if priv_attr_prefix in attribute:
        priv_attr_name = attribute
        property_name = attribute.replace(priv_attr_prefix, "")
      else:
        priv_attr_name = priv_attr_prefix + attribute
        property_name = attribute

      setattr(self, priv_attr_name, kwargs[attribute])
      if not hasattr(type(self), property_name):
        setattr(type(self), property_name,
          property(operator.attrgetter(priv_attr_name)))

  def __eq__(self, other):
    if type(self) == type(other):
      return self.__dict__ == other.__dict__
    return False

  def __repr__(self):
    return str(self.json)

  @property
  def json(self):
    """JSON compatible dictionary representation of the object"""
    json_format = self.__dict__.copy()
    for key, value in json_format.items():
      if isinstance(value, LadokData):
        json_format[key] = value.json
    json_format["type"] = type(self).__name__
    return json_format
class LadokDataEncoder(json.JSONEncoder):
  def default(self, object):
    if isinstance(object, LadokData):
      return object.json
    return super().default(object)
class LadokRemoteData(LadokData):
  """Base class for remote LADOK data"""
  def __init__(self, /, **kwargs):
    super().__init__(**kwargs)
    if "_LadokRemoteData__ladok" in kwargs:
      self.make_properties(**kwargs)
    else:
      self.__ladok = kwargs.pop("ladok")

  @property
  def ladok(self):
    return self.__ladok

  def pull(self):
    """Pull updates for object from LADOK"""
    raise NotImplementedError("This object doesn't support pulling from LADOK")

  def push(self):
    """Push changes made to the object to LADOK"""
    raise NotImplementedError("This object doesn't support pushing to LADOK")
class GradeScale(LadokData):
  """A grade scale"""
  def __init__(self, /, **kwargs):
    super().__init__(**kwargs)

    if "_GradeScale__id" in kwargs:
      self.make_properties(**kwargs)
    else:
      self.__id = int(kwargs.pop("ID"))
      self.__code = kwargs.pop("Kod")
      self.__name = kwargs.pop("Benamning")["sv"]
      self.__grades = [Grade(**grade_data)
                        for grade_data in kwargs.pop("Betygsgrad")]

  @property
  def id(self):
    return self.__id

  @property
  def code(self):
    return self.__code

  @property
  def name(self):
    return self.__name

  def grades(self, /, **kwargs):
    """Returns grades filtered on keyword"""
    return filter_on_keys(self.__grades, **kwargs)

  def __contains__(self, grade):
    return grade in self.__grades

  def __iter__(self):
    return iter(self.__grades)
class Grade(LadokData):
  """An individual grade part of a grade scale"""
  def __init__(self, /, **json_data):
    """Constructor taking a dictionary (JSON-like) structure"""
    if "_Grade__id" in json_data:
      self.make_properties(**json_data)
    else:
      self.__id = int(json_data.pop("ID"))
      self.__code = json_data.pop("Kod")
      self.__accepted = json_data.pop("GiltigSomSlutbetyg")

  @property
  def id(self):
    return self.__id

  @property
  def code(self):
    return self.__code

  def __str__(self):
    return self.code

  @property
  def accepted(self):
    return self.__accepted

  def __eq__(self, other):
    if isinstance(other, Grade):
      return self.__dict__ == other.__dict__
    elif isinstance(other, str):
      return self.code == other
    else:
      raise NotImplementedError(f"can't test equality with {type(other)}")
class Student(LadokRemoteData):
  """Class representing a student and related data"""
  def __init__(self, /, **kwargs):
    """Requires ladok (a LadokSession object),
    id (either a personnummer or LADOK ID)"""
    super().__init__(**kwargs)
    id = kwargs.pop("id")
    self.__personnummer = format_personnummer(id)
    if not self.__personnummer:
      self.__ladok_id = id
    else:
      self.__ladok_id = None

  def pull(self):
    """pull student data from LADOK"""
    self.__get_personal_attributes()

  def __get_personal_attributes(self):
    """Helper method that fetches personal attributes"""
    if self.__ladok_id:
      response = self.ladok.session.get(
        url=self.ladok.base_gui_proxy_url +
          '/studentinformation/student/' + self.ladok_id,
        headers=self.ladok.headers)
      if response.status_code == 200:
        record = response.json()
      else:
        raise AttributeError("can't fetch student attributes by LADOK ID")
    elif self.__personnummer:
      response = self.ladok.session.get(
        url=self.ladok.base_gui_proxy_url +
          '/studentinformation/student/filtrera?limit=2&orderby=EFTERNAMN_ASC&orderby=FORNAMN_ASC&orderby=PERSONNUMMER_ASC&page=1&personnummer=' +
            self.personnummer + '&skipCount=false&sprakkod=sv',
              headers=self.ladok.headers).json()['Resultat']

      if len(response) != 1:
        raise ValueError("can't find student based on personnummer")

      record = response[0]
    else:
      raise AttributeError("neither personnummer, nor LADOK ID set")

    self.__ladok_id = record['Uid']
    self.__personnummer = record['Personnummer'] # twelve digits only
    self.__first_name = record['Fornamn']
    self.__last_name = record['Efternamn']
    self.__alive = not record['Avliden']

  @property
  def ladok_id(self):
    """Return the student's LADOK ID"""
    try:
      if self.__ladok_id:
        return self.__ladok_id
    except:
      pass
    self.__get_personal_attributes()
    return self.__ladok_id

  @property
  def personnummer(self):
    """Return the student's personnummer"""
    try:
      if self.__personnummer:
        return self.__personnummer
    except:
      pass
    self.__get_personal_attributes()
    return self.__personnummer

  @property
  def first_name(self):
    """Return the student's first name"""
    try:
      return self.__first_name
    except:
      self.__get_personal_attributes()
    return self.__first_name

  @property
  def last_name(self):
    """Return the student's last name"""
    try:
      return self.__last_name
    except:
      self.__get_personal_attributes()
    return self.__last_name

  def __str__(self):
    return f"{self.personnummer} {self.first_name} {self.last_name}"

  @property
  def alive(self):
    """Return whether student is alive or not"""
    try:
      return self.__alive
    except:
      self.__get_personal_attributes()
    return self.__alive
  def __get_study_attributes(self):
    """Helper method to fetch study related attributes"""
    # detta är egentligen kurstillfällen, inte kurser (ID-numret är alltså ett 
    # ID-nummer för ett kurstillfälle)
    response = self.ladok.session.get(
      url=self.ladok.base_gui_proxy_url+
        '/studiedeltagande/tillfallesdeltagande/kurstillfallesdeltagande/student/'+
          self.ladok_id,
      headers=self.ladok.headers).json()
        
    self.__courses = []

    for course in response['Tillfallesdeltaganden']:
      if not course['Nuvarande'] or \
        'Utbildningskod' not in course['Utbildningsinformation']:
        continue
      
      self.__courses.append(CourseRegistration(
        ladok=self.ladok,
        student=self,
        **course["Utbildningsinformation"]))

  def courses(self, /, **kwargs):
    """Returns a list of courses that the student is registered on.
    Filtered based on keywords."""
    try:
      courses = self.__courses
    except:
      self.__get_study_attributes()
      courses = self.__courses

    return filter_on_keys(courses, **kwargs)
class CourseInstance(LadokRemoteData):
  """Represents a course instance. Must be constructed from at least
  ladok (a LadokSession object),
  UtbildningsinstansUID (an instance_id from LADOK),
  optionally a data dictionary from LADOK"""
  def __init__(self, /, **kwargs):
    super().__init__(**kwargs)
    self.__instance_id = kwargs.pop("UtbildningsinstansUID")

    try:
      self.__assign_attr(kwargs)
    except:
      self.__pull_attributes()

  def __assign_attr(self, data):
    self.__education_id = data.pop("UtbildningUID")

    self.__code = data.pop("Utbildningskod")
    self.__name = {}
    names = data.pop("Benamning")
    for name in names:
      self.__name[name["Sprakkod"]] = name["Text"]
    self.__version = data.pop("Versionsnummer")

    self.__credits = data.pop("Omfattning")
    self.__unit = data.pop("Enhet")

    self.__grade_scale = self.ladok.get_grade_scales(
      id=data.pop("BetygsskalaID"))

    self.__components = [CourseComponent(
        ladok=self.ladok,
        **component) for component in data["Moduler"]]

  def __pull_attributes(self):
    headers = self.ladok.headers.copy()
    headers["Content-Type"] = "application/vnd.ladok-resultat+json"
    headers["X-XSRF-TOKEN"] = self.ladok.get_xsrf_token()
    headers["Referer"] = self.ladok.base_gui_url

    put_data = {"Identitet": [self.__instance_id]}

    response = self.ladok.session.put(
      url=self.ladok.base_gui_proxy_url + '/resultat/utbildningsinstans/moduler',
      json=put_data,
      headers=headers)
    response = response.json()

    data = response["Utbildningsinstans"][0]
    self.__assign_attr(data)

  def pull(self):
    self.__pull_attributes()

  @property
  def instance_id(self):
    return self.__instance_id

  @property
  def education_id(self):
    return self.__education_id

  @property
  def code(self):
    return self.__code

  @property
  def name(self):
    return self.__name.copy()

  @property
  def version(self):
    return self.__version

  @property
  def grade_scale(self):
    return self.__grade_scale

  @property
  def credits(self):
    return self.__credits

  @property
  def unit(self):
    return self.__unit

  def components(self, /, **kwargs):
    """Returns the list of components, filtered on keywords"""
    return filter_on_keys(self.__components, **kwargs)

class CourseRound(CourseInstance):
  """Represents a course round"""
  def __init__(self, /, **kwargs):
    """Must be constructed from at least:
    Uid, TillfallesKod, Startdatum, Slutdatum"""
    instance_data = kwargs.pop("Utbildningsinstans")
    instance_data["UtbildningsinstansUID"] = instance_data.pop("Uid")
    super().__init__(ladok=kwargs.pop("ladok"), **instance_data)

    self.__round_id = kwargs.pop("Uid")
    self.__round_code = kwargs.pop("TillfallesKod")

    self.__start = datetime.date.fromisoformat(kwargs.pop("Startdatum"))
    self.__end = datetime.date.fromisoformat(kwargs.pop("Slutdatum"))

  @property
  def round_id(self):
    return self.__round_id

  @property
  def round_code(self):
    return self.__round_code

  @property
  def start(self):
    return self.__start

  @property
  def end(self):
    return self.__end

  def results(self, /, **kwargs):
    """Returns all students' results on the course"""
    try:
      self.__results
    except:
      self.__fetch_results()

    return filter_on_keys(self.__results, **kwargs)
  def __fetch_results(self):
    raise NotImplementedError(
      f"{type(self).__name__}.__fetch_results not implemented")
  def participants(self, /, **kwargs):
    """Returns a Student object for each participant in the course."""
    try:
      self.__participants
    except:
      self.__fetch_participants()

    return filter_on_keys(self.__participants, **kwargs)
  def __fetch_participants(self):
    self.__participants = []
    for student in self.ladok.participants_JSON(self.round_id):
      self.__participants.append(
        self.ladok.get_student(student["Student"]["Uid"]))
class CourseComponent(LadokData):
  """Represents a course component of a course registration"""
  def __init__(self, /, **kwargs):
    super().__init__(**kwargs)

    if "UtbildningsinstansUID" in kwargs:
      self.__instance_id = kwargs.pop("UtbildningsinstansUID")
    else:
      self.__instance_id = kwargs.pop("Uid")

    self.__education_id = kwargs.pop("UtbildningUID")

    self.__code = kwargs.pop("Utbildningskod")
    description = kwargs.pop("Benamning")
    if isinstance(description, dict):
      self.__description = get_translation("sv", description)
    else:
      self.__description = description

    self.__credits = kwargs.pop("Omfattning")
    self.__unit = kwargs.pop("Enhet")

    ladok = kwargs.pop("ladok")
    grade_scale_id = kwargs.pop("BetygsskalaID")
    self.__grade_scale = ladok.get_grade_scales(id=grade_scale_id)[0]

  @property
  def instance_id(self):
    return self.__instance_id

  @property
  def education_id(self):
    return self.__education_id

  @property
  def code(self):
    """Returns the name of the component (as in syllabus)"""
    return self.__code

  @property
  def description(self):
    """Returns description of component (as in syllabus)"""
    return self.__description

  @property
  def unit(self):
    """Returns the unit for the credits"""
    return self.__unit

  @property
  def credits(self):
    """Returns the number of credits"""
    return self.__credits

  @property
  def grade_scale(self):
    return self.__grade_scale

  def __str__(self):
    return self.code

  def __eq__(self, other):
    if isinstance(other, str):
      return self.code == other
    return self.__dict__ == other.__dict__
class CourseRegistration(CourseInstance):
  """Represents a student's participation in a course instance"""
  def __init__(self, /, **kwargs):
    super().__init__(**kwargs)

    self.__student = kwargs.pop("student")

    # ett Ladok-ID för kursomgången
    self.__round_id = kwargs.pop("UtbildningstillfalleUID")
    self.__round_code = kwargs.pop("Utbildningstillfalleskod")

    dates = kwargs.pop("Studieperiod")
    self.__start = datetime.date.fromisoformat(dates["Startdatum"])
    self.__end = datetime.date.fromisoformat(dates["Slutdatum"])

  @property
  def round_id(self):
    """Returns LADOK ID for the course round (kursomgång)"""
    return self.__round_id

  @property
  def round_code(self):
    """Returns the human-readable round code (tillfälleskod)"""
    return self.__round_code

  @property
  def start(self):
    return self.__start

  @property
  def end(self):
    return self.__end

  def __str__(self):
    return f"{self.code} {self.round_code} ({self.start}--{self.end})"

  def __repr__(self):
    return f"{self.code}:{self.round_code}:{self.start}--{self.end}"

  def results(self, /, **kwargs):
    """Returns the student's results on the course, filtered on keywords"""
    try:
      return filter_on_keys(self.__results, **kwargs)
    except:
      self.__fill_results()
    return filter_on_keys(self.__results, **kwargs)

  def __fill_results(self):
    """Helper method to fetch results from LADOK"""
    response = self.ladok.student_results_JSON(
      self.__student.ladok_id, self.round_id
    )

    self.__results_id = response["Uid"]
    self.__results = []
    for result in response["ResultatPaUtbildningar"]:
      try:
        self.__results.append(CourseResult(
          ladok=self.ladok,
          components=self.components(),
          student=self.__student,
          study_results_id=self.__results_id,
          **result))
      except TypeError:
        pass
    for component in self.components():
      if not list(filter_on_keys(self.__results, component=component.code)):
        self.__results.append(
          CourseResult(
            ladok=self.ladok,
            component=component,
            student=self.__student,
            study_results_id=self.__results_id))

  def push(self):
    """Pushes any new results"""
    for result in self.results():
      result.push()
class CourseResult(LadokRemoteData):
  """Represents a result on a course module"""
  def __init__(self, /, **kwargs):
    """To construct this object we must give existing data, i.e.
    Arbetsunderlag or SenastAttesteradeResultat directly from LADOK."""
    super().__init__(**kwargs)

    self.__student = kwargs.pop("student")
    self.__study_results_id = kwargs.pop("study_results_id")

    if "component" in kwargs:
      self.__component = kwargs.pop("component")
      self.__attested = False
      self.__populate_attributes()
    elif "components" in kwargs and \
        ("Arbetsunderlag" in kwargs or "SenastAttesteradeResultat" in kwargs):
      components = kwargs.pop("components")

      if "Arbetsunderlag" in kwargs:
        self.__attested = False
        data = kwargs.pop("Arbetsunderlag")
      elif "SenastAttesteradeResultat" in kwargs:
        self.__attested = True
        data = kwargs.pop("SenastAttesteradeResultat")

      self.__populate_attributes(**data, components=components)
    else:
      raise TypeError("not enough keys given to construct object")

  def __populate_attributes(self, /, **data):
    if not data:
      self.__uid = None
      self.__instance_id = self.__component.instance_id

      self.__date = None
      self.__grade_scale = self.__component.grade_scale
      self.__grade = None

      self.__modified = False
      self.__last_modified = None
    else:
      self.__uid = data.pop("Uid")
      self.__instance_id = data.pop("UtbildningsinstansUID")
      self.__results_id = data.pop("ResultatUID")
      self.__study_results_id = data.pop("StudieresultatUID")

      grade_scale_id = data.pop("BetygsskalaID")
      grade = data.pop("Betygsgrad")

      self.__date = data.pop("Examinationsdatum")
      self.__grade_scale = self.ladok.get_grade_scales(id=grade_scale_id)[0]
      self.__grade = self.__grade_scale.grades(id=grade)[0]

      if "components" in data:
        components = data.pop("components")
        component_list = filter_on_keys(components, instance_id=self.__instance_id)
        self.__component = component_list[0] if component_list \
                                            else None

      self.__last_modified = data.pop("SenasteResultatandring")
      self.__modified = False

  @property
  def component(self):
    """Returns the component the results is for"""
    return self.__component

  @property
  def grade_scale(self):
    """Returns the grade scale for the component"""
    return self.__grade_scale

  @property
  def grade(self):
    """Returns the grade set for the component"""
    return self.__grade

  def set_grade(self, grade, date):
    """Sets a new grade and date for the component"""
    if self.attested:
      raise AttributeError("can't change already attested grade")

    if isinstance(grade, Grade) and grade not in self.grade_scale.grades():
      raise TypeError(f"The grade {grade} is not in"
        f"the scale {self.grade_scale.code}")
    elif isinstance(grade, str):
      try:
        grade = self.grade_scale.grades(code=grade)[0]
      except:
        raise TypeError(
          f"The grade {grade} is not in the scale {self.grade_scale.code}")
    else:
      raise TypeError(f"Can't use type {type(grade)} for grade")

    if isinstance(date, str):
      date = datetime.date.fromisoformat(date)
    elif not isinstance(date, datetime.date):
      raise TypeError(f"Type {type(date)} not supported for date")

    self.__grade = grade
    self.__date = date

    self.__modified = True
    self.push()

  def finalize(self, notify=False):
    """Finalizes the set grade"""
    if self.modified:
      self.push()

    reporter_id = self.ladok.user_info_JSON()["AnvandareUID"]

    if notify:
      response = self.ladok.finalize_result_JSON(
        self.__results_id, self.__last_modified, reporter_id, reporter_id
      )
    else:
      response = self.ladok.finalize_result_JSON(
        self.__results_id, self.__last_modified, reporter_id
      )

    self.__populate_attributes(**response)

  @property
  def modified(self):
    """Returns True if there are unpushed changes"""
    return self.__modified

  @property
  def date(self):
    """Returns the date of the grade"""
    return self.__date

  @property
  def attested(self):
    """Returns True if the grade has been attested in LADOK"""
    return self.__attested

  def push(self):
    if self.__uid:
      try:
        response = self.ladok.update_result_JSON(
          self.grade.id, self.grade_scale.id, self.date.isoformat(),
          self.__uid, self.__last_modified
        )
      except Exception as err:
        raise Exception(
          f"couldn't update {self.component.code} to {self.grade} ({self.date})"
          f" to LADOK: {err}"
        )

      self.__populate_attributes(**response[0])
    else:
      try:
        response = self.ladok.create_result_JSON(
          self.grade.id, self.grade_scale.id, self.date.isoformat(),
          self.__study_results_id, self.__instance_id
        )
      except Exception as err:
        raise Exception("Couldn't register "
          f"{self.component} {self.grade} {self.date}: {err}")

      self.__populate_attributes(**response[0])
    self.__modified = False
def filter_on_keys(items, /, **kwargs):
  for key in kwargs:
    items = filter(
      lambda x: operator.attrgetter(key)(x) == kwargs[key],
      items)
  return list(items)
def filter_on_any_key(items, /, **kwargs):
  matching_items = []
  for item in items:
    for key in kwargs:
      if operator.attrgetter(key)(item) == kwargs[key]:
        matching_items.append(item)
        break

  return matching_items
def get_translation(lang_code, list_of_translations):
  for translation in list_of_translations:
    if translation["Sprakkod"] == lang_code:
      return translation["Text"]
  raise KeyError(f"no translation for language {lang_code}")
def format_personnummer(person_nr_raw):
  """Returns None or a LADOK-formated person nr"""
  pnrregex = re.compile("^(\d\d)?(\d\d)(\d\d\d\d)[+\-]?(\w\w\w\w)$")
  pnr = pnrregex.match(person_nr_raw)
  if pnr:
    now = datetime.datetime.now()
    if pnr.group(1) == None: # first digits 19 or 20 missing
      if now.year - 2000 >= int(pnr.group(2)) + 5: # must be > 5 years old
        return "20" + pnr.group(2) + pnr.group(3) + pnr.group(4)
      else:
        return "19" + pnr.group(2) + pnr.group(3) + pnr.group(4)
    else:
      return pnr.group(1) + pnr.group(2) + pnr.group(3) + pnr.group(4)
  else:
    return None
def clean_data(json_obj):
  remove_links(json_obj)
  pseudonymize(json_obj)
def remove_links(json_obj):
  """Recursively removes all "link" keys and values"""
  if isinstance(json_obj, dict):
    if "link" in json_obj:
      json_obj.pop("link")
    for key, value in json_obj.items():
      remove_links(value)
  elif isinstance(json_obj, list):
    for item in json_obj:
      remove_links(item)
def pseudonymize(json_obj):
  """Recursively pseudonymizes a JSON data record"""
  if isinstance(json_obj, dict):
    if "Fornamn" in json_obj:
      json_obj["Fornamn"] = "Student"
    if "Efternamn" in json_obj:
      json_obj["Efternamn"] = "Studentsson"
    if "Personnummer" in json_obj:
      json_obj["Personnummer"] = "191234561234"
    for key, value in json_obj.items():
      pseudonymize(value)
  elif isinstance(json_obj, list):
    for item in json_obj:
      pseudonymize(item)
