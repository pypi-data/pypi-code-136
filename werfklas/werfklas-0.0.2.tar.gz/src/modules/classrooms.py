from src.modules.common import find_class, find_teacher


def get_classroom(cid):
    # provision classroom based upon class id per child.
    # find classroom
    if cid is None:
        return None
    classrooms = find_class(cid)
    # find teacher
    teachers = find_teacher(classrooms['teacher'])
    _classroom = ({
        'name': classrooms['class_name'],
        'id': classrooms['id'],
        'start_date': classrooms['start_date'],
        'end_date': classrooms['end_date'],
        'teacher_id': classrooms['teacher'],
        'teacher_firstname': teachers['firstname'],
        'teacher_lastname': teachers['lastname'],
    })
    return _classroom
