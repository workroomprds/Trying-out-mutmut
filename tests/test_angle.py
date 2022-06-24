from src import angle


def test_twelve():
    assert angle.between(12, 0) == 0


def test_three():
    assert angle.between(3, 0) == 90


def test_hr_not_at_0():
    assert angle.between(6, 30) == 15


def test_hr_not_at_0_and_before_min():
    assert angle.between(5, 30) == 15  ## is this as required?


def test_hr_gt_12():
    assert angle.between(15, 0) == 90


def test_odd_hours_and_minutes():
    assert angle.between(413.9410929040945, 168.36399694656427) == 747.951194556551 # from probe - clearly undesirable!?

def test_great_correction():
    assert angle.between(6, 31) == 9


def test_great_correction1():
    assert angle.between(6, 32) == 4


def test_great_correction2():
    assert angle.between(6, 33) == 2


def test_great_correction3():
    assert angle.between(6, 34) == 7


def test_great_correction4():
    assert angle.between(6, 34.5) == 10

