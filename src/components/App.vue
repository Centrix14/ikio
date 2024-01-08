<template>
  <Authorization 
    v-if="authoriz_data.authoriz_status == false"
    v-bind:authorization_status="authoriz_data.authoriz_status"
    @authoriz_success="authoriz_success"
  />
  <Main 
    v-if="authoriz_data.authoriz_status == true"
  />
</template>
  
<script>
import Authorization from "@/components/Authorization.vue";
import Main from "@/components/Main.vue";
export default {
  name: "App",
  components: {
    Authorization, Main
  },
  data: () => {
    return {
      authoriz_data: {
        authoriz_status: false
      }
    }
  },
  methods: {
    authoriz_success() {
      this.authoriz_data.authoriz_status = true;
    }
  }
}
</script>

<style>
  
</style>