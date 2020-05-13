from random import shuffle

class Card:
    suits  = ["space", "hearts", "diamonds", "clubs"]

    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """ｽｰﾄ(ﾏｰｸ)も値も整数値です"""
        self.value = v
        self.suit   = s

    def __lt__(self, c2):
        if self.values < c2.values:
            return True

        if self.values == c2.values:
            if self.suit < c2.suit:
                return True

            else:
                return False

        return False

    def __lt__(self, c2):
        if self.values > c2.values:
            return True

        if self.values == c2.values:
            if self.suit > c2.suit:
                return True

            else:
                return False

        return False

    def __repr__(self):
        v = self.values[self.value] + " + " \
            + self.suits[self.suit]

        return v

  
"""
確認用
card1 = Card(10,2)
card2 = Card(11,3)

print(card1 > card2)
print(card1 < card2)
print(card1)
"""
class Deck:
    def __init__(self):
        self.cards = []

        for i in range (2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))

        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return

        return self.cards.pop()

"""

deck = Deck()

for card in deck.cards:
    print(card)

"""
class Player:
    def __init__(self, name):
        self.win = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("プレーヤー１の名前")
        name2 = input("プレーヤー２の名前")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)


    def wins(self, winner):
        w = "このラウンドは{}が勝ちました"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{}は{}、{}は{}を引きました"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards

        while len(cards) >= 2:
            m = "qで終了、それ以外のキーでPlay:"
            response = input(m)

            if response == "q":
                break

            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c, p2n, p2c)
        
            if p1c > p2c:
                self.p1.win += 1
                self.wins(self.p1.name)

            else:
                self.p2.win += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("ゲーム終了、{}の勝利です".format(win))


    def winner(self, p1, p2):
        if p1.win > p2.win:
            return p1.name

        if p1.win < p2.win:
            return p2.name

        return "引き分け!"
        

game = Game()
game.play_game()
































        

        

