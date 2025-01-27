# k8scheck

[![Build Status](https://github.com/3sIT/k8scheck/actions/workflows/main.yaml/badge.svg)](https://github.com/3sIT/k8scheck/actions/workflows/main.yaml)
[![codecov](https://codecov.io/gh/3sIT/k8scheck/branch/main/graph/badge.svg?token=XPYVCIGQNZ)](https://codecov.io/gh/3sIT/k8scheck)
[![PyPI](https://img.shields.io/pypi/v/k8scheck.svg)](https://pypi.org/project/k8scheck/)
[![Documentation Status](https://readthedocs.org/projects/k8scheck/badge/?version=latest)](https://k8scheck.readthedocs.io/en/latest/?badge=latest)

This is a (for the time being) compatible fork of [k8scheck](https://github.com/vapor-ware/k8scheck) as it now seems to be abandoned, installable using the package name k8scheck

# k8scheck
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

For more information, see the [k8scheck documentation][k8scheck-docs].

## Installation

This plugin can be installed with `pip`

```
pip install k8scheck
```

Note that the `k8scheck` package has entrypoint hooks defined in its [`setup.py`](setup.py)
which allow it to be automatically made available to pytest. This means that it will run
whenever pytest is run. Since `k8scheck` expects a cluster to be set up and to be given
configuration for that cluster, pytest will fail if those are not present. It is therefore
recommended to only install `k8scheck` in a virtual environment or other managed environment,
such as a CI pipeline, where you can assure that cluster access and configuration are
available.

## Documentation

See the [k8scheck documentation page][k8scheck-docs] for details on command line usage,
available fixtures and markers, and general pytest integration.

## Feedback

Feedback for k8scheck is greatly appreciated! If you experience any issues, find the
documentation unclear, have feature requests, or just have questions about it, we'd
love to know. Feel free to open an issue for any feedback you may have.

## License

k8scheck is released under the [GPL-3.0](LICENSE) license.



[pytest]: https://docs.pytest.org/en/latest/
[k8s-py]: https://github.com/kubernetes-client/python
[k8scheck-docs]: https://k8scheck.readthedocs.io/en/latest/
