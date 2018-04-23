<template>
  <div id="app">
    <menuHeader/>
    <router-view/>
  </div>
</template>

<script>

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Header from '@/components/shared/Header.vue';

export default {
  name: 'App',
  components:{
    'menuHeader': Header,
  },
}
</script>

<style>
</style>
