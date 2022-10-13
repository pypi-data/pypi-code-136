'''
Created on Mar 15, 2016

@author: Startech M <startechm@proton.me>
@license: Apache License 2.0

This software is licensed under the Apache License v2.0
 It comes with NO WARRANTIES whatsoever so please use at your OWN RISK.
 If you would like to contribute, please contact me at startechm@proton.me
'''
import sys
import os
import shutil
from .utils import migrate_utils
from datetime import datetime
import traceback

MIGRATIONS_PATH = 'sql'
MAIN_TABLE = 'migrations'
MAIN_FOLDER = 'migrations'
CFG_PATH = 'config/db.cnf'

MIGRATION_TEMPLATE_FOLDER = os.path.dirname(__file__)


def check_cwd_is_migrations_folder():
    '''
        This will error out if we are not in migrations/ folder
    '''
    current_folder = os.getcwd()
    if not os.path.basename(current_folder) == MAIN_FOLDER:  #  and os.path.exists(f"{current_folder}/{CFG_PATH}")
        print("Must be in migrations/ folder to run this command")
        sys.exit(1)


def migrate_init():

    current_folder = os.getcwd()

    # If we are in migrations/ folder already and it already ran
    if os.path.basename(current_folder) == MAIN_FOLDER and os.path.exists(f"{current_folder}/{CFG_PATH}"):
        print("Init already ran")
        sys.exit(1)

    migration_folder_path = f"{current_folder}/{MAIN_FOLDER}"

    # TESTING: cleanup first
    # if os.path.exists(migration_folder_path):
    #    os.removedirs(migration_folder_path)

    if os.path.exists(migration_folder_path):
        print(f"Folder {MAIN_FOLDER}/ already exists")
        sys.exit(1)
    else:
        # Creating the entire folder structure
        os.mkdir(migration_folder_path)

        # os.mkdir("f{migration_folder_path}/sql")
        # os.mkdir("f{migration_folder_path}/sql/base")
        # os.mkdir("f{migration_folder_path}/config")

        shutil.copytree(f"{MIGRATION_TEMPLATE_FOLDER}/sql", f"{migration_folder_path}/sql")
        shutil.copytree(f"{MIGRATION_TEMPLATE_FOLDER}/config", f"{migration_folder_path}/config")

        print("XTMigrations folder structure created.")
        print(f"  Now, you need to configure {migration_folder_path}/{CFG_PATH}")


def check_migrations():
    try:
        cursor.execute("SELECT * FROM {t} LIMIT 1".format(t=MAIN_TABLE))
        return True
    except:
        return False

def get_section(file_path, section):
    ''' Fetches @Up or @Down section.
      Section param can be either 'up' or 'down' (string)
     '''

    if section not in ['up', 'down']:
        raise RuntimeError("get_section: section argument can only be \"up\" or \"down\"")

    section_capture = False
    content = ''

    f = open(file_path, "r")
    for l in f:
        if l=='\n' or l[0] == '#':
            continue
        elif (l.startswith("@Up") and section=='up') or (l.startswith("@Down") and section=='down') :
            section_capture = True
            continue
        else:
            if section_capture:
                if not (l.startswith("@Up") or l.startswith("@Down")):
                    content += l + "\n"
                else:
                    section_capture = False

    return content


def _apply_migration(conn, file_path, title, section):
    '''
        @section can be up or down
    '''
    c = get_section(file_path, section)
    if c == '':
        raise RuntimeError("Migration file must contain a migration " + file_path)

    cursor = conn.cursor()
    cursor.execute(c)

    cursor = conn.cursor()
    if section == 'up':
        q = f"INSERT INTO {MAIN_TABLE} (title) VALUES ('{title}')"
    elif section == 'down':
        if title == "init":
            return  # no need to do anything else
        else:
            q = f"DELETE FROM {MAIN_TABLE} WHERE title = '{title}'"
    else:
        raise RuntimeError("_apply_migration: section param only accepts \"up\" or \"down\"")

    cursor.execute(q)
    conn.commit()


def migrate_init__OLD():
    if check_migrations():
        print("./migrate init was already run!")
        sys.exit(1)
    else:
        print("Running migrate init")
        from_path = "base/init_{engine}.sql".format(engine=db.CURRENT_ENGINE)
        print("from_path: " + from_path)

        init_path = MIGRATIONS_PATH + "/init.sql"
        if os.path.islink(init_path):
            os.remove(init_path)
        os.symlink(from_path, init_path)

        _apply_migration(init_path, 'up')

        print("executed")

def get_title(file_path):
    title = os.path.basename(file_path)
    if title.endswith('.sql'):
        title = title[:-4]
    else:
        raise RuntimeError("Migration file name must end with .sql --> Got: " + title)

    # if title!='init':
    #    ar = title.split("_") # file path has <date>_<timestamp>_<file_name>
    #    ix = len(ar[0])+1+len(ar[1])+1+len(ar[2])+1
    #    title = title[ix:]

    return title

def get_migration_files():
    ''' Returns ordered list of migration files excluding init.sql '''

    l0 = os.listdir(MIGRATIONS_PATH)
    l = [ i for i in l0 if not os.path.isdir(MIGRATIONS_PATH + '/' + i) ]
    if len(l) > 0:
        l.sort()
        last = l[-1] # Last is init
        if last!="init.sql":
            raise RuntimeError("Problem with sorting - init should be the last element at this point")
        l = l[:-1] # not including init.sql
        l = ['init.sql'] + l
    
    return l


def is_in_migrations_folder():
    cf = os.getcwd()
    return os.path.basename(cf) == MAIN_FOLDER


def is_bootstrapped(conn, config):
    cursor = conn.cursor()
    cursor.execute(f"""SELECT 1 FROM information_schema.tables 
                        WHERE table_catalog='{config["database"]}' AND 
                              table_schema='{config["schema"]}' AND 
                              table_name='{MAIN_TABLE}'
                    """)
    row = cursor.fetchone()
    return row is not None


def migrate_status():

    # This can only be run when in migrations/
    if not is_in_migrations_folder():
        print(f"You must be in {MAIN_FOLDER}/ folder to run this.")
        sys.exit(1)

    config = migrate_utils.get_config()
    conn = migrate_utils.get_conn(config)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM information_schema.schemata WHERE schema_name = %s", (config['schema'],))
    if not cursor.fetchone():
        print(f"Schema {config['schema']} does not exist!")
        sys.exit(1)


    # Checking if init file exists
    init_path = f"{os.getcwd()}/sql/init.sql"
    if not os.path.exists(init_path):
        # Depending on engine, creating symlink
        src_init_path = f"{os.getcwd()}/sql/base/init_{config['engine']}.sql"
        os.symlink(src_init_path, init_path)

    files = get_migration_files()
    # print("files: " + str(files)) 

    file_lengths = [len(f) for f in files]
    max_len = max(file_lengths)
    if max_len < 20:
        max_len = 20  # min
    elif max_len > 60:
        max_len = 60  # max

    bootstrapped = is_bootstrapped(conn, config)

    cursor = conn.cursor()
    print(f"--{ max_len * '-'} - { 20 * '-'}")  # -------- | -------
    print(f"| Name{(max_len - 4) * ' '} |   Status{11 * ' '}|")
    print(f"--{ max_len * '-'} - { 20 * '-'}")
    for f in files:
        title = get_title(MIGRATIONS_PATH + "/" + f)
        if bootstrapped:
            cursor.execute(f"SELECT * FROM {MAIN_TABLE} WHERE title = '{title}'")
            if cursor.fetchone():
                applied = "Applied   "
            else:
                applied = "Pending..."
        else:
            applied = "Pending..."

        print(f"| {title}{ (max_len - len(title)) * ' '} |   {applied}{ (20 - len(applied) - 3) * ' '}|")
    print(f"--{ max_len * '-'} - { 20 * '-'}")  # ---------- - ----------


def migrate_new(base_title):

    check_cwd_is_migrations_folder()

    ''' Checking if a migration file already exists '''
    base_title_file_name = base_title.replace(" ", "_") + ".sql"
    for i in get_migration_files():
        if i.endswith(base_title_file_name):
            raise RuntimeError("Similar migration file already exists %s" %(i))

    dt = datetime.now()
    title = str(dt.year)
    if dt.month<10:
        title += '0'
    title += str(dt.month)
    if dt.day<10:
        title += '0'
    title += str(dt.day)
    title += '_' + dt.time().isoformat().replace(':', '').replace(".", "_")

    file_path = MIGRATIONS_PATH + '/' + title + '_' + base_title_file_name
    f = open(file_path,  'w+')
    f.write("# Autogenerated: "+ file_path + "\n\n")
    f.write("@Up\n")
    f.write("# Your Up migration goes here\n\n\n")
    f.write("@Down\n")
    f.write("# Your Down migration goes here\n")
    f.close()

    print("Migration file generated %s" %(file_path))


def migrate_up(n):

    check_cwd_is_migrations_folder()

    config = migrate_utils.get_config()
    conn = migrate_utils.get_conn(config)

    migration_files = get_migration_files()

    if n:
        if n > len(migration_files):
            print(f"n cannot be greater than the number of migrations ({len(migration_files)})")
    else:
        n = len(migration_files)

    cursor = conn.cursor()
    was_run = False
    cnt = 1
    for f in migration_files:
        title = get_title(MIGRATIONS_PATH + '/' + f)
        if title == 'init':
            if not is_bootstrapped(conn, config):
                print(f"Applying first migration")
                _apply_migration(conn, MIGRATIONS_PATH + "/" + f, title, 'up')
                was_run = True
                cnt += 1
        else:
            cursor.execute(f"SELECT * FROM {MAIN_TABLE} WHERE title = '{title}'")
            if not cursor.fetchone():
                print("Applying %s" %(f))
                _apply_migration(conn, MIGRATIONS_PATH + "/" + f, title, 'up')
                was_run = True
                cnt += 1  # only counting pending migrations
        
        if cnt > n:
            break

    if not was_run:
        print("Nothing to do")

def migrate_down(n):

    check_cwd_is_migrations_folder()

    config = migrate_utils.get_config()
    conn = migrate_utils.get_conn(config)

    cursor = conn.cursor()
    migration_files = get_migration_files()
    migration_files.reverse() # Reversing the list

    if n:
        if n > len(migration_files):
            print(f"n cannot be greater than the number of migrations ({len(migration_files)})")
            sys.exit(1)
    else:
        n = len(migration_files)

    bootstrapped = is_bootstrapped(conn, config)
    if not bootstrapped:
        print("No migrations to unapply")
        sys.exit(1)

    was_run = False
    cnt = 1
    for f in migration_files:
        title = get_title(MIGRATIONS_PATH + '/' + f)
        if title == 'init':
            print("Undoing %s" %(title))
            _apply_migration(conn, MIGRATIONS_PATH + "/" + f, title, 'down')
            was_run = True
            cnt += 1
        else:
            cursor.execute(f"SELECT * FROM {MAIN_TABLE} WHERE title = '{title}'")
            if cursor.fetchone():
                print("Undoing %s" %(title))
                _apply_migration(conn, MIGRATIONS_PATH + "/" + f, title, 'down')
                was_run = True
                cnt += 1

        if cnt > n:  # only counting pending migrations
            break

    if not was_run:
        print("Nothing to do")

def usage():
    print("""Usage:
    migrate init | status | new <title> | up [<number>] | down [<number>] | help
            """)

def main(argv):
    
    try:

        if len(argv) < 2:
            return usage()
        # Need to check if other commands can be run
        
        # get_migration_files()

        if argv[1] == 'status':
            return migrate_status()
        elif argv[1] == 'new' and len(argv)>2:
            migration_title = '_'.join(argv[2:])
            migrate_new(migration_title)
        elif argv[1] == 'up':
            if len(argv)>2:
                n = argv[2]
                if not n.isdigit() or int(n)<0:
                    raise RuntimeError("In ./migrate up <n>, <n> must be a number and greater than 0")
                else:
                    n = int(n)
            else:
                n = None
            return migrate_up(n)
        elif argv[1]=='down':
            if len(argv)>2:
                n = argv[2]
                if not n.isdigit() or int(n)<0:
                    raise RuntimeError("In ./migrate down <n>, <n> must be a number and greater than 0")
                else:
                    n = int(n)
            else:
                n = 1 # default value!
            return migrate_down(n)

        elif argv[1] == 'init':
            migrate_init()
        else:
            return usage()

    # except SystemError as se:
    #    sys.exit(e.code)

    except SystemExit as se:
        # print(se)
        sys.exit(se.code)
    except:
        raise
        #e, val, tb = sys.exc_info()
        #if e:
        #    traceback.print_exc(val)
        #    # raise Exception("Unable to connect to the database")


if __name__ == '__main__':
    main(sys.argv)
