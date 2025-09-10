from dtype.datasets.PuplayNet.PuplayNet import PuplayNet
from utils.drawer import Drawer
dataset = PuplayNet()
for i in range(10):
    Drawer.draw_with_arrows(dataset.pages[i])