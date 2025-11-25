import argparse

from my_io import (
    write_to_file,
)

from itx_map import (
    parse_binary,
    to_mms,
)

from lint import (
    fix,
    lint,
)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='mapgenie',
        description='An assistant for IBM Sterling Transformation Extender maps',
    )
    parser.add_argument(
        'filename',
        help='The path of an ITX map source file (the `.mms`)'
    )
    parser.add_argument(
        '-f', '--fix',
        action='store_true',
        help='Apply automatic fixes for anything the linter can fix'
    )
    args = parser.parse_args()

    itx_map = parse_binary(args.filename)
    lint_result = lint(itx_map)

    if args.fix:
        new_map = fix(itx_map, lint_result)
        if not all(correct for correct, _ in lint_result):
            write_to_file(to_mms(new_map), args.filename)
