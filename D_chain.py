import time
import itertools

from Lection_04.A_increase import RangeIterable
from Lection_04.B_decrease import RangeIterableIterator
from Lection_04.C_sinus import SinusIterableWithGenerator

main_iter = itertools.chain(
    RangeIterableIterator(32),
    RangeIterable(16),
    SinusIterableWithGenerator(64,32)
)
for line in main_iter:
    print(line)
    time.sleep(0.25)