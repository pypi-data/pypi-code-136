from src.modules.common import find_class, find_teacher, stringdate


def get_classroom(uuid):
    # provision classroom based upon class id per child.
    # find classroom
    if uuid == "None":
        return None
    classrooms = find_class(uuid)
    # find teacher
    teachers = find_teacher(classrooms['teacher_uuid'])

    _classroom = ({
        'name': classrooms['class_name'],
        'uuid': classrooms['uuid'],
        'start_date': classrooms['start_date'],
        'end_date': classrooms['end_date'],
        'teacher_uuid': classrooms['teacher_uuid'],
        'teacher_firstname': teachers['firstname'],
        'teacher_lastname': teachers['lastname'],
        'active': (classrooms['start_date'] >= stringdate() <= classrooms['end_date'])
    })
    return _classroom
