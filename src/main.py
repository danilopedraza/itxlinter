import argparse

from my_io import (
    get_binary,
    write_to_file,
)

from parse_binary import (
    parse_binary,
)

from lint import (
    fix,
    lint,
)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='itxlinter',
        description='A linter for IBM Sterling Transformation Extender maps.',
    )
    parser.add_argument(
        'filename',
        help='The path of a ITX map file (the `.mms`).'
    )
    parser.add_argument(
        '-f', '--fix',
        action='store_true',
        help='Apply automatic fixes for anything the linter can fix.'
    )
    args = parser.parse_args()

    binary = get_binary(args.filename)
    itx_map = parse_binary(binary)
    result = lint(itx_map)

    if args.fix:
        new_map = fix(itx_map, result)
        write_to_file(itx_map, args.filename)
