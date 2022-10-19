import csv
import datetime
import ladok3
import os
import sys

def filter_rounds(all_rounds, desired_rounds):
  """Returns only the round objects with round code in desired_rounds."""
  if not desired_rounds:
    return all_rounds
  return filter(
    lambda x: x.round_code in desired_rounds,
    all_rounds
  )
def extract_data_for_round(ladok, course_round, args):
  course_start = course_round.start
  course_length = course_round.end - course_start
  component = course_round.components()[0]
  results = ladok.search_reported_results_JSON(
    course_round.round_id, component.instance_id)

  students = filter_students(course_round.participants(), args.students)

  for student in students:
    student_results = filter_student_results(student, results)

    if not should_include(ladok, student, course_round, student_results):
      continue

    components = filter_components(course_round.components(), args.components)

    for component in components:
      if len(student_results) < 1:
        result_data = None
      else:
        result_data = filter_component_result(
          component, student_results[0]["ResultatPaUtbildningar"])

      if not result_data:
        grade = "-"
        normalized_date = None
      else:
        if "Betygsgradsobjekt" in result_data:
          grade = result_data["Betygsgradsobjekt"]["Kod"]
          date = datetime.date.fromisoformat(
            result_data["Examinationsdatum"])
          normalized_date = (date - course_start) / course_length
          if args.time_limit and normalized_date > args.time_limit:
            grade = "-"
            normalized_date = None
        else:
          grade = "-"
          normalized_date = None

      yield student, component, grade, normalized_date
def filter_student_results(student, results):
  return list(filter(
    lambda x: x["Student"]["Uid"] == student.ladok_id,
    results))
def filter_component_result(component, results):
  for component_result in results:
    if "Arbetsunderlag" in component_result:
      result_data = component_result["Arbetsunderlag"]
    elif "SenastAttesteradeResultat" in component_result:
      result_data = component_result["SenastAttesteradeResultat"]
    else:
      continue
    if component.instance_id != result_data["UtbildningsinstansUID"]:
      continue
    return result_data

  return None
def filter_students(all_students, desired_students):
  """Returns only the students with personnummer in desired_students."""
  if not desired_students:
    return all_students
  return filter(
    lambda x: x.personnummer in desired_students,
    all_students
  )

def filter_components(all_components, desired_components):
  """Returns only the components with a code in the desired_components."""
  if not desired_components:
    return all_components
  return filter(
    lambda x: x.code in desired_components,
    all_components
  )
def should_include(ladok, student, course_round, result):
  """Returns True if student should be included, False if to be excluded"""
  if is_reregistered(ladok, student.ladok_id, course_round):
    return False

  if has_credit_transfer(result):
    return False

  return True
def is_reregistered(ladok, student_id, course):
  """Check if the student is reregistered on the course round course."""
  registrations = ladok.registrations_on_course_JSON(
    course.education_id, student_id)
  registrations.sort(
    key=lambda x: x["Utbildningsinformation"]["Studieperiod"]["Startdatum"])
  first_reg = registrations[0]
  return first_reg["Utbildningsinformation"]["Utbildningstillfalleskod"] != \
    course.round_code
def has_credit_transfer(results):
  """Returns True if there exists a credit tranfer among the results."""
  for result in results:
    for component_result in result["ResultatPaUtbildningar"]:
      if component_result["HarTillgodoraknande"]:
        return True

  return False

def add_command_options(parser):
  data_parser = parser.add_parser("data",
    help="Returns course results data in CSV form",
    description="""
  Returns the results in CSV form for all first-time registered students.
  """.strip())
  data_parser.set_defaults(func=command)
  data_parser.add_argument("course_code",
    help="The course code of the course for which to export data")

  data_parser.add_argument("-d", "--delimiter",
    default="\t",
    help="The delimiter for the CSV output; "
      "default is a tab character to be compatible with POSIX commands, "
      "use `-d,` or `-d ,` to get comma-separated values.")
  data_parser.add_argument("-r", "--rounds", nargs="+",
    help="The round codes for the rounds to include, "
      "otherwise all rounds will be included.")
  data_parser.add_argument("-t", "--time-limit", type=float,
    help="The time (normalized) for cutting off results, "
      "use `-t 1.0` to cut off at course end.")
  data_parser.add_argument("-s", "--students", nargs="+",
    help="List of personnummer for students to include, "
      "otherwise all students will be included.")

  data_parser.add_argument("-c", "--components", nargs="+",
    help="List of component codes for components to include, "
      "otherwise all components will be included.")

def command(ladok, args):
  data_writer = csv.writer(sys.stdout, delimiter=args.delimiter)
  course_rounds = filter_rounds(
    ladok.search_course_rounds(code=args.course_code),
    args.rounds)

  data_writer.writerow([
    "Course", "Round", "Component", "Student", "Grade", "Time"
  ])
  for course_round in course_rounds:
    data = extract_data_for_round(ladok, course_round, args)

    for student, component, grade, time in data:
      data_writer.writerow(
        [course_round.code, course_round.round_code, component,
          student, grade, time]
      )
