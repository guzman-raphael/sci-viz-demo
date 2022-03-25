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

### Acknowledgements

We'd like to thank [internationalbrainlab.org](https://data.internationalbrainlab.org) for releasing
publicly various sets of experimental workflow data. In order to provide a DEMO that
seems more *relevant* we've used this public data to help grasp some of the concepts
of what is currently supported in SciViz.

## Instructions to run the DEMO

To run this environment, all that is needed is to have [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/gettingstarted/) available. Be sure to refer to the comment header in the `docker-compose.yaml` on specific command details to bring up the environment. Please create a `.env` (at least empty) as a placeholder for storing sensitive data.

For the login, there are 2 options:
1. (recommended) If you are a member of DataJoint's full time staff, you can use the credentials called `SciViz DEMO: IBL Public (internal)` in our LastPass for application login. This will allow the `Psychometric Curves` page to render the plots properly. Also, have a look at `SciViz DEMO: IBL Public S3 (internal)` in LastPass for S3 connection details for the spinning brain GIF. Since this data is sensitive, it should be included in the `.env` so that it is properly ignored from commits. Have a look in `example.env` for more instructions.
1. For external contributors, you may use the public credential set provided by IBL; see [here](https://int-brain-lab.github.io/iblenv/dj_docs/public_datajoint.html#accessing-the-public-database-on-your-local-machine) for more details. Be aware that based on IBL's current policy around plots, none of the plots or images will render properly as IBL has not yet made the plots publicly accessible. Specifically the plots in the `Psychometric Curves` page and the plots and spinning brain GIF in the individual `Session` pages.

## Tips and Notes
- Loading the frontend after a fresh start takes the longest since it is optimizing the hot-reloads based on the first load. After that, reloads will be much faster.
- To allow bearer tokens to be reused between service restarts:
  - Make sure to create a `.env` file with the asymmetric key pair stored in environment variables:
    - `PHARUS_PRIVATE_KEY`
    - `PHARUS_PUBLIC_KEY`
  - See `example.env` for a pair that is valid. You may directly use this for DEMO's as well.
