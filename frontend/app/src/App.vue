<template>
  <div id="app" class="h-full  bg-grey-lightest font-sans leading-tight text-black focus:outline-none">
    <div  v-for="(message, index) in messages" :key="index">
      <Message :message-text="message" :index="index" />
    </div>
    <router-view/>
  </div>
</template>

<script>
import Message from './components/message/Message.vue'
export default {
  name: "app",
      components: {
        Message
  },
  computed: {
    messages () {
      return this.$store.state.messages
    }
  },
  created: function () {
    // wake up the server
    this.$store.dispatch('actionPingServer')
  },

};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#editor :focus {
  outline: none;
}
.ProseMirror {
  height: 100%;
  word-wrap: break;
  word-break: break-all;
}
</style>
