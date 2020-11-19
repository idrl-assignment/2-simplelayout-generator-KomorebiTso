import argparse
import sys


def get_options():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='list the parameter')
    parser.add_argument('--board_grid', type=int, help='布局板分辨率')
    parser.add_argument('--unit_grid', type=int, help='矩形组件分辨率')
    parser.add_argument('--unit_n', type=int, help='组件数')
    parser.add_argument('--positions', type=int, nargs='*', help='矩形组件分辨率')
    parser.add_argument(
        '-o', '--outdir', type=str, default='example_dir', help='输出目录')
    parser.add_argument(
        '--file_name', type=str, default='example', help='输出文件名')
    args = parser.parse_args()

    if args.board_grid % args.unit_grid != 0:
        print('布局板分辨率须整除组件分辨率')
        sys.exit(1)

    if len(args.positions) != args.unit_n:
        sys.exit(1)

    Max = max(args.positions)
    Min = min(args.positions)
    if not (Min >= 1 and Max <= int(args.board_grid / args.unit_grid) ** 2):
        sys.exit(1)
    options = parser.parse_args()
    return options
