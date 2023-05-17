<template>
  <button @click="this.component = 'Simple'">Simple Calculator</button>
  <button @click="this.component = 'Advanced'">Amazing imba calculator</button>
  <keep-alive>
    <component
      :is="this.component"
    >
    </component>
  </keep-alive>
</template>

<script>
import Simple from './tabs/Simple.vue'
import Advanced from './tabs/Advanced.vue'

export default {
  name: 'HelloWorld',
  components: {
    Simple,
    Advanced
  },
  data() {
    return {
      component: 'Simple'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
