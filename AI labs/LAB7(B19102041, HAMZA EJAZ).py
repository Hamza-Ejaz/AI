# LAB7(B19102041, Hamza Ejaz)
class FA:
    def __init__(self, nStates, domain, initial_state, final_state, TT):
        self.nStates = nStates
        self.domain = domain
        self.initial_state = initial_state
        self.final_state = final_state
        self.TT = TT

    def transition(self, state, ch):
        for i in range(len(self.domain)):
            if ch == self.domain[i]:
                return self.TT[state][i]
        return -1

A = FA(2, ['a', 'b'], 0, [1], [[1, 0], [1, 0]])
B = FA(3, ['a', 'b'], 0, [1], [[2, 1], [1, 1], [2, 2]])

def DFA_OR(DFA1, DFA2):
    if DFA1.domain != DFA2.domain:
        print("Incorrect DFA")
        return None
    Equation = [[0,0]]
    i = 0
    new_TT = []
    while len(Equation) > i:
        current_state = Equation[i]
        connection = []
        for domain in DFA1.domain:
            flag = False
            s1 = DFA1.transition(current_state[0], domain)
            s2 = DFA2.transition(current_state[1], domain)

            for j in range(len(Equation)):
                if [s1, s2] == Equation[j]:
                    flag = True
                    index=j
                    break
            if not flag:
                Equation.append([s1, s2])
                index = len(Equation) - 1

            connection.append(index)
        new_TT.append(connection);
        i += 1

    return new_TT

# Driver Code
DFA_OR_TT = DFA_OR(A, B)
print(DFA_OR_TT)

