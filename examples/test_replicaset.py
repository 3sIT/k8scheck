"""An example of using k8st3st to manage a deployment."""

import os


def test_replicaset(kube):

    f = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "configs", "replicaset.yaml"
    )

    r = kube.load_replicaset(f)

    kube.create(r)

    r.wait_until_ready(timeout=20)
    r.refresh()

    assert 'test-replica'  in kube.get_replicasets()


    pods = r.get_pods()
    assert len(pods) == 1

    p = pods[0]
    p.wait_until_ready(timeout=10)

    # Issue an HTTP GET against the Pod. The deployment
    # is an http echo server, so we should get back data
    # about the request.
    req = p.http_proxy_get(
        "/test/get",
        query_params={"abc": 123},
    )
    get_data = req.json()
    assert get_data["path"] == "/test/get"
    assert get_data["method"] == "GET"
    assert get_data["body"] == ""
    # fixme (etd): I would expect this to be {'abc': 123}, matching
    #   the input data types (e.g. value not a string). Need to determine
    #   where this issue lies..
    #   This may be an issue with the image reflecting the request back.
    assert get_data["query"] == {"abc": "123"}

    # Issue an HTTP POST against the Pod. The deployment
    # is an http echo server, so we should get back data
    # about the request.
    req = p.http_proxy_post(
        "/test/post",
        query_params={"abc": 123},
        data="foobar",
    )
    post_data = req.json()
    assert post_data["path"] == "/test/post"
    assert post_data["method"] == "POST"
    assert post_data["body"] == '"foobar"'
    # fixme (etd): I would expect this to be {'abc': 123}, matching
    #   the input data types (e.g. value not a string). Need to determine
    #   where this issue lies..
    #   This may be an issue with the image reflecting the request back.
    assert post_data["query"] == {"abc": "123"}

    containers = p.get_containers()
    c = containers[0]
    assert len(c.get_logs()) != 0

    kube.delete(r)
    r.wait_until_deleted(timeout=20)
