def proc_file_name_author_km_num(tablename):
    # 用python的exec可以把表名作为参数传进来
    global only_author_set
    # only_author_set = ''
    qs_str = f"""global only_author_set
only_author_set = jou_mds.{tablename}.objects.all()
    """
    exec(qs_str)
    print(f'only_author_set是什么呢->{only_author_set}')
    print(f"共{only_author_set.count()}条数据")
    import time
    start = time.time()
    for author in only_author_set:
        author:jou_mds.OnlyAuthorTable
        kan_num = len(set(kna_li))
        author.kan_num = kan_num
    only_author_set.bulk_update(only_author_set, ['kan_num'], batch_size=20000)
    end = time.time()
    print(f"耗时{end-start}")


if __name__ == "__main__":
    # proc_dbf_author()
    # proc_km_num()
    tablename = 'SingleDbfTable'
    proc_file_name_author_km_num(tablename)