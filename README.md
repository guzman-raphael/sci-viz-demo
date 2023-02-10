# SciViz DEMO

Welcome 👋

This repository is meant to be used as a SciViz local demonstration to illustrate the latest features included as part of the visualization framework. Below you can read more about the motivation and components. 

## DataJoint™ powered visualization that adapts to *your* workflows

![](https://images.squarespace-cdn.com/content/v1/60e5a50c0632d17c36f6b2d3/1638463454411-SMVPVS9EBPLU9T9T5YMN/unsplash-image-Pyut03Gn98w.jpg?format=1000w)

### Features

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

### Component Library Types
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
  - font/backgrond highlighting
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
