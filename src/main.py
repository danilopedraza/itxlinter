import argparse

from my_io import (
    write_to_file,
)

from itx_map import (
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
        help='The path of an ITX map file (the `.mms`).'
    )
    parser.add_argument(
        '-f', '--fix',
        action='store_true',
        help='Apply automatic fixes for anything the linter can fix.'
    )
    args = parser.parse_args()

    itx_map = parse_binary(args.filename)
    result = lint(itx_map)

    if args.fix:
        new_map = fix(itx_map, result)
        write_to_file(itx_map, args.filename)
