# Changelog

## 0.4.0 (2026-04-09)

Full Changelog: [v0.4.0-beta.1...v0.4.0](https://github.com/mirurobotics/python-device-sdk/compare/v0.4.0-beta.1...v0.4.0)

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([60fcd65](https://github.com/mirurobotics/python-device-sdk/commit/60fcd65ff9436bb249c1efad1c4d4517dbe5365b))

## 0.4.0-beta.1 (2026-04-07)

Full Changelog: [v0.3.0...v0.4.0-beta.1](https://github.com/mirurobotics/python-device-sdk/compare/v0.3.0...v0.4.0-beta.1)

### Features

* **api:** regenerate with v0.2.1 release version ([5c227e5](https://github.com/mirurobotics/python-device-sdk/commit/5c227e56961d6bd0c2bc6fc85db25ac4cd0fffa6))
* **internal:** implement indices array format for query and form serialization ([b737cae](https://github.com/mirurobotics/python-device-sdk/commit/b737cae51f1e2e7171767ec1638a3a0b794b05c4))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([5787705](https://github.com/mirurobotics/python-device-sdk/commit/5787705bd4d745b52113af76a37532ab6b1ecb6d))
* **pydantic:** do not pass `by_alias` unless set ([ebde1af](https://github.com/mirurobotics/python-device-sdk/commit/ebde1af34610a632c00c5bcef2915a1fd5bac315))
* sanitize endpoint path params ([757293e](https://github.com/mirurobotics/python-device-sdk/commit/757293ec4220d42156d996cf24b47a4118fdfd77))


### Chores

* **ci:** skip lint on metadata-only changes ([4f76a08](https://github.com/mirurobotics/python-device-sdk/commit/4f76a088c4fd75483e252ff09d9e3e14e33f938b))
* **internal:** tweak CI branches ([c197558](https://github.com/mirurobotics/python-device-sdk/commit/c1975584103308b7e1e2ee909a73a83e456c5002))
* **internal:** update gitignore ([7a1b103](https://github.com/mirurobotics/python-device-sdk/commit/7a1b10309ddc8a64e87b4d55c4b9ccd5296c67d3))
* move event definitions to shared section stainless spec ([f83513a](https://github.com/mirurobotics/python-device-sdk/commit/f83513a4c89ff2ee8e36edb8fa1bfcc354db48cd))


### Refactors

* don't skip stream endpoint ([2dd2504](https://github.com/mirurobotics/python-device-sdk/commit/2dd25040ff22f140b81dfa90905d3a2b4935de06))
* remove stream endpoint ([b392d58](https://github.com/mirurobotics/python-device-sdk/commit/b392d580bc44319d70ad9a1c706c32bad48f341f))

## 0.3.0 (2026-03-10)

Full Changelog: [v0.3.0-beta.3...v0.3.0](https://github.com/mirurobotics/python-device-sdk/compare/v0.3.0-beta.3...v0.3.0)

### Features

* **api:** bump api spec to version v0.2.0 ([a86a5eb](https://github.com/mirurobotics/python-device-sdk/commit/a86a5eb2d0e938d0d6909e68e0a5003157164e4e))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([ac4ece9](https://github.com/mirurobotics/python-device-sdk/commit/ac4ece9a21bd48827186134e590c45547a9ad5a4))

## 0.3.0-beta.3 (2026-03-05)

Full Changelog: [v0.3.0-beta.2...v0.3.0-beta.3](https://github.com/mirurobotics/python-device-sdk/compare/v0.3.0-beta.2...v0.3.0-beta.3)

### Bug Fixes

* remove config instances from being nested inside deployments ([cd35a12](https://github.com/mirurobotics/python-device-sdk/commit/cd35a122583d74cef41db66a63ac42a29d9d8742))


### Chores

* update SDK settings ([bc7d9a1](https://github.com/mirurobotics/python-device-sdk/commit/bc7d9a1ea6fe3274804ca7f03f8b61770c201d05))
* update SDK settings ([10d3ea5](https://github.com/mirurobotics/python-device-sdk/commit/10d3ea5b22ec6f735e602f1c94e068a575b31152))

## 0.3.0-beta.2 (2026-03-05)

Full Changelog: [v0.3.0-beta.1...v0.3.0-beta.2](https://github.com/mirurobotics/python-device-sdk/compare/v0.3.0-beta.1...v0.3.0-beta.2)

### Features

* **api:** bump stainless edition to 2026-02-23 ([31cb0b9](https://github.com/mirurobotics/python-device-sdk/commit/31cb0b94e8799fc1a59ee17c738bbc038b793379))


### Bug Fixes

* correct client to talk to the miru unix socket ([4a7b9db](https://github.com/mirurobotics/python-device-sdk/commit/4a7b9db8b0561f82b0212a8e325d20f4cbddde6e))
* put python edition back to 2025-11-20 ([060cbf1](https://github.com/mirurobotics/python-device-sdk/commit/060cbf118e4ca81f4b9ebdbb73b297965e74598a))

## 0.3.0-beta.1 (2026-03-05)

Full Changelog: [v0.0.1...v0.3.0-beta.1](https://github.com/mirurobotics/python-device-sdk/compare/v0.0.1...v0.3.0-beta.1)

### Features

* **api:** init to v0.2.0-beta.3 ([1bbcc7a](https://github.com/mirurobotics/python-device-sdk/commit/1bbcc7acc6dd85c01d71588cf3f6527184826b8b))


### Bug Fixes

* host to point to correct localhost v0.2 version ([214fe96](https://github.com/mirurobotics/python-device-sdk/commit/214fe96ed48a8f5da3d09b7773cfe2c12bb4d033))


### Chores

* pin sdk to 2025-11-20 ([da48345](https://github.com/mirurobotics/python-device-sdk/commit/da483456ff2ce81b72b30b30311baf29e998ee1a))
* update SDK settings ([b8d224b](https://github.com/mirurobotics/python-device-sdk/commit/b8d224b9b9a1ba344780c2044c1402f38d10b016))
* update SDK settings ([cb90cd0](https://github.com/mirurobotics/python-device-sdk/commit/cb90cd0eedceee625945b1497d261a6c0491284c))
* use MIRU_AGENT_SOCKET for reading socket path from environment variable ([0b44866](https://github.com/mirurobotics/python-device-sdk/commit/0b448669a77106823ffa9b7d80d75cf84ae7c8de))
