# Changelog

## [0.7.0](https://github.com/mirurobotics/python-device-sdk/compare/v0.6.0...v0.7.0) (2026-10-09)


### ⚠ BREAKING CHANGES

* **deployments:** rename deployed_by to queued_by and add derived staged_by ([#316](https://github.com/mirurobotics/python-device-sdk/issues/316))
* **frontend:** remove release migrate endpoint ([#310](https://github.com/mirurobotics/python-device-sdk/issues/310))

### Features

* **cli:** add POST /config_schemas/validate dry-run endpoint ([#242](https://github.com/mirurobotics/python-device-sdk/issues/242)) ([926c448](https://github.com/mirurobotics/python-device-sdk/commit/926c448ff93c0926ce8f75114fc88138b97d577b))
* **client:** reach the agent over loopback TCP with its discovery file ([#3](https://github.com/mirurobotics/python-device-sdk/issues/3)) ([c620e55](https://github.com/mirurobotics/python-device-sdk/commit/c620e55244401a59f77a9d20beba2e6875dea7c2))
* **configs:** Windows file rule globs and read-only os fields ([#293](https://github.com/mirurobotics/python-device-sdk/issues/293)) ([542e06f](https://github.com/mirurobotics/python-device-sdk/commit/542e06fe790523dd2fa3b485e83185ef71f94d2f))
* **deployments:** rename deployed_by to queued_by and add derived staged_by ([#316](https://github.com/mirurobotics/python-device-sdk/issues/316)) ([1855452](https://github.com/mirurobotics/python-device-sdk/commit/1855452923ceb646e23c57d66aa8f490668fd364))
* **device:** add file_rule_ids to releases and GET /file_rules/{file_rule_id} ([#291](https://github.com/mirurobotics/python-device-sdk/issues/291)) ([c1555c7](https://github.com/mirurobotics/python-device-sdk/commit/c1555c7a471c50ec7f6940c9e8e030c8f7b92e89))
* **device:** bearer auth and SDK client options for the agent's loopback TCP API ([#302](https://github.com/mirurobotics/python-device-sdk/issues/302)) ([63afc05](https://github.com/mirurobotics/python-device-sdk/commit/63afc057977b07f85427fde82e25172d84e4b3c6))


### Bug Fixes

* **stlc:** make generate CI install work on Blacksmith (ssh-auth + npm cache) ([#147](https://github.com/mirurobotics/python-device-sdk/issues/147)) ([1cae83b](https://github.com/mirurobotics/python-device-sdk/commit/1cae83b20a90a3592a061bff2af4d56c9feb48af))


### Chores

* regenerate SDK from openapi config ([85afd61](https://github.com/mirurobotics/python-device-sdk/commit/85afd6104f6f2084a10f70e79f57d3b6bc392a78))
* **sdkgen:** repin stlc-python at a7fb576, set python floor &gt;= 3.10 ([#285](https://github.com/mirurobotics/python-device-sdk/issues/285)) ([d202ddf](https://github.com/mirurobotics/python-device-sdk/commit/d202ddf2e1dd8c333666f4d64a3fdb09d7ae525b))
* **sdkgen:** repin stlc-python to surgical re-lock (570bf02) ([#287](https://github.com/mirurobotics/python-device-sdk/issues/287)) ([8218315](https://github.com/mirurobotics/python-device-sdk/commit/8218315a114d40ab2e1d7f06307ffdeb8ecfeb84))


### Refactors

* **frontend:** remove release migrate endpoint ([#310](https://github.com/mirurobotics/python-device-sdk/issues/310)) ([e90cffa](https://github.com/mirurobotics/python-device-sdk/commit/e90cffa1c20228c00f6cc6dbccaea0196582f34a))

## 0.6.0 (2026-05-13)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/mirurobotics/python-device-sdk/compare/v0.5.0...v0.6.0)

### Features

* **internal/types:** support eagerly validating pydantic iterators ([7eeeef4](https://github.com/mirurobotics/python-device-sdk/commit/7eeeef4959b712d8a775756a9ccfcf118fa44557))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([c2a3082](https://github.com/mirurobotics/python-device-sdk/commit/c2a3082060589bd138f23d238c49f18fcbb507fe))


### Chores

* **internal:** reformat pyproject.toml ([0b1f068](https://github.com/mirurobotics/python-device-sdk/commit/0b1f0687b6a70d6628bec935d6db08fc0d08a63d))

## 0.5.0 (2026-04-28)

Full Changelog: [v0.4.2...v0.5.0](https://github.com/mirurobotics/python-device-sdk/compare/v0.4.2...v0.5.0)

### Features

* support setting headers via env ([da7da67](https://github.com/mirurobotics/python-device-sdk/commit/da7da6791838df33e5434184474e1d108439d452))


### Bug Fixes

* use correct field name format for multipart file arrays ([6a12b31](https://github.com/mirurobotics/python-device-sdk/commit/6a12b315a3abaf3047c46378a152533aefc28fed))


### Chores

* **internal:** more robust bootstrap script ([c35b72a](https://github.com/mirurobotics/python-device-sdk/commit/c35b72ad6ba2abfdbdf8a0f39701f27ccf8e73bb))

## 0.4.2 (2026-04-18)

Full Changelog: [v0.4.1...v0.4.2](https://github.com/mirurobotics/python-device-sdk/compare/v0.4.1...v0.4.2)

### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([fd3b74c](https://github.com/mirurobotics/python-device-sdk/commit/fd3b74cd8ecdcef06990954af65b75ad7837cb16))

## 0.4.1 (2026-04-11)

Full Changelog: [v0.4.0...v0.4.1](https://github.com/mirurobotics/python-device-sdk/compare/v0.4.0...v0.4.1)

### Bug Fixes

* ensure file data are only sent as 1 parameter ([04d351a](https://github.com/mirurobotics/python-device-sdk/commit/04d351a9b1708e7e9a807a7f8691134f0c8b2a5a))

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
