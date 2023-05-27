<template>
    <!-- <form method="POST" action="/"> -->
        <input type="file">
        <button type="submit" @click="sendData()"> Submit </button>
    <!-- </form> -->
</template>

<script>
export default {
    data(){
        return{

        }
    },
    methods: {
        async sendData() {
            const formData = new FormData();
            const fileField = document.querySelector('input[type="file"]');

            formData.append('example', fileField.files[0]);

            try {
            const response = await fetch('https://localhost:8080/', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            console.log('Успех:', JSON.stringify(result));
            } catch (error) {
            console.error('Ошибка:', error);
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

</style>