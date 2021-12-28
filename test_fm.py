import os
import shutil
import pytest
import fm_defs


@pytest.fixture
def mkdir_fixture():
    fm_defs.mkdir('TestDir')
    return True


def test_mkdir(mkdir_fixture):
    assert mkdir_fixture == 1, "Mkdir Error"


@pytest.fixture
def mrdir_fixture():
    fm_defs.remove_dir('TestDir')
    return True


def test_remove_dir(mrdir_fixture):
    assert mrdir_fixture == 1, "Mkdir Error"


@pytest.fixture
def cd_fixture():
    fm_defs.cd('Test_for_cd')
    return True


def test_cd(cd_fixture):
    assert cd_fixture == 1, "Cd Error"


@pytest.fixture
def writing_fixture():
    fm_defs.writing('test_file_for_writing')
    return True


def test_writing(writing_fixture):
    assert writing_fixture == 1, "Writing Error"


@pytest.fixture
def reading_fixture():
    fm_defs.reading('test_file_for_writing')
    return True


def test_reading(reading_fixture):
    assert reading_fixture == 1, "Reading Error"


@pytest.fixture
def touch_fixture():
    fm_defs.touch('TestFile')
    return True


def test_touch(touch_fixture):
    assert touch_fixture == 1, "Touch Error"


@pytest.fixture
def remove_fixture():
    fm_defs.remove('TestFile')
    return True


def test_remove(remove_fixture):
    assert remove_fixture == 1, "Remove Error"


@pytest.fixture
def cp_fixture():
    fm_defs.cp('test_file_for_cp_from', 'test_file_for_cp_to')
    return True


def test_cp(cp_fixture):
    assert cp_fixture == 1, "Cp Error"


@pytest.fixture
def move_fixture():
    fm_defs.move('Dir_from', 'Dir_to')
    return True


def test_move(move_fixture):
    assert move_fixture == 1, "Move Error"


@pytest.fixture
def rename_fixture():
    fm_defs.rename('file_1', 'file_renamed')
    return True


def test_rename(rename_fixture):
    assert rename_fixture == 1, "Rename Error"
