#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: march 17 2025
# The program is supposed to scope variables
# global variable
variable_x = 55


def local_variable() -> None:
    """The local_variable() function creates local variables, returns None."""
    variable_x = 20
    variable_y = 25

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Local variable:  {variable_x} + {variable_y} = {variable_z}")


def global_variable() -> None:
    """The global_variable() function uses a global variable, returns None."""
    global variable_x
    variable_y = 30

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Global variable: {variable_x} + {variable_y} = {variable_z}")


def main() -> None:
    """The main() function shows local and global variables, returns None."""
    local_variable()
    global_variable()

    print("\nDone.")


if __name__ == "__main__":
    main()
