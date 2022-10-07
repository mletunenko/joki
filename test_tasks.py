from tasks import first_non_repeating_letter, count_change, make_looper, is_merge


def test_first_non_repeating_letter():
    assert first_non_repeating_letter('a') == 'a'
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('moonmen') == 'e'
    assert first_non_repeating_letter('') == ''
    assert first_non_repeating_letter('abba') == ''
    assert first_non_repeating_letter('hello world, eh?') == 'w'
    assert first_non_repeating_letter('sTreSS') == 'T'
    assert first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!') == ','


def test_count_change():
    assert count_change(4, [1, 2]) == 3
    assert count_change(10, [5, 2, 3]) == 4
    assert count_change(11, [5, 7]) == 0


def test_make_looper():
    abc = make_looper('abc')
    assert abc() == 'a'
    assert abc() == 'b'
    assert abc() == 'c'
    assert abc() == 'a'


def test_is_merge():
    assert (is_merge('helloworld', 'hello', 'world')) is True
    assert (is_merge('helloworld', 'how', 'ellorld')) is True
    assert (is_merge('helloworld', 'hell', 'world')) is False
    assert (is_merge('helloworld', 'ehll', 'world')) is False
