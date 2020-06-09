<template>
  <v-app>
    <Navbar />
  <ListView />
   <Fetcher />
  </v-app>
</template>

<script>
import Fetcher from "./components/Fetcher.vue";
import ListView from "./components/ListView.vue";
import Navbar from "./components/Navbar.vue"

export default {
  name: 'App',

  components: {
    Fetcher,
    ListView,
    Navbar
  },

  data: () => ({
    //
  }),
};
</script>

<style>
  v-app{
    background: #fafafa;
  }
</style>