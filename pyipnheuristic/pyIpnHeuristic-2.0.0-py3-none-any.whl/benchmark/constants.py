PROBLEM_G01: str = r"""## Problem G01:
Minimize: 
$$f(\mathbf{x}) = 5\sum_{i=1}^{4} x_i - 5 \sum_{i=1}^{4} x_i^2 - \sum_{i=5}^{13} x_i$$
subject to:
$$g_1(\mathbf{x}) = 2 x_1 + 2 x_2 + x_{10} + x_{11} - 10 \leq 0 $$
$$g_2(\mathbf{x}) = 2 x_1 + 2 x_2 + x_{10} + x_{12} - 10 \leq 0 $$
$$g_3(\mathbf{x}) = 2 x_2 + 2 x_3 + x_{11} + x_{12} - 10 \leq 0 $$
$$g_4(\mathbf{x}) = -8x_1 + x_{10} \leq 0 $$
$$g_5(\mathbf{x}) = -8x_2 + x_{11} \leq 0 $$
$$g_6(\mathbf{x}) = -8x_3 + x_{12} \leq 0 $$
$$g_7(\mathbf{x}) = -2x_4 -x_5 + x_{10} \leq 0 $$
$$g_8(\mathbf{x}) = -2x_6 -x_7 + x_{11} \leq 0 $$
$$g_9(\mathbf{x}) = -2x_8 -x_9 + x_{12} \leq 0 $$
where: $0 \leq x_i \leq 1$ ($i=1,\ldots.9,13$) and $0 \leq x_i \leq 100$ ($i=10,11,12$)"""

PROBLEM_G02: str = r"""## Problem G02:
Minimize: 
$$f(\mathbf{x}) = -\left| \frac{\sum_{i=1}^{n}\cos^{4}({x_i}) - 
2\prod_{i=1}^{n}\cos^2(x_i)}{\sqrt{\sum_{i=1}^{n}i x_{i}^{2}}} \right|$$
subject to:
$$g_1(\mathbf{x}) = 0.75 - \prod_{i=1}^{n} x_i \leq 0 $$
$$g_2(\mathbf{x}) = \sum_{i=1}^{n} x_i - 7.5n \leq 0 $$
where: $n=20$ and $0 \leq x_i \leq 10$ $(i=1, \ldots, n)$"""

PROBLEM_G03: str = r"""## Problem G03:
Minimize: 
$$f(\mathbf{x}) = - \left( \sqrt{n}\right)^{n} \prod_{i=1}^{n} x_i$$
subject to:
$$h_1(\mathbf{x}) = \sum_{i=1}^{n} x_i^{2} - 1 = 0$$
where: $n=10$ and $0 \leq x_i \leq 1$ $(i=1, \ldots, n)$"""

PROBLEM_G04: str = r"""## Problem G04:
Minimize:
$$f(\mathbf{x}) = 5.3575847 x_3^{2} + 0.835689 x_1 x_5 + 37.293239 x_1 - 40792.141$$
subject to:
$$g_1(\mathbf{x}) = 85.334407 + 0.0056858x_2 x_5 + 0.0006262x_1 x_4 - 0.0022053x_3 x_5 - 92 \leq 0$$
$$g_2(\mathbf{x}) = -85.334407 - 0.0056858x_2 x_5 - 0.0006262x_1 x_4 + 0.0022053x_3 x_5 \leq 0$$
$$g_3(\mathbf{x}) = 80.51249 + 0.0071317x_2 x_5 + 0.0029955x_1 x_2 + 0.0021813x_3^{2} - 110 \leq 0$$
$$g_4(\mathbf{x}) = -80.51249 - 0.0071317x_2 x_5 - 0.0029955x_1 x_2 - 0.0021813x_3^{2} + 90 \leq 0$$
$$g_5(\mathbf{x}) = 9.300961 + 0.0047026x_3 x_5 + 0.0012547x_1 x_3 + 0.0019085x_3 x_4 - 25 \leq 0$$
$$g_6(\mathbf{x}) = -9.300961 - 0.0047026x_3 x_5 - 0.0012547x_1 x_3 - 0.0019085x_3 x_4 + 20 \leq 0$$
where: $78 \leq x_1 \leq 102$, $33 \leq x_2 \leq 45$ and $27 \leq x_i \leq 45$ $(i=3,4,5)$"""

PROBLEM_G05: str = r"""## Problem G05:
Minimize: 
$$f(\mathbf{x}) = 3x_1 + 0.000001x_1^{3} + 2x_2 + (0.000002/3)x_2^{3} $$
subject to:
$$g_1(\mathbf{x}) = -x_4 + x_3 -0.55 \leq 0$$
$$g_2(\mathbf{x}) = -x_3 + x_4 -0.55 \leq 0$$
$$h_1(\mathbf{x}) = 1000 \sin(-x_3 - 0.25) + 1000 \sin(x_4 - 0.25) + 894.8 - x_1 = 0$$
$$h_2(\mathbf{x}) = 1000 \sin(x_3 - 0.25) + 1000 \sin(x_3 - x_4 - 0.25) + 894.8 - x_2 = 0$$
$$h_3(\mathbf{x}) = 1000 \sin(x_4 - 0.25) + 1000 \sin(x_4 - x_3 - 0.25) + 1294.8 = 0$$
where: $0 \leq x_i \leq 1200$ $(i=1,2)$ and $-0.55 \leq x_i \leq 0.55$ $(i=3,4)$"""

PROBLEM_G06: str = r"""## Problem G06:
Minimize: 
$$f(\mathbf{x}) = (x_1 - 10)^3 + (x_2 - 20)^3$$
subject to:
$$g_1(\mathbf{x}) = -(x_1-5)^2 - (x_2-5)^2 + 100 \leq 0 $$
$$g_2(\mathbf{x}) = (x_1-6)^2 + (x_2-5)^2 - 82.81 \leq 0 $$
where: $13 \leq x_1 \leq 100$, $0 \leq x_2 \leq 100$"""

PROBLEM_G07: str = r"""## Problem G07:
Minimize:
$$f(\mathbf{x}) = x_1^{2} + x_2^{2} + x_1 x_2 - 14x_1 -16x_2 
+ (x_3 - 10)^{2} + 4(x_4 - 5)^{2} + (x_5 -3)^{2} + 2(x_6-1)^{2}
+ 5x_7^{2} + 7(x_8 - 11)^{2} + 2(x_9 - 10)^2 + (x_{10} -7)^2 + 45
$$
subject to:
$$g_1(\mathbf{x}) = -105 + 4x_1 + 5x_2 - 3x_7 + 9x_8 \leq 0$$
$$g_2(\mathbf{x}) = 10x_1 - 8x_2 - 17x_7 + 2x_8 \leq 0$$
$$g_3(\mathbf{x}) = -8x_1 + 2x_2 + 5x_9 - 2x_{10} - 12 \leq 0$$
$$g_4(\mathbf{x}) = 3(x_1 -2)^{2} + 4(x_2 - 3)^{2} + 2x_3^{2} - 7x_4 - 120 \leq 0$$
$$g_5(\mathbf{x}) = 5x_1^{2} + 8x_2 + (x_3 - 6)^{2} - 2x_4 - 40 \leq 0$$
$$g_6(\mathbf{x}) = x_1^{2} + 2(x_2 - 2)^{2} - 2x_1 x_2 + 14x_5 - 6x_6 \leq 0$$
$$g_7(\mathbf{x}) = 0.5(x_2-8)^2 + 2(x_2 -4)^2 - 3x_5^{2} -x_6 - 30 \leq 0$$
$$g_8(\mathbf{x}) = -3x_1 + 6x_2 + 12(x_9 - 8)^{2} - 7x_{10} \leq 0$$
where: $-10 \leq x_i \leq 10$ $(i=1,\ldots,10)$"""

PROBLEM_G08: str = r"""## Problem G08
Minimize:
$$f(\mathbf{x}) = - \frac{ \sin^{3}(2\pi x_1) \sin (2\pi x_2) }{ x_1^{3} (x_1 + x_2) }$$
subject to:
$$g_1 (\mathbf{x}) = x_1^{2} - x_2 + 1 \leq 0$$
$$g_2 (\mathbf{x}) = 1 - x_1 + (x_2 - 4)^{2} \leq 0$$
where: $0 \leq x_1 \leq 10$ and $0 \leq x_2 \leq 10$"""

PROBLEM_G09: str = r"""## Problem G09
Minimize:
$$f(\mathbf{x}) = (x_1 - 10)^2 + 5 (x_2 -12)^2 + x_3^{4} + 3(x_4 - 11)^2
+ 10 x_5^{6} + 7x_6^{2} + x_7^{4} - 4x_6 x_7 - 10x_6 - 8x_7
$$
subject to:
$$g_1 (\mathbf{x}) = -127 + 2x_1^{2} 3x_2^{4} + x_3 + 4x_4^{2} + 5x_5 \leq 0$$
$$g_2 (\mathbf{x}) = -282 + 7x_1 + 3x_2 + 10x_3^{2} + x_4 - x_5 \leq 0$$
$$g_3 (\mathbf{x}) = -196 + 23x_1 + x_2^{2} + 6x_6^{2} - 8x_7 \leq 0$$
$$g_4 (\mathbf{x}) = 4x_1^{2} + x_2^{2} - 3x_1 x_2 + 2x_3^{2} + 5x_6 - 11x_7 \leq 0$$
where: $-10 \leq x_1 \leq 10$ ($i=1,\ldots,7$)"""

PROBLEM_G10: str = r"""## Problem G10
Minimize:
$$f(\mathbf{x}) = x_1 + x_2 + x_3$$
subject to:
$$g_1 (\mathbf{x}) = -1 + 0.0025 (x_4 + x_6) \leq 0$$
$$g_2 (\mathbf{x}) = -1 + 0.0025 (x_5 + x_7 - x_4) \leq 0$$
$$g_3 (\mathbf{x}) = -1 + 0.01 (x_8 - x_5) \leq 0$$
$$g_4 (\mathbf{x}) = -x_1 x_6 + 833.33252x_4 + 100x_1 - 83333.333 \leq 0$$
$$g_5 (\mathbf{x}) = -x_1 x_7 + 1250 x_5 + x_2 x_4 - 1250 x_4 \leq 0$$
$$g_6 (\mathbf{x}) = -x_3 x_8 + 1250000 + x_3 x_5 - 2500 x_5 \leq 0$$
where: $100 \leq x_1 \leq 10000$, $1000 \leq x_i \leq 10000$ ($i=2,3$) and
$10 \leq x_i \leq 1000$ ($i=4,\ldots,8$)"""

PROBLEM_G11: str = r"""## Problem G11:
Minimize: 
$$f(\mathbf{x}) = x_1^{2} + (x_{2} - 1)^{2}$$
subject to:
$$h_1(\mathbf{x}) = x_2 -x_{1}^{2} \leq 0 $$
where: $-1 \leq x_1 \leq 1$, $-1 \leq x_2 \leq 1$"""

PROBLEM_G12: str = r"""## Problem G12
Minimize: 
$$f(\mathbf{x}) = -(100 - (x_1 - 5)^{2} - (x_2 - 5)^{2} - (x_3 - 5)^{2}) / 100$$
subject to:
$$g_1(\mathbf{x}) = (x_1 - p)^{2} + (x_2 - q)^{2} + (x_3 - r)^{2} - 0.0625 \leq 0 $$
where: $0 \leq x_i \leq 10$ ($i=1,2,3$) and $p,q,r = 1,2,\ldots,9$"""

PROBLEM_G13: str = r"""## Problem G13
Minimize:
$$f(\mathbf{x}) = e^{x_1 x_2 x_3 x_4 x_5}$$
subject to:
$$h_1 (\mathbf{x}) = x_1^{2} + x_2^{2} + x_3^{2} + x_4^{2} + x_5^{2} - 10 = 0$$
$$h_2 (\mathbf{x}) = x_2 x_3 - 5 x_4 x_5 = 0$$
$$h_3 (\mathbf{x}) = x_1^{3} + x_2^{3} + 1 = 0$$
where: $-2.3 \leq x_i \leq 2.3$ ($i=1,2$) and $-3.2 \leq x_i \leq 3.2$ ($i=3,4,5$)"""

PROBLEM_G14: str = r"""## Problem G14
Minimize:
$$f(\mathbf{x}) = \sum_{i=1}^{10} x_i \left( c_i + \ln \frac{x_i}{\sum_{j=1}^{10} x_j} \right)$$
subject to:
$$h_1(\mathbf{x}) = x_1 + 2 x_2 + 2 x_3 + x_6 + x_{10} - 2 = 0 $$
$$h_2(\mathbf{x}) = x_4 + 2 x_5 + x_6 + x_7 - 1 = 0 $$
$$h_3(\mathbf{x}) = x_3 + x_7 + x_8 + 2 x_9 + x_{10} - 1 = 0 $$
where: $0 < x_i \leq 10$ ($i=1,\ldots,10$) and $c_1 = -6.089$, $c_2 = -17.164$, $c_3 = -34.054$,
$c_4 = -5.914$, $c_5 = -24.721$, $c_6 = -14.986$, $c_7 = -24.1$, $c_8 = -10.708$, $c_9 = -26.662$ and
$c_{10} = -22.179$"""

PROBLEM_G14_PARAMETERS: list = [-6.089, -17.164, -34.054, -5.914, -24.721,
                                -14.986, -24.1, -10.708, -26.662, -22.179]

PROBLEM_G15: str = r"""## Problem G15
Minimize:
$$f(\mathbf{x}) = 1000 - x_1^{2} - 2x_2^{2} - x_3^{2} - x_1 x_2 - x_1 x_3$$
subject to:
$$h_1(\mathbf{x}) = x_1^{2} + x_2^{2} + x_3^{2} - 25 = 0 $$
$$h_2(\mathbf{x}) = 8x_1 + 14x_2 + 7x_3 - 56 = 0 $$
where: $0 < x_i \leq 10$ ($i=1,2,3$)"""

PROBLEM_G16: str = r"""## Problem G16
Minimize:
$$ f(\mathbf{x}) = 0.000117 y_14 + 0.1365 + 0.00002358 y_13 + 0.000001502 y_16 +
0.0321 y_12 + 0.004324 c_5 + 0.0001 c_15 / c_16 +
37.84 c_2 / c_12 - 0.0000005843 y_17 $$
subject to:
$$ g_1 (\mathbf{x}) = (0.28 / 0.72) y_5 - y_4 \leq 0$$
$$ g_2 (\mathbf{x}) = x_3 - 1.5 x_2 \leq 0$$
$$ g_3 (\mathbf{x}) = 3496 y_2 / c_{12} - 21 \leq 0$$
$$ g_4 (\mathbf{x}) = 110.6 + y_1- 62212 / c_{17} \leq 0$$
$$ g_5 (\mathbf{x}) = 213.1 - y_1 \leq 0 $$
$$ g_6(\mathbf{x}) = y_1 - 405.23 \leq 0 $$
$$ g_7(\mathbf{x}) = 17.505 - y_2 \leq 0 $$
$$ g_8 (\mathbf{x}) = y_2 - 1053.6667 \leq 0 $$
$$ g_9(\mathbf{x}) = 11.275 - y_3 \leq 0 $$
$$ g_{11}(\mathbf{x}) = 214.228 - y_4 \leq 0 $$
$$ g_{12} (\mathbf{x}) = y_4 - 665.585 \leq 0 $$
$$ g_{13}(\mathbf{x}) = 7.458 - y_5 \leq 0 $$ 
$$ g_{14}(\mathbf{x}) = y_5 - 584.463 \leq 0 $$
$$ g_{15} (\mathbf{x}) = 0.961 - y_6 \leq 0 $$ 
$$ g_{16}(\mathbf{x}) = y_6 - 265.916 \leq 0 $$ 
$$ g_{10}(\mathbf{x}) = y_3 - 35.03 \leq 0 $$
$$ g_{17} (\mathbf{x}) = 1.612 - y_7 \leq 0 $$ 
$$ g_{18}(\mathbf{x}) = y_7 - 7.046 \leq 0 $$ 
$$ g_{19}(\mathbf{x}) = 0.146 - y_8 \leq 0 $$
$$ g_{20} (\mathbf{x}) = y_8 - 0.222 \leq 0 $$ 
$$ g_{21}(\mathbf{x}) = 107.99 - y_9 \leq 0 $$
$$ g_{22}(\mathbf{x}) = y_9 - 273.366 \leq 0 $$
$$ g_{23} (\mathbf{x}) = 922.693 - y_{10} \leq 0 $$ 
$$ g_{24}(\mathbf{x}) = y_{10} - 1286.105 \leq 0 $$
$$ g_{25} (\mathbf{x}) = 926.832 - y_{11} \leq 0 $$ 
$$ g_{26} (\mathbf{x}) = y_{11} - 1444.046 \leq 0 $$
$$ g_{27} (\mathbf{x}) = 18.766 - y_{12} \leq 0 $$
$$ g_{28}(\mathbf{x}) = y_{12} - 537.141 \leq 0 $$ 
$$ g_{29} (\mathbf{x}) = 1072.163 - y_{13} \leq 0 $$
$$ g_{30}(\mathbf{x}) = y_{13} - 3247.039 \leq 0 $$
$$ g_{31} (\mathbf{x}) = 8961.448 - y_{14} \leq 0 $$
$$ g_{32} (\mathbf{x}) = y_{14} - 26844.086 \leq 0 $$
$$ g_{33} (\mathbf{x}) = 0.063 - y_{15} \leq 0 $$ 
$$ g_{34}(\mathbf{x}) = y_{15} - 0.386 \leq 0 $$
$$ g_{35} (\mathbf{x}) = 71084.33 - y_{16} \leq 0 $$ 
$$ g_{36}(\mathbf{x}) = -140000 + y_{16} \leq 0 $$
$$ g_{37} (\mathbf{x}) = 2802713 - y_{17} \leq 0 $$
$$ g_{38} (\mathbf{x}) = y_{17} - 12146108 \leq 0 $$
where: $y_1 = x_2 + x_3 + 41.6$, $c_1 = 0.024 x_4 - 4.62$, $y_2 = 12.5 / c_1 + 12$,
$c_2 = 0.0003535 x_1^{2} + 0.5311 x_1 + 0.08705 y_2 x_1$,
$c_3 = 0.052 x_1 + 78 + 0.002377 y_2 x_1$, $y_3 = c_2 / c_3$, $y_4 = 19 y_3$,
$c_4 = 0.04782 (x_1 - y_3) + 0.1956 (x_1 - y_3^{2} / (x_2) + 0.6376 y_4 + 1.594 y_3$, $c_5 = 100 x_2$,
$c_6 = x_1 - y_3 - y_4$, $c_7 = 0.950 - c_4 / c_5$, $y_5 = c_6 c_7$, $y_6 = x_1 - y_5 - y_4 - y_3$,
$c_8 = (y_5 + y_4) 0.995$, $y_7 = c_8 / y_1$, $y_8 = c_8 / 3798$, $c_9 = y_7 - 0.0663 y_7 / y_8 - 0.3153$,
$y_9 = 96.82 / c_9 + 0.321 y_1$, $y_{10} = 1.29 y_5 + 1.258 y_4 + 2.29 y_3 + 1.71 y_6$,
$y_{11} = 1.71 x_1 - 0.452 y_4 + 0.580 y_3$, $c_{10} = 12.3 / 752.3$, $c_{11} = (1.75 y_2 ) (0.995 x_1)$,
$c_{12} = 0.995 y_{10} + 1998$, $y_{12} = c_{10} x_1 + c_{11} / c_{12}$, $y_{13} = c_{12} - 1.75 y_2$,
$y_{14} = 3623 + 64.4 x_2 + 58.4 x_3 + 146312 / (y_9 + x_5)$, 
$c_{13} = 0.995 y_{10} + 60.8 x_2 + 48 x_4 - 0.1121 y_{14} - 5095$, $y_{15} = y_{13} / c_{13}$,
$y_{16} = 148000 - 331000 y_{15} + 40 y_{13} - 61 y_{15} y_{13}$,
$c_{14} = 2324 y_{10} - 28740000 y_2$, $y_{17} = 14130000 - 1328 y_{10} - 531 y_{11} + c_{14} / c_{12}$,
$c_{15} = y_{13} / y_{15} - y_{13} / 0.52$, $c_{16} = 1.104 - 0.72 y_{15}$, $c_{17} = y_9 + x_5$ and
$704.4148 \leq x 1 \leq 906.3855$, $68.6 \leq x 2 \leq 288.88$, $0 \leq x 3 \leq 134.75$, $193 \leq x 4 \leq 287.0966$
and $25 \leq x 5 \leq 84.1988$"""

PROBLEM_G17: str = r"""## Problem G17
Minimize:
$$f(\mathbf{x}) = f_1(x_1) + f_2(x_2)$$
where:
$$ f_1(x_1) = \left\lbrace \begin{array}{l l}
30 x_1 & 0\leq x_1 < 300 \\
31x_1 & 300 \leq x_1 < 400 \end{array} \right. $$

$$ f_2(x_2) = \left\lbrace \begin{array}{l l}
28 x_2 & 0\leq x_2 < 100 \\
29 x_2 & 100\leq x_2 < 200 \\
30 x_2 & 200\leq x_2 < 1000 \end{array} \right. $$
subject to:
$$h_1(\mathbf{x}) = - x_1 + 300 - \frac{x_3 x_4}{131.078} \cos (1.48477 - x_6) + 
\frac{0.90798 x_3^{2}}{131.078} \cos (1.47588) = 0 $$
$$h_2(\mathbf{x}) = - x_2 - \frac{x_3 x_4}{131.078} \cos (1.48477 + x_6) + 
\frac{0.90798 x_4^{2}}{131.078} \cos (1.47588) = 0 $$
$$h_3(\mathbf{x}) = - x_5 - \frac{x_3 x_4}{131.078} \sin (1.48477 + x_6) + 
\frac{0.90798 x_4^{2}}{131.078} \sin (1.47588) = 0 $$
$$h_4(\mathbf{x}) = 200 - \frac{x_3 x_4}{131.078} \sin (1.48477 - x_6) + 
\frac{0.90798 x_3^{2}}{131.078} \sin (1.47588) = 0 $$

where: $0 \leq x_1 \leq 300$, $0 \leq x_2 \leq 1000$, $340 \leq x_3 \leq 420$,
$340 \leq x_4 \leq 420$, $-1000 \leq x_5 \leq 1000$ and $0 \leq x_6 \leq 0.5236$"""

PROBLEM_G18: str = r"""## Problem G18
Minimize:
$$f(\mathbf{x}) = -0.5 (x_1 x_4 - x_2 x_3 + x_3 x_9 - x_5 x_9 + x_5 x_8 - x_6 x_7)$$
subject to:
$$g_1(\mathbf{x}) = x_3^{2} + x_4^{2} - 1 \leq 0$$
$$g_2(\mathbf{x}) = x_9^{2} - 1 \leq 0$$
$$g_3(\mathbf{x}) = x_5^{2} + x_6^{2} - 1 \leq 0$$
$$g_4(\mathbf{x}) = x_1^{2} + (x_2 - x_9)^{2} - 1 \leq 0$$
$$g_5(\mathbf{x}) = (x_1 - x_5)^{2} + (x_2 - x_6)^{2} - 1 \leq 0$$
$$g_6(\mathbf{x}) = (x_1 - x_7)^{2} + (x_2 - x_8)^{2} - 1 \leq 0$$
$$g_7(\mathbf{x}) = (x_3 - x_5)^{2} + (x_4 - x_6)^{2} - 1 \leq 0$$
$$g_8(\mathbf{x}) = (x_3 - x_7)^{2} + (x_4 - x_8)^{2} - 1 \leq 0$$
$$g_9(\mathbf{x}) = x_7^{2} + (x_8 - x_9)^{2} - 1 \leq 0$$
$$g_10(\mathbf{x}) = x_2 x_3 - x_1 x_4 \leq 0$$
$$g_11(\mathbf{x}) = - x_3 x_9 \leq 0$$
$$g_12(\mathbf{x}) = x_5 x_9 \leq 0$$
$$g_13(\mathbf{x}) = x_6 x_7 - x_5 x_8 \leq 0$$
where: $-10 \leq x_i \leq 10$ ($i=1,\ldots,8$) and $0 \leq x_9 \leq 20$"""

PROBLEM_G19: str = r"""## Problem G19
Minimize:
$$f(\mathbf{x}) = \sum_{j=1}^{5} \sum_{i=1}^{5} c_{i,j} x_{10+i} x_{10+j} +
2 \sum_{j=1}^{5} d_j x_{10+j}^{3} - \sum_{i=1}^{10} b_i x_i$$
subject to:
$$g_j(\mathbf{x}) = - 2 \sum_{i=1}^{5} c_{i,j} x_{10+i} - 3 d_j x_{10+j}^{2} -  
e_{j} + \sum_{i=1}^{10} a_{i,j} x_i \leq 0 \ \ \ j=1,\ldots,5$$
where: $0 \leq x_i \leq 10$ ($i=1,\ldots,15$)"""

PROBLEM_G19_PARAMETERS: dict = {
    "b": [-40, -2, -0.25, -4, -4, -1, -40, -60, 5, 1],
    "e": [-15, -27, -36, -18, -12],
    "c": [
        [30, -20, -10, 32, -10],
        [-20, 39, -6, -31, 32],
        [-10, -6, 10, -6, -10],
        [32, -31, -6, 39, -20],
        [-10, 32, -10, -20, 30]
    ],
    "d": [4, 8, 10, 6, 2],
    "a": [
        [-16, 2, 0, 1, 0],
        [0, -2, 0, 0.4, 2],
        [-3.5, 0, 2, 0, 0],
        [0, -2, 0, -4, -1],
        [0, -9, -2, 1, -2.8],
        [2, 0, -4, 0, 0],
        [-1, -1, -1, -1, -1],
        [-1, -2, -3, -2, -1],
        [1, 2, 3, 4, 5],
        [1, 1, 1, 1, 1]
    ]
}

PROBLEM_G20: str = r"""## Problem G20
Minimize:
$$f(\mathbf{x}) = \sum_{i=1}^{24} a_i x_i$$
subject to:
$$g_i(\mathbf{x}) = \frac{x_i + x_{i+12}}{\sum_{j=1}^{24} x_j + e_i} \leq 0 \ \ \ j=1,2,3$$
$$g_i(\mathbf{x}) = \frac{x_{i+3} + x_{i+15}}{\sum_{j=1}^{24} x_j + e_i} \leq 0 \ \ \ j=4,5,6$$
$$h_i(\mathbf{x}) = \frac{x_{i+12}}{b_{i+12}\sum_{j=13}^{24}\frac{x_j}{b_j}} -
\frac{c_i x_i}{40 b_i \sum_{j=1}^{12} \frac{x_j}{b_j}} = 0 \ \ \ j=1,\ldots,12$$
$$h_13(\mathbf{x}) = \sum_{i=1}^{24} x_i - 1 = 0$$
$$h_14(\mathbf{x}) = \sum_{i=1}^{12} \frac{x_i}{d_i} + k \sum_{i=13}^{24} \frac{x_i}{b_i} - 1.671 = 0$$
where: $0 \leq x_i \leq 10$ ($i=1,\ldots,15$)"""

PROBLEM_G20_PARAMETERS: dict = {
    "a": [0.0693, 0.0577, 0.05, 0.2, 0.26,
          0.55, 0.06, 0.1, 0.12, 0.18, 0.1, 0.09,
          0.0693, 0.0577, 0.05, 0.2, 0.26, 0.55,
          0.06, 0.1, 0.12, 0.18, 0.1, 0.09],
    "b": [44.094, 58.12, 58.12, 137.4, 120.9,
          170.9, 62.501, 84.94, 133.425, 82.507,
          46.07, 60.097, 44.094, 58.12, 58.12,
          137.4, 120.9, 170.9, 62.501, 84.94,
          133.425, 82.507, 46.07, 60.097],
    "c": [123.7, 31.7, 45.7, 14.7, 84.7, 27.7,
          49.7, 7.1, 2.1, 17.7, 0.85, 0.64],
    "d": [31.244, 36.12, 34.784, 92.7, 82.7, 91.6,
          56.708, 82.7, 80.8, 64.517, 49.4, 49.1],
    "e": [0.1, 0.3, 0.4, 0.3, 0.6, 0.3],
    "k": 0.7302 * 530. * 14.7 / 40
}

PROBLEM_G21: str = r"""## Problem G21
Minimize:
$$f(\mathbf{x}) = x_1$$
subject to:
$$g_1(\mathbf{x}) = - x_1 + 35 x_2^{0.6} + 35 x_3^{0.6} \leq 0 $$
$$h_1(\mathbf{x}) = - 300 x_3 + 7500 x_5 - 7500 x_6 - 25 x_4 x_5 + 25 x_4 x_6 + x_3 x_4 = 0$$
$$h_2(\mathbf{x}) = 100 x_2 + 155.365 x_4 + 2500 x_7 - x_2 x_4 - 25 x_4 x_7 - 15536.5 = 0$$
$$h_3(\mathbf{x}) = - x_5 + \ln (- x_4 + 900) = 0$$
$$h_4(\mathbf{x}) = - x_6 + \ln (x_4 + 300) = 0$$
$$h_5(\mathbf{x}) = - x_7 + \ln (- 2 x_4 + 700) = 0$$
where: $0 \leq x_1 \leq 1000$, $0 \leq x_2, x_3 \leq 40$, $100 \leq x_4 \leq 300$, 
$6.3 \leq x_5 \leq 6.7$, $5.9 \leq x_6 \leq 6.4$ and $4.5 \leq x_7 \leq 6.25$"""

PROBLEM_G22: str = r"""## Problem G22
Minimize:
$$f(\mathbf{x}) = x_1$$
subject to:
$$g_1(\mathbf{x}) = -x_1 + x_2^{0.6} + x_3^{0.6} + x_4^{0.6} \leq 0$$
$$h_1(\mathbf{x}) = x_5 - 100000 x_8 + 10^{7} = 0$$
$$h_2(\mathbf{x}) = x_6 + 100000 x_8 - 100000 x_9 = 0$$
$$h_3(\mathbf{x}) = x_7 + 100000 x_9 - 5 \times 10^7 = 0$$
$$h_4(\mathbf{x}) = x_5 + 100000 x_{10} - 3.3 \times 10^7 = 0$$
$$h_5(\mathbf{x}) = x_6 + 100000 x_{11} - 4.4 \times 10^7 = 0$$
$$h_6(\mathbf{x}) = x_7 + 100000 x_{12} - 6.6 \times 10^7 = 0$$
$$h_7(\mathbf{x}) = x_5 - 120 x_2 x_{13} = 0$$
$$h_8(\mathbf{x}) = x_6 - 80 x_3 x_{14} = 0$$
$$h_9(\mathbf{x}) = x_7 - 40 x_4 x_{15} = 0$$
$$h_10(\mathbf{x}) = x_8 - x_{11} + x_{16} = 0$$
$$h_11(\mathbf{x}) = x_9 - x_{12} + x_{17} = 0$$
$$h_12(\mathbf{x}) = -x_{18} + \ln (x_{10} - 100) = 0$$
$$h_13(\mathbf{x}) = -x_{19} + \ln (-x_8 + 300) = 0$$
$$h_14(\mathbf{x}) = -x_{20} + \ln (x_{16}) = 0$$
$$h_15(\mathbf{x}) = -x_{21} + \ln (-x_9 + 400) = 0$$
$$h_16(\mathbf{x}) = -x_{22} + \ln (x_{17}) = 0$$
$$h_17(\mathbf{x}) = -x_8 - x_{10} + x_{13} x_{18} - x_{13} x_{19} + 400 = 0$$
$$h_18(\mathbf{x}) = x_8 - x_9 - x_{11} + x_{14} x_{20} - x_{14} x_{21} + 400 = 0$$
$$h_19(\mathbf{x}) = x_9 - x_{12} - 4.60517 x_{15} + x_{15} x_{22} + 100 = 0$$
where $0 \leq x_{1}\leq 20000$, $0 \leq x_{2}, x_{3}, x_{4}\leq 1 \times 10^6 $,
$0 \leq x_{5}, x_{6}, x_{7}\leq 4 \times 10^7 $, $100 \leq x_{8}\leq 299.99$,
$100 \leq x_{9}\leq 399.99$, $100.01 \leq x_{10} \leq 300$, $100 \leq x_{11} \leq 400$,
$100 \leq x_{12} \leq 600$, $0 \leq x_{13} , x_{14} , x_{15} \leq 500$,
$0.01 \leq x_{16} \leq 300$, $0.01 \leq x_{17} \leq 400$,
$-4.7 \leq x_{18} , x_{19} , x_{20} , x_{21} , x_{22} \leq 6.25$"""

PROBLEM_G23: str = r"""## Problem G23
Minimize:
$$f(\mathbf{x}) = - 9 x_5 - 15 x_8 + 6 x_1 + 16 x_2 + 10 (x_6 + x_7 )$$
subject to:
$g_1 (\mathbf{x}) = x_9 x_3 + 0.02 x_6 - 0.025 x_5 \leq 0$
$g_2 (\mathbf{x}) = x_9 x_4 + 0.02 x_7 - 0.015 x_8 \leq 0$
$h_1 (\mathbf{x}) = x_1 + x_2 - x_3 - x_4 = 0$
$h_2 (\mathbf{x}) = 0.03 x_1 + 0.01 x_2 - x_9 (x_3 + x_4 ) = 0$
$h_3 (\mathbf{x}) = x_3 + x_6 - x_5 = 0$
$h_4 (\mathbf{x}) = x_4 + x_7 - x_8 = 0$
where: $0 \leq x_1 , x_2 , x_6 \leq 300$, $0 \leq x_3 , x_5 , x_7 \leq 100$, 
$0 \leq x_4 , x_8 \leq 200$ and $0.01 \leq x_9 \leq 0.03$"""

PROBLEM_G24: str = r"""## Problem G24
Minimize:
$$f(\mathbf{x}) = - x_1 - x_2$$
subject to:
$$g_1(\mathbf{x}) = - 2 x_1^{4} + 8 x_1^{3} - 8 x_1^{2} + x_2 - 2 \leq 0 $$
$$g_2(\mathbf{x}) = - 4 x_1^{4} + 32 x_1^{3} - 88 x_1^{2} + 96 x_1 + x_2 - 36 \leq 0 $$
where: $0 \leq x_1 \leq 3$ and $0 \leq x_2 \leq 4$"""
