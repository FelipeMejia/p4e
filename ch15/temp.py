import os


class TempEnvVar:
    def __init__(self, var, value):
        self.var = var
        self.value = value

    def __enter__(self):
        self.old = os.environ.get(self.var)
        os.environ[self.var] = self.value
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.old is None:
            del os.environ[self.var]
        else:
            os.environ[self.var] = self.old


with TempEnvVar("hola", "valor") as temp_env:
    print(temp_env)
