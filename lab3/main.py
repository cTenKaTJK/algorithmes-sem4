class fsm:
    def __init__(self, s1, s2):
        self.curr_state = (s1 == s2)
        self.changed = False
    
    def change_state(self):
        self.changed = True
        self.curr_state = not self.curr_state

    def update(self, text_sym, pattern_sym):
        if (text_sym == pattern_sym) != self.curr_state:
            self.change_state()
            return True
        return False
    

if __name__ == '__main__':
    text = 'abcacbca'
    pattern = 'cac'
    lnp, lnt = len(pattern), len(text)
    for i in range(lnt - lnp + 1):
        subtext = text[i:i + lnp]
        robot = fsm(pattern[0], subtext[0])
        f = robot.curr_state
        for j in range(1, lnp):
            changed = robot.update(pattern[j], subtext[j])
            if changed:
                f = False
                break
        if f:
            print(i)

    