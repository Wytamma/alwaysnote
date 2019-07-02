<template>
<div class="w-full max-w-xs">
    <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" :model="signIn" ref="signIn">
        <div class="mb-4">
        <label class="block text-grey-darker text-sm font-bold mb-2" for="username">
            Email
        </label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker leading-tight focus:outline-none focus:shadow-outline" id="username" type="email" placeholder="Email" v-model="signIn.email">
        </div>
        <div class="mb-6">
        <label class="block text-grey-darker text-sm font-bold mb-2" for="password">
            Password
        </label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************" v-model="signIn.password">
        </div>
        <div class="flex items-center justify-between">
        <button @click="submitForm('signIn')" class="w-24 bg-green hover:bg-green-dark text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
            <font-awesome-icon v-if="signIn.disabled" icon="spinner" pulse />
            <span v-else>Sign In</span>
        </button>
        <router-link :to="{name: 'Forgot'}" class="inline-block align-baseline font-bold text-sm text-blue hover:text-blue-darker" href="#">
            Forgot Password?
        </router-link>
        </div>
    </form>
    <div class="text-center text-grey text-xs pb-10">
        <p>You don't have an account ? You can <router-link :to="{name: 'New'}">create one</router-link></p>
    </div>
</div>
</template>

<script>
import { log } from 'util';
  export default {
    name: 'login',
    data: function () {
      return {
        signIn: {
          email: '',
          password: '',
          disabled: false
        }
      }
    },
    methods: {
      submitForm (formName) {
        console.log('submit')
        this.signIn.disabled = true
        this.$store.dispatch('actionLogIn', {email: this.signIn.email, password: this.signIn.password})
        .then(() => this.signIn.disabled = false)
      }
    }
  }
</script>

<style scoped>  /* "scoped" attribute limit the CSS to this component only */

</style>