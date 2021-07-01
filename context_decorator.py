import contextlib
import functools


@contextlib.contextmanager
def my_context():
    print("Setup context")
    try:
        yield "Something"
    except Exception:
        print("Rollback")
    else:
        print("Success")
    finally:
        print("Teardown")


def context_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if context := kwargs.pop('context', None):
            return func(*args, context=context, **kwargs)
        else:
            with my_context() as context:
                return func(*args, context=context, **kwargs)
    return wrapper


@context_decorator
def test(context):
    print(context)
    if context == 42:
        raise Exception()


if __name__ == '__main__':
    test()

