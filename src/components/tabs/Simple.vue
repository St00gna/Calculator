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
        getResult() {  
            if (this.expression !== '') {
                this.result = this.expression.replace(/%(\d+(?:\.\d+)?)/g, "*($1/100)");        
                this.result = eval( this.result );
            } 
        }

        // getResult(){
        //     this.result = eval(this.expression) //виконання коду, котрий записанний рядком. Небезпечний варіант але дуже простий (можна вставити безкінечну кількість фільтрів, щоб якось код зробити безпесним для коритувачів та серверу)
        // }
    },
    computed: {

    },
    mounted(){

    }
}
</script>

<style scoped>

</style>