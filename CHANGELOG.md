# Changelog

## [0.8.1](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.8.0...v0.8.1) (2025-03-26)


### Bug Fixes

* adapt to changes in storage interface 4.1.0 ([930e19f](https://github.com/snakemake/poetry-snakemake-plugin/commit/930e19fb3b23f54e7b5a9e1b9e1aaf7df2bd9b64))
* adapt to snakemake 9 main codebase refactoring ([25b4c6a](https://github.com/snakemake/poetry-snakemake-plugin/commit/25b4c6ab4857fe204d926b8318e92db254822fc0))


### Documentation

* add info about improved storage interface ([ba62af2](https://github.com/snakemake/poetry-snakemake-plugin/commit/ba62af2a2a768685ec6212b0d60a7252cb42d1c7))

## [0.8.0](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.7.2...v0.8.0) (2025-03-14)


### Features

* Add postprocess_query and safe_print to the storage scaffold ([#35](https://github.com/snakemake/poetry-snakemake-plugin/issues/35)) ([a9123f6](https://github.com/snakemake/poetry-snakemake-plugin/commit/a9123f6580941e1a5c2a4f9a60644fcd3898c75f))


### Bug Fixes

* add common_settings to software deployment skeleton ([509bd83](https://github.com/snakemake/poetry-snakemake-plugin/commit/509bd834b17403196356c71cb6840f4441d0f55a))

## [0.7.2](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.7.1...v0.7.2) (2025-03-08)


### Bug Fixes

* adapt skeleton ([325a836](https://github.com/snakemake/poetry-snakemake-plugin/commit/325a83644ecaadf21baea0018d81d7e4628c0da9))
* adapt to changes in software deployment interface ([930e7ec](https://github.com/snakemake/poetry-snakemake-plugin/commit/930e7ecd9353f326cccf6a37c1c19f333d805aad))
* adapt to changes in software deployment interface ([5142d7f](https://github.com/snakemake/poetry-snakemake-plugin/commit/5142d7f1ec4440a7fd2f12eae8d4709f41cb0e72))
* adapt to changes in software deployment interface ([279bb5d](https://github.com/snakemake/poetry-snakemake-plugin/commit/279bb5d2f9b21174ef59308a3134f983c7220ffc))
* adapt to changes in software deployment interface ([a548c07](https://github.com/snakemake/poetry-snakemake-plugin/commit/a548c0729e1163b045d2e2139153fadf850ad89e))
* adapt to interface changes ([2920722](https://github.com/snakemake/poetry-snakemake-plugin/commit/2920722f7b0ff9a4fb7bf6950b1357f566a1abb4))
* adapt to latest changes in software deployment interface ([66b4706](https://github.com/snakemake/poetry-snakemake-plugin/commit/66b470685de9b888ccab869f3973a0e39dfac9ba))
* more documentation in software deployment plugin template ([14e0d78](https://github.com/snakemake/poetry-snakemake-plugin/commit/14e0d78181c26f0f256573e85e755f80dbe6e274))
* provide WorkflowError and instruct on error handling ([c6740c8](https://github.com/snakemake/poetry-snakemake-plugin/commit/c6740c81cc83fb2ba3d374bdc6bc67be48d8554b))


### Documentation

* fix plugin naming ([185104f](https://github.com/snakemake/poetry-snakemake-plugin/commit/185104f7d7443497d7f69941efdd2f6cdb8d4f17))
* update plugin ([e095337](https://github.com/snakemake/poetry-snakemake-plugin/commit/e095337e0aaa51e1660fa51c70f644a5bc2e815f))

## [0.7.1](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.7.0...v0.7.1) (2025-03-07)


### Bug Fixes

* adapt to improvements in snakemake software deployment plugin interface ([#32](https://github.com/snakemake/poetry-snakemake-plugin/issues/32)) ([0744e32](https://github.com/snakemake/poetry-snakemake-plugin/commit/0744e32fe297518419d8cb79e6c968aad20dc139))
* only include snakemake as a dev dependency if that is absolutely necessary ([#30](https://github.com/snakemake/poetry-snakemake-plugin/issues/30)) ([408c6fb](https://github.com/snakemake/poetry-snakemake-plugin/commit/408c6fb2a0e708fc39ee83c040b26ff15bc821ce))

## [0.7.0](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.6.1...v0.7.0) (2025-03-05)


### Features

* use ruff for formatting and linting ([#28](https://github.com/snakemake/poetry-snakemake-plugin/issues/28)) ([08885d2](https://github.com/snakemake/poetry-snakemake-plugin/commit/08885d21c360cc07fb694c7c715c30b07e1331e1))

## [0.6.1](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.6.0...v0.6.1) (2025-03-05)


### Bug Fixes

* adapt template structure to poetry 2 ([#26](https://github.com/snakemake/poetry-snakemake-plugin/issues/26)) ([29c9512](https://github.com/snakemake/poetry-snakemake-plugin/commit/29c95124bdd682d0842c005e5f37af1f535228f3))

## [0.6.0](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.5.0...v0.6.0) (2025-03-02)


### Miscellaneous Chores

* Release 0.6.0 ([06a01c7](https://github.com/snakemake/poetry-snakemake-plugin/commit/06a01c79665873dafc885616bb63538a1a223de3))

## [0.5.0](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.4.0...v0.5.0) (2025-03-02)


### Features

* support for software deployment plugins ([#22](https://github.com/snakemake/poetry-snakemake-plugin/issues/22)) ([32508f6](https://github.com/snakemake/poetry-snakemake-plugin/commit/32508f67b70888f0e4c408297cb3578cf2437d47))


### Bug Fixes

* extend tests template for storage plugins ([#20](https://github.com/snakemake/poetry-snakemake-plugin/issues/20)) ([90e22b1](https://github.com/snakemake/poetry-snakemake-plugin/commit/90e22b174553e651dcd5a3fe3cab55179df87d03))
* nargs ([0f42900](https://github.com/snakemake/poetry-snakemake-plugin/commit/0f4290036b5c40c4956f17f0b96d258f60a942ad))

## [0.4.0](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.3.4...v0.4.0) (2024-02-16)


### Features

* support for report plugins ([#18](https://github.com/snakemake/poetry-snakemake-plugin/issues/18)) ([91da3d3](https://github.com/snakemake/poetry-snakemake-plugin/commit/91da3d3d4c992eb48dcd3a350717388dfc97a57b))


### Bug Fixes

* python version order and CI scaffold ([#9](https://github.com/snakemake/poetry-snakemake-plugin/issues/9)) ([f5f7250](https://github.com/snakemake/poetry-snakemake-plugin/commit/f5f725065bf2fb056ebc4fcfb3efa04a7489bb40))

## [0.3.4](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.3.3...v0.3.4) (2023-12-12)


### Bug Fixes

* adapt to interface changes; add more metadata to templates ([#14](https://github.com/snakemake/poetry-snakemake-plugin/issues/14)) ([d3efe48](https://github.com/snakemake/poetry-snakemake-plugin/commit/d3efe48ba27fdade0d56920463448b9d90f24606))
* job_deploy_sources in CommonSettings ([#16](https://github.com/snakemake/poetry-snakemake-plugin/issues/16)) ([321998e](https://github.com/snakemake/poetry-snakemake-plugin/commit/321998e62771b8a4af0d9534fefac1f813d30a38))
* JobExecutorInterface ([#15](https://github.com/snakemake/poetry-snakemake-plugin/issues/15)) ([8cb86f3](https://github.com/snakemake/poetry-snakemake-plugin/commit/8cb86f39bd0a47fa8559dd9cfbff211ca6b3530d))

## [0.3.3](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.3.2...v0.3.3) (2023-12-06)


### Bug Fixes

* adapt to interface changes ([#12](https://github.com/snakemake/poetry-snakemake-plugin/issues/12)) ([513e702](https://github.com/snakemake/poetry-snakemake-plugin/commit/513e7028952da9826dfc4453ffcc434d4dd079a0))

## [0.3.2](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.3.1...v0.3.2) (2023-11-23)


### Bug Fixes

* improve templates ([920825f](https://github.com/snakemake/poetry-snakemake-plugin/commit/920825f5d5554362dc12a05fe1548d3527bce53c))
* remove superfluous method ([36dcc42](https://github.com/snakemake/poetry-snakemake-plugin/commit/36dcc421c18691fc7a46362b959b903b04a42f49))

## [0.3.1](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.3.0...v0.3.1) (2023-11-15)


### Bug Fixes

* update storage plugin template ([cabf4d8](https://github.com/snakemake/poetry-snakemake-plugin/commit/cabf4d850e24567a2aa3abaf7c14d257e4f2bf70))
* update template ([35c733d](https://github.com/snakemake/poetry-snakemake-plugin/commit/35c733d5597cff9dcb6fafd97dfb8c4c967df83b))
* update test template ([13037c7](https://github.com/snakemake/poetry-snakemake-plugin/commit/13037c7611bb9a87afbe495d00279502d9040a46))
* update test template ([175ac0a](https://github.com/snakemake/poetry-snakemake-plugin/commit/175ac0a9148b8c9526d21472165dc8dc7f7425e5))


### Documentation

* update comments in template ([c503631](https://github.com/snakemake/poetry-snakemake-plugin/commit/c5036311d9b979869c15819728ad7b43999ef340))

## [0.3.0](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.2.2...v0.3.0) (2023-10-17)


### Features

* add unparse_func ([b5cd066](https://github.com/snakemake/poetry-snakemake-plugin/commit/b5cd0669f26fe19168d5d304e01e2055dc080707))
* support for storage plugins ([a769e93](https://github.com/snakemake/poetry-snakemake-plugin/commit/a769e93d8685c93775182fa0baf729c3410c7d83))


### Bug Fixes

* adapt to API changes in snakemake-interface-storage-plugins ([70c0655](https://github.com/snakemake/poetry-snakemake-plugin/commit/70c0655896ae0681e3c05888da2ff55482357646))
* adapt to upcoming API changes in Snakemake 8 ([97f5a50](https://github.com/snakemake/poetry-snakemake-plugin/commit/97f5a50d8a98f2bea45b1a5cea7e117e565e7a3f))


### Documentation

* add explanation for envvar handling ([16b7884](https://github.com/snakemake/poetry-snakemake-plugin/commit/16b78844c2338b94ce0e98222fec8bb183bec9ec))
* improve documentation ([976c05e](https://github.com/snakemake/poetry-snakemake-plugin/commit/976c05ededde9f97b4bf10460e0e3a1de4f411f8))

## [0.2.2](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.2.1...v0.2.2) (2023-09-11)


### Bug Fixes

* fixed formatting and lints ([f38e0e7](https://github.com/snakemake/poetry-snakemake-plugin/commit/f38e0e70b175704e21dcae4dcaf65c3a37aa5832))

## [0.2.1](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.2.0...v0.2.1) (2023-09-11)


### Bug Fixes

* add snakemake-interface-common as dependency ([05074f8](https://github.com/snakemake/poetry-snakemake-plugin/commit/05074f8bb1cb52ba3470720fba94880976b67c79))
* update skeleton tp latest changes in snakemake-interface-executor-plugins ([b69f552](https://github.com/snakemake/poetry-snakemake-plugin/commit/b69f552c2d44e3617ea9b48279d21e586c687af1))


### Documentation

* add information about env var specification ([a9827f8](https://github.com/snakemake/poetry-snakemake-plugin/commit/a9827f820b604af8937c8b994ad8be1a14738119))
* init_sleep_seconds ([f629cc0](https://github.com/snakemake/poetry-snakemake-plugin/commit/f629cc036e4ce3df5ff8ac4aef543003febff80b))
* mention self.next_sleep_seconds ([e605a6b](https://github.com/snakemake/poetry-snakemake-plugin/commit/e605a6b4b9ecdb0e1ab9f957b5ac3b01e9f1a68d))
* update skeleton ([9ccff06](https://github.com/snakemake/poetry-snakemake-plugin/commit/9ccff063249062299e87606fe882814e434a0b9a))

## [0.2.0](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.1.1...v0.2.0) (2023-09-07)


### Features

* add test template ([08d7b0d](https://github.com/snakemake/poetry-snakemake-plugin/commit/08d7b0dc2c44be120b6b054b1860a18d2e1045db))


### Bug Fixes

* fix function output ([2d96cda](https://github.com/snakemake/poetry-snakemake-plugin/commit/2d96cda296173a5a917b986128e139456b2b8857))
* fixed lints in template, cleanup superfluous file ([d9c64ea](https://github.com/snakemake/poetry-snakemake-plugin/commit/d9c64ea4d501723fb3836aa36e0a403df8323e49))

## [0.1.1](https://github.com/snakemake/poetry-snakemake-plugin/compare/v0.1.0...v0.1.1) (2023-09-06)


### Bug Fixes

* improve description ([c95edea](https://github.com/snakemake/poetry-snakemake-plugin/commit/c95edea466ffac3342846c9dcca8182b806c4e60))


### Documentation

* instructions ([cbaf704](https://github.com/snakemake/poetry-snakemake-plugin/commit/cbaf704eac4a3ffff6b5318ee8222ca942ae5bb8))

## 0.1.0 (2023-09-06)


### Bug Fixes

* move coverage dependency to dev group ([a606263](https://github.com/snakemake/poetry-snakemake-plugin/commit/a606263076875dae49570458fce731093567b6fb))
* update template ([7869360](https://github.com/snakemake/poetry-snakemake-plugin/commit/7869360b0fe8382b0096b9bbbedde92ba07358b2))
