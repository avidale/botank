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
        parts.append("Summary:\n")
        parts.append('Codes: {}'.format(', '.join([
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
            json.dump({
                'requests': self.requests,
                'responses': self.responses,
                'times': self.times,
                'codes': self.codes,
            }, f)
