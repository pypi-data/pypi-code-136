#!/usr/bin/env python
# coding: utf-8

import sqlite3

from datetime import datetime
from nopea.dbobject import DbObject
from nopea.fields import ForeignKey, DateTimeField


class IsNull:
    """ Used as identifier for NULL values in query_args """

    def __init__(self):
        pass


class SQLiteAdaptor(object):

    PLACEHOLDER = '?'

    def __init__(self, database):
        self.database = database

    def get_connection_and_cursor(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        return connection, cursor

    def execute_query(self, query, query_args):
        connection, cursor = self.get_connection_and_cursor()
        if not query_args:
            cursor.execute(query)
        else:
            query_args = [q for q in query_args if not isinstance(q, IsNull)]
            cursor.execute(query, query_args)
        connection.commit()
        result = cursor.fetchall()

        cursor.execute("""SELECT last_insert_rowid()""")
        last_id = cursor.fetchone()[0]

        connection.close()
        return (result, last_id)

    def get_filter_query(self, filter_partial):
        key, value = list(filter_partial.items())[0]
        if key.endswith('__in'):
            query = ('%s IN (%s)' % (key.replace('__in', ''), ', '.join('?' * len(value))))
        elif key.endswith('__lt'):
            query = '%s < %s' % (key.replace('__lt', ''), '?')
        elif key.endswith('__lte'):
            query = '%s <= %s' % (key.replace('__lte', ''), '?')
        elif key.endswith('__gt'):
            query = '%s > %s' % (key.replace('__gt', ''), '?')
        elif key.endswith('__gte'):
            query = '%s >= %s' % (key.replace('__gte', ''), '?')
        elif key.endswith('__contains'):
            query = '%s LIKE %s' % (key.replace('__contains', ''), '?')
            value = '%' + value + '%'
        elif key.endswith('__startswith'):
            query = '%s LIKE %s || "%%"' % (key.replace('__startswith', ''), '?')
        elif key.endswith('__endswith'):
            query = '%s LIKE "%%" || %s' % (key.replace('__endswith', ''), '?')
        else:
            if value is not None:
                query = '%s=?' % key
            else:
                query = '%s IS NULL' % key
                value = IsNull()
        return query, value

    def get_exclude_query(self, exclude_partial):
        key, value = list(exclude_partial.items())[0]
        if key.endswith('__in'):
            query = ('%s NOT IN (%s)' % (key.replace('__in', ''), ', '.join('?' * len(value))))
        elif key.endswith('__lt'):
            query = '%s >= %s' % (key.replace('__lt', ''), '?')
        elif key.endswith('__lte'):
            query = '%s > %s' % (key.replace('__lte', ''), '?')
        elif key.endswith('__gt'):
            query = '%s <= %s' % (key.replace('__gt', ''), '?')
        elif key.endswith('__gte'):
            query = '%s < %s' % (key.replace('__gte', ''), '?')
        elif key.endswith('__startswith'):
            query = '%s NOT LIKE %s || "%%"' % (key.replace('__startswith', ''), '?')
        elif key.endswith('__endswith'):
            query = '%s NOT LIKE "%%" || %s' % (key.replace('__endswith', ''), '?')
        else:
            if value is not None:
                query = '%s <> ?' % key
            else:
                value = IsNull()
                query = '%s IS NOT NULL' % key
        return query, value

    def get_offset_query(self, offset, limit):
        q = f" OFFSET {offset}"
        if not limit:
            q = " LIMIT -1" + q
        return q

    def get_limit_query(self, limit, offset):
        if offset and offset > 0:
            limit = limit - offset
        return f" LIMIT {limit if limit >=0 else 0}"

    def get_select_query(self, base, *args, **kwargs):
        query = "SELECT %s FROM %s" % (', '.join(base.fieldnames), base.tablename)
        return query

    def get_count_query(self, base, *args, **kwargs):
        query = f'SELECT COUNT(*) FROM "{base.tablename}"'
        return query

    def get_insert_query(self, base, create_partial):
        values = []
        for field in base.fields:
            value = create_partial.get(field.fieldname)
            if isinstance(value, DbObject):
                value = value.id
            if value is None:
                try:
                    value = field.default
                    if hasattr(field.default, '__call__'):
                        value = field.default()
                except AttributeError:
                    pass
            values.append(value)
        query = "INSERT INTO %s (%s) VALUES (%s)" % (base.tablename,
                                                     ', '.join(base.fieldnames),
                                                     ', '.join(['?' for item in base.fields]))
        return (query, tuple(values))

    def get_delete_query(self, base):
        query = "DELETE FROM %s " % base.tablename
        return query

    def get_update_query(self, base, update_partial):
        values = []
        affected_fields = []
        settings = ''
        for field in base.fields:
            value = update_partial.get(field.fieldname)
            if not value:
                pass
            else:
                values.append(value)
                affected_fields.append(field.fieldname)

        settings = ', '.join(['%s=?' % item for item in affected_fields])
        query = "UPDATE %s SET %s " % (base.tablename, settings)
        return (query, tuple(values))

    def bulk_create(self, objects, base):
        max_params = 999
        max_inserts_per_query = int(max_params / len(base.fieldnames))
        iterations = (len(base.fieldnames) * len(objects)) / max_params

        lower = 0
        for i in range(0, int(iterations) + 1):
            lower = int(i * max_inserts_per_query)
            upper = int(lower + max_inserts_per_query)
            query, query_args = self.get_bulk_insert_query(objects[lower:upper], base)
            self.execute_query(query, query_args)

    def get_bulk_insert_query(self, objects, base):
        values = [tuple(getattr(item, fieldname) for fieldname in item.fieldnames) for item in objects]
        placeholders = ', '.join(['(%s)' % (', '.join("?" * len(item))) for item in values])
        query = '''INSERT INTO "%s" (%s) VALUES %s''' % (base.tablename, ', '.join(base.fieldnames), placeholders)
        return (query, tuple(v for tupl in values for v in tupl))

    def get_create_table_query(self, base, tablename):
        if not tablename:
            tablename = base.tablename
        query = "CREATE TABLE %s (%%s);" % tablename
        fk_fields = []
        fields = []
        fieldnames = []
        for field in base.fields:
            if isinstance(field, ForeignKey):
                fk_fields.append(field)
            fields.append(field)
            fieldnames.append(field.fieldname)

        field_queries = [field.partial_create_table_query for field in fields]

        for field in fk_fields:
            fieldnames.append(field.fieldname)
        field_queries.extend([field.partial_create_table_query_extension for field in fk_fields])

        query = query % ', '.join(field_queries)
        query = query % tuple(fieldnames)
        return (query, None)

    def get_drop_table_query(self, base, tablename):
        if not tablename:
            tablename = base.tablename
        query = "DROP TABLE %s;" % tablename
        return (query, None)

    def get_drop_column_query(self, field, base):
        tablename = base.tablename
        fieldnames = base.fieldnames
        fieldnames.remove(field.fieldname)
        delattr(base, field.fieldname)
        queries_1 = ["CREATE TABLE t_backup({0})".format(', '.join(fieldnames)),
                     "INSERT INTO t_backup SELECT {0} FROM {1}".format(', '.join(fieldnames), tablename),
                     "DROP TABLE {0}".format(tablename)]

        queries_2 = ["INSERT INTO {1} SELECT {0} FROM t_backup".format(', '.join(fieldnames), tablename),
                     "DROP TABLE t_backup",
                     "VACUUM"]
        for query in queries_1:
            self.execute_query(query, None)

        base.create_table()

        for query in queries_2:
            self.execute_query(query, None)
        return "SELECT NULL"

    def get_pkfield_create_query(self):
        return '%s INTEGER PRIMARY KEY AUTOINCREMENT'

    def get_integer_field_create_query(self, field):
        query = '%s INTEGER'
        if field.default is not None:
            query += ' DEFAULT %s' % field.default
        return query

    def get_integer_field_create_column_query(self, field):
        query = 'ALTER TABLE %%s ADD COLUMN %s INTEGER' % field.fieldname
        if field.default is not None:
            query += ' DEFAULT %s' % field.default
        return query

    def get_char_field_create_query(self, field):
        query = '%%s CHAR(%s)' % field.max_length
        if field.default is not None:
            query += ' DEFAULT "%s"' % field.default
        return query

    def get_charfield_create_column_query(self, field):
        query = 'ALTER TABLE %%s ADD COLUMN %s CHAR(%s)' % (field.fieldname, field.max_length)
        if field.default is not None:
            query += ' DEFAULT "%s"' % field.default
        return query

    def get_text_field_create_query(self, field):
        query = '%s TEXT'
        if field.default is not None:
            query += ' NOT NULL DEFAULT "%s"' % field.default
        return query

    def get_text_field_create_column_query(self, field):
        query = 'ALTER TABLE %%s ADD COLUMN %s TEXT' % (field.fieldname)
        if field.default is not None:
            query += ' NOT NULL DEFAULT "%s"' % field.default
        return query

    def get_datetime_field_create_query(self, default):
        if default is None:
            default = 'NULL'
        elif default == 'now':
            default = 'CURRENT_TIMESTAMP'
        return '%%s TIMESTAMP DEFAULT %s' % default

    def get_boolean_field_create_query(self, default):
        return '%%s TINYINT DEFAULT %s' % default

    def get_boolean_field_create_column_query(self, field):
        query = 'ALTER TABLE %%s ADD COLUMN %s TINYINT DEFAULT %s' % (field.fieldname, field.default)
        return query

    def get_foreignkey_field_create_query_base(self):
        return '%s INTEGER'

    def get_foreignkey_field_create_query_extension(self, reference, on_delete=''):
        if on_delete != '':
            on_delete = ' ON DELETE %s' % on_delete.upper()
        if type(DbObject) == type(reference):
            reference = reference.tablename
        return 'FOREIGN KEY(%%s) REFERENCES "%s"(id)%s' % (reference, on_delete)

    def create_migration_table(self):
        query = """CREATE TABLE IF NOT EXISTS nopea_migrations
                    (name CHAR(250), id INTEGER PRIMARY KEY AUTOINCREMENT)"""
        self.execute_query(query, None)

    def get_done_migrations(self):
        query = "SELECT id, name FROM nopea_migrations"
        return self.execute_query(query, None)

    def insert_migration(self, name):
        query = "INSERT INTO nopea_migrations (name) VALUES (?)"
        return self.execute_query(query, (name,))
