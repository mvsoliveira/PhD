import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from scipy import optimize


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

def exponenial_func(x, a, b, c):
    return a*np.exp(-b*x)+c


# data for plot
N = 352

input = np.arange(2,N+1)
comparators = [i*(i-1)/2 for i in input]




LF =[
 [2, 17, 34],
 [3, 58, 50],
 [4, 151, 66],
 [5, 298, 82],
 [6, 442, 98],
 [7, 639, 114],
 [8, 1000, 130],
 [9, 1051, 146],
 [10, 1188, 162],
 [11, 1777, 178],
 [12, 2258, 194],
 [13, 2838, 210],
 [14, 3462, 226],
 [15, 5325, 242],
 [16, 7388, 258],
 [17, 5462, 258],
 [18, 5823, 258],
 [19, 6359, 258],
 [20, 6875, 258],
 [21, 7211, 258],
 [22, 8403, 258],
 [23, 8706, 258],
 [24, 9658, 258],
 [25, 10339, 258],
 [26, 10760, 258],
 [27, 11549, 258],
 [28, 12366, 258],
 [29, 12952, 258],
 [30, 13585, 258],
 [31, 14398, 258],
 [32, 14889, 258],
 [33, 16689, 258],
 [34, 18970, 258],
 [35, 19675, 258],
 [36, 21611, 258],
 [37, 22704, 258],
 [38, 24731, 258],
 [39, 24517, 258],
 [40, 24944, 258],
 [41, 26071, 258],
 [42, 26444, 258],
 [43, 29301, 258],
 [44, 27156, 258],
 [45, 38921, 258],
 [46, 32740, 258],
 [47, 31115, 258],
 [48, 36393, 258],
 [49, 40195, 258],
 [50, 40856, 258],
 # [51, np.NaN, np.NaN],
 # [52, np.NaN, np.NaN],
 # [53, np.NaN, np.NaN],
 # [54, np.NaN, np.NaN],
 # [55, np.NaN, np.NaN],
 [56, 52970, 258],
 # [57, np.NaN, np.NaN],
 # [58, np.NaN, np.NaN],
 # [59, np.NaN, np.NaN],
 # [60, np.NaN, np.NaN],
 # [61, np.NaN, np.NaN],
 # [62, np.NaN, np.NaN],
 # [63, np.NaN, np.NaN],
 [64, 85159, 258],
 # [65, np.NaN, np.NaN],
 # [66, np.NaN, np.NaN],
 # [67, np.NaN, np.NaN],
 # [68, np.NaN, np.NaN],
 # [69, np.NaN, np.NaN],
 # [70, np.NaN, np.NaN],
 # [71, np.NaN, np.NaN],
 [72, 93225, 258],
 # [73, np.NaN, np.NaN],
 # [74, np.NaN, np.NaN],
 # [75, np.NaN, np.NaN],
 # [76, np.NaN, np.NaN],
 # [77, np.NaN, np.NaN],
 # [78, np.NaN, np.NaN],
 # [79, np.NaN, np.NaN],
 [80, 108892, 258],
 # [81, np.NaN, np.NaN],
 # [82, np.NaN, np.NaN],
 # [83, np.NaN, np.NaN],
 # [84, np.NaN, np.NaN],
 # [85, np.NaN, np.NaN],
 # [86, np.NaN, np.NaN],
 # [87, np.NaN, np.NaN],
 [88, 147302, 258],
 # [89, np.NaN, np.NaN],
 # [90, np.NaN, np.NaN],
 # [91, np.NaN, np.NaN],
 # [92, np.NaN, np.NaN],
 # [93, np.NaN, np.NaN],
 # [94, np.NaN, np.NaN],
 # [95, np.NaN, np.NaN],
 # [96, np.NaN, np.NaN],
 # [97, np.NaN, np.NaN],
 # [98, np.NaN, np.NaN],
 # [99, np.NaN, np.NaN],
 # [100, np.NaN, np.NaN],
 # [101, np.NaN, np.NaN],
 # [102, np.NaN, np.NaN],
 # [103, np.NaN, np.NaN],
 # [104, np.NaN, np.NaN],
 # [105, np.NaN, np.NaN],
 # [106, np.NaN, np.NaN],
 # [107, np.NaN, np.NaN],
 # [108, np.NaN, np.NaN],
 # [109, np.NaN, np.NaN],
 # [110, np.NaN, np.NaN],
 # [111, np.NaN, np.NaN],
 # [112, np.NaN, np.NaN],
 # [113, np.NaN, np.NaN],
 # [114, np.NaN, np.NaN],
 # [115, np.NaN, np.NaN],
 # [116, np.NaN, np.NaN],
 # [117, np.NaN, np.NaN],
 # [118, np.NaN, np.NaN],
 # [119, np.NaN, np.NaN],
 # [120, np.NaN, np.NaN],
 # [121, np.NaN, np.NaN],
 # [122, np.NaN, np.NaN],
 # [123, np.NaN, np.NaN],
 # [124, np.NaN, np.NaN],
 # [125, np.NaN, np.NaN],
 # [126, np.NaN, np.NaN],
 # [127, np.NaN, np.NaN],
 # [128, np.NaN, np.NaN],
 # [129, np.NaN, np.NaN],
 # [130, np.NaN, np.NaN],
 # [131, np.NaN, np.NaN],
 # [132, np.NaN, np.NaN],
 # [133, np.NaN, np.NaN],
 # [134, np.NaN, np.NaN],
 # [135, np.NaN, np.NaN],
 # [136, np.NaN, np.NaN],
 # [137, np.NaN, np.NaN],
 # [138, np.NaN, np.NaN],
 # [139, np.NaN, np.NaN],
 # [140, np.NaN, np.NaN],
 # [141, np.NaN, np.NaN],
 # [142, np.NaN, np.NaN],
 # [143, np.NaN, np.NaN],
 # [144, np.NaN, np.NaN],
 # [145, np.NaN, np.NaN],
 # [146, np.NaN, np.NaN],
 # [147, np.NaN, np.NaN],
 # [148, np.NaN, np.NaN],
 # [149, np.NaN, np.NaN],
 # [150, np.NaN, np.NaN],
 # [151, np.NaN, np.NaN],
 # [152, np.NaN, np.NaN],
 # [153, np.NaN, np.NaN],
 # [154, np.NaN, np.NaN],
 # [155, np.NaN, np.NaN],
 # [156, np.NaN, np.NaN],
 # [157, np.NaN, np.NaN],
 # [158, np.NaN, np.NaN],
 # [159, np.NaN, np.NaN],
 # [160, np.NaN, np.NaN],
 # [161, np.NaN, np.NaN],
 # [162, np.NaN, np.NaN],
 # [163, np.NaN, np.NaN],
 # [164, np.NaN, np.NaN],
 # [165, np.NaN, np.NaN],
 # [166, np.NaN, np.NaN],
 # [167, np.NaN, np.NaN],
 # [168, np.NaN, np.NaN],
 # [169, np.NaN, np.NaN],
 # [170, np.NaN, np.NaN],
 # [171, np.NaN, np.NaN],
 # [172, np.NaN, np.NaN],
 # [173, np.NaN, np.NaN],
 # [174, np.NaN, np.NaN],
 # [175, np.NaN, np.NaN],
 # [176, np.NaN, np.NaN],
 # [177, np.NaN, np.NaN],
 # [178, np.NaN, np.NaN],
 # [179, np.NaN, np.NaN],
 # [180, np.NaN, np.NaN],
 # [181, np.NaN, np.NaN],
 # [182, np.NaN, np.NaN],
 # [183, np.NaN, np.NaN],
 # [184, np.NaN, np.NaN],
 # [185, np.NaN, np.NaN],
 # [186, np.NaN, np.NaN],
 # [187, np.NaN, np.NaN],
 # [188, np.NaN, np.NaN],
 # [189, np.NaN, np.NaN],
 # [190, np.NaN, np.NaN],
 # [191, np.NaN, np.NaN],
 # [192, np.NaN, np.NaN],
 # [193, np.NaN, np.NaN],
 # [194, np.NaN, np.NaN],
 # [195, np.NaN, np.NaN],
 # [196, np.NaN, np.NaN],
 # [197, np.NaN, np.NaN],
 # [198, np.NaN, np.NaN],
 # [199, np.NaN, np.NaN],
 # [200, np.NaN, np.NaN],
 # [201, np.NaN, np.NaN],
 # [202, np.NaN, np.NaN],
 # [203, np.NaN, np.NaN],
 # [204, np.NaN, np.NaN],
 # [205, np.NaN, np.NaN],
 # [206, np.NaN, np.NaN],
 # [207, np.NaN, np.NaN],
 # [208, np.NaN, np.NaN],
 # [209, np.NaN, np.NaN],
 # [210, np.NaN, np.NaN],
 # [211, np.NaN, np.NaN],
 # [212, np.NaN, np.NaN],
 # [213, np.NaN, np.NaN],
 # [214, np.NaN, np.NaN],
 # [215, np.NaN, np.NaN],
 # [216, np.NaN, np.NaN],
 # [217, np.NaN, np.NaN],
 # [218, np.NaN, np.NaN],
 # [219, np.NaN, np.NaN],
 # [220, np.NaN, np.NaN],
 # [221, np.NaN, np.NaN],
 # [222, np.NaN, np.NaN],
 # [223, np.NaN, np.NaN],
 # [224, np.NaN, np.NaN],
 # [225, np.NaN, np.NaN],
 # [226, np.NaN, np.NaN],
 # [227, np.NaN, np.NaN],
 # [228, np.NaN, np.NaN],
 # [229, np.NaN, np.NaN],
 # [230, np.NaN, np.NaN],
 # [231, np.NaN, np.NaN],
 # [232, np.NaN, np.NaN],
 # [233, np.NaN, np.NaN],
 # [234, np.NaN, np.NaN],
 # [235, np.NaN, np.NaN],
 # [236, np.NaN, np.NaN],
 # [237, np.NaN, np.NaN],
 # [238, np.NaN, np.NaN],
 # [239, np.NaN, np.NaN],
 # [240, np.NaN, np.NaN],
 # [241, np.NaN, np.NaN],
 # [242, np.NaN, np.NaN],
 # [243, np.NaN, np.NaN],
 # [244, np.NaN, np.NaN],
 # [245, np.NaN, np.NaN],
 # [246, np.NaN, np.NaN],
 # [247, np.NaN, np.NaN],
 # [248, np.NaN, np.NaN],
 # [249, np.NaN, np.NaN],
 # [250, np.NaN, np.NaN],
 # [251, np.NaN, np.NaN],
 # [252, np.NaN, np.NaN],
 # [253, np.NaN, np.NaN],
 # [254, np.NaN, np.NaN],
 # [255, np.NaN, np.NaN],
 # [256, np.NaN, np.NaN],
 # [257, np.NaN, np.NaN],
 # [258, np.NaN, np.NaN],
 # [259, np.NaN, np.NaN],
 # [260, np.NaN, np.NaN],
 # [261, np.NaN, np.NaN],
 # [262, np.NaN, np.NaN],
 # [263, np.NaN, np.NaN],
 # [264, np.NaN, np.NaN],
 # [265, np.NaN, np.NaN],
 # [266, np.NaN, np.NaN],
 # [267, np.NaN, np.NaN],
 # [268, np.NaN, np.NaN],
 # [269, np.NaN, np.NaN],
 # [270, np.NaN, np.NaN],
 # [271, np.NaN, np.NaN],
 # [272, np.NaN, np.NaN],
 # [273, np.NaN, np.NaN],
 # [274, np.NaN, np.NaN],
 # [275, np.NaN, np.NaN],
 # [276, np.NaN, np.NaN],
 # [277, np.NaN, np.NaN],
 # [278, np.NaN, np.NaN],
 # [279, np.NaN, np.NaN],
 # [280, np.NaN, np.NaN],
 # [281, np.NaN, np.NaN],
 # [282, np.NaN, np.NaN],
 # [283, np.NaN, np.NaN],
 # [284, np.NaN, np.NaN],
 # [285, np.NaN, np.NaN],
 # [286, np.NaN, np.NaN],
 # [287, np.NaN, np.NaN],
 # [288, np.NaN, np.NaN],
 # [289, np.NaN, np.NaN],
 # [290, np.NaN, np.NaN],
 # [291, np.NaN, np.NaN],
 # [292, np.NaN, np.NaN],
 # [293, np.NaN, np.NaN],
 # [294, np.NaN, np.NaN],
 # [295, np.NaN, np.NaN],
 # [296, np.NaN, np.NaN],
 # [297, np.NaN, np.NaN],
 # [298, np.NaN, np.NaN],
 # [299, np.NaN, np.NaN],
 # [300, np.NaN, np.NaN],
 # [301, np.NaN, np.NaN],
 # [302, np.NaN, np.NaN],
 # [303, np.NaN, np.NaN],
 # [304, np.NaN, np.NaN],
 # [305, np.NaN, np.NaN],
 # [306, np.NaN, np.NaN],
 # [307, np.NaN, np.NaN],
 # [308, np.NaN, np.NaN],
 # [309, np.NaN, np.NaN],
 # [310, np.NaN, np.NaN],
 # [311, np.NaN, np.NaN],
 # [312, np.NaN, np.NaN],
 # [313, np.NaN, np.NaN],
 # [314, np.NaN, np.NaN],
 # [315, np.NaN, np.NaN],
 # [316, np.NaN, np.NaN],
 # [317, np.NaN, np.NaN],
 # [318, np.NaN, np.NaN],
 # [319, np.NaN, np.NaN],
 # [320, np.NaN, np.NaN],
 # [321, np.NaN, np.NaN],
 # [322, np.NaN, np.NaN],
 # [323, np.NaN, np.NaN],
 # [324, np.NaN, np.NaN],
 # [325, np.NaN, np.NaN],
 # [326, np.NaN, np.NaN],
 # [327, np.NaN, np.NaN],
 # [328, np.NaN, np.NaN],
 # [329, np.NaN, np.NaN],
 # [330, np.NaN, np.NaN],
 # [331, np.NaN, np.NaN],
 # [332, np.NaN, np.NaN],
 # [333, np.NaN, np.NaN],
 # [334, np.NaN, np.NaN],
 # [335, np.NaN, np.NaN],
 # [336, np.NaN, np.NaN],
 # [337, np.NaN, np.NaN],
 # [338, np.NaN, np.NaN],
 # [339, np.NaN, np.NaN],
 # [340, np.NaN, np.NaN],
 # [341, np.NaN, np.NaN],
 # [342, np.NaN, np.NaN],
 # [343, np.NaN, np.NaN],
 # [344, np.NaN, np.NaN],
 # [345, np.NaN, np.NaN],
 # [346, np.NaN, np.NaN],
 # [347, np.NaN, np.NaN],
 # [348, np.NaN, np.NaN],
 # [349, np.NaN, np.NaN],
 # [350, np.NaN, np.NaN],
 # [351, np.NaN, np.NaN],
 # [352, np.NaN, np.NaN],
]

LFT = list(map(list, zip(*LF)))

Comparators = (input, comparators)
LUTs = (LFT[0], [x/1000 for x in LFT[1]])
FFs = (LFT[0], LFT[2])

# exponential extrapolation LUT
fp = 16 # first point to be considered for fitting
x= LUTs[0]
y= LUTs[1]
popt, pcov = optimize.curve_fit(exponenial_func, x[fp:], y[fp:], p0=(1, 1e-6, 1))
xx = np.linspace(2, 352, 1000)
yy = exponenial_func(xx, *popt)
LUTsi = (xx, yy)
# linear extrapolation FF
f = interpolate.interp1d(FFs[0], FFs[1], fill_value='extrapolate')
FFsi = (input, f(input))

# plotting

xafter2 = 32
xstep = 32

fig, host = plt.subplots()
fig.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()

# Offset the right spine of par2.  The ticks and label have already been
# placed on the right by twinx above.
par2.spines["right"].set_position(("axes", 1.2))
# Having been created by twinx, par2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
make_patch_spines_invisible(par2)
# Second, show the right spine.
par2.spines["right"].set_visible(True)

p1, = host.plot(*Comparators, "b-", label="Comparators")
p2, = par1.plot([2,352],[1182,1182], "r--",label="k LUTs")
par1.text(5, 1225, "Limit for XCVU9P", fontsize=10, fontdict=dict(color='red'))
p2, = par1.plot([2,352],[1728,1728], "r--",label="k LUTs")
par1.text(5, 1775, "Limit for XCVU13P", fontsize=10, fontdict=dict(color='red'))
p2, = par1.plot(*LUTs, "r*", label="k LUTs")
p2, = par1.plot(*LUTsi, "r-",label="k LUTs")
p3, = par2.plot(*FFs, "g^", label="FFs")
p3, = par2.plot([2,352],[0.00015*2364000,0.00015*2364000], "g--",label="k LUTs")
par2.text(5, 370, "0.015% of XCVU9P", fontsize=10, fontdict=dict(color='green'))
p3, = par2.plot(*FFsi, "g-", label="FFs")


host.set_xlim(2, 352)
host.set_ylim(0, 65000)
par1.set_ylim(0, 2500)
par2.set_ylim(1, 1000)

xticks = np.concatenate(([2],np.arange(xafter2,N+1,xstep)))
plt.xticks(xticks,xticks)

host.set_xlabel("Inputs")
host.set_ylabel("Comparators")
par1.set_ylabel("k LUTs")
par2.set_ylabel("FFs")

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
par2.yaxis.label.set_color(p3.get_color())

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
host.tick_params(axis='x', **tkw)

lines = [p1, p2, p3]

host.legend(lines, [l.get_label() for l in lines])

plt.title('Paralell Sorting Logic Resources Usage')

plt.show()

plt.savefig('NumberOfComparatorsAndLUT.pdf')
