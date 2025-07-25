from typing import Generic, TypeVar, Any, Callable, get_type_hints, Union, get_args
from importlib.util import find_spec
from os import system
from keyword import iskeyword
from sys import exit as sys_exit
from inspect import signature

if find_spec("IPython") == None:
    system("pip install IPython")

from IPython.display import clear_output


def enforced_typing(func: Callable[[], Any]):
    """
    Enforces type constraints on the function built.
    It uses the inspect and typing modules for getting and enforcing types.
    """

    def wrapper(*args, **kwargs):
        type_hints = get_type_hints(func)
        sig = signature(func)
        bind = sig.bind(*args, **kwargs)
        bind.apply_defaults()
        map_gen = lambda iterable: tuple(map(lambda x: x.__name__, get_args(iterable)))

        for parameter, value in bind.arguments.items():
            hint: Union[Any] = type_hints[parameter]
            value_type = type(value)
            if hint == Union and not isinstance(value, get_args(hint)):
                if value_type == Union:
                    raise TypeError(
                        f"Expected types, {map_gen(hint)} for parameter, "
                        f"{parameter}, but got type, {map_gen(value_type)}."
                    )
                else:
                    raise TypeError(
                        f"Expected types, {map_gen(hint)} for parameter, "
                        f"{parameter}, but got type, {value_type.__name__}."
                    )
            elif not isinstance(value, hint):
                if value_type == Union:
                    raise TypeError(
                        f"Expected type, {hint.__name__} for parameter, "
                        f"{parameter}, but got type, {map_gen(value_type)}."
                    )
                else:
                    raise TypeError(
                        f"Expected type, {hint.__name__} for parameter, "
                        f"{parameter}, but got type, {value_type.__name__}."
                    )

        result = func(*args, **kwargs)

        return_hint = type_hints["return"]
        if return_hint != Any and not type(hint) == Union and not isinstance(result, return_hint):
            if type(return_hint) == Union:
                raise TypeError(
                    f"Invalid return from function, {func.__name__}. "
                    f"Expected return type, {map_gen(return_hint)}, "
                    f"but got return type {type(result).__name__}."
                )
            else:
                raise TypeError(
                    f"Invalid return from function, {func.__name__}. "
                    f"Expected return type, {return_hint.__name__}, "
                    f"but got return type {type(result).__name__}."
                )
        elif not isinstance(result, get_args(hint)):
            if type(return_hint) == Union:
                raise TypeError(
                    f"Invalid return from function, {func.__name__}. "
                    f"Expected return type, {map_gen(return_hint)}, "
                    f"but got return type {type(result).__name__}."
                )
            else:
                raise TypeError(
                    f"Invalid return from function, {func.__name__}. "
                    f"Expected return type, {return_hint.__name__}, "
                    f"but got return type {type(result).__name__}."
                )

    return wrapper


@enforced_typing
def install_package(package_name: str) -> None:
    system(f"pip install {package_name}")


def log_arguments(func: Callable[..., Any]):
    def wrapper(*args, **kwargs):
        sig = signature(func)
        sig = sig.bind(*args, **kwargs)
        sig.apply_defaults()
        _return = func(*args, **kwargs)
        arguments = sig.arguments
        join = ""
        for parameter, value in arguments.items():
            join += f"(param {parameter}: value {value}),"

        join = "{" + join[: len(join) - 1] + "}"
        print(f"Return: {_return} \n" f"Passed arguments: {join}")

        return _return

    return wrapper


T = TypeVar("T")


class new(Generic[T]):
    """
    Constructs a generic object, in which supports standard operations just as you would get.

    ## Currently supported operands:
        comparisions:(>,<,==,ect.)
        numberical/standard operations:(+,-,/,ect.)
        bitwise:(<<,&,>>,ect.)
        note the numerical/standard and the bitwise all can be used in tandom with =.
        ### example:
        ```
        x = 0
        x += 1
        ```

    ## How to set a value with its identity
    Because the class suports all known operands avaliable to be overloaded, (Besides =)
    in order to mimic '=', use the function, set_to. This will set a new value to the variable.
    This does not mean functions that are called when a operation symbol gets refrenced, (For example,+=)
    It only means that if the symbol '=' is used, and only that, it will replace the variables type without explicit declaration
        ### explicit and non-explicit
        ```
        #explicit declaration
        x = new[float](10)
        x = new[float](15) #inefficent repeating a declaration.

        #non-explicit declaration
        x = new[float](10)
        x.set_to(15) #Clean way to set the variable to its new value.
        ```
    """

    def __init__(self, value: T):
        self._value: T = value

    def set_to(self, new_value: T):
        self._value = new_value

    # main dunders
    def __repr__(self):
        return str(self._value)

    def __get__(self, *_):
        return self._value

    def __add__(self, value: T):
        return self._value + value

    def __sub__(self, value: T):
        return self._value - value

    def __mul__(self, value: T):
        return self._value * value

    def __truediv__(self, value: T):
        return self._value / value

    def __floordiv__(self, value: T):
        return self._value // value

    def __mod__(self, value: T):
        return self._value % value

    def __pow__(self, value: T):
        return self._value**value

    def __and__(self, value: T):
        return self._value & value

    def __or__(self, value: T):
        return self._value | value

    def __xor__(self, value: T):
        return self._value ^ value

    def __lshift__(self, value: T):
        return self._value << value

    def __rshift__(self, value: T):
        return self._value >> value

    def __radd__(self, value: T):
        return value + self._value

    def __rsub__(self, value: T):
        return value - self._value

    def __rmul__(self, value: T):
        return value * self._value

    def __rtruediv__(self, value: T):
        return value / self._value

    def __rfloordiv__(self, value: T):
        return value // self._value

    def __rmod__(self, value: T):
        return value % self._value

    def __rpow__(self, value: T):
        return value**self._value

    def __rand__(self, value: T):
        return value & self._value

    def __ror__(self, value: T):
        return value | self._value

    def __rxor__(self, value: T):
        return value ^ self._value

    def __rlshift__(self, value: T):
        return value << self._value

    def __rrshift__(self, value: T):
        return value >> self._value

    def __iadd__(self, value: T):
        self._value += value
        return self

    def __isub__(self, value: T):
        self._value -= value
        return self

    def __imul__(self, value: T):
        self._value *= value
        return self

    def __itruediv__(self, value: T):
        self._value /= value
        return self

    def __ifloordiv__(self, value: T):
        self._value //= value
        return self

    def __imod__(self, value: T):
        self._value %= value
        return self

    def __ipow__(self, value: T):
        self._value **= value
        return self

    def __iand__(self, value: T):
        self._value &= value
        return self

    def __ior__(self, value: T):
        self._value |= value
        return self

    def __ixor__(self, value: T):
        self._value ^= value
        return self

    def __ilshift__(self, value: T):
        self._value <<= value
        return self

    def __irshift__(self, value: T):
        self._value >>= value
        return self

    def __gt__(self, value: T | Any):
        return self._value > value

    def __ge__(self, value: T | Any):
        return self._value >= value

    def __lt__(self, value: T | Any):
        return self._value < value

    def __le__(self, value: T | Any):
        return self._value <= value

    def __eq__(self, value: T | Any):
        return self._value == value

    def __ne__(self, value: T | Any):
        return self._value != value

    # main dunders


def EntryPoint(func: Callable):
    """
    Auto runs a function as it is the program's entry point.
    The function must also be named, 'Main' for it to work.
    """
    if func.__name__ == "Main":
        sys_exit(int(func() or 0))


class classproperty:
    """
    Creates a class property that can either be called on the instance or the class.
    """

    def __init__(self, func):
        self.func = classmethod(func)

    def __get__(self, _, owner):
        return self.func.__get__(owner, owner)()


class staticproperty:
    """
    Creates a static property that can either be called on instance or the class. However, it recieves no first argument.
    """

    def __init__(self, func):
        self.func = staticmethod(func)

    def __get__(self, _, owner):
        return self.func.__get__(None, owner)()


@enforced_typing
def is_valid_name(name: str) -> bool:
    "Checks if a string can be classified as an variable,function, or class name."
    return name.isidentifier() and not iskeyword(name)


@enforced_typing
def clear_console(enviorment: str) -> Any:
    """
    Clears the output of the your current enviorment.\n
    avaliable enviorments:
        -notebook
        -nt
        -posix
    Any other enviorments provided will raise an error.
    For the notebook enviorment, it will return a function that will clear the output depending on the parameter wait, which has the type of bool.
    For the other enviorments, it will not return anything.
    """
    match enviorment:
        case "notebook":

            def wrapper(wait: bool = False):
                clear_output(wait)

            return wrapper
        case "nt":
            system("cls")
        case "posix":
            system("clear")
        case _:
            raise EnvironmentError("Invalid enviorment name provided.")

            and "." in file_path
            and file_path.split(".")[1] == next(i for i in FILE_EXTENSIONS)
        ):
            if not file_path in CANNOTREMOVE:
                os.remove(f"cleaned:{file_path}")

