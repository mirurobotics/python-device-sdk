# Health

Types:

```python
from miru_device.types import HealthRetrieveResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/miru_device/resources/health.py">retrieve</a>() -> <a href="./src/miru_device/types/health_retrieve_response.py">HealthRetrieveResponse</a></code>

# Version

Types:

```python
from miru_device.types import VersionRetrieveResponse
```

Methods:

- <code title="get /version">client.version.<a href="./src/miru_device/resources/version.py">retrieve</a>() -> <a href="./src/miru_device/types/version_retrieve_response.py">VersionRetrieveResponse</a></code>

# Deployments

Types:

```python
from miru_device.types import Deployment
```

Methods:

- <code title="get /deployments/{deployment_id}">client.deployments.<a href="./src/miru_device/resources/deployments.py">retrieve</a>(deployment_id) -> <a href="./src/miru_device/types/deployment.py">Deployment</a></code>
- <code title="get /deployments/current">client.deployments.<a href="./src/miru_device/resources/deployments.py">get_current</a>() -> <a href="./src/miru_device/types/deployment.py">Deployment</a></code>

# Device

Types:

```python
from miru_device.types import DeviceRetrieveResponse, DeviceSyncResponse
```

Methods:

- <code title="get /device">client.device.<a href="./src/miru_device/resources/device.py">retrieve</a>() -> <a href="./src/miru_device/types/device_retrieve_response.py">DeviceRetrieveResponse</a></code>
- <code title="post /device/sync">client.device.<a href="./src/miru_device/resources/device.py">sync</a>() -> <a href="./src/miru_device/types/device_sync_response.py">DeviceSyncResponse</a></code>

# GitCommits

Types:

```python
from miru_device.types import GitCommitRetrieveResponse
```

Methods:

- <code title="get /git_commits/{git_commit_id}">client.git_commits.<a href="./src/miru_device/resources/git_commits.py">retrieve</a>(git_commit_id) -> <a href="./src/miru_device/types/git_commit_retrieve_response.py">GitCommitRetrieveResponse</a></code>

# Releases

Types:

```python
from miru_device.types import Release
```

Methods:

- <code title="get /releases/{release_id}">client.releases.<a href="./src/miru_device/resources/releases.py">retrieve</a>(release_id) -> <a href="./src/miru_device/types/release.py">Release</a></code>
- <code title="get /releases/current">client.releases.<a href="./src/miru_device/resources/releases.py">retrieve_current</a>() -> <a href="./src/miru_device/types/release.py">Release</a></code>
