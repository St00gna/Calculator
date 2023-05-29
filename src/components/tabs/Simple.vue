<template>
    <div class="wrapper">
        <h1>Write expression</h1>
        <input type="text" placeholder="Write" v-model="this.expression"/>
        <button @click="this.getResult">Submit</button>
        <input v-modbrackets[items]="this.result"/>
    </div>
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
            this.result = eval(this.expression)
            // if(/[a-zа-яё]/i.test(this.expression) == true) {
            //     alert("Error")
            //     return
            // }
            // if(this.expression.includes('(') == true && his.expression.includes(')') == true) {
            //     console.log(true)
            // } else {
            //     this.expression = this.expression.replaceAll(/\d{1,}.\d{1,}/, /\d{1,} . \d{1,}/)
            //     console.log(this.expression)
            // }
        } 
    },
    computed: {

    },
    mounted(){

    }
}
</script>

<style lang='scss' scoped>
    .wrapper{
        display: grid;
        text-align: center;
        input{
            margin: 10px 25%;
            border-radius: 5px;
            border: 2px solid black;
            padding: 10px; 
            font-family: 'Courier New', Courier, monospace;
        }
        button{
            margin: 10px 25%;
            border: 2px solid blue;
            border-radius: 20px;
            background-color: rgb(249, 249, 249);
            box-shadow: 2px 5px 5px 1px rgba(0, 0, 0, .1);
            color: rgb(31, 30, 30);
        }
    }
</style>