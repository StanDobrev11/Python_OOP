from typing import List



class Stack:
    def __init__(self):
        self.data: List = []

    def __str__(self) -> str:
        return f"[{', '.join(self.data[::-1])}]"  # "[{element(N)}, {element(N-1)} ... {element(0)}]"

    def push(self, element: str) -> None:
        if isinstance(element, str):
            self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True


# class BaseStack:
#     def __init__(self):
#         self.data: TL_03_List[str] = []
#
#     def is_empty(self):
#         return False if self.data else True
#
#     def __str__(self):
#         return f"[{', '.join(self.data[::-1])}]"
#
#
# class AddStack(BaseStack):
#     def push(self, element: str) -> None:
#         if isinstance(element, str):
#             self.data.append(element)
#
#
# class RemoveStack(BaseStack):
#     def pop(self) -> str:
#         return self.data.pop()
#
#
# class TopStack(BaseStack):
#     def top(self) -> None:
#         self.data.pop()
#
#
# class Stack(AddStack, RemoveStack, TopStack):
#     pass


# stack = Stack()
# print(stack)
# stack.push('1')
# stack.push('2')
# stack.push('3')
# print()
