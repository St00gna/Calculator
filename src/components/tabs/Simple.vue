<template>
    <div class="wrapper">
        <h1>Write expression</h1>
        <input type="text" placeholder="Write" v-model="this.expression"/>
        <button @click="this.getResult">Submit</button>
        <input v-model="this.result"/>
    </div>
</template>

<script>
export default {
    data(){
        return{
            expression: "",
            result: '',
            count: 0,
            i: 0,
            multiplyAndDivide: 0,
        }
    },
    methods: {
        getResult() {
            // this.result = eval(this.expression)
            if(/[a-zа-яё]/i.test(this.expression) == true) {
                alert("Error")
                return
            }
            if(this.expression.includes('(') == true && this.expression.includes(')') == true) {
                this.result = this.expression.replaceAll(' ', '').replaceAll("+", " + ").replaceAll("/", ' / ').replaceAll('*', ' * ').replaceAll('-', ' - ').replaceAll('(', ' ( ').replaceAll(')', ' ) ').split(' ')
                console.log(this.result)
                
            } else {
                this.result = this.expression.replaceAll(' ', '').replaceAll("+", " + ").replaceAll("/", ' / ').replaceAll('*', ' * ').replaceAll('-', ' - ')
                console.log(this.result)
                this.result = this.result.split(' ')
                console.log(this.result)
                for(let i=0; i<this.result.length; i++) {
                    console.log(i)
                    if(this.result[i] == '*' || this.result[i] == '/') {
                        let firstNumber = Number(this.result[this.result.indexOf(this.result[i-1])])
                        let secondNumber = Number(this.result[this.result.indexOf(this.result[i+1])])
                        if(this.result[i] == '*') {
                            console.log(this.result)
                            this.result.splice(this.result.indexOf(this.result[i-1]), 3, firstNumber * secondNumber)
                            i=0
                            console.log('after', this.result)
                        } else {
                            this.result.splice(this.result.indexOf(this.result[i-1]), 3, firstNumber / secondNumber)
                            i=0
                            console.log('after', this.result)
                        }
                    } 
                };
                for(let i=0; i<this.result.length; i++) {
                    console.log(i)
                    if(this.result[i] == '+' || this.result[i] == '-') {
                        let firstNumber = Number(this.result[this.result.indexOf(this.result[i-1])])
                        let secondNumber = Number(this.result[this.result.indexOf(this.result[i+1])])
                        if(this.result[i] == '+') {
                            console.log(this.result)
                            this.result.splice(this.result.indexOf(this.result[i-1]), 3, firstNumber + secondNumber)
                            i=0
                            console.log('after', this.result)
                        } else {
                            this.result.splice(this.result.indexOf(this.result[i-1]), 3, firstNumber - secondNumber)
                            i=0
                            console.log('after', this.result)
                        }
                    } 
                };
            }
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