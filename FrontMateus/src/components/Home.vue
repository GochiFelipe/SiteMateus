<template>
  <div>
    <headerfull/>
    <b-container>
      <h1>CORPO</h1>
    </b-container>
  </div>
</template>

<script>

  import HeaderFull from './shared/header/HeaderFull.vue';
  import HeaderMobile from './shared/header/HeaderFull.vue';

  export default {
    name: 'Home',

    data:{
    },

    components:{
      'headerfull': HeaderFull
    },

    computed:{
    },

    methods:{
    }
  }
</script>
<style scoped>
</style>
