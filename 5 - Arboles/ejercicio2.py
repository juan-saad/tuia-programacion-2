from typing import Any


class Tree:
    def __init__(self, cargo: Any, left: "Tree" = None, right: "Tree" = None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def nodes(self) -> int:
        count = 1
        if self.left:
            count += self.left.nodes()
        if self.right:
            count += self.right.nodes()
        return count

    def min_max(self) -> tuple[Any, Any]:
        min_val = max_val = self.cargo

        if self.left:
            left_min, left_max = self.left.min_max()
            min_val = min(min_val, left_min)
            max_val = max(max_val, left_max)

        if self.right:
            right_min, right_max = self.right.min_max()
            min_val = min(min_val, right_min)
            max_val = max(max_val, right_max)

        return (min_val, max_val)

    def search(self, elem: Any) -> bool:
        if self.cargo == elem:
            return True

        if self.left and self.left.search(elem):
            return True

        if self.right and self.right.search(elem):
            return True

        return False

    def height(self) -> int:
        pass

    def __str__(self) -> str:
        return str(self.cargo)


tree = Tree(
    10,
    Tree(5, Tree(2), Tree(7, Tree(30, None, Tree(1, None, Tree(100))))),
    Tree(15, Tree(12, None, Tree(20)), Tree(18)),
)

print(tree.search(30))
