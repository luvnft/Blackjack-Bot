# AI-powered bot (pretrained bot from hugging face...)

class Bot2:
    def __init__(self, money):
        self.money = money
        self.hand = []
        self.hand2 = []

    
    def hit(self, card):
        self.hand.append(card)
        
    def hit_2(self, card):
        self.hand2.append(card)

    def calculate_hand_val(self):
        return    
    