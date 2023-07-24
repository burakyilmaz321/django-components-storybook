# django-components-storybook

Create [Storybook](https://storybook.js.org/) stories for [Django Components](https://github.com/EmilStenstrom/django-components).

Inspired by [View Component Storybook](https://jonspalmer.github.io/view_component-storybook/) of Ruby on Rails [View Component](https://viewcomponent.org/). Uses [Storybook Server Framework](https://github.com/storybookjs/storybook/tree/next/code/frameworks/server-webpack5).

> **Warning:** This is a very early stage draft of the initial idea.

**Usage**

Add this to your url configuration:

```python
urlpatterns = [
    # ...your existing url configuration
    path("storybook/components/", include("django_components_storybook.urls")),
]
```

Initialize Storybook:

```bash
npx storybook@latest init -t server
```

Add the following configuration to ``.storybook/preview.js``

```javascript
const preview = {
  parameters: {
    // ...existing configuration
    server: {
      url: `http://localhost:8000/storybook/components`,
    },
  },
};
```

**Roadmap**

- Handle slots
- Generate ``.storybook/preview-head.html`` 
- Generate stories automatically
