from mnemonic import Mnemonic
import random

mnemo = Mnemonic("english")

tests = [
    "juice velvet giggle paper boy amused ugly kick state foam melody account",
    "casino alley glance very work pledge number welcome spirit frozen report case",
    "tide silly zero range tennis fiber grace record fuel suggest fun sunny",
    "diesel wool destroy devote flock unhappy raccoon debate chase filter cluster repeat",
    "citizen brief lamp snack hammer unique survey sauce hair tiger fortune sea",
    "spoil toward wait prize brown unusual borrow loop maze figure inject wasp",
    "view runway protect amount card oppose escape panic anxiety kite shield salad",
    "recall west actor luxury agent evoke mystery enter person ginger keen day",
    "grape soldier bunker truly company state mom battle believe foot member cash",
    "desk drink solid magic amazing embody guide sorry debris vendor hope fiction"
]

def makeShuffle(list, size):
    valid = 0
    for each in range(size):
        random.shuffle(list)
        if mnemo.check(" ".join(list)):
            valid += 1
    print(valid)
    
if __name__ == "__main__":
    for test in tests:
        makeShuffle(test.split(), 10000)
        # prints:
        # 599
        # 612
        # 625
        # 631
        # 672
        # 635
        # 635
        # 643
        # 617
        # 607
        # ~600 out of 10,000 attempts comes out to 6% valid phrases
