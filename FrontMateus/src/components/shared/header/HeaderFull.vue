<template>
    <div>
        <div class="full">
            <div class="grid-header">
                <h1>Jovem Black Mirror</h1>
                <ul class="direcao-snaps" id="paginas">
                    <li class="grid-snap" v-for="pagina in paginas">
                        <snap/>
                        <label>{{ pagina }}</label>
                    </li>
                </ul>
                <img src="../../../../static/eu1.jpeg" class="imagem-capa">
            </div>
        </div>
        <div class="mobile">
            <b-navbar class="nav-bar">
                <b-navbar-toggle style="color:{white;}" target="nav_collapse"></b-navbar-toggle>
                <b-navbar-brand class="nav-color" href="#">Jovem Black Mirror</b-navbar-brand>
                <b-collapse is-nav id="nav_collapse">
                    <b-navbar-nav class="flex-position">
                        <b-nav-item class="direcao-snap nav-color" v-for="pagina in paginas">
                            <snap class="posicao-snap"/>
                            <label class="posicao-label nav-color">{{ pagina }}</label>
                        </b-nav-item>
                    </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </div>
    </div>
</template>
<script>
    import Snaps from '../snaps/Snap.vue';

    export default {
        components:{
            'snap': Snaps
        },

        props: {
        },

        data () {
            return {
                paginas: ['Eventos','Arte','Diagrama','Conceitual','A&D', 'Youtube','Blog']
            }
        },

        methods:{
        }
    }
</script>
<style scoped>
    @media (max-width:1024px) and (min-width:769px) {
        
        label, h1{
            color:white;
        }

        .full{
            display: block;
        }
        .mobile{
            display: none;
        }

        h1{
            justify-content: center;
            justify-self:center;
            align-self:center;
            font-size: 60px;
        }

        .direcao-snaps{
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            justify-content: center;
            grid-row-start:2;
            grid-row-end:3;
            justify-self:left;
            align-self:end;

        }

        .grid-snap{
            display:grid;
            grid-column-gap: 50px;
            margin:0px 5px;
            justify-items:center;
        }

        .imagem-capa{
            grid-column-start:1;
            grid-column-end:2;
            grid-row-start:1;
            grid-row-end:3;
            justify-self:stretch;
            align-self:stretch;
        }

        .grid-header{
            display:grid;
            grid-template-columns:40% 60%;
            grid-template-rows:175px 75px;
            background:linear-gradient(to left,#282725ff)
        }
    }

    @media (min-width:1025px){
        label, h1{
            color:white;
        }

        .full{
            display: block;
        }

        .mobile{
            display: none;
        }

        h1{
            justify-content: center;
            justify-self:center;
            align-self:center;
            font-size: 60px;
        }

        .direcao-snaps{
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            justify-content: center;
            grid-row-start:2;
            grid-row-end:3;
            justify-self:left;
            align-self:end;

        }

        .grid-snap{
            display:grid;
            grid-column-gap: 50px;
            margin:0px 15px;
            justify-items:center;
        }

        .imagem-capa{
            grid-column-start:1;
            grid-column-end:2;
            grid-row-start:1;
            grid-row-end:3;
            justify-self:stretch;
            align-self:stretch;
        }

        .grid-header{
            display:grid;
            grid-template-columns:40% 60%;
            grid-template-rows:200px 100px;
            background:linear-gradient(to left,#282725ff)
        }
    }

    @media (max-width:769px) {
        .full{
            display:none;
        }
        .mobile{
            display: block;
        }

        .flex-position{
            display: flex;
            flex-flow: column wrap;
        }
        
        .posicao-snap{
            position: relative;
            height: 25px;
        }

        .posicao-label{
            position: relative;
            left: 70px;
            bottom: 10px;
        }

        .nav-bar{
            background-color: #282725ff;
        }

        .nav-color{
            color:white;
        }
        
    }
</style>