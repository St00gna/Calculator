<template>
    <div class="wrapper" style="display: grid; grid-template-columns: 10% 80% 10%; grid-template-rows: 25% 75%; height: 100vh; width: 100%;">
        <div><p></p></div>  <!-- пустая строка -->
        <div >
            <div>
                <label for="file-upload" class="custom-file-upload" style="margin-bottom: 10px; margin:0% 25%">Send your file in PDf, DOCX, TXT=)</label>
                <div><p></p></div>
                <input type="file" name="file-upload" style="margin:0% 25%">
                <div><p></p></div>
                <button type="button" @click="this.sendData()" style="margin:0% 25%" class="btn btn-info">Send</button>
            </div>
            <div class="result">
                <h1 style="font-family: 'Courier New', Courier, monospace;">Result:</h1>
                <div style="padding: 20px;">
                    <p v-for="item in resultExpression">{{item[0]}} -> {{item[1]}}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return{
            resultExpression: '',
        }
    },
    methods: {
        async sendData() {
            const file = document.querySelector('input').files[0];
            const formData = new FormData();
            formData.append('file', file);

            try {
                const response = await axios.post('http://127.0.0.1:5000/api/process_file', formData);
                console.log('Успішно:', response.data);
                this.resultExpression = Object.keys(response.data).map((key) => [key, response.data[key]]);
                console.log(this.resultExpression)
            } catch (error) {
                console.error('Помилка:', error);
            }
        }
    },
    computed: {
        
    },
    mounted(){

    }
}
</script>

<style scoped>
input[type=file]::file-selector-button {
  margin-right: 20px;
  border: none;
  background: #084cdf;
  padding: 10px 20px;
  border-radius: 10px;
  color: #fff;
  cursor: pointer;
  transition: background .2s ease-in-out;
}

input[type=file]::file-selector-button:hover {
  background: #0d45a5;
}
</style>