#!/usr/bin/python3
import importlib.util


def print_module_names(module_path):
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    m_names = dir(module)

    f_names = sorted(name for name in m_names if not name.startswith('__'))

    for name in f_names:
        print(name)


if __name__ == "__main__":
    module_path = "hidden_4.pyc"
    print_module_names(module_path)
