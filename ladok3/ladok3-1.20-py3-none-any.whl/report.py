import csv
import datetime
import ladok3
import sys

def report_one_result(ladok, args):
  if not (args.course_code and args.component_code and
    args.student_id and args.grade):
    print(f"{sys.argv[0]} report: "
      "not all positional args given: course_code, component, student, grade",
      file=sys.stderr)
    sys.exit(1)
  try:
    student = ladok.get_student(args.student_id)
    course = student.courses(code=args.course_code)[0]
    result = course.results(component=args.component_code)[0]
    result.set_grade(args.grade, args.date)
    if args.finalize:
      result.finalize()
  except Exception as err:
    try:
      print(f"{student}: {err}")
    except ValueError as verr:
      print(f"{verr}: {args.student_id}: {err}")

def report_many_results(ladok, args):
  data_reader = csv.reader(sys.stdin, delimiter=args.delimiter)
  for course_code, component_code, student_id, grade, date in data_reader:
    try:
      student = ladok.get_student(student_id)

      try:
        course = student.courses(code=course_code)[0]
      except IndexError:
        raise Exception(f"{course_code}: no such course.")

      try:
        component = course.results(component=component_code)[0]
      except IndexError:
        raise Exception(f"{course_code} has no component {component_code}.")

      if not component.attested and component.grade != grade:
        component.set_grade(grade, date)
        component.finalize()
        if args.verbose:
          print(f"{course_code} {student}: reported "
            f"{component.component} = {component.grade} ({date}).")
      elif component.grade != grade:
        print(f"{course_code} {student}: attested {component.component} "
          f"result {component.grade} ({component.date}) "
          f"is different from {grade} ({date}).")
    except Exception as err:
      try:
        print(f"{course_code} {component_code}={grade} ({date}) {student}: {err}",
          file=sys.stderr)
      except ValueError as verr:
        print(f"{verr}: "
          f"{course_code} {component_code}={grade} ({date}) {student_id}: {err}",
          file=sys.stderr)

def add_command_options(parser):
  report_parser = parser.add_parser("report",
    help="Reports course results to LADOK",
    description="Reports course results to LADOK"
  )
  report_parser.set_defaults(func=command)
  one_parser = report_parser.add_argument_group(
    "one result as positional args, only date is optional")
  one_parser.add_argument("course_code", nargs="?",
    help="The course code (e.g. DD1315) for which the grade is for"
  )

  one_parser.add_argument("component_code", nargs="?",
    help="The component code (e.g. LAB1) for which the grade is for"
  )

  one_parser.add_argument("student_id", nargs="?",
    help="Student identifier (personnummer or LADOK ID)"
  )

  one_parser.add_argument("grade", nargs="?",
    help="The grade (e.g. A or P)"
  )
  one_parser.add_argument("date", nargs="?",
    help="Date on ISO format (e.g. 2021-03-18), "
      f"defaults to today's date ({datetime.date.today()})",
    type=datetime.date.fromisoformat,
    default=datetime.date.today()
  )
  many_parser = report_parser.add_argument_group(
    "many results read from standard input as CSV, columns: "
    "course, component, student, grade, date.")
  many_parser.add_argument("-d", "--delimiter",
    default="\t",
    help="The delimiter for the CSV input; "
      "default is a tab character to be compatible with POSIX commands, "
      "use `-d,` or `-d ,` to get comma-separated values.")
  many_parser.add_argument("-v", "--verbose",
    action="count", default=0,
    help="Increases the verbosity of the output: -v will print results that "
      "were reported to standard out. Otherwise only errors are printed.")
  report_parser.add_argument("-f", "--finalize",
    help="Finalize the grade (mark as ready/klarmarkera) for examiner to attest",
    action="store_true",
    default=False
  )

def command(ladok, args):
  if args.course_code:
    report_one_result(ladok, args)
  else:
    report_many_results(ladok, args)
