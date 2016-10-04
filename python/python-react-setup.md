* [Step 1: Create your Django project](#Step-1:-Create-your-Django-Project)
* [Step 2: Add non-reactJS views](#Step-2:-Add-non-reactJS-views)
* [Refer to](#Refer-to)

## Step 1: Create your Django project

### Install Django

```bash
$ mkdir django-reactjs-boilerplate && cd django-reactjs-boilerplate
$ python3 -m venv env
$ source env/bin/activate
$ pip install --upgrade pip
$ pip install Django
```

### Create Django Project

```bash
# $ django-admin startproject django
# This command occurs error so we use other steps below.
$ django-admin startproject djreact
$ mv djreact django
```

### Create [`requirements.txt`](https://pip.readthedocs.io/en/1.1/requirements.html) file

```bash
$ vim requirements.txt
```

```
Django==1.9.3
```

### Set Up for Git

```bash
$ git init
$ vim .gitignore
```

```
*.pyc
db.sqlite3
__pycache__
```

### Run Server

```bash
$ cd django
$ python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000)

## Step 2: Add non-reactJS views

### Add to `urls.py`

```
$ cd djreact
$ vim urls.py
```

```python
from django.views import generic

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^view2/',
      generic.TemplateView.as_view(template_name='view2.html')),
  url(r'^$',
      generic.TemplateView.as_view(template_name='view1.html')),
]
```

### Add templates

Make directory named `templates` in `djreact` folder.

```bash
$ mkdir templates
```

Add `templates` directory path to `settings.py`. Add below codes in `setting.py`.

```python
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'djreact/templates')],
        ...
    },
]
```

```bash
$ vim base.html
```
```html
<!doctype html>
<html class="no-js" lang="">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
  </head>
  <body>
    {% block main %}{% endblock %}
  </body>
</html>
```

```bash
$ vim view1.html
```
```html
{% extends "base.html" %}

{% block main %}
<div class="container">
  <h1>View 1</h1>
</div>
{% endblock %}
```

```bash
$ vim view2.html
```
```html
{% extends "base.html" %}

{% block main %}
<div class="container">
  <h1>View 2</h1>
</div>
{% endblock %}
```

### Run Server

```bash
$ python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000) and [http://localhost:8000/view2/](http://localhost:8000/view2/)

## Step 3: Add django-webpack-loader


```bash
$ pip freeze
$ pip install django-webpack-loader
$ vim requirements.txt
```

```txt
Django==1.9.3
django-webpack-loader==0.2.4
```

Add `webpack_loader` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'webpack_loader',
]
```

Add `static` folder directory in `settings.py`:

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'djreact/static'),
]
```

Create `package.json` in django

```bash
$ vim package.json
```

```json
{
  "name": "djreact",
  "version": "0.0.1",
  "devDependencies": {
    "babel": "^6.5.2",
    "babel-core": "^6.6.5",
    "babel-eslint": "^5.0.0",
    "babel-loader": "^6.2.4",
    "babel-plugin-transform-decorators-legacy": "^1.3.4",
    "babel-preset-es2015": "^6.6.0",
    "babel-preset-react": "^6.5.0",
    "babel-preset-stage-0": "^6.5.0",
    "eslint": "^2.2.0",
    "react": "^0.14.7",
    "react-hot-loader": "^1.3.0",
    "redux-devtools": "^3.1.1",
    "webpack": "^1.12.13",
    "webpack-bundle-tracker": "0.0.93",
    "webpack-dev-server": "^1.14.1"
  },
  "dependencies": {
    "es6-promise": "^3.1.2",
    "isomorphic-fetch": "^2.2.1",
    "lodash": "^4.5.1",
    "radium": "^0.16.6",
    "react-cookie": "^0.4.5",
    "react-dom": "^0.14.7",
    "react-redux": "^4.4.0",
    "redux": "^3.3.1",
    "redux-thunk": "^1.0.3"
  }
}
```

```bash
$ npm install
```

```bash
$ vim .gitignore
```

```vim
...
node_modules
...
```

```bash
$ touch webpack.base.config.js webpack.local.config.js
```

In `webpack.base.config.js`:

```javascript
var path = require("path")
var webpack = require('webpack')

module.exports = {
  context: __dirname,

  entry: {
    // Add as many entry points as you have container-react-components here
    App1: './reactjs/App1',
    vendors: ['react'],
  },

  output: {
      path: path.resolve('./djreact/static/bundles/local/'),
      filename: "[name]-[hash].js"
  },

  externals: [
  ], // add all vendor libs

  plugins: [
    new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js'),
  ], // add all common plugins here

  module: {
    loaders: [] // add all common loaders here
  },

  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  },
}
```

In `webpack.local.config.js`:

```javascript
var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var config = require('./webpack.base.config.js')

config.devtool = "#eval-source-map"

config.plugins = config.plugins.concat([
  new BundleTracker({filename: './webpack-stats-local.json'}),
])

config.module.loaders.push(
  { test: /\.jsx?$/, exclude: /node_modules/, loaders: ['react-hot', 'babel'] }
)

module.exports = config
```

```bash
$ touch .babelrc
```

```
{
  "presets": ["es2015", "react", "stage-0"],
  "plugins": [
    ["transform-decorators-legacy"],
  ]
}
```

### Write ReackJS codes

Create `reactjs` folder in `django` folder.

```
$ mkdir reactjs && cd reactjs
$ mkdir containers components
$ touch App1.jsx containers/App1Container.jsx components/Headline.jsx
```

#### `App1.jsx`

```jsx
import React from "react"
import { render } from "react-dom"

import App1Container from "./containers/App1Container"

class App1 extends React.Component {
  render() {
    return (
      <App1Container />
    )
  }
}

render(<App1/>, document.getElementById('App1'))
```

#### `containers/App1Container.jsx`

```jsx
import React from "react"

import Headline from "../components/Headline"

export default class App1Container extends React.Component {
  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <Headline>Sample App!</Headline>
          </div>
        </div>
      </div>
    )
  }
}
```

#### `components/Headline.jsx`

```jsx
import React from "react"

export default class Headline extends React.Component {
  render() {
    return (
      <h1>{ this.props.children }</h1>
    )
  }
}
```

## Step 4: Use the bundle

#### `view1.html`

```html
{% extends "base.html" %}
{% load render_bundle from webpack_loader %}

{% block main %}
<div id="App1"></div>
{% render_bundle 'vendors' %}
{% render_bundle 'App1' %}
{% endblock %}
```

#### `settings.py`

```python
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/local/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-local.json'),
    }
}
```

#### Run server

```
$ python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000)

#### Make a change

In `App1Container.jsx`, change `Sample App!` to `Something New!`.

```bash
$ node_modules/.bin/webpack --config webpack.local.config.js
$ python manage.py runserver
```
Open [http://localhost:8000](http://localhost:8000)


## Step 5: Hot Reloading

Make `server.js` file in `django` folder

```bash
$ touch server.js
```

#### `server.js`

```javascript
var webpack = require('webpack')
var WebpackDevServer = require('webpack-dev-server')
var config = require('./webpack.local.config')

new WebpackDevServer(webpack(config), {
  publicPath: config.output.publicPath,
  hot: true,
  inline: true,
  historyApiFallback: true,
}).listen(3000, config.ip, function (err, result) {
  if (err) {
    console.log(err)
  }

  console.log('Listening at ' + config.ip + ':3000')
})
```

#### `webpack.local.config.js`

```javascript
var ip = 'localhost'

config.entry = {
  App1: [
    'webpack-dev-server/client?http://' + ip + ':3000',
    'webpack/hot/only-dev-server',
    './reactjs/App1',
  ],
}

config.output.publicPath = 'http://' + ip + ':3000' + '/assets/bundles/'

config.plugins = config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NoErrorsPlugin(),
  new BundleTracker({filename: './webpack-stats-local.json'}),
])
```

```bash
# run these two commands in different terminer!
$ node server.js
$ python manage.py runserver
```

Change codes in `App1Container.jsx` and checkout the updates in [https://localhost:8000](https://localhost:8000)


## Step 6: Going to production

#### Create `webpack.stage.config.js`

```bash
$ touch webpack.stage.config.js
```

```javascript
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

var config = require('./webpack.base.config.js')

config.output.path = require('path').resolve('./djreact/static/bundles/stage/')

config.plugins = config.plugins.concat([
  new BundleTracker({filename: './webpack-stats-stage.json'}),

  // removes a lot of debugging code in React
  new webpack.DefinePlugin({
    'process.env': {
      'NODE_ENV': JSON.stringify('staging'),
      'BASE_API_URL': JSON.stringify('https://sandbox.example.com/api/v1/'),
  }}),

  // keeps hashes consistent between compilations
  new webpack.optimize.OccurenceOrderPlugin(),

  // minifies your code
  new webpack.optimize.UglifyJsPlugin({
    compressor: {
      warnings: false
    }
  })
])

// Add a loader for JSX files
config.module.loaders.push(
  { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel' }
)

module.exports = config
```

#### Create `webpack.prod.config.js`

```bash
$ touch webpack.prod.config.js
```

```javascript
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

var config = require('./webpack.base.config.js')

config.output.path = require('path').resolve('./djreact/static/bundles/prod/')

config.plugins = config.plugins.concat([
  new BundleTracker({filename: './webpack-stats-prod.json'}),

  // removes a lot of debugging code in React
  new webpack.DefinePlugin({
    'process.env': {
      'NODE_ENV': JSON.stringify('production'),
      'BASE_API_URL': JSON.stringify('https://example.com/api/v1/'),
  }}),

  // keeps hashes consistent between compilations
  new webpack.optimize.OccurenceOrderPlugin(),

  // minifies your code
  new webpack.optimize.UglifyJsPlugin({
    compressor: {
      warnings: false
    }
  })
])

// Add a loader for JSX files
config.module.loaders.push(
  { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel' }
)

module.exports = config
```

#### Update `webpack.local.config`

```javascript
config.plugins = config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NoErrorsPlugin(),
  new BundleTracker({filename: './webpack-stats-local.json'}),
  new webpack.DefinePlugin({
    'process.env': {
      'NODE_ENV': JSON.stringify('development'),
      'BASE_API_URL': JSON.stringify('https://'+ ip +':8000/api/v1/'),
  }}),
])
```

#### Install Fabric

```bash
$ pip install Fabric
```

#### Modify `requirements.txt`

```txt
Django==1.9.3
Fabric==1.10.2
django-webpack-loader==0.2.4
```


#### Create `fabfile.py`

```python
from fabric.api import local

def webpack():
    local('rm -rf djreact/static/bundles/stage/*')
    local('rm -rf djreact/static/bundles/prod/*')
    local('webpack --config webpack.stage.config.js --progress --colors')
    local('webpack --config webpack.prod.config.js --progress --colors')
```

Your workflow will now look like this:

1. Start `./manage.py runserver`
2. Start `node server.js`
3. Edit your ReactJS app
4. When done, commit your changes
5. Run `fab webpack` and commit your new bundles
6. Run a deployment

On your servers, you will need a `local_settings.py` where you override the `WEBPACK_LOADER` setting like this:

```javascript
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/stage/',  # end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-stage.json'),
    }
}
```

And similar for prod, of course, just replace `stage` with `prod`.


## Step 7: Add [Redux](http://redux.js.org)

#### Create Action Creators in `reactjs/actions/counterActions.js`:

```javascript
export const INCREASE = "INCREASE"
export function increaseCounter() {
    return {type: INCREASE}
}
```

#### Create `reactjs/reducers/counters.js`

```javascript
import * as sampleActions from "../actions/counterActions"

const initialState = {
  clicks: 0,
}

export default function counters(state=initialState, action={}) {
  switch (action.type) {
  case sampleActions.INCREASE:
    return {...state, clicks: state.clicks + 1}
  default:
    return state
  }
}
```

#### Create `reactjs/reducers/index.js`

```javascript
export { default as counters } from './counters'
```

#### Update App1.jsx

```jsx
import React from "react"
import { render } from "react-dom"
import {
  createStore,
  compose,
  applyMiddleware,
  combineReducers,
} from "redux"
import { Provider } from "react-redux"
import thunk from "redux-thunk"

import * as reducers from "./reducers"
import App1Container from "./containers/App1Container"

let finalCreateStore = compose(
  applyMiddleware(thunk),
  window.devToolsExtension ? window.devToolsExtension() : f => f
)(createStore)
let reducer = combineReducers(reducers)
let store = finalCreateStore(reducer)

class App1 extends React.Component {
  render() {
    return (
      <Provider store={store}>
        <App1Container />
      </Provider>
    )
  }
}

render(<App1/>, document.getElementById('App1'))
```

#### Update `App1Container.jsx`

```jsx
import React from "react"

import { connect } from "react-redux"

import * as counterActions from "../actions/counterActions"
import Headline from "../components/Headline"

@connect(state => ({
  counters: state.counters,
}))
export default class SampleAppContainer extends React.Component {
  handleClick() {
    let {dispatch} = this.props;
    dispatch(counterActions.increaseCounter())
  }

  render() {
    let {counters} = this.props
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <Headline>Sample App!</Headline>
            <div onClick={() => this.handleClick()}>INCREASE</div>
            <p>{counters.clicks}</p>
            <p>{process.env.BASE_API_URL}</p>
          </div>
        </div>
      </div>
    )
  }
}
```






---

## Refer to

[Django React Boilerplate](https://github.com/mbrochh/django-reactjs-boilerplate)
