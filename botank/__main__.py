import argparse

from botank.shooter import run_simulation


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the simulation')
    parser.add_argument('url', help='webhook url of the skill')
    parser.add_argument('--number', '-n', type=int, default=10, help='number of requests to shoot into')
    parser.add_argument('--silent', '-s', action='store_true', help='whether to print the dialog')
    parser.add_argument('--output', '-o', help='file to write the results')
    args = parser.parse_args()

    print('Running {} turns of Botank simulation'.format(args.number))
    results = run_simulation(url=args.url, verbose=not args.silent, n=args.number)
    print(results.summary())
    if args.output:
        results.write_to_disk(args.output)
