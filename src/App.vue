<template>
  <nav class="navbar bg-body-tertiary">
    <form>
      <button class="btn btn-outline-success me-2" type="button"><router-link to="/" class="link">Home</router-link></button>
      <button class="btn btn-sm btn-outline-secondary" type="button"><router-link to="/thanks" class="link">Thanks</router-link></button>
    </form>
  </nav>
<router-view/>
</template>

<style lang="scss" scoped>
  nav{
      text-decoration: none;
      font-size: 20px;
      form {
        width: 100%;
        display: grid;
        grid-template-columns: 40% 10% 10% 40%;
      }
      .btn.btn-outline-success.me-2{
        grid-column-start: 2;
        grid-column-end: 3;
        .link{
          font-size: 24px;
          color: green;
          text-decoration: none;
        }
      }
      .btn.btn-sm.btn-outline-secondary{
        grid-column-start: 3;
        grid-column-end: 4;
        .link{
          font-size: 24px;
          color: gray;
          text-decoration: none;
        }
      }
    }
</style>