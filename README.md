# Bazel Worksop

This repository includes examples of bazel projects along with execises which are to be used for the [HiQ](https://hiq.se/) Academy Bazel workshop.

## Environment

### Bazelisk

Bazelisk is a wrapper of Bazel and will install the relevant bazel version when running bazel commands.

macOS
```
brew install bazelisk
```
Windows
```
winget install Bazel.Bazelisk
```
Ubuntu
```
sudo apt-get install npm
npm install -g @bazel/bazelisk
```

Editor: [VS Code](https://code.visualstudio.com/download)
Extensions:
- [Bazel](https://marketplace.visualstudio.com/items?itemName=BazelBuild.vscode-bazel)

## Useful links

* [Get Started with Bazel quickley](https://bazel.build/start/cpp) - Getting started turtorial
* [bazelbuild/examples](https://github.com/bazelbuild/examples) - Bazel examples for many different languages using many different features in bazel
* [Bazel Central Registry](https://registry.bazel.build/) - Registry of publicly available Bazel rules

## Task List

### 1) Verify Bazel install

**New feature:** Bazel CLI basics

- Install Bazel or Bazelisk.
- Run `bazel version` and `bazel help`.

**Done when:** You can run Bazel commands successfully.

### 2) Initialize a Bazel workspace

**New feature:** `MODULE.bazel`

- Create `MODULE.bazel` at repo root.
- Add module name and version.

**Done when:** `bazel info` works from the repo root.

### 3) Bring in an external dependency using Bzlmod

**New feature:** `bazel_dep`

- Add one third-party library from the Bazel registry.
- Tip: For the next task, you may need to bring in the language specific rules from [Bazel Central Registry](https://registry.bazel.build/)

**Done when:** External dep is resolved and used in build/test.

### 4) Create your first package and target

**New feature:** `BUILD.bazel`, packages, labels

- Create one package (for example `app/`).
- Add one executable target in your language.

**Done when:** `bazel run //app:main` works.

### 5) Split code into libraries and binary

**New feature:** `deps` and target graph

- Move reusable code into a library target.
- Make binary depend on library.

**Done when:** Binary still runs and tests still pass.

### 6) Add your first test

**New feature:** `*_test` rules

- Add at least one unit test target.
- Make one passing assertion.

**Done when:** `bazel test //app:...` passes.

### 7) Create a second package and use cross-package labels

**New feature:** package boundaries and absolute labels

- Add another package (for example `lib/` or `util/`).
- Reference it from your app package via `//pkg:target` label syntax.

**Done when:** Build succeeds with cross-package dependency.

### 8) Restrict target access with visibility

**New feature:** `visibility`

- Mark one internal library as private.
- Keep one API library public.

**Done when:** Invalid dependency attempts fail with visibility errors.

### 9) Use `glob()` and `filegroup`

**New feature:** source aggregation

- Replace explicit source lists with `glob()` where sensible.
- Create a `filegroup` for a non-code asset collection.

**Done when:** Build uses grouped files without manual per-file listing.

### 10) Add runtime data files

**New feature:** `data` attribute and runfiles

- Add config/template/input files consumed at runtime.
- Access them via Bazel runfiles-friendly approach.

**Done when:** `bazel run` works without relying on working-directory hacks.

### 11) Introduce tags and test size metadata

**New feature:** `tags`, `size`, `timeout`

- Tag tests (for example `unit`, `integration`).
- Set size/timeout intentionally.

**Done when:** You can filter tests with Bazel flags.
Example bazel command to run all small tests:

```
bazel test --test_size_filters=small //:all
```

### 12) Write a simple Starlark macro

**New feature:** `.bzl` macros

- Create macro wrapping repeated target patterns.
- Use macro in at least two packages.

**Done when:** Repetition in BUILD files decreases.

### 13) Write a custom Starlark rule

**New feature:** `rule()`, `ctx.actions`

- Implement a tiny custom rule (for example transform text, validate schema, etc.).
- Expose useful outputs/providers.

**Done when:** Custom rule runs as part of normal build graph.

### 14) Explore dependency graph with query

**New feature:** `bazel query`

- Visualize deps and reverse deps for key targets.
- Identify one unnecessary dependency and remove it.

**Done when:** Dependency graph is cleaner and justified.
