import argparse

from botank.simple_responders import UserModel
from botank.shooter import run_simulation


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Shoot random requests into your Alice skill')
    parser.add_argument('url', help='webhook url of the skill')
    parser.add_argument('--number', '-n', type=int, default=10, help='number of requests to shoot into')
    parser.add_argument('--silent', '-s', action='store_true', help='suppress printing the dialog to the stdout')
    parser.add_argument('--output', '-o', help='the file to write the results to')
    parser.add_argument('--texts', '-t', action='append', help='the file(s) with custom texts to send')
    parser.add_argument('--button', '-b', nargs='?', default=0.5, const=1, type=float,
                        help='probability of choosing a random suggest (defaults 0.5)')
    parser.add_argument('--repeat', '-r', nargs='?', default=0.5, const=1, type=float,
                        help='probability of repeating a random substring (defaults 0.5)')
    # todo: threads
    args = parser.parse_args()

    texts = []
    for filename in args.texts or []:
        with open(filename, 'r', encoding='utf-8') as f:
            texts.append(f.readlines())

    user_model = UserModel(
        p_button=args.button,
        p_resample=args.repeat,
        texts_collections=texts or None,
    )

    print('Running {} turns of Botank simulation...\n'.format(args.number))
    results = run_simulation(url=args.url, verbose=not args.silent, n=args.number, user_model=user_model)
    print(results.summary())
    if args.output:
        results.write_to_disk(args.output)
