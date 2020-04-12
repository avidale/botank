import json

from collections import Counter


class ShooterResults:
    def __init__(self, requests, responces, times, codes):
        self.requests = requests
        self.responses = responces
        self.times = times
        self.codes = codes

    def summary(self):
        parts = list()
        parts.append("\nBotank simulation summary:\n")
        parts.append('Codes: {}\n'.format(', '.join([
            '{} - {}'.format(k, v)
            for k, v in Counter(self.codes).most_common()
        ])))
        parts.append(
            'Timings: min {}, max {}, average {}\n'.format(
                min(self.times),
                max(self.times),
                sum(self.times) / len(self.times),
            )
        )
        return ''.join(parts)

    def write_to_disk(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for i in range(len(self.requests)):
                json.dump({
                    'request': self.requests[i],
                    'response': self.responses[i],
                    'time': self.times[i],
                    'code': self.codes[i],
                }, f, ensure_ascii=False)
                f.write('\n')
