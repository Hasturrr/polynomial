class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return f"({repr(self.p1)}) - ({repr(self.p2)})"



class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    #sub should also be considered
    def __repr__(self):
        if isinstance(self.p1, (Add, Sub)):
            if isinstance(self.p2, (Add, Sub)):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub)):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        p1_repr = f"({repr(self.p1)})" if isinstance(self.p1, (Add, Sub, Mul)) else repr(self.p1)
        p2_repr = f"({repr(self.p2)})" if isinstance(self.p2, (Add, Sub, Mul)) else repr(self.p2)
        return f"{p1_repr} / {p2_repr}"


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

poly_sub = Sub( Add( Int(4), Int(3)), Mul(X(), X()))
poly_div = Div( Mul( Int(2), X()), Add( X(), Int(1)))

print(poly_sub)
print(poly_div)