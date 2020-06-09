<template>
  <header>
    <v-toolbar dense dark color="primary">
    <img src="../assets/favicon.svg" width="40">

      <v-toolbar-title class="title">Todo List</v-toolbar-title>

      <v-spacer></v-spacer>

    </v-toolbar>
  </header>
</template>

<script>

export default {
  name: "Navbar",

}

</script>

<style scoped>

.navbar{
  padding-left: 10em;
  background-color: #4E77E0;
  color: white;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  height: 10vh;
}

.title{
  margin-left: 2em;
}

.nav-links{
  display: flex;
  justify-content: space-around;
  flex-direction: row;
  list-style: none;
  width: 20%;
}

</style>