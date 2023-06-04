const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    port: 5000,
    proxy: 'http://45.146.164.34:8080/'
  }

})
