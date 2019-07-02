<template>
<div @click="remove()" class="flex items-center absolute pin-t pin-r m-4 py-4 px-2 hover:text-grey-darker bg-white border-green-light border-4 rounded shadow-md hover:shadow-lg cursor-pointer max-w-xs">
    <div class=" bg-green rounded-full text-white px-3 m-1">
        <h2>!</h2>
    </div>
    <div class="p-2 overflow-auto">
        <p>{{ messageText }}</p>
    </div>
</div>
</template>

<script>
export default {
    name: 'message',
    props: ['messageText', 'index'],
    methods: {
        remove () {
            console.log('remove');
            this.$store.dispatch('actionRemoveMessage', this.index)
        }
    },
    mounted() {
        setTimeout(() => this.remove(), 5000);
    },
  }
</script>

<style scoped>  /* "scoped" attribute limit the CSS to this component only */

</style>