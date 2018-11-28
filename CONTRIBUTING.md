# Contributing to hangman

First off, thanks for taking the time to contribute! It's much appreciated!

The following is a set of guidelines for contributing to hangman and its packages, which are hosted in the TODO: add pypi
#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[I don't want to read this whole thing, I just have a question!!!](#i-dont-want-to-read-this-whole-thing-i-just-have-a-question)

[What should I know before I get started?](#what-should-i-know-before-i-get-started)
  * [hangman and Packages](#hangman-and-packages)
  * [hangman Design Decisions](#design-decisions)

[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Your First Code Contribution](#your-first-code-contribution)
  * [Pull Requests](#pull-requests)

[Styleguides](#styleguides)
  * [Git Commit Messages](#git-commit-messages)
  * [Documentation Styleguide](#documentation-styleguide)

[Additional Notes](#additional-notes)
  * [Issue and Pull Request Labels](#issue-and-pull-request-labels)

## Code of Conduct

This project and everyone participating in it is governed by the [hangman Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [atom@github.com](mailto:atom@github.com).

## I don't want to read this whole thing I just have a question!!!

> **Note:** [Please don't file an issue to ask a question.] TODO You'll get faster results by using the resources below.

We have an official message board with a detailed FAQ and where the community chimes in with helpful advice if you have questions.

* [Discuss, the official hangman message board] TODO
* [hangman FAQ] TODO

If chat is more your speed, you can join the hangman Slack team:

* [Join the hangman Team](https://TODO)
    * Even though Slack is a chat service, sometimes it takes several hours for community members to respond &mdash; please be patient!
    * Use the `#` channel for general questions or discussion about hangman
    * Use the `#` channel for questions about Electron
    * Use the `#` channel for questions or discussion about writing or contributing to hangman packages (both core and community)
    * Use the `#` channel for questions and discussion about hangman UI and themes
    * There are many other channels available, check the channel list

## What should I know before I get started?

### hangman and Packages

hangman is an open source project that serves as a hands-on introduction to the magic world of Python! When you initially consider contributing to hangman, you might be unsure about which of those 200 repositories implements the functionality you want to change or report a bug for. This section should help you with that.

#### Package Conventions TODO

### Design Decisions TODO

### Reporting Bugs TODO

This section guides you through submitting a bug report for hangman. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

Before creating bug reports, please check [this list](#before-submitting-a-bug-report) as you might find out that you don't need to create one. When you are creating a bug report, please [include as many details as possible](#how-do-i-submit-a-good-bug-report). Fill out [the required template](ISSUE_TEMPLATE.md), the information it asks for helps us resolve issues faster.

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.

#### Before Submitting A Bug Report

* **Check the [debugging guide] TODO ** You might be able to find the cause of the problem and fix things yourself. Most importantly, check if you can reproduce the problem , and if you can get the desired behavior by changing [hangman's or packages' config settings].
* **Check the [FAQs on the forum] TODO ** for a list of common questions and problems.
* **Determine [which repository the problem should be reported in] **.
* **Perform a [cursory search] TODO ** to see if the problem has already been reported. If it has **and the issue is still open**, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/). After you've determined [which repository] TODO your bug is related to, create an issue on that repository and provide the following information by filling in [the template](ISSUE_TEMPLATE.md).

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem**  
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.

Provide more context by answering these questions:

Include details about your configuration and environment:


### Suggesting Enhancements


#### Before Submitting An Enhancement Suggestion


#### How Do I Submit A (Good) Enhancement Suggestion?


### Your First Code Contribution

Unsure where to begin contributing to hangman? You can start by looking through these `beginner` and `help-wanted` issues:

* [Beginner issues][beginner] - issues which should only require a few lines of code, and a test or two.
* [Help wanted issues][help-wanted] - issues which should be a bit more involved than `beginner` issues.

Both issue lists are sorted by total number of comments. While not perfect, number of comments is a reasonable proxy for impact a given change will have.

#### Local development TODO

### Pull Requests TODO

The process described here has several goals:

- Maintain hangman's quality
- Fix problems that are important to users
- Engage the community in working toward the best possible hangman
- Enable a sustainable system for hangman's maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Follow all instructions in [the template](PULL_REQUEST_TEMPLATE.md)
2. Follow the [styleguides](#styleguides)
3. After you submit your pull request, verify that all [status checks](https://help.github.com/articles/about-status-checks/) are passing <details><summary>What if the status checks are failing?</summary>If a status check is failing, and you believe that the failure is unrelated to your change, please leave a comment on the pull request explaining why you believe the failure is unrelated. A maintainer will re-run the status check for you. If we conclude that the failure was a false positive, then we will open an issue to track that problem with our status check suite.</details>

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

## Styleguides TODO

### Git Commit Messages TODO

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* When only changing documentation, include `[ci skip]` in the commit title
* Consider starting the commit message with an applicable emoji:
    * :art: `:art:` when improving the format/structure of the code
    * :racehorse: `:racehorse:` when improving performance
    * :non-potable_water: `:non-potable_water:` when plugging memory leaks
    * :memo: `:memo:` when writing docs
    * :penguin: `:penguin:` when fixing something on Linux
    * :apple: `:apple:` when fixing something on macOS
    * :checkered_flag: `:checkered_flag:` when fixing something on Windows
    * :bug: `:bug:` when fixing a bug
    * :fire: `:fire:` when removing code or files
    * :green_heart: `:green_heart:` when fixing the CI build
    * :white_check_mark: `:white_check_mark:` when adding tests
    * :lock: `:lock:` when dealing with security
    * :arrow_up: `:arrow_up:` when upgrading dependencies
    * :arrow_down: `:arrow_down:` when downgrading dependencies
    * :shirt: `:shirt:` when removing linter warnings

### Documentation Styleguide TODO

* Use [Markdown](https://daringfireball.net/projects/markdown)

## Additional Notes TODO

### Issue and Pull Request Labels TODO

This section lists the labels we use to help us track and manage issues and pull requests. Most labels are used across all Atom repositories, but some are specific to `atom/atom`.

[GitHub search](https://help.github.com/articles/searching-issues/) makes it easy to use labels for finding groups of issues or pull requests you're interested in. For example, you might be interested in [open issues across `atom/atom` and all Atom-owned packages which are labeled as bugs, but still need to be reliably reproduced](https://github.com/search?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+user%3Aatom+label%3Abug+label%3Aneeds-reproduction) or perhaps [open pull requests in `atom/atom` which haven't been reviewed yet](https://github.com/search?utf8=%E2%9C%93&q=is%3Aopen+is%3Apr+repo%3Aatom%2Fatom+comments%3A0). To help you find issues and pull requests, each label is listed with search links for finding open items with that label in `atom/atom` only and also across all Atom repositories. We  encourage you to read about [other search filters](https://help.github.com/articles/searching-issues/) which will help you write more focused queries.

The labels are loosely grouped by their purpose, but it's not required that every issue have a label from every group or that an issue can't have more than one label from the same group.

Please open an issue on `/` if you have suggestions for new labels, and if you notice some labels are missing on some repositories, then please open an issue on that repository.

#### Type of Issue and Issue State

| Label name | `/` :mag_right: | ``‑org :mag_right: | Description |
| --- | --- | --- | --- |
| `enhancement` | [search][] | [search][] | Feature requests. |
| `bug` | [search][] | [search][] | Confirmed bugs or reports that are very likely to be bugs. |
| `question` | [search][] | [search][] | Questions more than bug reports or feature requests (e.g. how do I do X). |
| `feedback` | [search][] | [search][] | General feedback more than bug reports or feature requests. |
| `help-wanted` | [search][] | [search][] | The hangman core team would appreciate help from the community in resolving these issues. |
| `beginner` | [search][] | [search][] | Less complex issues which would be good first issues to work on for users who want to contribute to hangman. |
| `more-information-needed` | [search][] | [search][] | More information needs to be collected about these problems or feature requests (e.g. steps to reproduce). |
| `needs-reproduction` | [search][] | [search][] | Likely bugs, but haven't been reliably reproduced. |
| `blocked` | [search][] | [search][] | Issues blocked on other issues. |
| `duplicate` | [search][] | [search][] | Issues which are duplicates of other issues, i.e. they have been reported before. |
| `wontfix` | [search][] | [search][] | The hangman core team has decided not to fix these issues for now, either because they're working as intended or for some other reason. |
| `invalid` | [search][] | [search][] | Issues which aren't valid (e.g. user errors). |
| `package-idea` | [search][] | [search][] | | 


#### `/` Topic Categories TODO

| Label name | `/` :mag_right: | ``‑org :mag_right: | Description |
| --- | --- | --- | --- |
| `editor-rendering` | [search][] | [search][] | Related to language-independent aspects of rendering text (e.g. scrolling, soft wrap, and font rendering). |
| `build-error` | [search][] | [search][] | Related to problems with building hangman from source. |
| `error-from-save` | [search][] | [search][] | Related to errors thrown when saving files. |
| `error-from-open` | [search][] | [search][] | Related to errors thrown when opening files. |
| `installer` | [search][] | [search][] | Related to the hangman installers for different OSes. |
| `auto-updater` | [search][] | [search][] | Related to the auto-updater for different OSes. |
| `deprecation-help` | [search][] | [search][] | Issues for helping package authors remove usage of deprecated APIs in packages. |

#### Pull Request Labels TODO

| Label name | `/` :mag_right: | ``‑org :mag_right: | Description
| --- | --- | --- | --- |
| `work-in-progress` | [search][] | [search][] | Pull requests which are still being worked on, more changes will follow. |
| `needs-review` | [search][] | [search][] | Pull requests which need code review, and approval from maintainers or hangman core team. |
| `under-review` | [search][] | [search][] | Pull requests being reviewed by maintainers or hangman core team. |
| `requires-changes` | [search][] | [search][] | Pull requests which need to be updated based on review comments and then reviewed again. |
| `needs-testing` | [search][] | [search][] | Pull requests which need manual testing. |

TODO


TODO
[beginner]:
[help-wanted]:
