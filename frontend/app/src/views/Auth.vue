<template>
  <div class="h-screen flex flex-col">
    <div class="flex justify-center my-8">
      <img src="@/assets/logo.png" class="h-48">
    </div>
    <div class="flex justify-center">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Auth'
}
</script>

<style scoped>
 .auth {
   margin-top: 40px;
 }
</style>
