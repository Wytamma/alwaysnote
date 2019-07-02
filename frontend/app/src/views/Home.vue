<template>
    <div class="min-h-screen max-h-screen md:min-w-1024px w-full">
      <div class="md:flex">
        <!-- Sidebar --> 
        <div  class="md:block hidden"> <!-- IDK feels like i should use v-if --> 
          <SideBar />
        </div>
        <div class="md:hidden block w-full bg-grey-darker">
          <SearchBar />
        </div>
        <!-- Notes --> 
        <div class="md:flex md:flex-grow ">
          <Notes v-if="!notesHidden" class="md:w-64 w-full" />
          <Note />
        </div>
      </div> 
    </div>
</template>

<script>
import SideBar from "@/components/SideBar.vue";
import Notes from "@/components/Notes.vue";
import Note from "@/components/Note.vue";
import SearchBar from "@/components/SearchBar.vue";

export default {
  name: "Home",
  components: {
    SideBar,
    Notes,
    Note,
    SearchBar
  },
  created: function () {
    this.$store.dispatch('actionGetNotes')
    
  },
  computed: {
    notesHidden() {
        return this.$store.state.notesHidden
    }
  },
};
</script>
