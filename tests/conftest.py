# coding: utf-8
from __future__ import unicode_literals, print_function, division

import pytest
from clldutils.path import Path
from clldutils.dsv import reader
import random

from pyclts import TranscriptionSystem, TranscriptionData, SoundClasses


def pytest_generate_tests(metafunc):
    if 'test_sounds' == metafunc.function.__name__:
        fixturenames = None
        tests = []
        for i, test in enumerate(reader(
            Path(__file__).parent / 'data' / 'test_data.tsv',
            delimiter='\t',
            dicts=True
        )):
            if i == 0:
                fixturenames = list(test.keys())
                fixturenames.pop(fixturenames.index('bipa'))
            del test['bipa']
            tests.append(tuple(test.values()))
        tests = random.sample(tests, 20)
        metafunc.parametrize(','.join(n.replace('-', '_') for n in fixturenames), tests)
    elif 'test_clicks' == metafunc.function.__name__:
        tests = []
        for test in reader(
            Path(__file__).parent / 'data' / 'clicks.tsv', delimiter='\t', dicts=True
        ):
            tests.append((test['GRAPHEME'], test['MANNER']))
        tests = random.sample(tests, 20)
        metafunc.parametrize('grapheme,gtype', tests)


@pytest.fixture
def bipa():
    return TranscriptionSystem()


@pytest.fixture
def asjp():
    return TranscriptionSystem('asjpcode')


@pytest.fixture
def gld():
    return TranscriptionSystem('gld')


@pytest.fixture
def sca():
    return SoundClasses('sca')


@pytest.fixture
def asjpd():
    return SoundClasses('asjp')


@pytest.fixture
def dolgo():
    return SoundClasses('dolgo')


@pytest.fixture
def dolgo():
    return SoundClasses('dolgo')


@pytest.fixture
def phoible():
    return TranscriptionData('phoible')


@pytest.fixture
def pbase():
    return TranscriptionData('pbase')
