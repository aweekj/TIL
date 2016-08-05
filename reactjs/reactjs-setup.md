# React.js
## 1. Install global package

```bash
npm install -g babel webpack webpack-dev-server
```

## 2. Create project folder

```bash
mkdir react-tutorial && cd react-tutorial
npm init
```

## 3. Install plugin

```bash
npm install --save react react-dom
npm install --save-dev babel-core babel-loader babel-preset-es2015 babel-preset-react webpack webpack-dev-server
```

## 4. Create files

```bash
mkdir src src/components public
touch public/index.html src/components/App.js src/index.js webpack.config.js
```

## 5. Configure compiler, server, loader
in **webpack.config.js**

```js
module.exports = {
  entry: './src/index.js',
  output: {
    path: __dirname + '/public/',
    filename: 'bundle.js'
  },
  devServer: {
    inline: true,
    port: 7777,
    contentBase: __dirname + '/public/'
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel',
        exclude: /node_modules/,
        query: {
          cacheDirectory: true,
          presets: ['es2015', 'react']
        }
      }
    ]
  }
};
```

in **package.json**

```json
"scripts": {
  "start": "webpack-dev-server --hot --host 0.0.0.0"
}
```

## 6. Components
in **public/index.html**

```html
<!DOCTYPE html>
<html>
   <head>
      <meta charset="UTF-8">
      <title>React App</title>
   </head>
   <body>
      <div id="root"></div>
      <script src="bundle.js"></script>
   </body>
</html>
```


in **src/components/App.js**

> It's **React's Naming Convention** to set component's and file's **first letter to Capital letter**.

```js
import React from 'react';

class App extends React.Component {
  render(){
    return(
      <h1>Hello, React!</h1>
    );
  }
}

export default App;
```

in **src/index.js**

```js
import React from 'react';
import ReactDom from 'react-dom';
import App from './components/App';

const rootElement = document.getElementById('root');
ReactDOM.render(<App />, rootElement);
```

## 7. Run server

```bash
npm start
```

Open browser, go to [localhost:7777](https://localhost:7777).
