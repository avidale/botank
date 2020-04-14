import math
import random
import razdel
import re


kwsl = {'скажите', 'или', 'команду', 'скажи', 'сказать', 'выбирайте', 'например', 'скажете'}
kwsr = {'или'}


re_anumpu = re.compile('[^a-zа-яё0-9,.?!;\"\'()«»]+')
re_anum = re.compile('[^a-zа-яё0-9]+')

_VARS = ('n', 'm', 'n2', 'shrink', 'lb', 'rb', 'lb_rel', 'rb_rel', 'after_kw', 'before_kw', 'brackets')
_INTERCEPT = 2.59215812
_COEF = (
    0.0935141900827697, -0.006324139966858152, -1.749261933574343, 0.4029871250243725,
    -4.107929717014756, -4.502369654111239, 9.234350360601544, -8.642836913987496,
    1.2875809726725325, 1.7366615629723197, 2.2080408075068516,
)


def normalize(text):
    text = text.lower().replace('ё', 'е')
    return re.sub(re_anumpu, ' ', text).strip()


def normalize_no_punct(text):
    text = text.lower().replace('ё', 'е')
    return re.sub(re_anum, ' ', text).strip()


def make_hypos(text, gt=None, max_len=5):
    toks = [t.text for t in razdel.tokenize(text)]
    m = len(toks)
    hypos = []
    for size in range(1, max_len+1):
        for beg in range(0, m):
            last = beg + size - 1
            if last >= m:
                continue
            if normalize_no_punct(toks[beg]) == '':
                continue
            if normalize_no_punct(toks[last]) == '':
                pass  # sometimes there is punctuation before brackets, we don't want to lose this
            subtoks = toks[beg:(beg+size)]
            subtext_raw = ' '.join(subtoks)
            subtext = normalize_no_punct(subtext_raw)
            if not subtext:
                continue
            hypo = dict(
                text=subtext,
                y=int(subtext == gt),
                n=size,
                m=m,
            )
            hypo['n'] = size
            hypo['n2'] = len(subtext.split())
            hypo['shrink'] = int(subtext_raw != subtext)
            hypo['lb'] = beg / len(toks)
            hypo['rb'] = 1 - (beg + size) / len(toks)
            hypo['lb_rel'] = hypo['lb'] / len(toks)
            hypo['rb_rel'] = hypo['rb'] / len(toks)
            hypo['after_kw'] = int(beg > 0 and toks[beg-1] in kwsl)
            hypo['before_kw'] = int(last + 1 < len(toks) and toks[last+1] in kwsr)
            hypo['brackets'] = 0
            if beg > 0 and last + 1 < m:
                l = toks[beg-1]
                r = toks[last+1]
                hypo['brackets'] = int(
                    l == r == "'"
                    or l == r == '"'
                    or l == "«" and r == "»"
                    or l == '``' and r == "''"
                )
            hypos.append(hypo)
    return hypos


def apply_logreg(data_dict, varnames=_VARS, intercept=_INTERCEPT, coef=_COEF):
    logit = intercept
    for k, v in zip(varnames, coef):
        logit += data_dict[k] * v
    return 1.0 / (1.0 + math.exp(-logit))


def copypaste(text, k=1):
    """ Return a random (non-uniform) substring of the text.
    Shorter substrings and substrings in brackets are preferred.
    """
    hypos = make_hypos(normalize(text), max_len=15)
    weights = [apply_logreg(h, _VARS, _INTERCEPT, _COEF) for h in hypos]
    result = random.choices(population=[h['text'] for h in hypos], weights=weights, k=k)
    if k == 1:
        return result[0]
    return result
