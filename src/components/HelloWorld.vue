<template>
  <div class="nav" style="display: grid; grid-template-columns: repeat(5, 1fr);">
    <button class="first" style="grid-column-start: 2; grid-column-end: 3; border-radius: 20px; color: violet; border: 3px solid violet; background-color: white;" @click="this.component = 'Simple'">Simple Calculator</button>
    <button class="second" style="grid-column-start: 4; grid-column-end: 5; border-radius: 20px; color: violet; border: 3px solid violet; background-color: white" @click="this.component = 'Advanced'">Amazing imba calculator</button>
  </div>
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
<style>

</style>
