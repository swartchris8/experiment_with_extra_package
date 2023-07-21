from .main_module import main_function

try:
    from my_package.my_local_package import extra_function
except ImportError:
    extra_function = None

