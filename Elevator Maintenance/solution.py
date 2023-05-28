class Elevator:
    def __init__(self, elevator):
        # Split the elevator string by '.' and convert each part to an integer
        div = list(map(int, elevator.strip().split('.')))
        # Store the original elevator string
        self.str = elevator
        # Extract the major version
        self.major = div[0]
        # Extract the minor version if present, otherwise set it to -1
        self.minor = div[1] if len(div) > 1 else -1
        # Extract the revision version if present, otherwise set it to -1
        self.revision = div[2] if len(div) > 2 else -1
        
    def __lt__(self, other):
        # Compare elevators based on major, minor, and revision versions
        if self.major < other.major: return True
        if self.major > other.major: return False
        if self.minor < other.minor: return True
        if self.minor > other.minor: return False
        if self.revision < other.revision: return True
        if self.revision > other.revision: return False

def solution(l):
    els = []
    for elevator in l:
        els.append(Elevator(elevator))
    # Sort the elevators based on their versions using the defined comparison (__lt__) method
    els.sort()
    # Return the sorted elevator strings
    return [el.str for el in els]

if __name__ == "__main__":
    l1 = {"1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"}
    print(solution(l1))

    l2 = {"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"}
    print(solution(l2))
