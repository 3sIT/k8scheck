# k8st3st

[![Build Status](https://github.com/3sIT/k8st3sT/actions/workflows/test.yaml/badge.svg)](https://github.com/3sIT/k8st3sT/actions/workflows/test.yaml)
[![PyPI](https://img.shields.io/pypi/v/k8st3st.svg)](https://pypi.org/project/k8st3st/)
[![Documentation Status](https://readthedocs.org/projects/k8st3st/badge/?version=latest)](https://k8st3st.readthedocs.io/en/latest/?badge=latest)

This is a (for the time being) compatible fork of [kubetest](https://github.com/vapor-ware/kubetest) as it now seems to be abandoned, installable using the package name k8st3st

# kubetest
Kubetest is a [pytest][pytest] plugin that makes it easier to manage a Kubernetes
cluster within your integration tests. While you can use the [Kubernetes Python client][k8s-py]
directly, this plugin provides some cluster and object management on top of that so you can
spend less time setting up and tearing down tests and more time actually writing your tests.
In particular, this plugin is useful for testing your Kubernetes infrastructure (e.g., ensure
it deploys and behaves correctly) and for testing disaster recovery scenarios (e.g. delete a
pod or deployment and inspect the aftermath).

**Features:**
* Simple API for common cluster interactions.
* Uses the Kubernetes Python client as the backend, so more complex custom
  actions are possible.
* Load Kubernetes manifest YAMLs into their Kubernetes models.
* Each test is run in its own namespace and the namespace is created and
  deleted automatically.
* Detailed logging to help debug error cases.
* Wait functions for object readiness and for object deletion.
* Get container logs and search for expected logging output.
* Plugin-managed RBAC permissions at test-case granularity using pytest markers.

For more information, see the [kubetest documentation][kubetest-docs].

## Installation

This plugin can be installed with `pip`

```
pip install kubetest
```

Note that the `kubetest` package has entrypoint hooks defined in its [`setup.py`](setup.py)
which allow it to be automatically made available to pytest. This means that it will run
whenever pytest is run. Since `kubetest` expects a cluster to be set up and to be given
configuration for that cluster, pytest will fail if those are not present. It is therefore
recommended to only install `kubetest` in a virtual environment or other managed environment,
such as a CI pipeline, where you can assure that cluster access and configuration are
available.

## Documentation

See the [kubetest documentation page][kubetest-docs] for details on command line usage,
available fixtures and markers, and general pytest integration.

## Feedback

Feedback for kubetest is greatly appreciated! If you experience any issues, find the
documentation unclear, have feature requests, or just have questions about it, we'd
love to know. Feel free to open an issue for any feedback you may have.

## License

kubetest is released under the [GPL-3.0](LICENSE) license.



[pytest]: https://docs.pytest.org/en/latest/
[k8s-py]: https://github.com/kubernetes-client/python
[kubetest-docs]: https://k8st3st.readthedocs.io/en/latest/
