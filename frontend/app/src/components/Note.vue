<template>
<div class="flex flex-col flex-grow bg-white h-screen" >
    <div v-show="note" id='editor' class="flex flex-col flex-grow editor w-full text-left">
        <div class="bg-white top-0 sticky">
        <div class="flex justify-end mx-6 border-b h-12">
            <div class="flex items-center">
                <div v-if="showConfrimDelete">
                    <button @click="deleteNote" class="bg-red-light hover:bg-red text-white font-bold py-2 px-4 mx-2 rounded">
                        Delete
                    </button>
                    <font-awesome-icon class="cursor-pointer" @click="showConfrimDelete = false" icon="times" size="lg"/>
                </div>
                <font-awesome-icon v-else @click="showConfrimDelete = true" class="hover:text-red my-1 cursor-pointer " icon="trash" size="lg"/>
            </div>

        </div>
        <div class="hidden md:flex items-center mx-6 py-2 justify-center">
        <editor-menu-bar :editor="editor" class="pl-8 flex items-center ">
            <div :class="{ 'is-focused': focused }" slot-scope="{ commands, isActive, focused }" class="flex flex-wrap is-hidden">
                <button class="flex content-center rounded border py-1 px-2 mr-2 my-1" :class="{ 'bg-green-lightest': isActive.bold() }" @click="commands.bold">
                    <font-awesome-icon icon="bold" size='xs' />
                </button>
                <button class="flex content-center rounded border py-1 px-2 mr-2 my-1" :class="{ 'bg-green-lightest': isActive.italic() }" @click="commands.italic">
                    <font-awesome-icon icon="italic" size='xs' />
                </button>
                <button
                    class="flex content-center rounded border py-1 px-2 mr-2 my-1"
                    :class="{ 'bg-green-lightest': isActive.strike() }"
                    @click="commands.strike"
                >
                    <font-awesome-icon icon="strikethrough" size='xs' />
                </button>

                <button
                    class="flex content-center rounded border py-1 px-2 mr-2 my-1"
                    :class="{ 'bg-green-lightest': isActive.underline() }"
                    @click="commands.underline"
                >
                    <font-awesome-icon icon="underline" size='xs' />
                </button>

                <button
                    class="flex content-center rounded border py-1 px-2 mr-2 my-1"
                    :class="{ 'bg-green-lightest': isActive.code() }"
                    @click="commands.code"
                >
                    <font-awesome-icon icon="code" size='xs' />
                </button>

                <button
                    class="flex content-center rounded border py-1 px-2 mr-2 my-1"
                    :class="{ 'bg-green-lightest': isActive.paragraph() }"
                    @click="commands.paragraph"
                >
                    <font-awesome-icon icon="paragraph" size='xs' />
                </button>

                <button
                    class="flex content-center rounded border py-1 px-2 mr-2 my-1 text-xs font-bold"
                    :class="{ 'bg-green-lightest': isActive.heading({ level: 1 }) }"
                    @click="commands.heading({ level: 1 })"
                >
                    H1
                </button>

                <button
                    class="flex content-center rounded border py-1 px-2 mr-2 my-1 text-xs font-bold"
                    :class="{ 'bg-green-lightest': isActive.heading({ level: 2 }) }"
                    @click="commands.heading({ level: 2 })"
                >
                    H2
                </button>

                <button
                    class="flex content-center rounded border py-1 px-2 mr-2 my-1 text-xs font-bold"
                    :class="{ 'bg-green-lightest': isActive.heading({ level: 3 }) }"
                    @click="commands.heading({ level: 3 })"
                >
                    H3
                </button>

                <button
                    class="flex content-center rounded border py-1 px-2 mr-2 my-1"
                    :class="{ 'bg-green-lightest': isActive.bullet_list() }"
                    @click="commands.bullet_list"
                >
                    <font-awesome-icon icon="list-ul" size='xs' />
                </button>

                <button
                    class="flex content-center rounded border py-1 px-2 mr-2 my-1"
                    :class="{ 'bg-green-lightest': isActive.ordered_list() }"
                    @click="commands.ordered_list"
                >
                    <font-awesome-icon icon="list-ol" size='xs' />
                </button>

                <button
                    class="flex content-center rounded border py-1 px-2 mr-2 my-1"
                    :class="{ 'bg-green-lightest': isActive.blockquote() }"
                    @click="commands.blockquote"
                >
                    <font-awesome-icon icon="quote-right" size='xs' />
                </button>

            </div>
        </editor-menu-bar>
        </div>
        <div class="flex justify-start">
            <input v-model="title" v-on:blur="updateNote()" placeholder="Title" class="bg-transparent text-black w-full text-4xl pl-8 mb-2 shadow-none focus:outline-none">
        </div>
        </div>
        <div class="overflow-auto h-full">
            <editor-content class="h-full w-full px-8 focus:outline-none break-words" :editor="editor" />
        </div>
    </div>
    <div id="NoNotes" v-show="!note" @click="newNote" class="flex flex-col flex-grow items-center justify-center cursor-pointer">

        <h1>No Notes!</h1>
        <h2>Click here to create a new note</h2>
        <div class="rounded-full h-10 w-10 mt-4 flex items-center justify-center bg-green">
            <span class="text-white group-hover:text-grey-light text-3xl font-medium ">
            +
            </span>
        </div>
    </div>
</div>
</template>

<script>
import Icon from '@/components/Icon.vue'
import { Editor, EditorContent, EditorMenuBar } from 'tiptap'
import {
  Blockquote,
  CodeBlock,
  HardBreak,
  Heading,
  HorizontalRule,
  OrderedList,
  BulletList,
  ListItem,
  TodoItem,
  TodoList,
  Bold,
  Code,
  Italic,
  Link,
  Strike,
  Underline,
  History,
  Placeholder,
} from 'tiptap-extensions'
import { log } from 'util';
import _ from 'lodash'

export default {
    name: "Note",
    components: {
        EditorContent,
        EditorMenuBar,
    },
    data() {
        return {
            editor: new Editor({
                extensions: [
                    new Blockquote(),
                    new BulletList(),
                    new CodeBlock(),
                    new HardBreak(),
                    new Heading({ levels: [1, 2, 3] }),
                    new HorizontalRule(),
                    new ListItem(),
                    new OrderedList(),
                    new TodoItem(),
                    new TodoList(),
                    new Bold(),
                    new Code(),
                    new Italic(),
                    new Link(),
                    new Strike(),
                    new Underline(),
                    new History(),
                    new Placeholder({
                        emptyClass: 'is-empty',
                        emptyNodeText: 'Write something…',
                    }),
                ],
                onFocus: () => {
                    console.log('focus')
                },
                onBlur: () => {
                    console.log('save on blur')
                },
                onUpdate: (state) => {
                    console.log('update');
                    this.content = JSON.stringify(state.getJSON())
                    this.debouncedUpdateNote()
                },
            }),
            title: null,
            focus: false,
            content: null,
            showConfrimDelete: false
        }
    },
    beforeDestroy() {
        this.editor.destroy()
    },
    computed: {
        note() {
            return this.$store.state.note
        },
        activeNote() {
            return this.$store.state.activeNote
        },
    },
    methods: {
        newActiveNote () {
            console.log('newActiveNote');
            if (this.note) {
                if (this.note.content) {
                    this.editor.setContent(JSON.parse(this.note.content))
                } else {
                    this.editor.setContent('')
                }
                if (this.note.title) {
                    this.title = this.note.title
                } else {
                    this.title = ''
                }
            }

        },
        deleteNote () {
            this.$store.dispatch('actionDeleteNote', this.note)
            this.showConfrimDelete = flase
        },
        newNote () {
            this.$store.dispatch('actionCreateNewNote')
        },
        updateNote () {
            var note = {id: this.note.id, title:this.title, content:this.content, updated: new Date().toJSON()}
            console.log('update');
            this.$store.dispatch('actionUpdateNote', note)
        }
    },
    watch: {
        activeNote: function (newNote, OldNote) {
            this.newActiveNote()
        }
    },
    created: function () {
        // _.debounce is a function provided by lodash to limit how
        // often a particularly expensive operation can be run.
        // In this case, we want to limit how often we access
        // yesno.wtf/api, waiting until the user has completely
        // finished typing before making the ajax request. To learn
        // more about the _.debounce function (and its cousin
        // _.throttle), visit: https://lodash.com/docs#debounce
        this.debouncedUpdateNote = _.debounce(this.updateNote, 500)
  },
};
</script>

<style>
p.is-empty:first-child::before {
  content: attr(data-empty-text);
  float: left;
  color: lightgray;
  pointer-events: none;
  height: 0;
}

.is-hidden {
    visibility: hidden;
    opacity: 0;
    transition: visibility 0.2s 0.4s, opacity 0.2s 0.4s;
  }
.is-focused {
visibility: visible;
opacity: 1;
transition: visibility 0.2s, opacity 0.2s;
transition: visibility 0.2s 0.4s, opacity 0.2s 0.4s;
}
</style>
