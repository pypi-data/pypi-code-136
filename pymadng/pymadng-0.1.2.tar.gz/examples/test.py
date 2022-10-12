import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, "/home/joshua/Documents/MADpy/src/pymadng")
from pymadng import MAD

with MAD("/home/joshua/Documents/MADpy/examples", log=True) as mad:
    mad["a"] = np.asarray([1.0, 2, 3, 4, 5])
    mad.sendall()
    print(mad.a)
    mad["circum", "lcell"] = 60, 20
    mad.sendVariables(["circum", "lcell"])
    mad.deferred("v", f="lcell/math.sin(math.pi/4)/4", k="1/v.f")
    mad.multipole(
        "qf", mad.deferedExpr(knl={0, mad.v.k})
    )  # Evaluates deferred expression before function
    mad.multipole("qd", mad.deferedExpr(knl={0, -mad.v.k}))
    mad.sequence(
        "seq",
        mad.qfSet(at=0 * mad.lcell),
        mad.qdSet(at=0.5 * mad.lcell),
        mad.qfSet(at=1 * mad.lcell),
        mad.qdSet(at=1.5 * mad.lcell),
        mad.qfSet(at=2 * mad.lcell),
        mad.qdSet(at=2.5 * mad.lcell),
        refer="centre",
        l=mad.circum,
    )
    mad.beam("beam1")
    mad.seq.beam = mad.beam1
    mad.twiss("mtbl2", sequence=mad.seq, method=4, chrom=True)
    # print(mad.mtbl2.gammatr.a)
    mad.receiveVar("qf")
    print(mad.mtbl2[1])
    mad.mtbl2.method("write", None, "'tfsTable.tfs'")
    mad.writeToProcess("do local a = {b = {c = {d = 3, 1}}}; print(#a.b.c) end")
    print(mad.mtbl2.header)
    # plt.plot(mad.mtbl2.s, mad.mtbl2["beta11"]) #Showing both methods of retrieving variables
    # plt.title("FODO Cell")
    # plt.xlabel("s")
    # plt.ylabel("beta11")
    # plt.show()
