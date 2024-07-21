from loguru import logger
from sys import stderr
from functools import wraps


logger.remove()

logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"    
)

logger.add(
    "meu_arquivo_de_logs.log",
    format="{time} {level} {message} {file}",
    level="INFO"
)

def meu_decorador(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@meu_decorador
def minha_funcao():
    """_summary_
    """
    pass

print(minha_funcao.__name__)
print(minha_funcao.__doc__)