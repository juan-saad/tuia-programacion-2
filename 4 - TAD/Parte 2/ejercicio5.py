from typing import Any


class Queue:
    def __init__(self) -> None:
        self.items = []
        
    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        if self.isEmpty():
            print("La cola está vacia")
            return

        return self.items.pop(0)
    
    def isEmpty(self) -> bool:
        return self.items == []
    
    def __str__(self) -> str:
        return str(self.items)

    def __len__(self) -> int:
        return len(self.items)
