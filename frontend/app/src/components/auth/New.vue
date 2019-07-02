<template>
<div class="w-full max-w-xs">
    <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" :model="createAccount" ref="createAccount">
        <div class="mb-4">
          <label class="block text-grey-darker text-sm font-bold mb-2" for="email">
            Email
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker leading-tight focus:outline-none focus:shadow-outline" id="email" type="email" placeholder="Email" v-model="createAccount.email">
        </div>
        <div class="mb-4">
          <label class="block text-grey-darker text-sm font-bold mb-2" for="email">
            Confirm
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker leading-tight focus:outline-none focus:shadow-outline" id="email" type="email" placeholder="Email" v-model="createAccount.confirm">
        </div>
        <div class="mb-6">
        <label class="block text-grey-darker text-sm font-bold mb-2" for="password">
            Password
        </label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************" v-model="createAccount.password">
        </div>
        <div class="flex justify-center">
          <button @click="submitForm('createAccount')" class="w-48 bg-green hover:bg-green-dark text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
            <font-awesome-icon v-if="createAccount.disabled" icon="spinner" pulse />
            <span v-else>Create Account</span>
          </button>
        </div>
    </form>
    <div class="text-center text-grey text-xs">
        <p>Already have an account ? Return to <router-link :to="{name: 'Login'}">login</router-link></p>
    </div>
</div>
</template>

<script>
import { log } from 'util';
  export default {
    name: 'new',
    data: function () {
      return {
        createAccount: {
          email: '',
          confirm: '',
          password: '',
          disabled: false
        }
      }
    },
    methods: {
      submitForm (formName) {
        console.log('submit')
        if (this.createAccount.email != this.createAccount.confirm) {
          return this.$store.dispatch('actionAddMessage', "Email does not match.")
        } 
        this.createAccount.disabled = true
        this.$store.dispatch('actionCreateAccount', {email: this.createAccount.email, password: this.createAccount.password})
        .then(() => this.createAccount.disabled = false)
      }
    }
  }
</script>

<style scoped>  /* "scoped" attribute limit the CSS to this component only */

</style>