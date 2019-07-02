<template>
    <section id="notes" class="flex flex-col border-r border-grey-light h-64 md:h-screen w-full md:min-w-320px ">
        <div class="px-6 pb-2 border-b bg-white sticky pin-t border-grey-light">
            <div class="flex items-center justify-between pt-6 pb-12 ">
                <div class="text-xl font-medium text-left"> 
                    All Notes
                </div>
                <div @click="hideNotes()" class=" mr-1 cursor-pointer hover:text-grey md:block hidden">
                    <font-awesome-icon icon="angle-left" size="lg"/> 
                </div>
            </div>
            <div class="flex justify-between">
                <div class="text-sm text-grey-dark">
                    {{ notes.length }} notes
                </div>
                <div>
                <svg class="fill-current inline-block h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                    <path d="M542.22 32.05c-54.8 3.11-163.72 14.43-230.96 55.59-4.64 2.84-7.27 7.89-7.27 13.17v363.87c0 11.55 12.63 18.85 23.28 13.49 69.18-34.82 169.23-44.32 218.7-46.92 16.89-.89 30.02-14.43 30.02-30.66V62.75c.01-17.71-15.35-31.74-33.77-30.7zM264.73 87.64C197.5 46.48 88.58 35.17 33.78 32.05 15.36 31.01 0 45.04 0 62.75V400.6c0 16.24 13.13 29.78 30.02 30.66 49.49 2.6 149.59 12.11 218.77 46.95 10.62 5.35 23.21-1.94 23.21-13.46V100.63c0-5.29-2.62-10.14-7.27-12.99z"></path>
                </svg>
                </div>
            </div>
        </div>
        <div class="flex flex-wrap overflow-auto ">
            <div @click="setActive(note.id)" :class="{ 'bg-grey-lighter': ActiveID == note.id }" class="cursor-pointer hover:bg-grey-lighter w-full text-left border-b border-grey-light px-6"  v-for="note in notes" :key="note.id">
            <div class="pt-4 pb-1 text-ms font-semibold break-words"> 
                {{note.title}}
            </div>
            <div class="text-sm h-16 overflow-hidden md:block hidden">
                {{note.content}}
            </div>
            <div class="text-xs text-grey-dark py-2">
                {{note.updated}}
            </div>
            </div>
        </div>
    </section>
</template>

<script>
// I THINK I CAN USE FLEX-GROW TO FIX THE SCROLLING SEE SIDE BAR
export default {
    name: "Notes",
    computed: {
        notes () {
            return this.$store.getters.orderedNotes
        },
        note () {
            return this.$store.state.note
        },
        ActiveID () {
            if (this.note) {
                return this.note.id
            } else {
                return null
            }
        }
    },
    methods: {
        setActive (note_id) {
            this.$store.dispatch('actionSetActiveNote', note_id)
        },
        hideNotes () {
            this.$store.dispatch('actionSetNotesHidden', true)
        }
    },
    mounted () {

    }

};
</script>
