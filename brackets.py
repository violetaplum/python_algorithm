class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item


def solution(S: str):
    stack = Stack()
    for bracket in S:
        if bracket == '{' or bracket == '[' or bracket == '(':
            stack.push(bracket)
        else:
            if stack.last is None:
                return 0
            item = stack.pop()
            if item == '(':
                if bracket != ')':
                    return 0
            elif item == '{':
                if bracket != '}':
                    return 0
            elif item == '(':
                if bracket != ')':
                    return 0

    if stack.last is not None:
        return 0
    return 1


if __name__ == '__main__':
    string = '{[()()]}'
    print(solution(string))

