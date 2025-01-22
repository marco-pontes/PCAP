
class Decorator:
    @staticmethod
    def execute_lesson(func, *args):
        print("=" * 40 + f' {args[0]} ' + "=" * 40 + "\n")
        func()
        print("=" * 40 + " End " + "=" * 50 + "\n\n")

    @staticmethod
    def execute_module(func, *args):
        print("_" * 100 + f" {args[0]} " + "_" * 100 + "\n")
        func()
        print("_" * 100 + " End Module " + "_" * 100 + "\n\n")
