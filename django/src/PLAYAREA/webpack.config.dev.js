// const VueLoaderPlugin = require('vue-loader/lib/plugin');
const { VueLoaderPlugin } = require('vue-loader');
const VuetifyLoaderPlugin = require('vuetify-loader/lib/plugin');

const path = require('path');

const entries = require('./entries.js');

module.exports = {
  mode: 'development',
  devtool: 'eval-cheap-source-map',
  entry: entries,
  context: path.resolve(__dirname, '.'),
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js',
  },
  devServer: {
    open: true,
    host: 'localhost',
  },
  plugins: [
    new VueLoaderPlugin(), // disable prettier
    new VuetifyLoaderPlugin(),
  ],
  module: {
    rules: [
      {
        test: /\\.(js|jsx)$/,
        loader: 'babel-loader',
      },
      {
        test: /\.s[ac]ss$/i,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
      {
        test: /\.css$/i,
        use: [
          'style-loader',
          'vue-style-loader',
          'css-loader',
          'postcss-loader',
        ],
      },
      {
        test: /\.(eot|svg|ttf|woff|woff2|png|jpg|gif)$/,
        type: 'asset',
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader',
      },

      // Add your rules for custom modules here
      // Learn more about loaders from https://webpack.js.org/loaders/
    ],
  },
  resolve: {
    extensions: ['*', '.js', '.vue', '.json'],
    alias: {
      // vue: 'vue/dist/vue.js',
      // vue: 'vue/dist/vue.runtime.js',
      // vue: 'vue/dist/vue.runtime.esm.js',
      // vue: 'vue/dist/vue.esm.js',
    },
  },
};
