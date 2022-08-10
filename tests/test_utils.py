"""Unit tests for the k8scheck.utils package."""

import pytest

from k8scheck import utils


@pytest.mark.parametrize(
    "name,expected",
    [
        ("", "k8scheck--1536849367"),
        ("TestName", "k8scheck-testname-1536849367"),
        ("TESTNAME", "k8scheck-testname-1536849367"),
        ("Test-Name", "k8scheck-test-name-1536849367"),
        ("Test1_FOO-BAR_2", "k8scheck-test1-foo-bar-2-1536849367"),
        ("123456", "k8scheck-123456-1536849367"),
        ("___", "k8scheck-----1536849367"),
        (
            "test-" * 14,
            "k8scheck-test-test-test-test-test-test-test-test-tes-1536849367",
        ),
        ("test[a]-foo", "k8scheck-test-a--foo-1536849367"),
    ],
)
def test_new_namespace(name, expected):
    """Test creating a new namespace for the given function name."""

    # mock the return of time.time() so we know what it will return
    utils.time.time = lambda: 1536849367.0

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
