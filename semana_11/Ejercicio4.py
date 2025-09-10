# Cree las siguientes clases: Head, Torso, Arm, Hand, Leg, Feet

class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self, head, right_arm, left_arm, right_hand, left_hand, right_leg, left_leg, right_foot, left_foot):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_hand = right_hand
        self.left_hand = left_hand
        self.right_leg = right_leg
        self.left_leg = left_leg
        self.right_foot = right_foot
        self.left_foot = left_foot

class Arm:
    def __init__(self, side):
        self.side = side

class Hand:
    def __init__(self, side):
        self.side = side

class Leg:
    def __init__(self, side):
        self.side = side

class Foot:
    def __init__(self, side):
        self.side = side

head_1 = Head()
l_arm = Arm('left')
r_arm = Arm('right')
l_hand = Hand('left')
r_hand = Hand('right')
l_leg = Leg('left')
r_leg = Leg('right')
l_foot = Foot('left')
r_foot = Foot('right')

torso_1 = Torso(head_1, r_arm, l_arm, r_hand, l_hand, r_leg, l_leg, r_foot, l_foot)
