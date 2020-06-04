<template>
  <v-app>
  <ListView />
   <Fetcher />
  </v-app>
</template>

<script>
import Fetcher from "./components/Fetcher.vue";
import ListView from "./components/ListView.vue";

export default {
  name: 'App',

  components: {
    Fetcher,
    ListView
  },

  data: () => ({
    //
  }),
};
</script>
