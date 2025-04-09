import sys
sys.stdout.reconfigure(encoding='utf-8')

class Handler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler 

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return "Ніхто не зміг обробити запит."


class OperatorHandler(Handler):
    def handle(self, request):
        if request == "легке питання":
            return "Оператор відповів на запит."
        return super().handle(request)


class ManagerHandler(Handler):
    def handle(self, request):
        if request == "питання середньої складності":
            return "Менеджер відповів на запит."
        return super().handle(request)


class DirectorHandler(Handler):
    def handle(self, request):
        if request == "складне питання":
            return "Директор відповів на запит."
        return super().handle(request)


operator = OperatorHandler()
manager = ManagerHandler()
director = DirectorHandler()

operator.set_next(manager).set_next(director)

requests = [
    "легке питання",
    "питання середньої складності",
    "складне питання",
    "незрозуміле питання"
]

for req in requests:
    print(f"\nЗапит: {req}")
    print("Відповідь:", operator.handle(req))
