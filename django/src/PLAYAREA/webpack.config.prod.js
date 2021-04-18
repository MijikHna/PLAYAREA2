// import { VueLoaderPlugin } from 'vue-loader/lib/plugin';
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const path = require('path');

const entries = require('./entries.js');

module.exports = {
  mode: 'production',
  entry: entries,
  context: path.resolve(__dirname, '.'),
  // output: {
  //   path: path.resolve(__dirname, '/dist/'),
  //   filename: '[name].bundle.js',
  // },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: { loader: 'babel-loader' },
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader',
      },
    ],
  },
  plugins: [new VueLoaderPlugin()],
  resolve: {
    extensions: ['*', '.js', '.vue', '.json'],
  },
};
