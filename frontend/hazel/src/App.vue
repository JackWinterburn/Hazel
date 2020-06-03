<template>
  <v-app>
   <Fetcher />
  </v-app>
</template>

<script>
import Fetcher from "./components/Fetcher.vue"

export default {
  name: 'App',

  components: {
    Fetcher
  },

  data: () => ({
    //
  }),
};
</script>
