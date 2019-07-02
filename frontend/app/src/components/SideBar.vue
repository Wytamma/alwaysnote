<template>
    <div class="h-screen min-w-64 w-64 pt-4 bg-black text-grey-light flex flex-col">
        <div class="flex items-center pl-4 pb-6 ">
        <div class="flex items-center mr-2">
            <img alt="Vue logo" src="../assets/logo.svg" class="w-8">
        </div>
        <div class="mr-2 text-sm">
            <div class="cursor-pointer hover:text-grey-lightest font-medium overflow-hidden">
                {{ email }}
            </div>
        </div>
        </div>
        <div class="px-2 pb-6">
            <SearchBar/>
        </div>
        <div @click="newNote" class="group cursor-pointer flex items-center pl-4 pb-6 ">
        <div class="mr-2">
            <div class="rounded-full h-8 w-8 flex items-center justify-center group-hover:bg-green bg-green-dark">
                <span class="text-white group-hover:text-grey-light text-3xl font-medium ">
                + 
                </span>
            </div>
        </div>
        <div class="mr-2 text-sm">
            <div class="font-semibold text-grey-lightest">
                New Note
            </div>
        </div>
        </div>
        <div class="text-sm font-semibold text-grey-light">
            <div @click="showNotes()" class="flex items-center hover:bg-grey-darker cursor-pointer pl-4 py-2">
                <div class='flex items-center mr-3'>
                    <svg class="fill-current inline-block h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                    <path d="M542.22 32.05c-54.8 3.11-163.72 14.43-230.96 55.59-4.64 2.84-7.27 7.89-7.27 13.17v363.87c0 11.55 12.63 18.85 23.28 13.49 69.18-34.82 169.23-44.32 218.7-46.92 16.89-.89 30.02-14.43 30.02-30.66V62.75c.01-17.71-15.35-31.74-33.77-30.7zM264.73 87.64C197.5 46.48 88.58 35.17 33.78 32.05 15.36 31.01 0 45.04 0 62.75V400.6c0 16.24 13.13 29.78 30.02 30.66 49.49 2.6 149.59 12.11 218.77 46.95 10.62 5.35 23.21-1.94 23.21-13.46V100.63c0-5.29-2.62-10.14-7.27-12.99z"></path>
                    </svg>
                </div>
                <div class="flex flex-grow items-center justify-between">
                    <div>
                        All Notes
                    </div> 
                    <div v-if="notesHidden" class=" mr-4 cursor-pointer">
                        <font-awesome-icon icon="angle-right" size="md"/> 
                    </div>
                </div>
            </div>
        </div>
        <div class="mt-4 flex flex-grow items-end justify-center">
                <button @click="signOut" class="bg-red-light hover:bg-red text-white text-sm font-bold py-1 px-2 mb-4 rounded focus:outline-none focus:shadow-outline" type="button">
                    Sign Out
                </button>
        </div>
    </div>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";

export default {
  name: "SideBar",
  components: {
      SearchBar
  },
  methods: {
    signOut () {
        this.$store.dispatch('actionLogOut')
    },
    newNote () {
        this.$store.dispatch('actionCreateNewNote')
    },
    showNotes () {
        this.$store.dispatch('actionSetNotesHidden', false)
    }
  },
  computed: {
    email () {
        return this.$store.state.email
    },
    notesHidden () {
        return this.$store.state.notesHidden
    },
  }
};
</script>
