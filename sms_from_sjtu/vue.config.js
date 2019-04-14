module.exports = {
  css: { loaderOptions: { less: { javascriptEnabled: true } } },
  lintOnSave: false,
  pluginOptions: {
    electronBuilder: {
      builderOptions: {
        win: {
          target: 'portable'
        }
      }
    }
  }
}
