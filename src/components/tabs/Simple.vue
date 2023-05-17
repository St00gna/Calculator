<template>
        <h1>Write expression</h1>
        <input type="text" placeholder="Write" v-model="this.expression"/>
        <button @click="this.getResult">Submit</button>
        <input v-model="this.result"/>
</template>

<script>
export default {
    data(){
        return{
            expression: "",
            result: ''
        }
    },
    methods: {
        getResult(){
            
        }
    },
    computed: {

    },
    mounted(){

    }
}
</script>

<style scoped>

</style>