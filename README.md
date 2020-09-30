# Enigma Discord bot

Discord bot for testing and fun purposes.

## Commit convention

Commit messages __MUST__ use [Conventional Commits](https://www.conventionalcommits.org/en/) format. It provides guidelines to create a better commit history log, making easier to have automated tasks around it (e.g. automated changelogs). Commits would follow the format `<type>[(optional scope)]: <description>`, where `<type>` might be `feat`/`fix`/`core`/`docs` etc. and breaking changes are indicated on the beginning of the optional body or footer section. 

Example:
```
git commit -m "feat(survey): add nps survey to the home page

BREAKING CHANGE:  `survey` objects in xml file have been re-used in the global configurations.
```

Types other than `fix` and `feat` are allowed. Some examples are `build` / `core` / `ci` / `docs` / `style` / `refactor` / `perf` / `test`, and any other descriptive enough type.

Please refer to the current Conventional Commits [docs](https://www.conventionalcommits.org/en/v1.0.0-beta.4/#specification) for more details.