<template>
<div>
    <button class="snaps">
        <b-img rounded="circle" blank class="imagem-snap"/>
    </button>
</div>
</template>
<script>
    export default{       
        props:{
        },
        methods:{
        },
        computed:{
        }
    }
</script>
<style scoped>
    div{
        border:none;
        padding:0px;
    }
    .snaps{
        border-radius:50%;
        width:60px;
        height:60px;
        color: black;
        padding: 0px;
        border-color: green;
        background: none;
    }
    .imagem-snap{
        background-color: black;
        width:50px;
        height:50px;
    }
</style>