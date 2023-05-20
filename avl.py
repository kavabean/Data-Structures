class TreeInc(object):
    def __init__(self, inc):
        self.inc = inc
        self.left = None
        self.right = None
        self.height = 1


class AVL(object):
    def nodeInsertion(self, root, inc):

        # indicator to place left or right (low high)
        """O(log n) -- length of process shortened dependent on imbalance type"""

        if not root:
            return TreeInc(inc)
        elif inc > root.inc:
            root.right = self.nodeInsertion(root.right, inc)
        else:
            root.left = self.nodeInsertion(root.left, inc)

        root.height = 1 + max(self.heightDet(root.right),
                              self.heightDet(root.left))

        # Determine if left or right rotation is needed, and if double rotation is needed

        bfValue = self.balanceDet(root)

        # Right imbalance, double rotation if Right Left imbalance

        if bfValue < -1:
            if inc > root.right.inc:
                return self.leftRotation(root)
            elif inc < root.right.inc:
                root.right = self.rightRotation(root.right)
                return self.leftRotation(root)

        # Left imbalance, double rotation if Left Right imbalance

        if bfValue > 1:
            if inc < root.left.inc:
                return self.rightRotation(root)
            elif inc > root.left.inc:
                root.left = self.leftRotation(root.left)
                return self.rightRotation(root)

        return root

    def leftRotation(self, thr):
        """O(1) -- variable swap linear regardless of assigned values"""

        # swaps indication values of nodes in need of rotation

        snd = thr.right
        temp = snd.left
        snd.left = thr
        thr.right = temp

        thr.height = 1 + max(self.heightDet(thr.left), self.heightDet(
            thr.right))
        snd.height = 1 + max(self.heightDet(snd.left), self.heightDet(
            snd.right))

        return snd

    def rightRotation(self, thr):
        """O(1) -- variable swap linear regardless of assigned values"""

        # swaps indication values of nodes in need of rotation

        snd = thr.left
        temp = snd.right
        snd.right = thr
        thr.left = temp

        thr.height = 1 + max(self.heightDet(thr.left), self.heightDet(
            thr.right))
        snd.height = 1 + max(self.heightDet(snd.left), self.heightDet(
            snd.right))

        return snd

    def balanceDet(self, root):
        """O(log n) -- process will be longer if not root"""

        # analyze height after rotation for balance factor

        if not root:
            return 0
        return self.heightDet(root.left) - self.heightDet(root.right)

    def heightDet(self, root):
        """O(1) -- both process equal length"""

        if not root:
            return 0
        return root.height

    def printLtR(self, root):
        """O(log n) -- process will be longer if not root"""

        # left to right value assigment for leaf printing

        if not root:
            return
        print("{} ".format(root.inc), end="")
        self.printLtR(root.left)
        self.printLtR(root.right)

    def gatherInfo(self, root):
        """O(n) -- time increases linear per indicator added"""

        yn = input(f'Would you like to add an indicator? Y/N \n')
        yn = yn.upper()

        if yn == 'Y':
            try:
                incList.append(int(input(f'Please insert your indicator.\n')))
                return self.gatherInfo(root)
            except:
                print('Please insert integer values only.')
                return self.gatherInfo(root)
        elif yn == 'N':
            print('Insertion process ending.\n')

        else:
            print('Please insert Y/N answers only.')

            return self.gatherInfo(root)

        return incList


if __name__ == "__main__":
    AVL = AVL()
    import time
    root = None
    incList = []

    # user input for node isertion indicatiors
    AVL.gatherInfo(root)
    """O(n) -- time increases linear per indicator"""
    # sort data function with timer start

    initial = time.time()

    # !!!!
    # !!!! Remove for manual input to work as intended !!!!
    incList = [10, 20, 30, 40, 50, 25]
    # !!!! Remove for manual input to work as intended !!!!
    # !!!!

    for inc in incList:
        root = AVL.nodeInsertion(root, inc)

    # print sort function and time elapsed

    print(f'Now sorting {len(incList)} indicator(s) from the AVL tree.')
    AVL.printLtR(root)
    print(
        f'\nFinished. \nApprox {time.time() - initial} instances elapsed before.'
    )
