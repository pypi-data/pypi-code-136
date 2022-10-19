# pip library by feb

from .sync_ import (User, Account, Journals)
from .async_ import (User)

# ----------------------

"""
	METHODS_URL = {

		/GET/
		Все сообщения: https://edu-tpi.donstu.ru/api/Mail/InboxMail
		Непрочитанные сообщения: https://edu-tpi.donstu.ru/api/Mail/CheckMail
		Конкретное сообщение: https://edu-tpi.donstu.ru/api/Mail/InboxMail?&id={id}
		Просмотр студентов в группе: https://edu-tpi.donstu.ru/api/Mail/Find/Students?groupID={groupID}
		Поиск студента по ФИО: https://edu-tpi.donstu.ru/api/Mail/Find/Students?fio={fio}
		Поиск преподователя по ФИО: https://edu-tpi.donstu.ru/api/Mail/Find/Prepods?fio={fio}
		Список всех групп в {N-N} учебном году: https://edu-tpi.donstu.ru/api/groups?year={N1}-{N2}
		Информация об аккаунте: https://edu-tpi.donstu.ru/api/tokenauth
		Информация о студенте: https://edu-tpi.donstu.ru/api/UserInfo/Student?studentID=-{studentID}
		Возвращает максимульный/минимальный/текущий день расписания группы GROUP: https://edu-tpi.donstu.ru/api/GetRaspDates?idGroup=GROUP 
		Возвращает расписание группы GROUP с DATE: https://edu-tpi.donstu.ru/api/Rasp?idGroup=GROUP&sdate=DATE
		Возвращает задолженности студента: https://edu-tpi.donstu.ru/api/StudentsDebts/list?studentID={studentID}
		Возвращает ленту пользователя: https://edu-tpi.donstu.ru/api/Feed?userID={userID}&startDate=null
[admin]	Возвращает достижения всех пользователей: https://edu-tpi.donstu.ru/api/Portfolio/Verifier/ListWorks?year={year}&sem=-1&finished={veref}&type={typeVeref}
[admin] Возвращает все файлы приклеплённые к работе: https://edu-tpi.donstu.ru/api/Portfolio/FilesList?workID={workID}

		/POST/
		Авторизация: https://edu-tpi.donstu.ru/Account/Login.aspx
		Отправить сообщение на почту: https://edu-tpi.donstu.ru/api/Mail/InboxMail
[admin]	Создание чата: https://edu-tpi.donstu.ru/api/Chats/Chat
"""		