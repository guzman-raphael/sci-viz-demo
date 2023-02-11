# DataJoint™ powered visualization that adapts to *your* workflows

![](https://images.squarespace-cdn.com/content/v1/60e5a50c0632d17c36f6b2d3/1638463454411-SMVPVS9EBPLU9T9T5YMN/unsplash-image-Pyut03Gn98w.jpg?format=1000w)

## Features

- Visualization that can **keep up with changing needs** of your lab
- Standardized YAML build specification providing a **Low-Code web application
  design** experience
- Transport-optimization by leveraging **client-side rendering** with
  [React](https://reactjs.org/)
- **Python+[DataJoint](https://www.datajoint.org/) interoperability** to allow
  streamlined integration
- Clear separation between business logic from product features i.e. **customization
  through configuration**
- **Backend-optimized** page rendering built for big-data and scale
- Comprehensive permission and security design enabling **flexible access control**
  modes
- Securely **manage sensitive information** by configuring it separtely and referencing it in LC spec
- Pain-free deployments by supporting **live-reload** on changes to configuration
- Shared, immutable **global variables** available to all components

## Component Library Types
- `markdown`: Often it is necessary to document or describe views via Markdown
- `page`:
  - Unique tabbed pages to separate areas within your single-page application
  - Hidden pages accessible through linking from records in table components
- `grid`: Layout structure for organizing subcomponents (as seen in
  [Grafana, AWS Console](https://github.com/react-grid-layout/react-grid-layout#projects-using-react-grid-layout))
  - `fixed`: For when you know exactly how many components you'd like to render
  - `dynamic`: Component templating mode when you need to render realtime views that
    vary in number of components
- `table`: Sometimes there's nothing better than a table view
  - paging
  - sorting
  - filtering
- `metadata`: Great for showing context info for particular views
- `plot`: Let's face it, we are going to need to be able to plot stuff
  - plotly
- `image`: When you need to render an image file's data directly within the grid
  - `*.apng`
  - `*.avif`
  - `*.gif`
  - `*.jpeg`
  - `*.png`
  - `*.svg`
  - `*.webp`
- `custom`: Adding new, custom components is easy with our extensibility hook. See our currently supported components [here](https://github.com/datajoint/pharus/blob/master/pharus/component_interface.py) which you can reference when creating your own.

# Running the DEMO

The recommended environment to run the demo is included as a [DevContainer](https://containers.dev/).

## Launch Environment

Here are some options that provide a great demo experience:

- **Cloud-based IDE**: (*recommended*)
  - Launch using [GitHub Codespaces](https://github.com/features/codespaces) using the option `Create codespace on main` in the codebase repository on your fork.
  - Build time for a 2-Core codespace is **~?m**. This is done infrequently and cached for convenience.
  - Start time for a 2-Core codespace is **~?m**. This will pull the built codespace from cache when you need it.
  - Tip: GitHub auto names the codespace but you can rename the codespace so that it is easier to identify later.
- **Local IDE**:
  - Ensure you have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  - Ensure you have [Docker](https://docs.docker.com/get-docker/)
  - Ensure you have [VSCode](https://code.visualstudio.com/)
  - Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
  - `git clone` the codebase repository and open it in VSCode
  - Use the `Dev Containers extension` to `Reopen in Container` (More info in the `Getting started` included with the extension)
  - Your environment will finish loading once the file tree is populated and the terminal become active??
