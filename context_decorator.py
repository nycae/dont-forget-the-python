import contextlib
import functools


@contextlib.contextmanager
def my_context():
    print("Setup context")
    try:
        yield "Something" or None
    except Exception:
        print("Rollback")
    else:
        print("Success")
    finally:
        print("Teardown")


def context_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not 'context' in kwargs:
            with my_context() as context:
                return func(*args, context=context, **kwargs)
        else:
            return func(*args, **kwargs)
    return wrapper


@context_decorator
def test(context):
    print(context)
    if context == 42:
        raise Exception()


if __name__ == '__main__':
    test()
    test(42)
