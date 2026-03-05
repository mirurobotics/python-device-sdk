# Agent

Types:

```python
from miru_device_sdk.types import AgentHealthResponse, AgentVersionResponse
```

Methods:

- <code title="get /health">client.agent.<a href="./src/miru_device_sdk/resources/agent.py">health</a>() -> <a href="./src/miru_device_sdk/types/agent_health_response.py">AgentHealthResponse</a></code>
- <code title="get /version">client.agent.<a href="./src/miru_device_sdk/resources/agent.py">version</a>() -> <a href="./src/miru_device_sdk/types/agent_version_response.py">AgentVersionResponse</a></code>

# Deployments

Types:

```python
from miru_device_sdk.types import Deployment
```

Methods:

- <code title="get /deployments/{deployment_id}">client.deployments.<a href="./src/miru_device_sdk/resources/deployments.py">retrieve</a>(deployment_id) -> <a href="./src/miru_device_sdk/types/deployment.py">Deployment</a></code>
- <code title="get /deployments/current">client.deployments.<a href="./src/miru_device_sdk/resources/deployments.py">current</a>() -> <a href="./src/miru_device_sdk/types/deployment.py">Deployment</a></code>

# Device

Types:

```python
from miru_device_sdk.types import DeviceRetrieveResponse, DeviceSyncResponse
```

Methods:

- <code title="get /device">client.device.<a href="./src/miru_device_sdk/resources/device.py">retrieve</a>() -> <a href="./src/miru_device_sdk/types/device_retrieve_response.py">DeviceRetrieveResponse</a></code>
- <code title="post /device/sync">client.device.<a href="./src/miru_device_sdk/resources/device.py">sync</a>() -> <a href="./src/miru_device_sdk/types/device_sync_response.py">DeviceSyncResponse</a></code>

# GitCommits

Types:

```python
from miru_device_sdk.types import GitCommit
```

Methods:

- <code title="get /git_commits/{git_commit_id}">client.git_commits.<a href="./src/miru_device_sdk/resources/git_commits.py">retrieve</a>(git_commit_id) -> <a href="./src/miru_device_sdk/types/git_commit.py">GitCommit</a></code>

# Releases

Types:

```python
from miru_device_sdk.types import Release
```

Methods:

- <code title="get /releases/{release_id}">client.releases.<a href="./src/miru_device_sdk/resources/releases.py">retrieve</a>(release_id) -> <a href="./src/miru_device_sdk/types/release.py">Release</a></code>
- <code title="get /releases/current">client.releases.<a href="./src/miru_device_sdk/resources/releases.py">current</a>() -> <a href="./src/miru_device_sdk/types/release.py">Release</a></code>
