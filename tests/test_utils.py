"""Unit tests for the k8scheck.utils package."""

import pytest

from k8scheck import utils


@pytest.mark.parametrize(
    "name,expected",
    [
        ("", "k8scheck--20160811210501"),
        ("TestName", "k8scheck-testname-20160811210501"),
        ("TESTNAME", "k8scheck-testname-20160811210501"),
        ("Test-Name", "k8scheck-test-name-20160811210501"),
        ("Test1_FOO-BAR_2", "k8scheck-test1-foo-bar-2-20160811210501"),
        ("123456", "k8scheck-123456-20160811210501"),
        ("___", "k8scheck-----20160811210501"),
        (
            "mytest-" * 6,
            "k8scheck-mytest-mytest-mytest-mytest-mytest-myte-20160811210501",
        ),
        ("test[a]-foo", "k8scheck-test-a--foo-20160811210501"),
    ],
)
def test_new_namespace(name, expected):
    """Test creating a new namespace for the given function name."""

    # mock the return of time.strftime() so we know what it will return
    utils.time.strftime = (lambda format, t=None: '20160811210501')

    actual = utils.new_namespace(name)
    assert actual == expected


@pytest.mark.parametrize(
    "labels,expected",
    [
        ({}, ""),
        ({"foo": "bar"}, "foo=bar"),
        ({"foo": 2}, "foo=2"),
        ({"foo": 2.024}, "foo=2.024"),
        ({"foo": "bar", "abc": "xyz"}, "foo=bar,abc=xyz"),
        ({"foo": "bar", "abc": "xyz", "app": "synse"}, "foo=bar,abc=xyz,app=synse"),
    ],
)
def test_selector_string(labels, expected):
    """Test creating a string for a dictionary of selectors."""

    actual = utils.selector_string(labels)
    assert actual == expected
