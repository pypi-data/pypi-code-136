def execute():
    import sys
    import time
    import ifcopenshell
    import ifcopenshell.ids as ids

    start = time.time()

    specs = ids.open('/home/dion/ids.xml')
#ifc = ifcopenshell.open('/home/dion/test.ifc')
    ifc = ifcopenshell.open('/home/dion/drive/bim/liverpool/isb/LHAP-AR-FPA-IFC-MW-81B103-0.ifc')

    print("LOADED IN", time.time() - start)
    start = time.time()

    specs.validate(ifc)


    print("RUN IN", time.time() - start)
    start = time.time()

    ids.ConsoleReporter(specs).report()

    print("REPORTED IN", time.time() - start)
    start = time.time()

def profile():
    import cProfile
    import pstats

    cProfile.run("execute()", "blender.prof")
    p = pstats.Stats("blender.prof")
    p.sort_stats("cumulative").print_stats(50)

execute()


